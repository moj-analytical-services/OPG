"""
==============================================================================
 OPG Supervision Caseflow Report
 @author: Stuart Stach
 MoJ Data Science Hub
==============================================================================
""" 

import os
import shutil
from datetime import datetime,timedelta
import pydbtools
import pandas as pd
import boto3
import numpy as np
import logging
import botocore
import s3fs
from dateutil.relativedelta import relativedelta

def create_log(name):
    #initialise the logger and create the logfile
    logfile = os.getcwd()+'/tmp/{}.log'.format(name)
    
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    
    fh = logging.FileHandler(logfile,mode='a')
    fh.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    log.addHandler(ch)
    log.addHandler(fh)

    log.info("*** Hello from {}.py ***".format(name))
    return log

def retrieve_gedates(log, tables):
    """Find latest glue export dates for annual report tables"""

    # Choose the most recent available source data
    target_date = pydbtools.read_sql_query(f"""
        SELECT max(glueexporteddate) AS glueexporteddate 
        FROM opg_sirius_prod.cases""")['glueexporteddate'][0]
    
    log.info('pydbtools: Last glue export date seems to be {}'.format(target_date))

    # What is the most recent glue export datetime for each table of interest?
    glueexporteddates = {}
    
    log.info('pydbtools: looking for contemporary glue exports of {} tables ...'.format(len(tables)))

    for table in tables: 
        query = f"""SELECT MAX(glueexporteddate) AS glueexporteddate 
                    FROM opg_sirius_prod.{table} 
                    WHERE glueexporteddate <= DATE('{target_date}')"""
        glueexporteddate = pydbtools.read_sql_query(query)['glueexporteddate'][0]
        log.info("pydbtools: using '{}' table glue export from {} in Sirius".format(table, glueexporteddate))
        glueexporteddates[table] = glueexporteddate
    
    return(glueexporteddates)

def retrieve_clients(log,glueexporteddates):
    
    query = (f"""
        with active_fee_reductions AS (
            SELECT
                fp.client_id,
                SUBSTRING(fre.type, 1, 1) || LOWER(SUBSTRING(fre.type, 2)) AS discounttype,
                fre.startdate AS startdate,
                fre.enddate AS enddate,
                fp.payment_method
            FROM opg_sirius_prod.fee_reduction fre
            INNER JOIN opg_sirius_prod.finance_client fp ON fp.id = fre.finance_client_id
                AND fp.glueexporteddate = DATE('{str(glueexporteddates['finance_client'])}')
            INNER JOIN (
                SELECT
                    MAX(fr.id) AS id,
                    fr.finance_client_id
                FROM opg_sirius_prod.fee_reduction fr
                WHERE fr.enddate >= current_date
                  AND fr.startdate <= current_date
                  AND fr.deleted = FALSE
                  AND fr.glueexporteddate = DATE('{str(glueexporteddates['fee_reduction'])}')
                GROUP BY fr.finance_client_id
            ) ids ON ids.id = fre.id
            WHERE fre.glueexporteddate = DATE('{str(glueexporteddates['fee_reduction'])}')
        ),

        earliest_orderdate AS (
            SELECT 
                MIN(c.orderdate) as orderdate,
                c.client_id
            FROM opg_sirius_prod.cases c
            WHERE c.glueexporteddate = DATE('{str(glueexporteddates['cases'])}')
            GROUP BY c.client_id
        ),

        earliest_receiptdate AS (
            SELECT 
                MIN(c.receiptdate) as receiptdate,
                c.client_id
            FROM opg_sirius_prod.cases c
            WHERE c.glueexporteddate = DATE('{str(glueexporteddates['cases'])}')
                AND c.receiptdate IS NOT NULL
            GROUP BY c.client_id
        ),

        regain AS (
            SELECT
                c.client_id,
                c.statusdate
            FROM opg_sirius_prod.cases c
            WHERE c.glueexporteddate = DATE('{str(glueexporteddates['cases'])}')
                AND c.orderclosurereason = 'CLIENT REGAINED CAPACITY'
        ),

        order_list AS (
            SELECT
                c.client_id as client_id,
                c.caserecnumber as court_number,
                ARRAY_AGG(c.id) AS order_ids,
                ARRAY_AGG(c.casesubtype) AS order_types,
                ARRAY_AGG(CAST(c.orderdate AS varchar)) AS order_made_dates,
                ARRAY_AGG(CAST(c.orderissuedate AS varchar)) AS order_issue_dates,
                ARRAY_AGG(CAST(c.orderexpirydate AS varchar)) AS order_expiry_dates,
                ARRAY_AGG(c.orderclosurereason) AS order_closure_reason,
                ARRAY_AGG(c.orderstatus) AS order_statuses,
                ARRAY_AGG(CAST(c.statusdate AS varchar)) AS order_status_dates
            FROM opg_sirius_prod.cases c
            WHERE c.glueexporteddate = DATE('{str(glueexporteddates['cases'])}')
                AND c.casetype = 'ORDER'
            GROUP BY c.client_id, c.caserecnumber
        )

        SELECT
            c.caserecnumber AS court_number,
            p.id AS client_id,
            p.firstname AS client_forename,
            p.surname AS client_surname,
            p.dob AS client_dob,
            p.clientaccommodation AS client_accommodation,
            p.maritalstatus AS client_maritalstatus,
            p.clientstatus AS client_status,
            CASE
                WHEN p.dateofdeath IS NOT NULL THEN p.dateofdeath
                WHEN p.clientstatus != 'ACTIVE' AND rc.statusdate IS NOT NULL THEN rc.statusdate
                WHEN p.dateofdeath IS NULL AND dn.datenotified IS NOT NULL THEN dn.datenotified
                ELSE NULL
            END AS termination_date,
            p.dateofdeath AS client_date_of_death,
            a.postcode AS client_postcode,
            p.risk_score AS CREC,
            dep.deputytype AS feepayer_deputy_type,
            eo.orderdate AS earliest_order_made_date,
            CAST(er.receiptdate AS DATE) AS earliest_receipt_date,
            afr.discounttype AS feereductiontype,
            afr.startdate AS awardstartdate,
            afr.enddate AS awardenddate,
            c.id as order_id,
            c.casesubtype as order_type,
            c.orderstatus as order_status,
            level.supervisionlevel as case_sup_level,
            level.assetlevel as assets_level,
            c.orderdate as order_made_date,
            c.orderissuedate as order_issue_date,
            c.orderexpirydate as order_expiry_date,
            c.orderclosurereason as order_closure_reason,
            CAST(c.statusdate AS varchar) as order_status_date


        FROM opg_sirius_prod.persons p
        LEFT JOIN opg_sirius_prod.addresses a on p.id = a.person_id
            AND a.glueexporteddate = DATE('{str(glueexporteddates['addresses'])}')
        LEFT JOIN opg_sirius_prod.persons dep ON dep.id = p.feepayer_id
            AND dep.glueexporteddate = DATE('{str(glueexporteddates['persons'])}')
        LEFT JOIN opg_sirius_prod.death_notifications dn on dn.person_id = p.id
            AND dn.glueexporteddate = DATE('{str(glueexporteddates['death_notifications'])}')
        LEFT JOIN active_fee_reductions afr ON afr.client_id = p.id
        LEFT JOIN earliest_orderdate eo ON eo.client_id = p.id
        LEFT JOIN earliest_receiptdate er ON er.client_id = p.id
        LEFT JOIN regain rc ON rc.client_id = p.id
        LEFT JOIN opg_sirius_prod.cases c ON p.id = c.client_id
            AND c.glueexporteddate = DATE('{str(glueexporteddates['cases'])}')
            AND lower(c.type) = 'order'
        LEFT JOIN (
            SELECT mr.order_id, MAX(mr.createddate) mostrecent
            FROM opg_sirius_prod.supervision_level_log mr
            WHERE mr.glueexporteddate = DATE('{str(glueexporteddates['supervision_level_log'])}')
                and mr.supervisionlevel is not null
            GROUP BY mr.order_id
        ) mostrecents ON c.id = mostrecents.order_id 
        LEFT JOIN opg_sirius_prod.supervision_level_log level ON mostrecents.order_id = level.order_id
        AND mostrecents.mostrecent = level.createddate
        AND level.glueexporteddate = DATE('{str(glueexporteddates['supervision_level_log'])}')
        WHERE p.glueexporteddate = DATE('{str(glueexporteddates['persons'])}')
            AND p.type = 'actor_client'
        ORDER BY c.caserecnumber, c.orderdate ASC""")

    query = " ".join(query.split()) 
    log.info("pydbtools: our SQL query is: '" + query + "'")

    # Send query to Athena, capture response in a pandas data frame
    cases = pydbtools.read_sql_query(query) 
    #log.info("pydbtools: received [" + str(1 + cases.index.max()) + "] records")
    
    return(cases)

if __name__ == "__main__":
    shutil.rmtree('tmp',ignore_errors=True)
    os.makedirs('tmp', exist_ok=True)

    name = 'supervision_clients_caseflow'
    log = create_log(name)

    tables = ['supervision_level_log',
              'cases',
              'persons',
              'death_notifications',
              'fee_reduction',
              'finance_client',
              'addresses']

    glueexporteddates = retrieve_gedates(log, tables)
    
    caseload = retrieve_clients(log,glueexporteddates)
    
    # -only include clients who joined within data retention period
    # -put this into the original sql query...not here
    seven_yrs_ago = datetime.now().date() - relativedelta(years=7)
    caseload_retention = caseload.loc[caseload.earliest_order_made_date > seven_yrs_ago].copy()
    
    # -read the uploaded old CASREC equivalent report...this should be unnecessary
    casrec_report = pd.read_excel('s3://alpha-opg-mi-dashboard/Supervisions/caseload_flow/order1.xlsx')
    casrec_report['Made Date'] = pd.to_datetime(casrec_report['Made Date'], format ='%Y-%m-%d', errors='coerce').dt.date

    # -match the CASREC excel sheet to the sirius data pull
    case_casrec = caseload_retention.merge(casrec_report, left_on = ['court_number','order_made_date'], right_on = ['Case','Made Date'],how = 'left')
    #case_casrec = case_casrec.groupby(['court_number']).reset_index()
    
    # -where sirius is missing termination dates and reasons - retrieve from casrec report
    case_casrec['termination_date'] = pd.to_datetime(case_casrec['termination_date'], errors = 'coerce')
    
    case_casrec['from_casrec'] = np.where(((case_casrec['client_status'] == 'CLOSED') &\
                                           pd.isnull(case_casrec['termination_date']) &\
                                           pd.notnull(case_casrec['Desc.1'])), True, False)
    
    case_casrec['client_status'] = np.where(case_casrec['from_casrec'],
                                            case_casrec['Desc.1'],
                                            case_casrec['client_status'])
    
    case_casrec['termination_date'] = np.where(case_casrec['from_casrec'],
                                               pd.to_datetime(case_casrec['Term Date'],
                                                              format = '%d/%m/%Y'),
                                               case_casrec['termination_date'])
    
    case_casrec['termination_date'] = pd.to_datetime(case_casrec['termination_date']).dt.date
    
    # -two clients have dateofdeaths confirmed placed by deputy mistake - remove these manually
    case_casrec.loc[case_casrec['client_id'] == 46671511, 
                    ['client_date_of_death','termination_date']] = np.nan
    case_casrec.loc[case_casrec['client_id'] == 20086536,
                    ['client_date_of_death','termination_date']] = np.nan  
    
    case_casrec.sort_values(by=['court_number','order_made_date'],inplace=True)
    
    with pd.ExcelWriter('./tmp/supervision_clients_caseflow.xlsx') as writer:  
        case_casrec.to_excel(writer, sheet_name='clients',index=False)
        
    s3r = boto3.resource('s3')
    bucket_name = 'alpha-opg-mi-dashboard'
    tday = datetime.today().strftime('%Y%m%d')

    s3dir = 'Supervisions/caseflow'
    s3logdir = s3dir+'/logs'
    filename = 'supervision_clients_caseflow_'+tday+'.xlsx'
    logfilename = 'supervision_clients_caseflow_'+tday+'.log'
    s3file = "{}/{}".format(s3dir,filename)
    s3logfile = "{}/{}".format(s3logdir,logfilename)

    try: 
        response = s3r.Object(bucket_name,s3file).put(Body=open('./tmp/supervision_clients_caseflow.xlsx', 'rb'))
        log.info(f'Uploaded report to {s3file}')
    except botocore.exceptions.ClientError as err:
        log.info('Error Message: {}'.format(err.response['Error']['Message']))
        log.info('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
        log.info('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))

    try:
        log.info(f'Uploading logfile to {s3logfile}')
        response = s3r.Object(bucket_name,s3logfile).put(Body=open('./tmp/supervision_clients_caseflow.log', 'rb'))
        shutil.rmtree('tmp',ignore_errors=True)
    except botocore.exceptions.ClientError as err:
        log.info('Error Message: {}'.format(err.response['Error']['Message']))
        log.info('Request ID: {}'.format(err.response['ResponseMetadata']['RequestId']))
        log.info('Http code: {}'.format(err.response['ResponseMetadata']['HTTPStatusCode'])) 
        
    shutil.rmtree('tmp',ignore_errors=True)
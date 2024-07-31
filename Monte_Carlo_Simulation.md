# Monte Carlo Simulation
- a method of estimating the value of an unknown quantity using principles of inferential statistics:
    - inferential statistics:
        - population: a set of examples
        - sample: a proper subset of population
        - key fact: a random sample tends to exhibit the same properties as the polulation from which is drown
    - similar to random walk
The provided VBA code below is written by Peter Sheir to implement a form of a Monte Carlo simulation for OPG exel-based model. 
Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. 
It is a technique used to understand the impact of risk and uncertainty in prediction and forecasting models.
To improve the accuracy, we could increase the number of iteration (Currently 500).


## Purpose of the Simulations

The purpose of these simulations is to perform multiple iterations of certain scenarios and record the results. This is often done in the context of risk analysis, forecasting, or optimisation where the outcome is uncertain and depends on a set of variable inputs.


The VBA code below is used to perform simulations on different scenarios in 'LPA Forecast PEOPLE' worksheet in Demand Forecast model for OPG.
The workbook contains forecasts for ‘LPA People’, ‘Deputyship’, and ‘Investigations’.

## The old VBA Code

```vba
Option Explicit
Option Base 1
Sub Simulate()
'Subroutine to recalculate the workbook to change the random numbers to give 500 iterations of one
'scenario in the LPA People forecast and copy the data to the sheet 'LPA FORECAST PEOPLE'.
'Paul Tuxworth, OPG Analysis, Income Analysis, 22/1/2020
Dim i As Long, vrtIteration() As Variant
Dim j As Long

'Reduce screen flicker by not continually updating the screen
Application.ScreenUpdating = False

'Clear the "Simulation" range
Range("Simulation").ClearContents

For i = 1 To 500
    'Recalculate the workbook
    Application.Calculate
    'Obtain the iteration data from the range "Iteration" on the "LPA Forecast PEOPLE" sheet
    Call UpdateArrayFromRow(vrtIteration, "Iteration")
    
    'Write the iteration data to row i of the range "Simulation"
    For j = 1 To UBound(vrtIteration)
        Range("Simulation").Cells(i, j).Value = vrtIteration(j)
    Next j
Next i

'Display message that data is updated
MsgBox ("Data in the Simulation range of the LPA Forecast PEOPLE sheet has been updated")


'Now allow screen updating
Application.ScreenUpdating = True

End Sub
Sub SimulateDep()
'Subroutine to recalculate the workbook to change the random numbers to give 500 iterations of one
'scenario in the Deputyship forecast and copy the data within the sheet 'Deputyship Forecast Simulations'.
'Paul Tuxworth, OPG Analysis, Income Analysis, 4/3/2020
Dim i As Long, vrtIteration() As Variant
Dim j As Long

'Reduce screen flicker by not continually updating the screen
Application.ScreenUpdating = False

'Clear the "SimulationDep" range
Range("SimulationDep").ClearContents

For i = 1 To 500
    'Recalculate the workbook
    Application.Calculate
    'Obtain the iteration data from the range "IterationDep" on the "Deputyship Forecast Simulations" sheet
    Call UpdateArrayFromRow(vrtIteration, "IterationDep")
    
    'Write the iteration data to row i of the range "SimulationDep"
    For j = 1 To UBound(vrtIteration)
        Range("SimulationDep").Cells(i, j).Value = vrtIteration(j)
    Next j
Next i

'Display message that data is updated
MsgBox ("Data in the SimulationDep range of the Deputyship Forecast Simulations sheet has been updated")


'Now allow screen updating
Application.ScreenUpdating = True

End Sub
Sub SimulateInv()
'Subroutine to recalculate the workbook to change the random numbers to give 500 iterations of one
'scenario in the Investigations forecast and copy the data within the sheet 'Forecast Iterations'.
'Paul Tuxworth, OPG Analysis, Income Analysis, 26/3/2020
Dim i As Long, vrtIteration() As Variant
Dim j As Long

'Reduce screen flicker by not continually updating the screen
Application.ScreenUpdating = False

'Clear the "SimulationInv" range
Range("SimulationInv").ClearContents

For i = 1 To 100 ' Temporary change
    'Recalculate the workbook
    Application.Calculate
    'Obtain the iteration data from the range "IterationInv" on the "Forecast Iterations" sheet
    Call UpdateArrayFromRow(vrtIteration, "IterationInv")
    
    'Write the iteration data to row i of the range "SimulationInv"
    For j = 1 To UBound(vrtIteration)
        Range("SimulationInv").Cells(i, j).Value = vrtIteration(j)
    Next j
Next i

'Display message that data is updated
MsgBox ("Data in the SimulationInv range of the Investigations 'Forecast Iterations' sheet has been updated")


'Now allow screen updating
Application.ScreenUpdating = True

End Sub

Sub UpdateArrayFromRow(vrtData() As Variant, strRow As String)
'Subroutine to update an array from a row defined as a named range
Dim i As Long, rngNamed As Range, lngCols As Long
Set rngNamed = Range(strRow)
lngCols = Application.WorksheetFunction.CountA(rngNamed.Columns)
ReDim vrtData(lngCols)

For i = 1 To lngCols
    vrtData(i) = rngNamed.Cells(1, i).Value
Next i

End Sub
Sub UpdateRow(vrtData() As Variant, strRow As String)
'Subroutine to update a row of a worksheet defined as a named range with data defined as a one-dimensional array
'We assume the named range is large enough to hold the data
Dim i As Long
For i = 1 To UBound(vrtData)
    Range(strRow).Cells(1, i).Value = vrtData(i)
Next i
End Sub
```

1. **Explanation of the VBA Code**:

The provided code is written in VBA (Visual Basic for Applications) and is used to perform simulations on different scenarios in a workbook. The workbook appears to contain forecasts for 'LPA People', 'Deputyship', and 'Investigations'. Here's a breakdown of the code:

- `Option Explicit`: This line requires that all variables be declared before they are used. It's a good practice to prevent typos and logic errors.
- `Option Base 1`: This line sets the default lower bound for array subscripts to 1. By default, in VBA, the lower bound for arrays is 0.
- `Sub Simulate()`, `Sub SimulateDep()`, `Sub SimulateInv()`: These subroutines perform 500 iterations of a scenario in the respective forecast. They recalculates the workbook, obtains iteration data from the respective range on the respective sheet, and writes this data to the respective range.
- `Sub UpdateArrayFromRow()`: This subroutine updates an array from a row defined as a named range. It counts the number of columns in the named range, resizes the array to match, and then populates the array with the values from the cells in the named range.

2. **Purpose of the Simulations**:

The purpose of these simulations is to perform multiple iterations of certain scenarios and record the results. This is often done in the context of risk analysis, forecasting, or optimization where the outcome is uncertain and depends on a set of variable inputs.

3. **Assumptions and Constraints of the Simulations**:

Based on the provided code, there are a few assumptions and constraints that can be inferred for these simulations:

- Number of Iterations: Each simulation is set to run a fixed number of iterations.
- Data Ranges: The simulations assume that the data for each iteration is contained in a specific named range in the workbook.
- Workbook Recalculation: Each iteration involves a recalculation of the entire workbook.
- Screen Updating: Screen updating is turned off at the start of each simulation and turned back on at the end.
- Array Size: The `UpdateArrayFromRow` subroutine assumes that the size of the `vrtIteration` array matches the number of columns in the named range.
- Data Types: The code assumes that all data can be stored as `Variant` data types.

4. **Modifying the Assumptions for Your Own Simulations**:

You can modify these assumptions for your own simulations. The code is flexible and can be adapted to suit your specific needs. Here's how you can modify the assumptions:

- Number of Iterations: You can change the number of iterations in each simulation by modifying the number in the `For i = 1 To 500` line in each subroutine.
- Data Ranges: If your data is in different ranges, you can change the named ranges in the code.
- Workbook Recalculation: If your workbook does not need to be recalculated with each iteration, you can modify or remove the `Application.Calculate` line.
- Screen Updating: If you want to see the changes in the workbook as they happen, you can remove the `Application.ScreenUpdating = False` and `Application.ScreenUpdating = True` lines.
- Array Size: If your data has a different number of columns, you can modify the `UpdateArrayFromRow` subroutine to resize the `vrtIteration` array accordingly.
- Data Types: If your data includes non-variant types, you may need to modify the code to handle these types correctly.

5. **Explanation of the `UpdateArrayFromRow` Subroutine**:

The `UpdateArrayFromRow` subroutine is used to update an array with values from a row in an Excel worksheet. The row is specified by a named range in the workbook. Here's a breakdown of the subroutine:

```vba
Sub UpdateArrayFromRow(vrtData() As Variant, strRow As String)
    'Subroutine to update an array from a row defined as a named range
    Dim i As Long, rngNamed As Range, lngCols As Long
    Set rngNamed = Range(strRow)
    lngCols = Application.WorksheetFunction.CountA(rngNamed.Columns)
    ReDim vrtData(lngCols)

    For i = 1 To lngCols
        vrtData(i) = rngNamed.Cells(1, i).Value
    Next i
End Sub
```

6. **Using the `UpdateArrayFromRow` Subroutine in Your Own Workbook**:

To use the `UpdateArrayFromRow` subroutine in your own workbook, you'll need to follow these steps:

- Open VBA Editor: Press `Alt + F11` in Excel to open the VBA editor.
- Insert a New Module: In the VBA editor, go to `Insert > Module`. This will create a new module where you can write your code.
- Copy the Subroutine: Copy the `UpdateArrayFromRow` subroutine into the new module.
- Use the Subroutine: You can now use the `UpdateArrayFromRow` subroutine in your own code. You'll need to pass two arguments to the subroutine: an array that will be updated with the values from the row, and a string that specifies the named range that contains the row.

7. **Creating a Dynamic Array Using the `UpdateArrayFromRow` Subroutine**:

The `UpdateArrayFromRow` subroutine already creates a dynamic array based on the number of columns in the specified named range. The `ReDim` statement is used to resize the `vrtIteration` array to match the number of columns in the named range.

However, if you want to create a dynamic array that can grow or shrink as needed during the execution of your code, you can use the `ReDim Preserve` statement. The `Preserve` keyword allows you to keep the existing values in the array when you resize it.

8. **Removing an Element from the Middle of an Array Using `ReDim Preserve`**:

Removing an element from the middle of an array in VBA requires shifting all the elements after the removed element down by one position, and then resizing the array. Unfortunately, VBA does not provide a built-in method to remove an element from an array. However, you can achieve this by creating a new array and copying over the elements you want to keep.

9. **Monte Carlo Simulation**:

Yes, the code you provided in your first question does appear to implement a form of a Monte Carlo simulation. Monte Carlo simulations are used to model the probability of different outcomes in a process that cannot easily be predicted due to the intervention of random variables. It is a technique used to understand the impact of risk and uncertainty in prediction and forecasting models.

10. **Converting the Simulation Codes into Monte Carlo Simulation**:

The code you provided already implements a form of Monte Carlo simulation. In a Monte Carlo simulation, an operation is repeated a large number of times, each time with different randomly selected inputs. The results of these iterations are used to analyse the overall behavior of the system.

However, if you want to make the Monte Carlo aspect of the simulation more explicit, you could add a step where you generate a set of random inputs for each iteration.

11. **Generating Random Numbers for Monte Carlo Simulation**:

In VBA, you can generate random numbers using the `Rnd` function, which returns a random number between 0 and 1. If you need random numbers in a different range, you can adjust the output of `Rnd` using some simple math.

12. **Generating Normally Distributed Random Numbers for Simulation**:

In VBA, you can generate normally distributed random numbers using the `Application.NormInv` function, which is the inverse of the normal cumulative distribution for the specified mean and standard deviation. This function takes three arguments: a probability, a mean, and a standard deviation.

13. **Generating Other Types of Random Distributions in VBA**:

In VBA, you can generate random numbers from various distributions using built-in Excel functions. Here are a few examples:

- Uniform Distribution: You can generate uniformly distributed random numbers using the `Rnd` function.
- Normal Distribution: As mentioned earlier, you can generate normally distributed random numbers using the `Application.NormInv` function.
- Exponential Distribution: You can generate exponentially distributed random numbers using the `Application.WorksheetFunction.ExponDist` function.
- Poisson Distribution: You can generate Poisson distributed random numbers using the `Application.WorksheetFunction.Poisson` function.
- Binomial Distribution: You can generate binomially distributed random numbers using the `Application.WorksheetFunction.BinomDist` function.

## Optimising the code

*Combine Similar Code: 
The Simulate, SimulateDep, and SimulateInv subroutines were very similar, so I combined them into a single SimulateAll subroutine. This reduces code duplication and makes the code easier to maintain.

*Use Arrays for Similar Operations: 
I used arrays to store the names of the ranges for the simulations and iterations. This allows us to use a loop to perform the same operations on each range, further reducing code duplication.

*Clear All Ranges at Once: 
Instead of clearing each range individually at the start of each simulation, I clear all the ranges at once before starting the simulations. This could potentially save a small amount of time if the ranges are large.


### The Optimised VBA Code

```vba
Option Explicit
Option Base 1

Sub SimulateAll()
    'Leila Yousefi, OPG Analysis, Income Analysis, 26/04/2024
    Dim i As Long, j As Long
    Dim vrtIteration() As Variant
    Dim simulations As Variant
    Dim iterationRange As String
    
    'Reduce screen flicker by not continually updating the screen
    Application.ScreenUpdating = False
    
    simulations = Array("Simulation", "SimulationDep", "SimulationInv")
    iterationRange = Array("Iteration", "IterationDep", "IterationInv")
    
    For Each simulation In simulations
        Range(simulation).ClearContents
    Next simulation
    
    For i = 1 To 500
        'Recalculate the workbook
        Application.Calculate
        
        For Each simulation In simulations
            'Obtain the iteration data from the range "Iteration" on the "LPA Forecast PEOPLE" sheet
            Call UpdateArrayFromRow(vrtIteration, iterationRange)
            
            'Write the iteration data to row i of the range "Simulation"
            For j = 1 To UBound(vrtIteration)
                Range(simulation).Cells(i, j).Value = vrtIteration(j)
            Next j
        Next simulation
    Next i
    
    'Display message that data is updated
    MsgBox ("Data in the Simulation range of the LPA Forecast PEOPLE sheet has been updated")
    
    'Now allow screen updating
    Application.ScreenUpdating = True
End Sub

Sub UpdateArrayFromRow(vrtData() As Variant, strRow As String)
    'Subroutine to update an array from a row defined as a named range
    Dim i As Long, rngNamed As Range, lngCols As Long
    Set rngNamed = Range(strRow)
    lngCols = Application.WorksheetFunction.CountA(rngNamed.Columns)
    ReDim vrtData(lngCols)
    
    For i = 1 To lngCols
        vrtData(i) = rngNamed.Cells(1, i).Value
    Next i
End Sub
```


### Dynamic Arrays

In VBA, an array is a data structure that allows you to store multiple values in a single variable. This can be very useful when you need to work with a large number of related values.

In the provided code, arrays are used in several ways:

1. **Storing Multiple Related Values**: The `vrtIteration` array is used to store the values from a row in the workbook. The `UpdateArrayFromRow` subroutine updates this array with the values from the specified named range.

2. **Dynamic Sizing**: The size of the `vrtIteration` array is not fixed. Instead, it's resized to match the number of columns in the named range using the `ReDim` statement. This allows the array to adapt to the data in the workbook.

3. **Accessing Values**: The values in the `vrtIteration` array are accessed using an index. For example, `vrtIteration(j)` gets the value at index `j` in the array.

4. **Storing Range Names for Iteration**: The `simulations` and `iterationRange` arrays are used to store the names of the ranges for the simulations and iterations. This allows the code to loop over each range and perform the same operations, reducing code duplication.


In this code, simulations and iterationRange are arrays that contain the names of the ranges for the simulations and iterations. The For Each simulation In simulations loop goes through each name in the simulations array, and the Call UpdateArrayFromRow(vrtIteration, iterationRange) line uses the iterationRange array to get the name of the range for the current iteration.


Here's a bit more detail on how the `simulations` and `iterationRange` arrays are used:

```vba
simulations = Array("Simulation", "SimulationDep", "SimulationInv")
iterationRange = Array("Iteration", "IterationDep", "IterationInv")

For Each simulation In simulations
    Range(simulation).ClearContents
Next simulation

For i = 1 To 500
    'Recalculate the workbook
    Application.Calculate

    For Each simulation In simulations
        'Obtain the iteration data from the range "Iteration" on the "LPA Forecast PEOPLE" sheet
        Call UpdateArrayFromRow(vrtIteration, iterationRange)

        'Write the iteration data to row i of the range "Simulation"
        For j = 1 To UBound(vrtIteration)
            Range(simulation).Cells(i, j).Value = vrtIteration(j)
        Next j
    Next simulation
Next i
```


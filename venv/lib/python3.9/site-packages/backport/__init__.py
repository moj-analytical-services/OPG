import sys
from importlib.metadata import version
__version__ = version("backport")

from . import abc_ext
from . import types
from . import typing
from . import dataclasses
from . import inspect_ext

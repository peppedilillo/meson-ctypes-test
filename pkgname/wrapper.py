import ctypes
import enum
from pathlib import Path

import numpy as np
import numpy.typing as npt


def library_path(libname: str) -> str:
    """Gets the path to the library, findind the appropriate extension based on
     OS. The lib is installed in `lib/pythonX.XX/site-packages/.sharedlibs`.
     Assumes this script to be installed at `lib/pythonX.XX/site-packages`"""
    from pathlib import Path
    import sys

    if sys.platform.startswith('win32'):
        suffix = ".dll"
    elif sys.platform.startswith('linux'):
        suffix = ".so"
    elif sys.platform.startswith('darwin'):
        suffix = ".dylib"
    else:
        raise OSError("System not supported")

    return str(Path(__file__).parent / ".sharedlibs" / f"{libname}{suffix}")


# Loads the C library.
lib = ctypes.CDLL(library_path("libsharedlibname"))


class Result(ctypes.Structure):
    """A ctypes wrapper to a structure where the C lib writes results"""
    _fields_ = [("mean", ctypes.c_double)]


class Errors(enum.IntEnum):
    """A ctypes wrapper to an error raised by the C lib"""
    NO_ERRORS = 0
    EMPTY_ARRAY = 1


# Wrapping the library's interface function.
_clib_calculate_mean = lib.calculateMean
_clib_calculate_mean.argtypes = [
    ctypes.POINTER(Result),
    ctypes.POINTER(ctypes.c_int32),
    ctypes.c_size_t
]
_clib_calculate_mean.restype = Errors


def calculate_mean(array: npt.NDArray[np.int32]) -> float:
    """Runs the wrapped library's interface function checking for errors"""
    result = Result()
    length = len(array)

    c_array = array.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))
    error = _clib_calculate_mean(ctypes.byref(result), c_array, length)

    if error:
        raise ValueError("Could not compute mean.")
    return result.mean

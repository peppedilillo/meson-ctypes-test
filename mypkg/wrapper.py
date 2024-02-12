import ctypes
import enum

import numpy as np

lib_path = "mylib.so"
lib = ctypes.CDLL(lib_path)


class Result(ctypes.Structure):
    _fields_ = [("mean", ctypes.c_double)]


class Errors(enum.IntEnum):
    NO_ERRORS = 0
    EMPTY_ARRAY = 1


calculate_mean = lib.calculateMean
calculate_mean.argtypes = [ctypes.POINTER(Result), ctypes.POINTER(ctypes.c_int32), ctypes.c_size_t]
calculate_mean.restype = Errors


def calculate_mean_interface(array):
    result = Result()
    length = len(array)

    c_array = array.ctypes.data_as(ctypes.POINTER(ctypes.c_int32))

    error = calculate_mean(ctypes.byref(result), c_array, length)
    return error, result


if __name__ == "__main__":
    array = np.array([1, 2, 3, 4, 5], dtype="int32")

    error, result = calculate_mean_interface(array)

    if error == Errors.EMPTY_ARRAY:
        print("Error: Empty array!")
    elif error == Errors.NO_ERRORS:
        print("Mean:", result.mean)

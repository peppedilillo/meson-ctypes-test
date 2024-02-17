import numpy as np
from pkgname.wrapper import calculate_mean


def callslib():
    array = np.array([1, 2, 3]).astype('int32')
    mean = calculate_mean(array)
    print(f"The mean of the array is {mean}.")


if __name__ == "__main__":
    callslib()
#include <stdio.h>
#include "include/mylib.h"


enum errors calculateMean(struct Result *result, const int32_t array[], size_t length) {
    if (length == 0) {
        return EMPTY_ARRAY;
    }

    int sum = 0;
    for (size_t i = 0; i < length; i++) {
        sum += array[i];
    }

    result->mean = (double)sum / length;

    return NO_ERRORS;
}

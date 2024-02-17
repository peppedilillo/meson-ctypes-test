#ifndef _TEST_CTYPES_H_
#define _TEST_CTYPES_H_
#include <stdint.h>

enum errors {
    NO_ERRORS,
    EMPTY_ARRAY
};

struct Result {
    double mean;
};

enum errors calculateMean(struct Result *result, const int32_t *array, size_t length);

#endif //_TEST_CTYPES_H_

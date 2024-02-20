#ifndef _TEST_CTYPES_H_
#define _TEST_CTYPES_H_
#include <stdint.h>

#if defined(_WIN32)
#  define DLL00_EXPORT_API __declspec(dllexport)
#else
#  define DLL00_EXPORT_API
#endif


enum errors {
    NO_ERRORS,
    EMPTY_ARRAY
};

struct Result {
    double mean;
};

DLL00_EXPORT_API enum errors calculateMean(struct Result *result, const int32_t *array, size_t length);

#endif //_TEST_CTYPES_H_
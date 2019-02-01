# cython: language_level=2

cpdef long fnv1a(char* s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef long f = 0xffffffff
    cdef long n = len(s)
    cdef long i
    for i in range(n):
        h = ((h ^ s[i]) * prime) & f
    return h

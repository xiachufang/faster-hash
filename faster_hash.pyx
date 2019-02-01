# cython: language_level=2

cpdef long fnv1a(char* s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef char c
    for c in s:
        h = (h ^ c * prime) & 0xffffffff
    return h


cpdef long fnv1a(s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    for c in s:
        h ^= ord(c)
        h = (h * prime) & 0xffffffff
    return h

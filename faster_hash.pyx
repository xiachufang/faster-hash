# coding: utf-8
# cython: language_level=2

cpdef long fnv1a(unsigned char* s):
    """Fowler–Noll–Vo hash function, see: https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function

    >>> fnv1a(b'3ce6330f-ab86-45df-b2ff-b16cad4f24f1')
    872280216
    >>> fnv1a(b'31eef3c2-42b8-4959-abd4-dc559aba7331')
    2859758067
    >>> fnv1a(b'646f39fb-c3bb-440b-befc-9aa56559d131')
    3424154349
    >>> fnv1a(b'3dc0be7a-30ca-452c-8cf0-19364f697a14')
    4099963837
    >>> try:
    ...   fnv1a(u'🦄🌈')
    ... except (TypeError, UnicodeError):
    ...   print('gotcha')
    gotcha
    >>> fnv1a(u'🦄🌈'.encode('utf-8'))
    2868248295
    """
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef long f = 0xffffffff
    cdef long n = len(s)
    cdef long i
    for i in range(n):
        h = ((h ^ s[i]) * prime) & f
    return h

# coding: utf-8

from __future__ import print_function

import timeit
import uuid

u = uuid.uuid4()

baseline = '''
def fnv1a(s):
    prime = 0x01000193
    h = 0x811c9dc5
    for c in s:
        h ^= ord(c)
        h = (h * prime) & 0xffffffff
    return h
'''

print('baseline:', timeit.timeit(stmt="fnv1a(s)", setup=baseline + 's = "{}"'.format(u)))

# ---------

# initial cython implementation
v0 = '''# cython: language_level=2

cpdef long fnv1a(s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    for c in s:
        h ^= ord(c)
        h = (h * prime) & 0xffffffff
    return h
'''

# iteration 1
# declare type for 's' and 'c'
v1 = '''# cython: language_level=2

cpdef long fnv1a(char* s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef char c
    for c in s:
        h = ((h ^ c) * prime) & 0xffffffff
    return h
'''

# iteration 2
# declare 0xffffffff as C var
v2 = '''# cython: language_level=2

cpdef long fnv1a(char* s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef long f = 0xffffffff
    cdef char c
    for c in s:
        h = ((h ^ c) * prime) & f
    return h
'''

# iteration 3
# compile into native for-loop
v3 = '''# cython: language_level=2

cpdef long fnv1a(char* s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef long f = 0xffffffff
    cdef long n = len(s)
    cdef int i
    for i in range(n):
        h = ((h ^ s[i]) * prime) & f
    return h
'''

# iteration 4
# ensure 'i' and 'n' are same long type
v4 = '''# cython: language_level=2

cpdef long fnv1a(char* s):
    cdef long prime = 0x01000193
    cdef long h = 0x811c9dc5
    cdef long f = 0xffffffff
    cdef long n = len(s)
    cdef long i
    for i in range(n):
        h = ((h ^ s[i]) * prime) & f
    return h
'''

import pyximport

def benchmark(v, pyx, b='b'):
    # write each .pyx iteration
    with open('faster_hash_v{}.pyx'.format(v), mode='w') as f:
        f.write(pyx)
    # install .pyx
    pyximport.install()
    # timeit
    print('v{}:'.format(v), timeit.timeit('fnv1a(b)', setup='from faster_hash_v{v} import fnv1a; b = {b}"{u}"'.format(v=v, u=u, b=b)))


benchmark(0, v0, b='')
benchmark(1, v1)
benchmark(2, v2)
benchmark(3, v3)
benchmark(4, v4)

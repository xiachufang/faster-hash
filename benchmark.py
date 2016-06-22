import timeit
import uuid

s = uuid.uuid4()
setup1 = 'from faster_hash import fnv1a'
code = 'fnv1a("%s")' % s

print timeit.timeit(code, setup=setup1)


setup2 = '''
def fnv1a(s):
    prime = 0x01000193
    h = 0x811c9dc5
    for c in s:
        h ^= ord(c)
        h = (h * prime) & 0xffffffff
    return h
'''
print timeit.timeit(code, setup=setup2)

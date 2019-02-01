import timeit
import uuid

u = uuid.uuid4()

setup1 = '''
b = b"{}"
from faster_hash import fnv1a
'''.format(u)

print(timeit.timeit('fnv1a(b)', setup=setup1))


setup2 = '''
s = "{}"
def fnv1a(s):
    prime = 0x01000193
    h = 0x811c9dc5
    for c in s:
        h ^= ord(c)
        h = (h * prime) & 0xffffffff
    return h
'''.format(u)

print(timeit.timeit('fnv1a(s)', setup=setup2))

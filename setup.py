from distutils.core import setup
from distutils.extension import Extension

USE_CYTHON = False   # command line option, try-import, ...

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("faster_hash", ["faster_hash"+ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name='faster_hash',
    version='0.0.2',
    url='https://github.com/xiachufang/faster-hash',
    description='fnv1a in Cython',
    author='gfreezy',
    author_email='gfreezy@gmail.com',
    ext_modules=extensions
)

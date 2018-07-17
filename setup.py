from setuptools import setup
from setuptools.extension import Extension

USE_CYTHON = False   # command line option, try-import, ...

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("faster_hash", ["faster_hash"+ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(
    name='faster_hash',
    version='0.0.3',
    url='https://github.com/xiachufang/faster-hash',
    description='fnv1a in Cython',
    author='gfreezy',
    author_email='gfreezy@gmail.com',
    ext_modules=extensions,
    classifiers=(
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    )
)

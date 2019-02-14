from setuptools import setup
from setuptools.extension import Extension

extensions = [Extension("faster_hash", ["faster_hash.pyx"])]

setup(
    name='faster_hash',
    version='0.0.4',
    url='https://github.com/xiachufang/faster-hash',
    description='fnv1a in Cython',
    author='gfreezy',
    author_email='gfreezy@gmail.com',
    ext_modules=extensions,
    classifiers=(
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3'
    ),
    setup_requires=['Cython >= 0.28'],
)

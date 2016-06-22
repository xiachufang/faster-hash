from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='faster_hash',
    version='0.0.1',
    description='fnv1a in Cython',
    author='gfreezy',
    author_email='gfreezy@gmail.com',
    install_requires=['Cython'],
    ext_modules=cythonize("faster_hash.pyx")
)

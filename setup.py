#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import accumulators


setup(
    name='accumulators',
    description='Statistical accumlators library',
    version=accumulators.__version__,

    author='Arnaud Porterie',
    author_email='icecrime@gmail.com',
    url='https://github.com/icecrime/Accumulators',

    packages=['accumulators', 'accumulators.statistics'],
    package_data={'': ['LICENSE']},
    package_dir={'accumulators': 'accumulators'},

    classifiers=(
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
    ),
)

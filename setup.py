# -*- coding: utf-8 -*-

import sys
from setuptools import setup, find_packages

if sys.version_info[0] < 3:
    with open('README.md', 'r') as fh:
        long_description = fh.read()
else:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()

setup(
    name='hapi',
    version='2.0.0',
    description='Python client library for VONQ Hiring API',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Marian Mazarovici',
    author_email='marian@vonq.com',
    url='https://vonq.com',
    packages=find_packages(),
    install_requires=[
        'jsonpickle~=1.4, >= 1.4.1',
        'requests~=2.25',
        'cachecontrol~=0.12.6',
        'python-dateutil~=2.8.1',
        'enum34~=1.1, >=1.1.10'
    ],
    tests_require=[
        'nose>=1.3.7'
    ],
    test_suite = 'nose.collector'
)
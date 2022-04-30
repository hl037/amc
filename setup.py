#!/usr/bin/env python
import sys

from setuptools import setup, find_packages


def read_file(name):
    """
    Read file content
    """
    f = open(name)
    try:
        return f.read()
    except IOError:
        print("could not read %r" % name)
        f.close()

LONG_DESC = read_file('README.md') + '\n\n' + read_file('HISTORY.md')

setup(
    name='amc',
    version='1.0',
    description='',
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    author='baderalat',
    author_email='baderalat@example.com',
    url='http://example.com',
    license='All right reserved',
    packages=find_packages(),
    test_suite=None,
    include_package_data=True,
    zip_safe=False,
    install_requires=['antlr4-python3-runtime>=4.10', 'click>=7.0'],
    extras_require=['pdbpp'],
    tests_require=['pytest', 'pytest-cov', 'coverage'],
    entry_points={
      'console_scripts':[
        'amc=amc.cli:main',
      ]
    },
    classifiers=[],
)

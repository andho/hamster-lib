#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'future',
    'sqlalchemy',
    'icalendar',
    'configparser',
]

setup(
    name='hamster-lib',
    version='0.11.0',
    description="A library for common timetracking functionality.",
    long_description=readme + '\n\n' + history,
    author="Eric Goller",
    author_email='eric.goller@ninjaduck.solutions',
    url='https://github.com/projecthamster/hamster-lib',
    packages=[
        'hamster_lib',
        'hamster_lib.backends',
        'hamster_lib.backends.sqlalchemy',
    ],
    package_dir={'hamster_lib':
                 'hamster_lib'},
    install_requires=requirements,
    license="GPL3",
    zip_safe=False,
    keywords='hamster-lib',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)

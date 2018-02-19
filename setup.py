#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for anyblok_address"""

from setuptools import setup, find_packages
import os


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'),
          'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(os.path.join(here, 'CHANGELOG.rst'),
          'r', encoding='utf-8') as changelog_file:
    changelog = changelog_file.read()

with open(os.path.join(here, 'VERSION'),
          'r', encoding='utf-8') as version_file:
    version = version_file.read().strip()

requirements = [
    'anyblok',
    'anyblok-pyramid-rest-api',
    'pycountry'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='anyblok_address',
    version=version,
    description="Address management",
    long_description=readme + '\n\n' + changelog,
    author="Franck Bret",
    author_email='f.bret@sensee.com',
    url='https://github.com/franckbret/anyblok_address',
    packages=find_packages(),
    entry_points={
        'bloks': [
            'address=anyblok_address.bloks.address:AddressBlok',
            'address_rest_api=anyblok_address.bloks.rest_api:AddressRestApiBlok',
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='anyblok_address',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
)

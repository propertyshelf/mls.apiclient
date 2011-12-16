# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2011 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License version 2 as published by the
# Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
###############################################################################
"""Setup for mls.apiclient package."""

import os
import sys
from setuptools import setup, find_packages

version = '0.1'

setup(
    name='mls.apiclient',
    version=version,
    description="Python client for the RESTful API of the Propertyshelf MLS.",
    long_description='\n\n'.join([
        open("README.txt").read() + "\n" +
        open(os.path.join("docs", "HISTORY.txt")).read(),
        open(os.path.join("docs", "INSTALL.txt")).read(),
        open(os.path.join("docs", "LICENSE.txt")).read(),
    ]),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intended Audience :: Other Audience",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    keywords='MLS API client',
    author='Thomas Massmann',
    author_email='thomas@propertyshelf.com',
    maintainer='Thomas Massmann',
    maintainer_email='thomas@propertyshelf.com',
    url='http://pypi.python.org/pypi/mls.apiclient',
    download_url='http://pypi.python.org/pypi/mls.apiclient',
    license='GPL',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    namespace_packages=['mls'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points="""""",
)

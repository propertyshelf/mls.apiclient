# -*- coding: utf-8 -*-

###############################################################################
#
# Copyright (c) 2012 Propertyshelf, Inc. and its Contributors.
# All Rights Reserved.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS AND ANY EXPRESSED OR
# IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO
# EVENT SHALL THE COPYRIGHT HOLDERS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
###############################################################################
"""Setup for mls.apiclient package."""

import os
import sys
from setuptools import setup, find_packages

sys.path.insert(0, os.path.abspath('src/'))
from mls.apiclient import __version__


setup(
    name='mls.apiclient',
    version=__version__,
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
    install_requires=[
        'setuptools',
        'anyjson',
    ],
    entry_points="""""",
)

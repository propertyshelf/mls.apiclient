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
"""mls.apiclient exception classes."""


class MLSError(Exception):
    """Main exception class."""
    pass


class ImproperlyConfigured(MLSError):
    """This exception is raised on configuration errors."""
    pass


class ObjectNotFound(MLSError):
    """This exception is raised if an object can not be found."""
    pass


class MultipleResults(MLSError):
    """This exception is raised on multiple results.

    That is, if a get request returns more than one result.
    """
    def __str__(self):
        return 'Your query had multiple results.'



# -*- coding: utf-8 -*-

"""
hapi

This file was automatically generated for VONQ by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FileWrapper():

    """A wrapper to allow passing in content type for file uploads."""

    def __init__(self, file, content_type='application/octet-stream'):
        self._file_stream = file
        self._content_type = content_type

    @property
    def file_stream(self):
        return self._file_stream

    @property
    def content_type(self):
        return self._content_type
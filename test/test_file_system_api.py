# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.file_system_api import FileSystemApi  # noqa: E501
from swagger_client.rest import ApiException


class TestFileSystemApi(unittest.TestCase):
    """FileSystemApi unit test stubs"""

    def setUp(self):
        self.api = FileSystemApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_attach_obs_bucket_to_fs(self):
        """Test case for attach_obs_bucket_to_fs

        Attach object store bucket to file system  # noqa: E501
        """
        pass

    def test_attach_obs_to_fs(self):
        """Test case for attach_obs_to_fs

        Attach object store bucket to file system  # noqa: E501
        """
        pass

    def test_create_file_system(self):
        """Test case for create_file_system

        Create file system  # noqa: E501
        """
        pass

    def test_delete_file_system(self):
        """Test case for delete_file_system

        Delete file system  # noqa: E501
        """
        pass

    def test_detach_obs_bucket_from_fs(self):
        """Test case for detach_obs_bucket_from_fs

        Detach object store bucket from file system  # noqa: E501
        """
        pass

    def test_detach_obs_from_fs(self):
        """Test case for detach_obs_from_fs

        Detach object store bucket from file system  # noqa: E501
        """
        pass

    def test_download_fs(self):
        """Test case for download_fs

        Download file system from object store  # noqa: E501
        """
        pass

    def test_get_file_system(self):
        """Test case for get_file_system

        Get file system  # noqa: E501
        """
        pass

    def test_get_file_systems(self):
        """Test case for get_file_systems

        Get all file systems  # noqa: E501
        """
        pass

    def test_update_file_system(self):
        """Test case for update_file_system

        Update file system  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
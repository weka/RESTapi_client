# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import wekarestapi
from wekarestapi.api.snapshots_api import SnapshotsApi  # noqa: E501
from wekarestapi.rest import ApiException


class TestSnapshotsApi(unittest.TestCase):
    """SnapshotsApi unit test stubs"""

    def setUp(self):
        self.api = SnapshotsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_copy_snapshot(self):
        """Test case for copy_snapshot

        Copy snapshot from the same file system  # noqa: E501
        """
        pass

    def test_create_snapshot(self):
        """Test case for create_snapshot

        Create snapshot  # noqa: E501
        """
        pass

    def test_delete_snapshot(self):
        """Test case for delete_snapshot

        Delete snapshot  # noqa: E501
        """
        pass

    def test_get_snapshot(self):
        """Test case for get_snapshot

        Get snapshot  # noqa: E501
        """
        pass

    def test_get_snapshots(self):
        """Test case for get_snapshots

        Get snapshots  # noqa: E501
        """
        pass

    def test_restore_file_system_from_snapshot(self):
        """Test case for restore_file_system_from_snapshot

        Restore file system from snapshot  # noqa: E501
        """
        pass

    def test_update_snapshot(self):
        """Test case for update_snapshot

        Update snapshot  # noqa: E501
        """
        pass

    def test_upload_snapshot(self):
        """Test case for upload_snapshot

        Upload snapshot to object store  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

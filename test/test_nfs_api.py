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
from wekarestapi.api.nfs_api import NFSApi  # noqa: E501
from wekarestapi.rest import ApiException


class TestNFSApi(unittest.TestCase):
    """NFSApi unit test stubs"""

    def setUp(self):
        self.api = NFSApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_client_group_rule(self):
        """Test case for add_client_group_rule

        create rule for nfs client group  # noqa: E501
        """
        pass

    def test_add_nfs_permission(self):
        """Test case for add_nfs_permission

        Add NFS permission  # noqa: E501
        """
        pass

    def test_create_client_group(self):
        """Test case for create_client_group

        Create nfs client group  # noqa: E501
        """
        pass

    def test_delete_client_group(self):
        """Test case for delete_client_group

        Delete nfs client group  # noqa: E501
        """
        pass

    def test_delete_client_group_rule(self):
        """Test case for delete_client_group_rule

        Delete rule for nfs client group  # noqa: E501
        """
        pass

    def test_delete_nfs_permission(self):
        """Test case for delete_nfs_permission

        Remove NFS permission  # noqa: E501
        """
        pass

    def test_get_client_group(self):
        """Test case for get_client_group

        Get nfs client group  # noqa: E501
        """
        pass

    def test_get_client_groups(self):
        """Test case for get_client_groups

        Get all nfs client groups  # noqa: E501
        """
        pass

    def test_get_nfs_global_config(self):
        """Test case for get_nfs_global_config

        Get NFS global configuration  # noqa: E501
        """
        pass

    def test_get_nfs_permission(self):
        """Test case for get_nfs_permission

        Get NFS permission  # noqa: E501
        """
        pass

    def test_get_nfs_permissions(self):
        """Test case for get_nfs_permissions

        Get NFS permissions  # noqa: E501
        """
        pass

    def test_update_nfs_global_config(self):
        """Test case for update_nfs_global_config

        Update NFS global configuration  # noqa: E501
        """
        pass

    def test_update_nfs_permission(self):
        """Test case for update_nfs_permission

        Update NFS permission  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

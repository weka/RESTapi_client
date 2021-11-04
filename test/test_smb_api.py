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
from swagger_client.api.smb_api import SMBApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSMBApi(unittest.TestCase):
    """SMBApi unit test stubs"""

    def setUp(self):
        self.api = SMBApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_samba_domain(self):
        """Test case for add_samba_domain

        Add trusted domain to smb  # noqa: E501
        """
        pass

    def test_add_share_to_samba(self):
        """Test case for add_share_to_samba

        add share to smb  # noqa: E501
        """
        pass

    def test_add_user_to_samba(self):
        """Test case for add_user_to_samba

        Add user to smb  # noqa: E501
        """
        pass

    def test_clear_samba(self):
        """Test case for clear_samba

        Clear smb cluster info  # noqa: E501
        """
        pass

    def test_delete_samba_active_directory(self):
        """Test case for delete_samba_active_directory

        Leave smb active directory  # noqa: E501
        """
        pass

    def test_delete_samba_domain(self):
        """Test case for delete_samba_domain

        Delete smb domain  # noqa: E501
        """
        pass

    def test_delete_samba_share(self):
        """Test case for delete_samba_share

        Delete smb share  # noqa: E501
        """
        pass

    def test_delete_samba_user(self):
        """Test case for delete_samba_user

        Delete smb user  # noqa: E501
        """
        pass

    def test_get_samba(self):
        """Test case for get_samba

        Get smb cluster info  # noqa: E501
        """
        pass

    def test_reset_samba_users(self):
        """Test case for reset_samba_users

        Reset smb users  # noqa: E501
        """
        pass

    def test_set_samba(self):
        """Test case for set_samba

        Set smb cluster info  # noqa: E501
        """
        pass

    def test_set_samba_active_directory(self):
        """Test case for set_samba_active_directory

        Join smb active directory  # noqa: E501
        """
        pass

    def test_set_samba_debug(self):
        """Test case for set_samba_debug

        Set smb debug level  # noqa: E501
        """
        pass

    def test_set_samba_domains(self):
        """Test case for set_samba_domains

        Get smb trusted domains  # noqa: E501
        """
        pass

    def test_set_samba_mount_options(self):
        """Test case for set_samba_mount_options

        Get smb mount options  # noqa: E501
        """
        pass

    def test_set_samba_shares(self):
        """Test case for set_samba_shares

        Get smb shares  # noqa: E501
        """
        pass

    def test_update_samba(self):
        """Test case for update_samba

        Update smb cluster info  # noqa: E501
        """
        pass

    def test_update_samba_share(self):
        """Test case for update_samba_share

        Update smb share  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

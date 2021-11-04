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
from swagger_client.api.interface_group_api import InterfaceGroupApi  # noqa: E501
from swagger_client.rest import ApiException


class TestInterfaceGroupApi(unittest.TestCase):
    """InterfaceGroupApi unit test stubs"""

    def setUp(self):
        self.api = InterfaceGroupApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_ip_range_to_interface_group(self):
        """Test case for add_ip_range_to_interface_group

        Add ip range to interface group  # noqa: E501
        """
        pass

    def test_add_port_to_interface_group(self):
        """Test case for add_port_to_interface_group

        Add port to interface group  # noqa: E501
        """
        pass

    def test_create_interface_group(self):
        """Test case for create_interface_group

        Create interface group  # noqa: E501
        """
        pass

    def test_delete_interface_group(self):
        """Test case for delete_interface_group

        delete interface group  # noqa: E501
        """
        pass

    def test_delete_ip_range_from_interface_group(self):
        """Test case for delete_ip_range_from_interface_group

        Delete ip range from interface group  # noqa: E501
        """
        pass

    def test_delete_port_from_interface_group(self):
        """Test case for delete_port_from_interface_group

        Delete port from interface group  # noqa: E501
        """
        pass

    def test_get_interface_group(self):
        """Test case for get_interface_group

        Get interface group  # noqa: E501
        """
        pass

    def test_get_interface_groups(self):
        """Test case for get_interface_groups

        Get interface groups  # noqa: E501
        """
        pass

    def test_update_interface_group(self):
        """Test case for update_interface_group

        Update interface group  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
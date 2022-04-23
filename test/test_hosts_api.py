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
from wekarestapi.api.hosts_api import HostsApi  # noqa: E501
from wekarestapi.rest import ApiException


class TestHostsApi(unittest.TestCase):
    """HostsApi unit test stubs"""

    def setUp(self):
        self.api = HostsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_host(self):
        """Test case for activate_host

        Activate host  # noqa: E501
        """
        pass

    def test_activate_hosts(self):
        """Test case for activate_hosts

        Activate hosts  # noqa: E501
        """
        pass

    def test_add_host(self):
        """Test case for add_host

        Add host to cluster  # noqa: E501
        """
        pass

    def test_apply_host(self):
        """Test case for apply_host

        Apply host  # noqa: E501
        """
        pass

    def test_apply_hosts(self):
        """Test case for apply_hosts

        Apply hosts  # noqa: E501
        """
        pass

    def test_clear_host_failure(self):
        """Test case for clear_host_failure

        Clear host last failure  # noqa: E501
        """
        pass

    def test_create_host_network(self):
        """Test case for create_host_network

        Create host network - Need to apply host after  # noqa: E501
        """
        pass

    def test_deactivate_host(self):
        """Test case for deactivate_host

        Deactivate host  # noqa: E501
        """
        pass

    def test_deactivate_hosts(self):
        """Test case for deactivate_hosts

        Deactivate hosts  # noqa: E501
        """
        pass

    def test_get_all_hosts_network(self):
        """Test case for get_all_hosts_network

        Get all hosts network  # noqa: E501
        """
        pass

    def test_get_host_network(self):
        """Test case for get_host_network

        Get host network  # noqa: E501
        """
        pass

    def test_get_host_resources(self):
        """Test case for get_host_resources

        Get host resources  # noqa: E501
        """
        pass

    def test_get_hosts(self):
        """Test case for get_hosts

        Get all hosts  # noqa: E501
        """
        pass

    def test_get_hosts_info(self):
        """Test case for get_hosts_info

        get hosts infos from IPs  # noqa: E501
        """
        pass

    def test_get_single_host(self):
        """Test case for get_single_host

        Get single host  # noqa: E501
        """
        pass

    def test_remove_host(self):
        """Test case for remove_host

        Remove host from cluster  # noqa: E501
        """
        pass

    def test_remove_host_network(self):
        """Test case for remove_host_network

        Remove host network - Need to apply host after  # noqa: E501
        """
        pass

    def test_update_host(self):
        """Test case for update_host

        Configure host - Need to apply host after  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

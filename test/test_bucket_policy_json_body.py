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
from wekarestapi.models.bucket_policy_json_body import BucketPolicyJsonBody  # noqa: E501
from wekarestapi.rest import ApiException


class TestBucketPolicyJsonBody(unittest.TestCase):
    """BucketPolicyJsonBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBucketPolicyJsonBody(self):
        """Test BucketPolicyJsonBody"""
        # FIXME: construct object with mandatory attributes with example values
        # model = wekarestapi.models.bucket_policy_json_body.BucketPolicyJsonBody()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()

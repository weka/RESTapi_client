# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class S3BucketsBody(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'bucket_name': 'str',
        'policy': 'str',
        'policy_file_content': 'str',
        'hard_quota': 'str',
        'existing_path': 'str',
        'fs_uid': 'str'
    }

    attribute_map = {
        'bucket_name': 'bucket_name',
        'policy': 'policy',
        'policy_file_content': 'policy_file_content',
        'hard_quota': 'hard_quota',
        'existing_path': 'existing_path',
        'fs_uid': 'fs_uid'
    }

    def __init__(self, bucket_name=None, policy=None, policy_file_content=None, hard_quota=None, existing_path=None, fs_uid=None):  # noqa: E501
        """S3BucketsBody - a model defined in Swagger"""  # noqa: E501
        self._bucket_name = None
        self._policy = None
        self._policy_file_content = None
        self._hard_quota = None
        self._existing_path = None
        self._fs_uid = None
        self.discriminator = None
        self.bucket_name = bucket_name
        if policy is not None:
            self.policy = policy
        if policy_file_content is not None:
            self.policy_file_content = policy_file_content
        if hard_quota is not None:
            self.hard_quota = hard_quota
        if existing_path is not None:
            self.existing_path = existing_path
        if fs_uid is not None:
            self.fs_uid = fs_uid

    @property
    def bucket_name(self):
        """Gets the bucket_name of this S3BucketsBody.  # noqa: E501

        bucket name  # noqa: E501

        :return: The bucket_name of this S3BucketsBody.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this S3BucketsBody.

        bucket name  # noqa: E501

        :param bucket_name: The bucket_name of this S3BucketsBody.  # noqa: E501
        :type: str
        """
        if bucket_name is None:
            raise ValueError("Invalid value for `bucket_name`, must not be `None`")  # noqa: E501

        self._bucket_name = bucket_name

    @property
    def policy(self):
        """Gets the policy of this S3BucketsBody.  # noqa: E501

        bucket policy  # noqa: E501

        :return: The policy of this S3BucketsBody.  # noqa: E501
        :rtype: str
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        """Sets the policy of this S3BucketsBody.

        bucket policy  # noqa: E501

        :param policy: The policy of this S3BucketsBody.  # noqa: E501
        :type: str
        """

        self._policy = policy

    @property
    def policy_file_content(self):
        """Gets the policy_file_content of this S3BucketsBody.  # noqa: E501

        S3 policy file contents  # noqa: E501

        :return: The policy_file_content of this S3BucketsBody.  # noqa: E501
        :rtype: str
        """
        return self._policy_file_content

    @policy_file_content.setter
    def policy_file_content(self, policy_file_content):
        """Sets the policy_file_content of this S3BucketsBody.

        S3 policy file contents  # noqa: E501

        :param policy_file_content: The policy_file_content of this S3BucketsBody.  # noqa: E501
        :type: str
        """

        self._policy_file_content = policy_file_content

    @property
    def hard_quota(self):
        """Gets the hard_quota of this S3BucketsBody.  # noqa: E501

        Hard limit for the bucket  # noqa: E501

        :return: The hard_quota of this S3BucketsBody.  # noqa: E501
        :rtype: str
        """
        return self._hard_quota

    @hard_quota.setter
    def hard_quota(self, hard_quota):
        """Sets the hard_quota of this S3BucketsBody.

        Hard limit for the bucket  # noqa: E501

        :param hard_quota: The hard_quota of this S3BucketsBody.  # noqa: E501
        :type: str
        """

        self._hard_quota = hard_quota

    @property
    def existing_path(self):
        """Gets the existing_path of this S3BucketsBody.  # noqa: E501

        bucket's existing path  # noqa: E501

        :return: The existing_path of this S3BucketsBody.  # noqa: E501
        :rtype: str
        """
        return self._existing_path

    @existing_path.setter
    def existing_path(self, existing_path):
        """Sets the existing_path of this S3BucketsBody.

        bucket's existing path  # noqa: E501

        :param existing_path: The existing_path of this S3BucketsBody.  # noqa: E501
        :type: str
        """

        self._existing_path = existing_path

    @property
    def fs_uid(self):
        """Gets the fs_uid of this S3BucketsBody.  # noqa: E501

        bucket's file system's uid  # noqa: E501

        :return: The fs_uid of this S3BucketsBody.  # noqa: E501
        :rtype: str
        """
        return self._fs_uid

    @fs_uid.setter
    def fs_uid(self, fs_uid):
        """Sets the fs_uid of this S3BucketsBody.

        bucket's file system's uid  # noqa: E501

        :param fs_uid: The fs_uid of this S3BucketsBody.  # noqa: E501
        :type: str
        """

        self._fs_uid = fs_uid

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(S3BucketsBody, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, S3BucketsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

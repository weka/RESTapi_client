# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.12.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20028DataRoleGroups(object):
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
        'org_admin': 'str',
        'cluster_admin': 'str',
        'read_only': 'str',
        'regular': 'str',
        's3': 'str'
    }

    attribute_map = {
        'org_admin': 'OrgAdmin',
        'cluster_admin': 'ClusterAdmin',
        'read_only': 'ReadOnly',
        'regular': 'Regular',
        's3': 'S3'
    }

    def __init__(self, org_admin=None, cluster_admin=None, read_only=None, regular=None, s3=None):  # noqa: E501
        """InlineResponse20028DataRoleGroups - a model defined in Swagger"""  # noqa: E501
        self._org_admin = None
        self._cluster_admin = None
        self._read_only = None
        self._regular = None
        self._s3 = None
        self.discriminator = None
        if org_admin is not None:
            self.org_admin = org_admin
        if cluster_admin is not None:
            self.cluster_admin = cluster_admin
        if read_only is not None:
            self.read_only = read_only
        if regular is not None:
            self.regular = regular
        if s3 is not None:
            self.s3 = s3

    @property
    def org_admin(self):
        """Gets the org_admin of this InlineResponse20028DataRoleGroups.  # noqa: E501


        :return: The org_admin of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :rtype: str
        """
        return self._org_admin

    @org_admin.setter
    def org_admin(self, org_admin):
        """Sets the org_admin of this InlineResponse20028DataRoleGroups.


        :param org_admin: The org_admin of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :type: str
        """

        self._org_admin = org_admin

    @property
    def cluster_admin(self):
        """Gets the cluster_admin of this InlineResponse20028DataRoleGroups.  # noqa: E501


        :return: The cluster_admin of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :rtype: str
        """
        return self._cluster_admin

    @cluster_admin.setter
    def cluster_admin(self, cluster_admin):
        """Sets the cluster_admin of this InlineResponse20028DataRoleGroups.


        :param cluster_admin: The cluster_admin of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :type: str
        """

        self._cluster_admin = cluster_admin

    @property
    def read_only(self):
        """Gets the read_only of this InlineResponse20028DataRoleGroups.  # noqa: E501


        :return: The read_only of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :rtype: str
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this InlineResponse20028DataRoleGroups.


        :param read_only: The read_only of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :type: str
        """

        self._read_only = read_only

    @property
    def regular(self):
        """Gets the regular of this InlineResponse20028DataRoleGroups.  # noqa: E501


        :return: The regular of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :rtype: str
        """
        return self._regular

    @regular.setter
    def regular(self, regular):
        """Sets the regular of this InlineResponse20028DataRoleGroups.


        :param regular: The regular of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :type: str
        """

        self._regular = regular

    @property
    def s3(self):
        """Gets the s3 of this InlineResponse20028DataRoleGroups.  # noqa: E501


        :return: The s3 of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :rtype: str
        """
        return self._s3

    @s3.setter
    def s3(self, s3):
        """Sets the s3 of this InlineResponse20028DataRoleGroups.


        :param s3: The s3 of this InlineResponse20028DataRoleGroups.  # noqa: E501
        :type: str
        """

        self._s3 = s3

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
        if issubclass(InlineResponse20028DataRoleGroups, dict):
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
        if not isinstance(other, InlineResponse20028DataRoleGroups):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

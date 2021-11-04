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

class FileSystemsUidBody(object):
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
        'new_name': 'str',
        'total_capacity': 'float',
        'ssd_capacity': 'float',
        'auth_required': 'bool'
    }

    attribute_map = {
        'new_name': 'new_name',
        'total_capacity': 'total_capacity',
        'ssd_capacity': 'ssd_capacity',
        'auth_required': 'auth_required'
    }

    def __init__(self, new_name=None, total_capacity=None, ssd_capacity=None, auth_required=None):  # noqa: E501
        """FileSystemsUidBody - a model defined in Swagger"""  # noqa: E501
        self._new_name = None
        self._total_capacity = None
        self._ssd_capacity = None
        self._auth_required = None
        self.discriminator = None
        if new_name is not None:
            self.new_name = new_name
        if total_capacity is not None:
            self.total_capacity = total_capacity
        if ssd_capacity is not None:
            self.ssd_capacity = ssd_capacity
        if auth_required is not None:
            self.auth_required = auth_required

    @property
    def new_name(self):
        """Gets the new_name of this FileSystemsUidBody.  # noqa: E501

        New name  # noqa: E501

        :return: The new_name of this FileSystemsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this FileSystemsUidBody.

        New name  # noqa: E501

        :param new_name: The new_name of this FileSystemsUidBody.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def total_capacity(self):
        """Gets the total_capacity of this FileSystemsUidBody.  # noqa: E501

        Total capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The total_capacity of this FileSystemsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this FileSystemsUidBody.

        Total capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param total_capacity: The total_capacity of this FileSystemsUidBody.  # noqa: E501
        :type: float
        """

        self._total_capacity = total_capacity

    @property
    def ssd_capacity(self):
        """Gets the ssd_capacity of this FileSystemsUidBody.  # noqa: E501

        SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The ssd_capacity of this FileSystemsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._ssd_capacity

    @ssd_capacity.setter
    def ssd_capacity(self, ssd_capacity):
        """Sets the ssd_capacity of this FileSystemsUidBody.

        SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param ssd_capacity: The ssd_capacity of this FileSystemsUidBody.  # noqa: E501
        :type: float
        """

        self._ssd_capacity = ssd_capacity

    @property
    def auth_required(self):
        """Gets the auth_required of this FileSystemsUidBody.  # noqa: E501

        Require the mounting user to be authenticated for mounting this filesystem. This flag is only effective in the root organization, users in non-root organizations must be authenticated to perform a mount operation  # noqa: E501

        :return: The auth_required of this FileSystemsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._auth_required

    @auth_required.setter
    def auth_required(self, auth_required):
        """Sets the auth_required of this FileSystemsUidBody.

        Require the mounting user to be authenticated for mounting this filesystem. This flag is only effective in the root organization, users in non-root organizations must be authenticated to perform a mount operation  # noqa: E501

        :param auth_required: The auth_required of this FileSystemsUidBody.  # noqa: E501
        :type: bool
        """

        self._auth_required = auth_required

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
        if issubclass(FileSystemsUidBody, dict):
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
        if not isinstance(other, FileSystemsUidBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
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

class FileSystemGroupsUidBody(object):
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
        'target_ssd_retention': 'float',
        'start_demote': 'float'
    }

    attribute_map = {
        'new_name': 'new_name',
        'target_ssd_retention': 'target_ssd_retention',
        'start_demote': 'start_demote'
    }

    def __init__(self, new_name=None, target_ssd_retention=None, start_demote=None):  # noqa: E501
        """FileSystemGroupsUidBody - a model defined in Swagger"""  # noqa: E501
        self._new_name = None
        self._target_ssd_retention = None
        self._start_demote = None
        self.discriminator = None
        if new_name is not None:
            self.new_name = new_name
        if target_ssd_retention is not None:
            self.target_ssd_retention = target_ssd_retention
        if start_demote is not None:
            self.start_demote = start_demote

    @property
    def new_name(self):
        """Gets the new_name of this FileSystemGroupsUidBody.  # noqa: E501

        Filesystem group name  # noqa: E501

        :return: The new_name of this FileSystemGroupsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this FileSystemGroupsUidBody.

        Filesystem group name  # noqa: E501

        :param new_name: The new_name of this FileSystemGroupsUidBody.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def target_ssd_retention(self):
        """Gets the target_ssd_retention of this FileSystemGroupsUidBody.  # noqa: E501

        SSD retention period  # noqa: E501

        :return: The target_ssd_retention of this FileSystemGroupsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._target_ssd_retention

    @target_ssd_retention.setter
    def target_ssd_retention(self, target_ssd_retention):
        """Sets the target_ssd_retention of this FileSystemGroupsUidBody.

        SSD retention period  # noqa: E501

        :param target_ssd_retention: The target_ssd_retention of this FileSystemGroupsUidBody.  # noqa: E501
        :type: float
        """

        self._target_ssd_retention = target_ssd_retention

    @property
    def start_demote(self):
        """Gets the start_demote of this FileSystemGroupsUidBody.  # noqa: E501

        The retention period according to the amount of data that will be created  # noqa: E501

        :return: The start_demote of this FileSystemGroupsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._start_demote

    @start_demote.setter
    def start_demote(self, start_demote):
        """Sets the start_demote of this FileSystemGroupsUidBody.

        The retention period according to the amount of data that will be created  # noqa: E501

        :param start_demote: The start_demote of this FileSystemGroupsUidBody.  # noqa: E501
        :type: float
        """

        self._start_demote = start_demote

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
        if issubclass(FileSystemGroupsUidBody, dict):
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
        if not isinstance(other, FileSystemGroupsUidBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

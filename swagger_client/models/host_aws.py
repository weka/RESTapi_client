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

class HostAws(object):
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
        'availability_zone': 'str',
        'instance_id': 'str',
        'instance_type': 'str'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'instance_id': 'instance_id',
        'instance_type': 'instance_type'
    }

    def __init__(self, availability_zone=None, instance_id=None, instance_type=None):  # noqa: E501
        """HostAws - a model defined in Swagger"""  # noqa: E501
        self._availability_zone = None
        self._instance_id = None
        self._instance_type = None
        self.discriminator = None
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_type is not None:
            self.instance_type = instance_type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this HostAws.  # noqa: E501


        :return: The availability_zone of this HostAws.  # noqa: E501
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this HostAws.


        :param availability_zone: The availability_zone of this HostAws.  # noqa: E501
        :type: str
        """

        self._availability_zone = availability_zone

    @property
    def instance_id(self):
        """Gets the instance_id of this HostAws.  # noqa: E501


        :return: The instance_id of this HostAws.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this HostAws.


        :param instance_id: The instance_id of this HostAws.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_type(self):
        """Gets the instance_type of this HostAws.  # noqa: E501


        :return: The instance_type of this HostAws.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this HostAws.


        :param instance_type: The instance_type of this HostAws.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

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
        if issubclass(HostAws, dict):
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
        if not isinstance(other, HostAws):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

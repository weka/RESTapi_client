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

class NfsGlobalConfigBody(object):
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
        'mountd_port': 'int'
    }

    attribute_map = {
        'mountd_port': 'mountd_port'
    }

    def __init__(self, mountd_port=None):  # noqa: E501
        """NfsGlobalConfigBody - a model defined in Swagger"""  # noqa: E501
        self._mountd_port = None
        self.discriminator = None
        if mountd_port is not None:
            self.mountd_port = mountd_port

    @property
    def mountd_port(self):
        """Gets the mountd_port of this NfsGlobalConfigBody.  # noqa: E501

        mountd listening port  # noqa: E501

        :return: The mountd_port of this NfsGlobalConfigBody.  # noqa: E501
        :rtype: int
        """
        return self._mountd_port

    @mountd_port.setter
    def mountd_port(self, mountd_port):
        """Sets the mountd_port of this NfsGlobalConfigBody.

        mountd listening port  # noqa: E501

        :param mountd_port: The mountd_port of this NfsGlobalConfigBody.  # noqa: E501
        :type: int
        """

        self._mountd_port = mountd_port

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
        if issubclass(NfsGlobalConfigBody, dict):
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
        if not isinstance(other, NfsGlobalConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

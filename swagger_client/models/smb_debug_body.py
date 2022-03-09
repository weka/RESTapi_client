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

class SmbDebugBody(object):
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
        'debug_level': 'float',
        'samba_hosts': 'list[str]'
    }

    attribute_map = {
        'debug_level': 'debug_level',
        'samba_hosts': 'samba_hosts'
    }

    def __init__(self, debug_level=None, samba_hosts=None):  # noqa: E501
        """SmbDebugBody - a model defined in Swagger"""  # noqa: E501
        self._debug_level = None
        self._samba_hosts = None
        self.discriminator = None
        self.debug_level = debug_level
        if samba_hosts is not None:
            self.samba_hosts = samba_hosts

    @property
    def debug_level(self):
        """Gets the debug_level of this SmbDebugBody.  # noqa: E501

        The debug level (format - 0..10)  # noqa: E501

        :return: The debug_level of this SmbDebugBody.  # noqa: E501
        :rtype: float
        """
        return self._debug_level

    @debug_level.setter
    def debug_level(self, debug_level):
        """Sets the debug_level of this SmbDebugBody.

        The debug level (format - 0..10)  # noqa: E501

        :param debug_level: The debug_level of this SmbDebugBody.  # noqa: E501
        :type: float
        """
        if debug_level is None:
            raise ValueError("Invalid value for `debug_level`, must not be `None`")  # noqa: E501

        self._debug_level = debug_level

    @property
    def samba_hosts(self):
        """Gets the samba_hosts of this SmbDebugBody.  # noqa: E501

        Hosts to set debug level (pass host uid). All hosts as default  # noqa: E501

        :return: The samba_hosts of this SmbDebugBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._samba_hosts

    @samba_hosts.setter
    def samba_hosts(self, samba_hosts):
        """Sets the samba_hosts of this SmbDebugBody.

        Hosts to set debug level (pass host uid). All hosts as default  # noqa: E501

        :param samba_hosts: The samba_hosts of this SmbDebugBody.  # noqa: E501
        :type: list[str]
        """

        self._samba_hosts = samba_hosts

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
        if issubclass(SmbDebugBody, dict):
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
        if not isinstance(other, SmbDebugBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

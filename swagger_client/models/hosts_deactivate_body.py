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

class HostsDeactivateBody(object):
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
        'host_uids': 'list[str]'
    }

    attribute_map = {
        'host_uids': 'host_uids'
    }

    def __init__(self, host_uids=None):  # noqa: E501
        """HostsDeactivateBody - a model defined in Swagger"""  # noqa: E501
        self._host_uids = None
        self.discriminator = None
        self.host_uids = host_uids

    @property
    def host_uids(self):
        """Gets the host_uids of this HostsDeactivateBody.  # noqa: E501

        Host uids to deactivate  # noqa: E501

        :return: The host_uids of this HostsDeactivateBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_uids

    @host_uids.setter
    def host_uids(self, host_uids):
        """Sets the host_uids of this HostsDeactivateBody.

        Host uids to deactivate  # noqa: E501

        :param host_uids: The host_uids of this HostsDeactivateBody.  # noqa: E501
        :type: list[str]
        """
        if host_uids is None:
            raise ValueError("Invalid value for `host_uids`, must not be `None`")  # noqa: E501

        self._host_uids = host_uids

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
        if issubclass(HostsDeactivateBody, dict):
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
        if not isinstance(other, HostsDeactivateBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

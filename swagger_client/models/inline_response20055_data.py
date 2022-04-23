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

class InlineResponse20055Data(object):
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
        '_0x0000092ddf3d00000': 'InlineResponse20055Data0x0000092ddf3d00000'
    }

    attribute_map = {
        '_0x0000092ddf3d00000': '0x0000092ddf3d0000:0'
    }

    def __init__(self, _0x0000092ddf3d00000=None):  # noqa: E501
        """InlineResponse20055Data - a model defined in Swagger"""  # noqa: E501
        self.__0x0000092ddf3d00000 = None
        self.discriminator = None
        if _0x0000092ddf3d00000 is not None:
            self._0x0000092ddf3d00000 = _0x0000092ddf3d00000

    @property
    def _0x0000092ddf3d00000(self):
        """Gets the _0x0000092ddf3d00000 of this InlineResponse20055Data.  # noqa: E501


        :return: The _0x0000092ddf3d00000 of this InlineResponse20055Data.  # noqa: E501
        :rtype: InlineResponse20055Data0x0000092ddf3d00000
        """
        return self.__0x0000092ddf3d00000

    @_0x0000092ddf3d00000.setter
    def _0x0000092ddf3d00000(self, _0x0000092ddf3d00000):
        """Sets the _0x0000092ddf3d00000 of this InlineResponse20055Data.


        :param _0x0000092ddf3d00000: The _0x0000092ddf3d00000 of this InlineResponse20055Data.  # noqa: E501
        :type: InlineResponse20055Data0x0000092ddf3d00000
        """

        self.__0x0000092ddf3d00000 = _0x0000092ddf3d00000

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
        if issubclass(InlineResponse20055Data, dict):
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
        if not isinstance(other, InlineResponse20055Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
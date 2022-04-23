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

class InlineResponse20034Data(object):
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
        'kms_type': 'str',
        'params': 'InlineResponse20034DataParams'
    }

    attribute_map = {
        'kms_type': 'kms_type',
        'params': 'params'
    }

    def __init__(self, kms_type=None, params=None):  # noqa: E501
        """InlineResponse20034Data - a model defined in Swagger"""  # noqa: E501
        self._kms_type = None
        self._params = None
        self.discriminator = None
        if kms_type is not None:
            self.kms_type = kms_type
        if params is not None:
            self.params = params

    @property
    def kms_type(self):
        """Gets the kms_type of this InlineResponse20034Data.  # noqa: E501


        :return: The kms_type of this InlineResponse20034Data.  # noqa: E501
        :rtype: str
        """
        return self._kms_type

    @kms_type.setter
    def kms_type(self, kms_type):
        """Sets the kms_type of this InlineResponse20034Data.


        :param kms_type: The kms_type of this InlineResponse20034Data.  # noqa: E501
        :type: str
        """

        self._kms_type = kms_type

    @property
    def params(self):
        """Gets the params of this InlineResponse20034Data.  # noqa: E501


        :return: The params of this InlineResponse20034Data.  # noqa: E501
        :rtype: InlineResponse20034DataParams
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this InlineResponse20034Data.


        :param params: The params of this InlineResponse20034Data.  # noqa: E501
        :type: InlineResponse20034DataParams
        """

        self._params = params

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
        if issubclass(InlineResponse20034Data, dict):
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
        if not isinstance(other, InlineResponse20034Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

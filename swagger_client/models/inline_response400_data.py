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

class InlineResponse400Data(object):
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
        'missing_params': 'list[str]',
        'param': 'str',
        'error': 'str'
    }

    attribute_map = {
        'missing_params': 'missing_params',
        'param': 'param',
        'error': 'error'
    }

    def __init__(self, missing_params=None, param=None, error=None):  # noqa: E501
        """InlineResponse400Data - a model defined in Swagger"""  # noqa: E501
        self._missing_params = None
        self._param = None
        self._error = None
        self.discriminator = None
        if missing_params is not None:
            self.missing_params = missing_params
        if param is not None:
            self.param = param
        if error is not None:
            self.error = error

    @property
    def missing_params(self):
        """Gets the missing_params of this InlineResponse400Data.  # noqa: E501


        :return: The missing_params of this InlineResponse400Data.  # noqa: E501
        :rtype: list[str]
        """
        return self._missing_params

    @missing_params.setter
    def missing_params(self, missing_params):
        """Sets the missing_params of this InlineResponse400Data.


        :param missing_params: The missing_params of this InlineResponse400Data.  # noqa: E501
        :type: list[str]
        """

        self._missing_params = missing_params

    @property
    def param(self):
        """Gets the param of this InlineResponse400Data.  # noqa: E501


        :return: The param of this InlineResponse400Data.  # noqa: E501
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this InlineResponse400Data.


        :param param: The param of this InlineResponse400Data.  # noqa: E501
        :type: str
        """

        self._param = param

    @property
    def error(self):
        """Gets the error of this InlineResponse400Data.  # noqa: E501


        :return: The error of this InlineResponse400Data.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this InlineResponse400Data.


        :param error: The error of this InlineResponse400Data.  # noqa: E501
        :type: str
        """

        self._error = error

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
        if issubclass(InlineResponse400Data, dict):
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
        if not isinstance(other, InlineResponse400Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

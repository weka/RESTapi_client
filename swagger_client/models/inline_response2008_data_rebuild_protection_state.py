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

class InlineResponse2008DataRebuildProtectionState(object):
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
        'percent': 'float',
        'num_failures': 'float',
        'mi_b': 'float'
    }

    attribute_map = {
        'percent': 'percent',
        'num_failures': 'numFailures',
        'mi_b': 'MiB'
    }

    def __init__(self, percent=None, num_failures=None, mi_b=None):  # noqa: E501
        """InlineResponse2008DataRebuildProtectionState - a model defined in Swagger"""  # noqa: E501
        self._percent = None
        self._num_failures = None
        self._mi_b = None
        self.discriminator = None
        if percent is not None:
            self.percent = percent
        if num_failures is not None:
            self.num_failures = num_failures
        if mi_b is not None:
            self.mi_b = mi_b

    @property
    def percent(self):
        """Gets the percent of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501


        :return: The percent of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this InlineResponse2008DataRebuildProtectionState.


        :param percent: The percent of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501
        :type: float
        """

        self._percent = percent

    @property
    def num_failures(self):
        """Gets the num_failures of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501


        :return: The num_failures of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501
        :rtype: float
        """
        return self._num_failures

    @num_failures.setter
    def num_failures(self, num_failures):
        """Sets the num_failures of this InlineResponse2008DataRebuildProtectionState.


        :param num_failures: The num_failures of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501
        :type: float
        """

        self._num_failures = num_failures

    @property
    def mi_b(self):
        """Gets the mi_b of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501


        :return: The mi_b of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501
        :rtype: float
        """
        return self._mi_b

    @mi_b.setter
    def mi_b(self, mi_b):
        """Sets the mi_b of this InlineResponse2008DataRebuildProtectionState.


        :param mi_b: The mi_b of this InlineResponse2008DataRebuildProtectionState.  # noqa: E501
        :type: float
        """

        self._mi_b = mi_b

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
        if issubclass(InlineResponse2008DataRebuildProtectionState, dict):
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
        if not isinstance(other, InlineResponse2008DataRebuildProtectionState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

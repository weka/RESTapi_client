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

class InlineResponse2005Data(object):
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
        'failures': 'object',
        'guid': 'str',
        'success': 'object'
    }

    attribute_map = {
        'failures': 'failures',
        'guid': 'guid',
        'success': 'success'
    }

    def __init__(self, failures=None, guid=None, success=None):  # noqa: E501
        """InlineResponse2005Data - a model defined in Swagger"""  # noqa: E501
        self._failures = None
        self._guid = None
        self._success = None
        self.discriminator = None
        if failures is not None:
            self.failures = failures
        if guid is not None:
            self.guid = guid
        if success is not None:
            self.success = success

    @property
    def failures(self):
        """Gets the failures of this InlineResponse2005Data.  # noqa: E501


        :return: The failures of this InlineResponse2005Data.  # noqa: E501
        :rtype: object
        """
        return self._failures

    @failures.setter
    def failures(self, failures):
        """Sets the failures of this InlineResponse2005Data.


        :param failures: The failures of this InlineResponse2005Data.  # noqa: E501
        :type: object
        """

        self._failures = failures

    @property
    def guid(self):
        """Gets the guid of this InlineResponse2005Data.  # noqa: E501


        :return: The guid of this InlineResponse2005Data.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this InlineResponse2005Data.


        :param guid: The guid of this InlineResponse2005Data.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def success(self):
        """Gets the success of this InlineResponse2005Data.  # noqa: E501


        :return: The success of this InlineResponse2005Data.  # noqa: E501
        :rtype: object
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this InlineResponse2005Data.


        :param success: The success of this InlineResponse2005Data.  # noqa: E501
        :type: object
        """

        self._success = success

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
        if issubclass(InlineResponse2005Data, dict):
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
        if not isinstance(other, InlineResponse2005Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

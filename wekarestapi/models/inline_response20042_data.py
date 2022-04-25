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

class InlineResponse20042Data(object):
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
        'id': 'str',
        'name': 'str',
        'rules': 'list[object]',
        'uid': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'rules': 'rules',
        'uid': 'uid'
    }

    def __init__(self, id=None, name=None, rules=None, uid=None):  # noqa: E501
        """InlineResponse20042Data - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._rules = None
        self._uid = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules
        if uid is not None:
            self.uid = uid

    @property
    def id(self):
        """Gets the id of this InlineResponse20042Data.  # noqa: E501


        :return: The id of this InlineResponse20042Data.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20042Data.


        :param id: The id of this InlineResponse20042Data.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20042Data.  # noqa: E501


        :return: The name of this InlineResponse20042Data.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20042Data.


        :param name: The name of this InlineResponse20042Data.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def rules(self):
        """Gets the rules of this InlineResponse20042Data.  # noqa: E501


        :return: The rules of this InlineResponse20042Data.  # noqa: E501
        :rtype: list[object]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this InlineResponse20042Data.


        :param rules: The rules of this InlineResponse20042Data.  # noqa: E501
        :type: list[object]
        """

        self._rules = rules

    @property
    def uid(self):
        """Gets the uid of this InlineResponse20042Data.  # noqa: E501


        :return: The uid of this InlineResponse20042Data.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this InlineResponse20042Data.


        :param uid: The uid of this InlineResponse20042Data.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(InlineResponse20042Data, dict):
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
        if not isinstance(other, InlineResponse20042Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
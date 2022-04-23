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

class InlineResponse20083Data(object):
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
        'org_id': 'float',
        'org_name': 'str',
        'role': 'str',
        'source': 'str',
        'username': 'str'
    }

    attribute_map = {
        'org_id': 'org_id',
        'org_name': 'org_name',
        'role': 'role',
        'source': 'source',
        'username': 'username'
    }

    def __init__(self, org_id=None, org_name=None, role=None, source=None, username=None):  # noqa: E501
        """InlineResponse20083Data - a model defined in Swagger"""  # noqa: E501
        self._org_id = None
        self._org_name = None
        self._role = None
        self._source = None
        self._username = None
        self.discriminator = None
        if org_id is not None:
            self.org_id = org_id
        if org_name is not None:
            self.org_name = org_name
        if role is not None:
            self.role = role
        if source is not None:
            self.source = source
        if username is not None:
            self.username = username

    @property
    def org_id(self):
        """Gets the org_id of this InlineResponse20083Data.  # noqa: E501


        :return: The org_id of this InlineResponse20083Data.  # noqa: E501
        :rtype: float
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this InlineResponse20083Data.


        :param org_id: The org_id of this InlineResponse20083Data.  # noqa: E501
        :type: float
        """

        self._org_id = org_id

    @property
    def org_name(self):
        """Gets the org_name of this InlineResponse20083Data.  # noqa: E501


        :return: The org_name of this InlineResponse20083Data.  # noqa: E501
        :rtype: str
        """
        return self._org_name

    @org_name.setter
    def org_name(self, org_name):
        """Sets the org_name of this InlineResponse20083Data.


        :param org_name: The org_name of this InlineResponse20083Data.  # noqa: E501
        :type: str
        """

        self._org_name = org_name

    @property
    def role(self):
        """Gets the role of this InlineResponse20083Data.  # noqa: E501


        :return: The role of this InlineResponse20083Data.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this InlineResponse20083Data.


        :param role: The role of this InlineResponse20083Data.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def source(self):
        """Gets the source of this InlineResponse20083Data.  # noqa: E501


        :return: The source of this InlineResponse20083Data.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this InlineResponse20083Data.


        :param source: The source of this InlineResponse20083Data.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def username(self):
        """Gets the username of this InlineResponse20083Data.  # noqa: E501


        :return: The username of this InlineResponse20083Data.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this InlineResponse20083Data.


        :param username: The username of this InlineResponse20083Data.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(InlineResponse20083Data, dict):
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
        if not isinstance(other, InlineResponse20083Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
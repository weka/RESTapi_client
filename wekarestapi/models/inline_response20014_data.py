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

class InlineResponse20014Data(object):
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
        'time': 'str',
        'hash': 'float',
        'entity': 'str',
        'severity': 'str',
        'permission': 'str',
        'category': 'str',
        'event_fields': 'InlineResponse20014EventFields',
        'type': 'str',
        'nid': 'str'
    }

    attribute_map = {
        'time': 'time',
        'hash': 'hash',
        'entity': 'entity',
        'severity': 'severity',
        'permission': 'permission',
        'category': 'category',
        'event_fields': 'eventFields',
        'type': 'type',
        'nid': 'nid'
    }

    def __init__(self, time=None, hash=None, entity=None, severity=None, permission=None, category=None, event_fields=None, type=None, nid=None):  # noqa: E501
        """InlineResponse20014Data - a model defined in Swagger"""  # noqa: E501
        self._time = None
        self._hash = None
        self._entity = None
        self._severity = None
        self._permission = None
        self._category = None
        self._event_fields = None
        self._type = None
        self._nid = None
        self.discriminator = None
        if time is not None:
            self.time = time
        if hash is not None:
            self.hash = hash
        if entity is not None:
            self.entity = entity
        if severity is not None:
            self.severity = severity
        if permission is not None:
            self.permission = permission
        if category is not None:
            self.category = category
        if event_fields is not None:
            self.event_fields = event_fields
        if type is not None:
            self.type = type
        if nid is not None:
            self.nid = nid

    @property
    def time(self):
        """Gets the time of this InlineResponse20014Data.  # noqa: E501


        :return: The time of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this InlineResponse20014Data.


        :param time: The time of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._time = time

    @property
    def hash(self):
        """Gets the hash of this InlineResponse20014Data.  # noqa: E501


        :return: The hash of this InlineResponse20014Data.  # noqa: E501
        :rtype: float
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this InlineResponse20014Data.


        :param hash: The hash of this InlineResponse20014Data.  # noqa: E501
        :type: float
        """

        self._hash = hash

    @property
    def entity(self):
        """Gets the entity of this InlineResponse20014Data.  # noqa: E501


        :return: The entity of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this InlineResponse20014Data.


        :param entity: The entity of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._entity = entity

    @property
    def severity(self):
        """Gets the severity of this InlineResponse20014Data.  # noqa: E501


        :return: The severity of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this InlineResponse20014Data.


        :param severity: The severity of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._severity = severity

    @property
    def permission(self):
        """Gets the permission of this InlineResponse20014Data.  # noqa: E501


        :return: The permission of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this InlineResponse20014Data.


        :param permission: The permission of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._permission = permission

    @property
    def category(self):
        """Gets the category of this InlineResponse20014Data.  # noqa: E501


        :return: The category of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this InlineResponse20014Data.


        :param category: The category of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def event_fields(self):
        """Gets the event_fields of this InlineResponse20014Data.  # noqa: E501


        :return: The event_fields of this InlineResponse20014Data.  # noqa: E501
        :rtype: InlineResponse20014EventFields
        """
        return self._event_fields

    @event_fields.setter
    def event_fields(self, event_fields):
        """Sets the event_fields of this InlineResponse20014Data.


        :param event_fields: The event_fields of this InlineResponse20014Data.  # noqa: E501
        :type: InlineResponse20014EventFields
        """

        self._event_fields = event_fields

    @property
    def type(self):
        """Gets the type of this InlineResponse20014Data.  # noqa: E501


        :return: The type of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20014Data.


        :param type: The type of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def nid(self):
        """Gets the nid of this InlineResponse20014Data.  # noqa: E501


        :return: The nid of this InlineResponse20014Data.  # noqa: E501
        :rtype: str
        """
        return self._nid

    @nid.setter
    def nid(self, nid):
        """Sets the nid of this InlineResponse20014Data.


        :param nid: The nid of this InlineResponse20014Data.  # noqa: E501
        :type: str
        """

        self._nid = nid

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
        if issubclass(InlineResponse20014Data, dict):
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
        if not isinstance(other, InlineResponse20014Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

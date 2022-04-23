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

class MachinesNodes(object):
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
        'dedicated_core': 'bool',
        'roles': 'list[str]',
        'status': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'dedicated_core': 'dedicated_core',
        'roles': 'roles',
        'status': 'status',
        'uid': 'uid'
    }

    def __init__(self, dedicated_core=None, roles=None, status=None, uid=None):  # noqa: E501
        """MachinesNodes - a model defined in Swagger"""  # noqa: E501
        self._dedicated_core = None
        self._roles = None
        self._status = None
        self._uid = None
        self.discriminator = None
        if dedicated_core is not None:
            self.dedicated_core = dedicated_core
        if roles is not None:
            self.roles = roles
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid

    @property
    def dedicated_core(self):
        """Gets the dedicated_core of this MachinesNodes.  # noqa: E501


        :return: The dedicated_core of this MachinesNodes.  # noqa: E501
        :rtype: bool
        """
        return self._dedicated_core

    @dedicated_core.setter
    def dedicated_core(self, dedicated_core):
        """Sets the dedicated_core of this MachinesNodes.


        :param dedicated_core: The dedicated_core of this MachinesNodes.  # noqa: E501
        :type: bool
        """

        self._dedicated_core = dedicated_core

    @property
    def roles(self):
        """Gets the roles of this MachinesNodes.  # noqa: E501


        :return: The roles of this MachinesNodes.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this MachinesNodes.


        :param roles: The roles of this MachinesNodes.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def status(self):
        """Gets the status of this MachinesNodes.  # noqa: E501


        :return: The status of this MachinesNodes.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MachinesNodes.


        :param status: The status of this MachinesNodes.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this MachinesNodes.  # noqa: E501


        :return: The uid of this MachinesNodes.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this MachinesNodes.


        :param uid: The uid of this MachinesNodes.  # noqa: E501
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
        if issubclass(MachinesNodes, dict):
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
        if not isinstance(other, MachinesNodes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class InterfaceGroup(object):
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
        'subnet_mask': 'str',
        'ports': 'list[InterfaceGroupPorts]',
        'name': 'str',
        'uid': 'str',
        'ips': 'list[str]',
        'allow_manage_gids': 'bool',
        'type': 'str',
        'gateway': 'str',
        'status': 'str'
    }

    attribute_map = {
        'subnet_mask': 'subnet_mask',
        'ports': 'ports',
        'name': 'name',
        'uid': 'uid',
        'ips': 'ips',
        'allow_manage_gids': 'allow_manage_gids',
        'type': 'type',
        'gateway': 'gateway',
        'status': 'status'
    }

    def __init__(self, subnet_mask=None, ports=None, name=None, uid=None, ips=None, allow_manage_gids=None, type=None, gateway=None, status=None):  # noqa: E501
        """InterfaceGroup - a model defined in Swagger"""  # noqa: E501
        self._subnet_mask = None
        self._ports = None
        self._name = None
        self._uid = None
        self._ips = None
        self._allow_manage_gids = None
        self._type = None
        self._gateway = None
        self._status = None
        self.discriminator = None
        if subnet_mask is not None:
            self.subnet_mask = subnet_mask
        if ports is not None:
            self.ports = ports
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if ips is not None:
            self.ips = ips
        if allow_manage_gids is not None:
            self.allow_manage_gids = allow_manage_gids
        if type is not None:
            self.type = type
        if gateway is not None:
            self.gateway = gateway
        if status is not None:
            self.status = status

    @property
    def subnet_mask(self):
        """Gets the subnet_mask of this InterfaceGroup.  # noqa: E501


        :return: The subnet_mask of this InterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._subnet_mask

    @subnet_mask.setter
    def subnet_mask(self, subnet_mask):
        """Sets the subnet_mask of this InterfaceGroup.


        :param subnet_mask: The subnet_mask of this InterfaceGroup.  # noqa: E501
        :type: str
        """

        self._subnet_mask = subnet_mask

    @property
    def ports(self):
        """Gets the ports of this InterfaceGroup.  # noqa: E501


        :return: The ports of this InterfaceGroup.  # noqa: E501
        :rtype: list[InterfaceGroupPorts]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this InterfaceGroup.


        :param ports: The ports of this InterfaceGroup.  # noqa: E501
        :type: list[InterfaceGroupPorts]
        """

        self._ports = ports

    @property
    def name(self):
        """Gets the name of this InterfaceGroup.  # noqa: E501


        :return: The name of this InterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InterfaceGroup.


        :param name: The name of this InterfaceGroup.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this InterfaceGroup.  # noqa: E501


        :return: The uid of this InterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this InterfaceGroup.


        :param uid: The uid of this InterfaceGroup.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def ips(self):
        """Gets the ips of this InterfaceGroup.  # noqa: E501


        :return: The ips of this InterfaceGroup.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this InterfaceGroup.


        :param ips: The ips of this InterfaceGroup.  # noqa: E501
        :type: list[str]
        """

        self._ips = ips

    @property
    def allow_manage_gids(self):
        """Gets the allow_manage_gids of this InterfaceGroup.  # noqa: E501


        :return: The allow_manage_gids of this InterfaceGroup.  # noqa: E501
        :rtype: bool
        """
        return self._allow_manage_gids

    @allow_manage_gids.setter
    def allow_manage_gids(self, allow_manage_gids):
        """Sets the allow_manage_gids of this InterfaceGroup.


        :param allow_manage_gids: The allow_manage_gids of this InterfaceGroup.  # noqa: E501
        :type: bool
        """

        self._allow_manage_gids = allow_manage_gids

    @property
    def type(self):
        """Gets the type of this InterfaceGroup.  # noqa: E501


        :return: The type of this InterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterfaceGroup.


        :param type: The type of this InterfaceGroup.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def gateway(self):
        """Gets the gateway of this InterfaceGroup.  # noqa: E501


        :return: The gateway of this InterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this InterfaceGroup.


        :param gateway: The gateway of this InterfaceGroup.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def status(self):
        """Gets the status of this InterfaceGroup.  # noqa: E501


        :return: The status of this InterfaceGroup.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InterfaceGroup.


        :param status: The status of this InterfaceGroup.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(InterfaceGroup, dict):
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
        if not isinstance(other, InterfaceGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

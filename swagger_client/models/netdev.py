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

class Netdev(object):
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
        'id_type': 'str',
        'netmask_bits': 'float',
        'owner_nodes': 'list[str]',
        'name': 'str',
        'uid': 'str',
        'hostname': 'str',
        'net_devices': 'list[NetdevNetDevices]',
        'ips': 'list[str]',
        'max_cores': 'float',
        'vlan_id': 'str',
        'gateway': 'str',
        'host_id': 'str',
        'identifier': 'str',
        'network_label': 'str'
    }

    attribute_map = {
        'id': 'id',
        'id_type': 'id_type',
        'netmask_bits': 'netmask_bits',
        'owner_nodes': 'owner_nodes',
        'name': 'name',
        'uid': 'uid',
        'hostname': 'hostname',
        'net_devices': 'net_devices',
        'ips': 'ips',
        'max_cores': 'max_cores',
        'vlan_id': 'vlan_id',
        'gateway': 'gateway',
        'host_id': 'host_id',
        'identifier': 'identifier',
        'network_label': 'network_label'
    }

    def __init__(self, id=None, id_type=None, netmask_bits=None, owner_nodes=None, name=None, uid=None, hostname=None, net_devices=None, ips=None, max_cores=None, vlan_id=None, gateway=None, host_id=None, identifier=None, network_label=None):  # noqa: E501
        """Netdev - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._id_type = None
        self._netmask_bits = None
        self._owner_nodes = None
        self._name = None
        self._uid = None
        self._hostname = None
        self._net_devices = None
        self._ips = None
        self._max_cores = None
        self._vlan_id = None
        self._gateway = None
        self._host_id = None
        self._identifier = None
        self._network_label = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if id_type is not None:
            self.id_type = id_type
        if netmask_bits is not None:
            self.netmask_bits = netmask_bits
        if owner_nodes is not None:
            self.owner_nodes = owner_nodes
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if hostname is not None:
            self.hostname = hostname
        if net_devices is not None:
            self.net_devices = net_devices
        if ips is not None:
            self.ips = ips
        if max_cores is not None:
            self.max_cores = max_cores
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if gateway is not None:
            self.gateway = gateway
        if host_id is not None:
            self.host_id = host_id
        if identifier is not None:
            self.identifier = identifier
        if network_label is not None:
            self.network_label = network_label

    @property
    def id(self):
        """Gets the id of this Netdev.  # noqa: E501


        :return: The id of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Netdev.


        :param id: The id of this Netdev.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def id_type(self):
        """Gets the id_type of this Netdev.  # noqa: E501


        :return: The id_type of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        """Sets the id_type of this Netdev.


        :param id_type: The id_type of this Netdev.  # noqa: E501
        :type: str
        """

        self._id_type = id_type

    @property
    def netmask_bits(self):
        """Gets the netmask_bits of this Netdev.  # noqa: E501


        :return: The netmask_bits of this Netdev.  # noqa: E501
        :rtype: float
        """
        return self._netmask_bits

    @netmask_bits.setter
    def netmask_bits(self, netmask_bits):
        """Sets the netmask_bits of this Netdev.


        :param netmask_bits: The netmask_bits of this Netdev.  # noqa: E501
        :type: float
        """

        self._netmask_bits = netmask_bits

    @property
    def owner_nodes(self):
        """Gets the owner_nodes of this Netdev.  # noqa: E501


        :return: The owner_nodes of this Netdev.  # noqa: E501
        :rtype: list[str]
        """
        return self._owner_nodes

    @owner_nodes.setter
    def owner_nodes(self, owner_nodes):
        """Sets the owner_nodes of this Netdev.


        :param owner_nodes: The owner_nodes of this Netdev.  # noqa: E501
        :type: list[str]
        """

        self._owner_nodes = owner_nodes

    @property
    def name(self):
        """Gets the name of this Netdev.  # noqa: E501


        :return: The name of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Netdev.


        :param name: The name of this Netdev.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def uid(self):
        """Gets the uid of this Netdev.  # noqa: E501


        :return: The uid of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Netdev.


        :param uid: The uid of this Netdev.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def hostname(self):
        """Gets the hostname of this Netdev.  # noqa: E501


        :return: The hostname of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Netdev.


        :param hostname: The hostname of this Netdev.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def net_devices(self):
        """Gets the net_devices of this Netdev.  # noqa: E501


        :return: The net_devices of this Netdev.  # noqa: E501
        :rtype: list[NetdevNetDevices]
        """
        return self._net_devices

    @net_devices.setter
    def net_devices(self, net_devices):
        """Sets the net_devices of this Netdev.


        :param net_devices: The net_devices of this Netdev.  # noqa: E501
        :type: list[NetdevNetDevices]
        """

        self._net_devices = net_devices

    @property
    def ips(self):
        """Gets the ips of this Netdev.  # noqa: E501


        :return: The ips of this Netdev.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this Netdev.


        :param ips: The ips of this Netdev.  # noqa: E501
        :type: list[str]
        """

        self._ips = ips

    @property
    def max_cores(self):
        """Gets the max_cores of this Netdev.  # noqa: E501


        :return: The max_cores of this Netdev.  # noqa: E501
        :rtype: float
        """
        return self._max_cores

    @max_cores.setter
    def max_cores(self, max_cores):
        """Sets the max_cores of this Netdev.


        :param max_cores: The max_cores of this Netdev.  # noqa: E501
        :type: float
        """

        self._max_cores = max_cores

    @property
    def vlan_id(self):
        """Gets the vlan_id of this Netdev.  # noqa: E501


        :return: The vlan_id of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this Netdev.


        :param vlan_id: The vlan_id of this Netdev.  # noqa: E501
        :type: str
        """

        self._vlan_id = vlan_id

    @property
    def gateway(self):
        """Gets the gateway of this Netdev.  # noqa: E501


        :return: The gateway of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this Netdev.


        :param gateway: The gateway of this Netdev.  # noqa: E501
        :type: str
        """

        self._gateway = gateway

    @property
    def host_id(self):
        """Gets the host_id of this Netdev.  # noqa: E501


        :return: The host_id of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this Netdev.


        :param host_id: The host_id of this Netdev.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def identifier(self):
        """Gets the identifier of this Netdev.  # noqa: E501


        :return: The identifier of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Netdev.


        :param identifier: The identifier of this Netdev.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def network_label(self):
        """Gets the network_label of this Netdev.  # noqa: E501


        :return: The network_label of this Netdev.  # noqa: E501
        :rtype: str
        """
        return self._network_label

    @network_label.setter
    def network_label(self, network_label):
        """Sets the network_label of this Netdev.


        :param network_label: The network_label of this Netdev.  # noqa: E501
        :type: str
        """

        self._network_label = network_label

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
        if issubclass(Netdev, dict):
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
        if not isinstance(other, Netdev):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
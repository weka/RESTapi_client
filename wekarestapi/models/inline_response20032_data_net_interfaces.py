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

class InlineResponse20032DataNetInterfaces(object):
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
        'mtu': 'float',
        'pci_slot': 'str',
        'mac': 'str',
        'pci_slot_slaves': 'list[str]',
        'ip4': 'str',
        'link_layer': 'str',
        'name': 'str',
        'ip4_netmask': 'float',
        'name_slaves': 'list[str]',
        'bond_type': 'str',
        'ip6': 'str'
    }

    attribute_map = {
        'mtu': 'mtu',
        'pci_slot': 'pciSlot',
        'mac': 'mac',
        'pci_slot_slaves': 'pciSlot_slaves',
        'ip4': 'ip4',
        'link_layer': 'linkLayer',
        'name': 'name',
        'ip4_netmask': 'ip4Netmask',
        'name_slaves': 'name_slaves',
        'bond_type': 'bondType',
        'ip6': 'ip6'
    }

    def __init__(self, mtu=None, pci_slot=None, mac=None, pci_slot_slaves=None, ip4=None, link_layer=None, name=None, ip4_netmask=None, name_slaves=None, bond_type=None, ip6=None):  # noqa: E501
        """InlineResponse20032DataNetInterfaces - a model defined in Swagger"""  # noqa: E501
        self._mtu = None
        self._pci_slot = None
        self._mac = None
        self._pci_slot_slaves = None
        self._ip4 = None
        self._link_layer = None
        self._name = None
        self._ip4_netmask = None
        self._name_slaves = None
        self._bond_type = None
        self._ip6 = None
        self.discriminator = None
        if mtu is not None:
            self.mtu = mtu
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if mac is not None:
            self.mac = mac
        if pci_slot_slaves is not None:
            self.pci_slot_slaves = pci_slot_slaves
        if ip4 is not None:
            self.ip4 = ip4
        if link_layer is not None:
            self.link_layer = link_layer
        if name is not None:
            self.name = name
        if ip4_netmask is not None:
            self.ip4_netmask = ip4_netmask
        if name_slaves is not None:
            self.name_slaves = name_slaves
        if bond_type is not None:
            self.bond_type = bond_type
        if ip6 is not None:
            self.ip6 = ip6

    @property
    def mtu(self):
        """Gets the mtu of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The mtu of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: float
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this InlineResponse20032DataNetInterfaces.


        :param mtu: The mtu of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: float
        """

        self._mtu = mtu

    @property
    def pci_slot(self):
        """Gets the pci_slot of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The pci_slot of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this InlineResponse20032DataNetInterfaces.


        :param pci_slot: The pci_slot of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def mac(self):
        """Gets the mac of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The mac of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this InlineResponse20032DataNetInterfaces.


        :param mac: The mac of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def pci_slot_slaves(self):
        """Gets the pci_slot_slaves of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The pci_slot_slaves of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: list[str]
        """
        return self._pci_slot_slaves

    @pci_slot_slaves.setter
    def pci_slot_slaves(self, pci_slot_slaves):
        """Sets the pci_slot_slaves of this InlineResponse20032DataNetInterfaces.


        :param pci_slot_slaves: The pci_slot_slaves of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: list[str]
        """

        self._pci_slot_slaves = pci_slot_slaves

    @property
    def ip4(self):
        """Gets the ip4 of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The ip4 of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._ip4

    @ip4.setter
    def ip4(self, ip4):
        """Sets the ip4 of this InlineResponse20032DataNetInterfaces.


        :param ip4: The ip4 of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._ip4 = ip4

    @property
    def link_layer(self):
        """Gets the link_layer of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The link_layer of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._link_layer

    @link_layer.setter
    def link_layer(self, link_layer):
        """Sets the link_layer of this InlineResponse20032DataNetInterfaces.


        :param link_layer: The link_layer of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._link_layer = link_layer

    @property
    def name(self):
        """Gets the name of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The name of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20032DataNetInterfaces.


        :param name: The name of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def ip4_netmask(self):
        """Gets the ip4_netmask of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The ip4_netmask of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: float
        """
        return self._ip4_netmask

    @ip4_netmask.setter
    def ip4_netmask(self, ip4_netmask):
        """Sets the ip4_netmask of this InlineResponse20032DataNetInterfaces.


        :param ip4_netmask: The ip4_netmask of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: float
        """

        self._ip4_netmask = ip4_netmask

    @property
    def name_slaves(self):
        """Gets the name_slaves of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The name_slaves of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: list[str]
        """
        return self._name_slaves

    @name_slaves.setter
    def name_slaves(self, name_slaves):
        """Sets the name_slaves of this InlineResponse20032DataNetInterfaces.


        :param name_slaves: The name_slaves of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: list[str]
        """

        self._name_slaves = name_slaves

    @property
    def bond_type(self):
        """Gets the bond_type of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The bond_type of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._bond_type

    @bond_type.setter
    def bond_type(self, bond_type):
        """Sets the bond_type of this InlineResponse20032DataNetInterfaces.


        :param bond_type: The bond_type of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._bond_type = bond_type

    @property
    def ip6(self):
        """Gets the ip6 of this InlineResponse20032DataNetInterfaces.  # noqa: E501


        :return: The ip6 of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :rtype: str
        """
        return self._ip6

    @ip6.setter
    def ip6(self, ip6):
        """Sets the ip6 of this InlineResponse20032DataNetInterfaces.


        :param ip6: The ip6 of this InlineResponse20032DataNetInterfaces.  # noqa: E501
        :type: str
        """

        self._ip6 = ip6

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
        if issubclass(InlineResponse20032DataNetInterfaces, dict):
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
        if not isinstance(other, InlineResponse20032DataNetInterfaces):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

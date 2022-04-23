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

class NetdevNetDevices(object):
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
        'aws': 'NetdevAws',
        'device': 'str',
        'driver': 'str',
        'interface_alias': 'str',
        'interface_name': 'str',
        'is_virtual': 'bool',
        'mac_address': 'str',
        'max_vfs_num': 'float',
        'mtu': 'float',
        'numa': 'float',
        'pci_slot': 'str',
        'slave_devices': 'list[str]',
        'vendor': 'str'
    }

    attribute_map = {
        'aws': 'aws',
        'device': 'device',
        'driver': 'driver',
        'interface_alias': 'interface_alias',
        'interface_name': 'interface_name',
        'is_virtual': 'is_virtual',
        'mac_address': 'mac_address',
        'max_vfs_num': 'max_vfs_num',
        'mtu': 'mtu',
        'numa': 'numa',
        'pci_slot': 'pci_slot',
        'slave_devices': 'slave_devices',
        'vendor': 'vendor'
    }

    def __init__(self, aws=None, device=None, driver=None, interface_alias=None, interface_name=None, is_virtual=None, mac_address=None, max_vfs_num=None, mtu=None, numa=None, pci_slot=None, slave_devices=None, vendor=None):  # noqa: E501
        """NetdevNetDevices - a model defined in Swagger"""  # noqa: E501
        self._aws = None
        self._device = None
        self._driver = None
        self._interface_alias = None
        self._interface_name = None
        self._is_virtual = None
        self._mac_address = None
        self._max_vfs_num = None
        self._mtu = None
        self._numa = None
        self._pci_slot = None
        self._slave_devices = None
        self._vendor = None
        self.discriminator = None
        if aws is not None:
            self.aws = aws
        if device is not None:
            self.device = device
        if driver is not None:
            self.driver = driver
        if interface_alias is not None:
            self.interface_alias = interface_alias
        if interface_name is not None:
            self.interface_name = interface_name
        if is_virtual is not None:
            self.is_virtual = is_virtual
        if mac_address is not None:
            self.mac_address = mac_address
        if max_vfs_num is not None:
            self.max_vfs_num = max_vfs_num
        if mtu is not None:
            self.mtu = mtu
        if numa is not None:
            self.numa = numa
        if pci_slot is not None:
            self.pci_slot = pci_slot
        if slave_devices is not None:
            self.slave_devices = slave_devices
        if vendor is not None:
            self.vendor = vendor

    @property
    def aws(self):
        """Gets the aws of this NetdevNetDevices.  # noqa: E501


        :return: The aws of this NetdevNetDevices.  # noqa: E501
        :rtype: NetdevAws
        """
        return self._aws

    @aws.setter
    def aws(self, aws):
        """Sets the aws of this NetdevNetDevices.


        :param aws: The aws of this NetdevNetDevices.  # noqa: E501
        :type: NetdevAws
        """

        self._aws = aws

    @property
    def device(self):
        """Gets the device of this NetdevNetDevices.  # noqa: E501


        :return: The device of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this NetdevNetDevices.


        :param device: The device of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def driver(self):
        """Gets the driver of this NetdevNetDevices.  # noqa: E501


        :return: The driver of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._driver

    @driver.setter
    def driver(self, driver):
        """Sets the driver of this NetdevNetDevices.


        :param driver: The driver of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._driver = driver

    @property
    def interface_alias(self):
        """Gets the interface_alias of this NetdevNetDevices.  # noqa: E501


        :return: The interface_alias of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._interface_alias

    @interface_alias.setter
    def interface_alias(self, interface_alias):
        """Sets the interface_alias of this NetdevNetDevices.


        :param interface_alias: The interface_alias of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._interface_alias = interface_alias

    @property
    def interface_name(self):
        """Gets the interface_name of this NetdevNetDevices.  # noqa: E501


        :return: The interface_name of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this NetdevNetDevices.


        :param interface_name: The interface_name of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._interface_name = interface_name

    @property
    def is_virtual(self):
        """Gets the is_virtual of this NetdevNetDevices.  # noqa: E501


        :return: The is_virtual of this NetdevNetDevices.  # noqa: E501
        :rtype: bool
        """
        return self._is_virtual

    @is_virtual.setter
    def is_virtual(self, is_virtual):
        """Sets the is_virtual of this NetdevNetDevices.


        :param is_virtual: The is_virtual of this NetdevNetDevices.  # noqa: E501
        :type: bool
        """

        self._is_virtual = is_virtual

    @property
    def mac_address(self):
        """Gets the mac_address of this NetdevNetDevices.  # noqa: E501


        :return: The mac_address of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """Sets the mac_address of this NetdevNetDevices.


        :param mac_address: The mac_address of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._mac_address = mac_address

    @property
    def max_vfs_num(self):
        """Gets the max_vfs_num of this NetdevNetDevices.  # noqa: E501


        :return: The max_vfs_num of this NetdevNetDevices.  # noqa: E501
        :rtype: float
        """
        return self._max_vfs_num

    @max_vfs_num.setter
    def max_vfs_num(self, max_vfs_num):
        """Sets the max_vfs_num of this NetdevNetDevices.


        :param max_vfs_num: The max_vfs_num of this NetdevNetDevices.  # noqa: E501
        :type: float
        """

        self._max_vfs_num = max_vfs_num

    @property
    def mtu(self):
        """Gets the mtu of this NetdevNetDevices.  # noqa: E501


        :return: The mtu of this NetdevNetDevices.  # noqa: E501
        :rtype: float
        """
        return self._mtu

    @mtu.setter
    def mtu(self, mtu):
        """Sets the mtu of this NetdevNetDevices.


        :param mtu: The mtu of this NetdevNetDevices.  # noqa: E501
        :type: float
        """

        self._mtu = mtu

    @property
    def numa(self):
        """Gets the numa of this NetdevNetDevices.  # noqa: E501


        :return: The numa of this NetdevNetDevices.  # noqa: E501
        :rtype: float
        """
        return self._numa

    @numa.setter
    def numa(self, numa):
        """Sets the numa of this NetdevNetDevices.


        :param numa: The numa of this NetdevNetDevices.  # noqa: E501
        :type: float
        """

        self._numa = numa

    @property
    def pci_slot(self):
        """Gets the pci_slot of this NetdevNetDevices.  # noqa: E501


        :return: The pci_slot of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._pci_slot

    @pci_slot.setter
    def pci_slot(self, pci_slot):
        """Sets the pci_slot of this NetdevNetDevices.


        :param pci_slot: The pci_slot of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._pci_slot = pci_slot

    @property
    def slave_devices(self):
        """Gets the slave_devices of this NetdevNetDevices.  # noqa: E501


        :return: The slave_devices of this NetdevNetDevices.  # noqa: E501
        :rtype: list[str]
        """
        return self._slave_devices

    @slave_devices.setter
    def slave_devices(self, slave_devices):
        """Sets the slave_devices of this NetdevNetDevices.


        :param slave_devices: The slave_devices of this NetdevNetDevices.  # noqa: E501
        :type: list[str]
        """

        self._slave_devices = slave_devices

    @property
    def vendor(self):
        """Gets the vendor of this NetdevNetDevices.  # noqa: E501


        :return: The vendor of this NetdevNetDevices.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this NetdevNetDevices.


        :param vendor: The vendor of this NetdevNetDevices.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

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
        if issubclass(NetdevNetDevices, dict):
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
        if not isinstance(other, NetdevNetDevices):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
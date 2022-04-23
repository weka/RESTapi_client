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

class HostOsInfoDrivers(object):
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
        'ib_uverbs': 'str',
        'ixgbe': 'str',
        'ixgbevf': 'str',
        'mlx5_core': 'str',
        'uio_pci_generic': 'str'
    }

    attribute_map = {
        'ib_uverbs': 'ib_uverbs',
        'ixgbe': 'ixgbe',
        'ixgbevf': 'ixgbevf',
        'mlx5_core': 'mlx5_core',
        'uio_pci_generic': 'uio_pci_generic'
    }

    def __init__(self, ib_uverbs=None, ixgbe=None, ixgbevf=None, mlx5_core=None, uio_pci_generic=None):  # noqa: E501
        """HostOsInfoDrivers - a model defined in Swagger"""  # noqa: E501
        self._ib_uverbs = None
        self._ixgbe = None
        self._ixgbevf = None
        self._mlx5_core = None
        self._uio_pci_generic = None
        self.discriminator = None
        if ib_uverbs is not None:
            self.ib_uverbs = ib_uverbs
        if ixgbe is not None:
            self.ixgbe = ixgbe
        if ixgbevf is not None:
            self.ixgbevf = ixgbevf
        if mlx5_core is not None:
            self.mlx5_core = mlx5_core
        if uio_pci_generic is not None:
            self.uio_pci_generic = uio_pci_generic

    @property
    def ib_uverbs(self):
        """Gets the ib_uverbs of this HostOsInfoDrivers.  # noqa: E501


        :return: The ib_uverbs of this HostOsInfoDrivers.  # noqa: E501
        :rtype: str
        """
        return self._ib_uverbs

    @ib_uverbs.setter
    def ib_uverbs(self, ib_uverbs):
        """Sets the ib_uverbs of this HostOsInfoDrivers.


        :param ib_uverbs: The ib_uverbs of this HostOsInfoDrivers.  # noqa: E501
        :type: str
        """

        self._ib_uverbs = ib_uverbs

    @property
    def ixgbe(self):
        """Gets the ixgbe of this HostOsInfoDrivers.  # noqa: E501


        :return: The ixgbe of this HostOsInfoDrivers.  # noqa: E501
        :rtype: str
        """
        return self._ixgbe

    @ixgbe.setter
    def ixgbe(self, ixgbe):
        """Sets the ixgbe of this HostOsInfoDrivers.


        :param ixgbe: The ixgbe of this HostOsInfoDrivers.  # noqa: E501
        :type: str
        """

        self._ixgbe = ixgbe

    @property
    def ixgbevf(self):
        """Gets the ixgbevf of this HostOsInfoDrivers.  # noqa: E501


        :return: The ixgbevf of this HostOsInfoDrivers.  # noqa: E501
        :rtype: str
        """
        return self._ixgbevf

    @ixgbevf.setter
    def ixgbevf(self, ixgbevf):
        """Sets the ixgbevf of this HostOsInfoDrivers.


        :param ixgbevf: The ixgbevf of this HostOsInfoDrivers.  # noqa: E501
        :type: str
        """

        self._ixgbevf = ixgbevf

    @property
    def mlx5_core(self):
        """Gets the mlx5_core of this HostOsInfoDrivers.  # noqa: E501


        :return: The mlx5_core of this HostOsInfoDrivers.  # noqa: E501
        :rtype: str
        """
        return self._mlx5_core

    @mlx5_core.setter
    def mlx5_core(self, mlx5_core):
        """Sets the mlx5_core of this HostOsInfoDrivers.


        :param mlx5_core: The mlx5_core of this HostOsInfoDrivers.  # noqa: E501
        :type: str
        """

        self._mlx5_core = mlx5_core

    @property
    def uio_pci_generic(self):
        """Gets the uio_pci_generic of this HostOsInfoDrivers.  # noqa: E501


        :return: The uio_pci_generic of this HostOsInfoDrivers.  # noqa: E501
        :rtype: str
        """
        return self._uio_pci_generic

    @uio_pci_generic.setter
    def uio_pci_generic(self, uio_pci_generic):
        """Sets the uio_pci_generic of this HostOsInfoDrivers.


        :param uio_pci_generic: The uio_pci_generic of this HostOsInfoDrivers.  # noqa: E501
        :type: str
        """

        self._uio_pci_generic = uio_pci_generic

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
        if issubclass(HostOsInfoDrivers, dict):
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
        if not isinstance(other, HostOsInfoDrivers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
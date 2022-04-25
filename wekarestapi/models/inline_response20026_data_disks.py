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

class InlineResponse20026DataDisks(object):
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
        'dev_name': 'str',
        'dev_number': 'str',
        'dev_path': 'str',
        'disk_size_bytes': 'float',
        'is_mounted': 'bool',
        'is_rotational': 'bool',
        'is_weka_partition': 'bool',
        'label': 'str',
        'model': 'str',
        'parent_name': 'str',
        'pci_addr': 'str',
        'size_bytes': 'float',
        'type': 'str',
        'uuid': 'str'
    }

    attribute_map = {
        'dev_name': 'devName',
        'dev_number': 'devNumber',
        'dev_path': 'devPath',
        'disk_size_bytes': 'diskSizeBytes',
        'is_mounted': 'isMounted',
        'is_rotational': 'isRotational',
        'is_weka_partition': 'isWekaPartition',
        'label': 'label',
        'model': 'model',
        'parent_name': 'parentName',
        'pci_addr': 'pciAddr',
        'size_bytes': 'sizeBytes',
        'type': 'type',
        'uuid': 'uuid'
    }

    def __init__(self, dev_name=None, dev_number=None, dev_path=None, disk_size_bytes=None, is_mounted=None, is_rotational=None, is_weka_partition=None, label=None, model=None, parent_name=None, pci_addr=None, size_bytes=None, type=None, uuid=None):  # noqa: E501
        """InlineResponse20026DataDisks - a model defined in Swagger"""  # noqa: E501
        self._dev_name = None
        self._dev_number = None
        self._dev_path = None
        self._disk_size_bytes = None
        self._is_mounted = None
        self._is_rotational = None
        self._is_weka_partition = None
        self._label = None
        self._model = None
        self._parent_name = None
        self._pci_addr = None
        self._size_bytes = None
        self._type = None
        self._uuid = None
        self.discriminator = None
        if dev_name is not None:
            self.dev_name = dev_name
        if dev_number is not None:
            self.dev_number = dev_number
        if dev_path is not None:
            self.dev_path = dev_path
        if disk_size_bytes is not None:
            self.disk_size_bytes = disk_size_bytes
        if is_mounted is not None:
            self.is_mounted = is_mounted
        if is_rotational is not None:
            self.is_rotational = is_rotational
        if is_weka_partition is not None:
            self.is_weka_partition = is_weka_partition
        if label is not None:
            self.label = label
        if model is not None:
            self.model = model
        if parent_name is not None:
            self.parent_name = parent_name
        if pci_addr is not None:
            self.pci_addr = pci_addr
        if size_bytes is not None:
            self.size_bytes = size_bytes
        if type is not None:
            self.type = type
        if uuid is not None:
            self.uuid = uuid

    @property
    def dev_name(self):
        """Gets the dev_name of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The dev_name of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._dev_name

    @dev_name.setter
    def dev_name(self, dev_name):
        """Sets the dev_name of this InlineResponse20026DataDisks.


        :param dev_name: The dev_name of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._dev_name = dev_name

    @property
    def dev_number(self):
        """Gets the dev_number of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The dev_number of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._dev_number

    @dev_number.setter
    def dev_number(self, dev_number):
        """Sets the dev_number of this InlineResponse20026DataDisks.


        :param dev_number: The dev_number of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._dev_number = dev_number

    @property
    def dev_path(self):
        """Gets the dev_path of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The dev_path of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._dev_path

    @dev_path.setter
    def dev_path(self, dev_path):
        """Sets the dev_path of this InlineResponse20026DataDisks.


        :param dev_path: The dev_path of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._dev_path = dev_path

    @property
    def disk_size_bytes(self):
        """Gets the disk_size_bytes of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The disk_size_bytes of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: float
        """
        return self._disk_size_bytes

    @disk_size_bytes.setter
    def disk_size_bytes(self, disk_size_bytes):
        """Sets the disk_size_bytes of this InlineResponse20026DataDisks.


        :param disk_size_bytes: The disk_size_bytes of this InlineResponse20026DataDisks.  # noqa: E501
        :type: float
        """

        self._disk_size_bytes = disk_size_bytes

    @property
    def is_mounted(self):
        """Gets the is_mounted of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The is_mounted of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: bool
        """
        return self._is_mounted

    @is_mounted.setter
    def is_mounted(self, is_mounted):
        """Sets the is_mounted of this InlineResponse20026DataDisks.


        :param is_mounted: The is_mounted of this InlineResponse20026DataDisks.  # noqa: E501
        :type: bool
        """

        self._is_mounted = is_mounted

    @property
    def is_rotational(self):
        """Gets the is_rotational of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The is_rotational of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: bool
        """
        return self._is_rotational

    @is_rotational.setter
    def is_rotational(self, is_rotational):
        """Sets the is_rotational of this InlineResponse20026DataDisks.


        :param is_rotational: The is_rotational of this InlineResponse20026DataDisks.  # noqa: E501
        :type: bool
        """

        self._is_rotational = is_rotational

    @property
    def is_weka_partition(self):
        """Gets the is_weka_partition of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The is_weka_partition of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: bool
        """
        return self._is_weka_partition

    @is_weka_partition.setter
    def is_weka_partition(self, is_weka_partition):
        """Sets the is_weka_partition of this InlineResponse20026DataDisks.


        :param is_weka_partition: The is_weka_partition of this InlineResponse20026DataDisks.  # noqa: E501
        :type: bool
        """

        self._is_weka_partition = is_weka_partition

    @property
    def label(self):
        """Gets the label of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The label of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this InlineResponse20026DataDisks.


        :param label: The label of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def model(self):
        """Gets the model of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The model of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this InlineResponse20026DataDisks.


        :param model: The model of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._model = model

    @property
    def parent_name(self):
        """Gets the parent_name of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The parent_name of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this InlineResponse20026DataDisks.


        :param parent_name: The parent_name of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._parent_name = parent_name

    @property
    def pci_addr(self):
        """Gets the pci_addr of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The pci_addr of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._pci_addr

    @pci_addr.setter
    def pci_addr(self, pci_addr):
        """Sets the pci_addr of this InlineResponse20026DataDisks.


        :param pci_addr: The pci_addr of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._pci_addr = pci_addr

    @property
    def size_bytes(self):
        """Gets the size_bytes of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The size_bytes of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: float
        """
        return self._size_bytes

    @size_bytes.setter
    def size_bytes(self, size_bytes):
        """Sets the size_bytes of this InlineResponse20026DataDisks.


        :param size_bytes: The size_bytes of this InlineResponse20026DataDisks.  # noqa: E501
        :type: float
        """

        self._size_bytes = size_bytes

    @property
    def type(self):
        """Gets the type of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The type of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InlineResponse20026DataDisks.


        :param type: The type of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uuid(self):
        """Gets the uuid of this InlineResponse20026DataDisks.  # noqa: E501


        :return: The uuid of this InlineResponse20026DataDisks.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this InlineResponse20026DataDisks.


        :param uuid: The uuid of this InlineResponse20026DataDisks.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

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
        if issubclass(InlineResponse20026DataDisks, dict):
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
        if not isinstance(other, InlineResponse20026DataDisks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
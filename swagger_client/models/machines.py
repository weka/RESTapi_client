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

class Machines(object):
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
        'drives': 'list[MachinesDrives]',
        'load': 'float',
        'name': 'str',
        'nodes': 'list[MachinesNodes]',
        'primary_ip_address': 'str',
        'primary_port': 'float',
        'ram_allocated': 'float',
        'roles': 'list[str]',
        'status': 'str',
        'uid': 'str',
        'up_since': 'str',
        'versions': 'list[str]'
    }

    attribute_map = {
        'drives': 'drives',
        'load': 'load',
        'name': 'name',
        'nodes': 'nodes',
        'primary_ip_address': 'primary_ip_address',
        'primary_port': 'primary_port',
        'ram_allocated': 'ram_allocated',
        'roles': 'roles',
        'status': 'status',
        'uid': 'uid',
        'up_since': 'up_since',
        'versions': 'versions'
    }

    def __init__(self, drives=None, load=None, name=None, nodes=None, primary_ip_address=None, primary_port=None, ram_allocated=None, roles=None, status=None, uid=None, up_since=None, versions=None):  # noqa: E501
        """Machines - a model defined in Swagger"""  # noqa: E501
        self._drives = None
        self._load = None
        self._name = None
        self._nodes = None
        self._primary_ip_address = None
        self._primary_port = None
        self._ram_allocated = None
        self._roles = None
        self._status = None
        self._uid = None
        self._up_since = None
        self._versions = None
        self.discriminator = None
        if drives is not None:
            self.drives = drives
        if load is not None:
            self.load = load
        if name is not None:
            self.name = name
        if nodes is not None:
            self.nodes = nodes
        if primary_ip_address is not None:
            self.primary_ip_address = primary_ip_address
        if primary_port is not None:
            self.primary_port = primary_port
        if ram_allocated is not None:
            self.ram_allocated = ram_allocated
        if roles is not None:
            self.roles = roles
        if status is not None:
            self.status = status
        if uid is not None:
            self.uid = uid
        if up_since is not None:
            self.up_since = up_since
        if versions is not None:
            self.versions = versions

    @property
    def drives(self):
        """Gets the drives of this Machines.  # noqa: E501


        :return: The drives of this Machines.  # noqa: E501
        :rtype: list[MachinesDrives]
        """
        return self._drives

    @drives.setter
    def drives(self, drives):
        """Sets the drives of this Machines.


        :param drives: The drives of this Machines.  # noqa: E501
        :type: list[MachinesDrives]
        """

        self._drives = drives

    @property
    def load(self):
        """Gets the load of this Machines.  # noqa: E501


        :return: The load of this Machines.  # noqa: E501
        :rtype: float
        """
        return self._load

    @load.setter
    def load(self, load):
        """Sets the load of this Machines.


        :param load: The load of this Machines.  # noqa: E501
        :type: float
        """

        self._load = load

    @property
    def name(self):
        """Gets the name of this Machines.  # noqa: E501


        :return: The name of this Machines.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Machines.


        :param name: The name of this Machines.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def nodes(self):
        """Gets the nodes of this Machines.  # noqa: E501


        :return: The nodes of this Machines.  # noqa: E501
        :rtype: list[MachinesNodes]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this Machines.


        :param nodes: The nodes of this Machines.  # noqa: E501
        :type: list[MachinesNodes]
        """

        self._nodes = nodes

    @property
    def primary_ip_address(self):
        """Gets the primary_ip_address of this Machines.  # noqa: E501


        :return: The primary_ip_address of this Machines.  # noqa: E501
        :rtype: str
        """
        return self._primary_ip_address

    @primary_ip_address.setter
    def primary_ip_address(self, primary_ip_address):
        """Sets the primary_ip_address of this Machines.


        :param primary_ip_address: The primary_ip_address of this Machines.  # noqa: E501
        :type: str
        """

        self._primary_ip_address = primary_ip_address

    @property
    def primary_port(self):
        """Gets the primary_port of this Machines.  # noqa: E501


        :return: The primary_port of this Machines.  # noqa: E501
        :rtype: float
        """
        return self._primary_port

    @primary_port.setter
    def primary_port(self, primary_port):
        """Sets the primary_port of this Machines.


        :param primary_port: The primary_port of this Machines.  # noqa: E501
        :type: float
        """

        self._primary_port = primary_port

    @property
    def ram_allocated(self):
        """Gets the ram_allocated of this Machines.  # noqa: E501


        :return: The ram_allocated of this Machines.  # noqa: E501
        :rtype: float
        """
        return self._ram_allocated

    @ram_allocated.setter
    def ram_allocated(self, ram_allocated):
        """Sets the ram_allocated of this Machines.


        :param ram_allocated: The ram_allocated of this Machines.  # noqa: E501
        :type: float
        """

        self._ram_allocated = ram_allocated

    @property
    def roles(self):
        """Gets the roles of this Machines.  # noqa: E501


        :return: The roles of this Machines.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Machines.


        :param roles: The roles of this Machines.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def status(self):
        """Gets the status of this Machines.  # noqa: E501


        :return: The status of this Machines.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Machines.


        :param status: The status of this Machines.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def uid(self):
        """Gets the uid of this Machines.  # noqa: E501


        :return: The uid of this Machines.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Machines.


        :param uid: The uid of this Machines.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def up_since(self):
        """Gets the up_since of this Machines.  # noqa: E501


        :return: The up_since of this Machines.  # noqa: E501
        :rtype: str
        """
        return self._up_since

    @up_since.setter
    def up_since(self, up_since):
        """Sets the up_since of this Machines.


        :param up_since: The up_since of this Machines.  # noqa: E501
        :type: str
        """

        self._up_since = up_since

    @property
    def versions(self):
        """Gets the versions of this Machines.  # noqa: E501


        :return: The versions of this Machines.  # noqa: E501
        :rtype: list[str]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this Machines.


        :param versions: The versions of this Machines.  # noqa: E501
        :type: list[str]
        """

        self._versions = versions

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
        if issubclass(Machines, dict):
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
        if not isinstance(other, Machines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

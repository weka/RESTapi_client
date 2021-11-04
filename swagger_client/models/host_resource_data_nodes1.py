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

class HostResourceDataNodes1(object):
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
        'roles': 'list[str]',
        'core_id': 'float',
        'http_port': 'float',
        'dedicate_core': 'bool',
        'rpc_port': 'float',
        'dedicated_mode': 'str'
    }

    attribute_map = {
        'roles': 'roles',
        'core_id': 'core_id',
        'http_port': 'http_port',
        'dedicate_core': 'dedicate_core',
        'rpc_port': 'rpc_port',
        'dedicated_mode': 'dedicated_mode'
    }

    def __init__(self, roles=None, core_id=None, http_port=None, dedicate_core=None, rpc_port=None, dedicated_mode=None):  # noqa: E501
        """HostResourceDataNodes1 - a model defined in Swagger"""  # noqa: E501
        self._roles = None
        self._core_id = None
        self._http_port = None
        self._dedicate_core = None
        self._rpc_port = None
        self._dedicated_mode = None
        self.discriminator = None
        if roles is not None:
            self.roles = roles
        if core_id is not None:
            self.core_id = core_id
        if http_port is not None:
            self.http_port = http_port
        if dedicate_core is not None:
            self.dedicate_core = dedicate_core
        if rpc_port is not None:
            self.rpc_port = rpc_port
        if dedicated_mode is not None:
            self.dedicated_mode = dedicated_mode

    @property
    def roles(self):
        """Gets the roles of this HostResourceDataNodes1.  # noqa: E501


        :return: The roles of this HostResourceDataNodes1.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this HostResourceDataNodes1.


        :param roles: The roles of this HostResourceDataNodes1.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def core_id(self):
        """Gets the core_id of this HostResourceDataNodes1.  # noqa: E501


        :return: The core_id of this HostResourceDataNodes1.  # noqa: E501
        :rtype: float
        """
        return self._core_id

    @core_id.setter
    def core_id(self, core_id):
        """Sets the core_id of this HostResourceDataNodes1.


        :param core_id: The core_id of this HostResourceDataNodes1.  # noqa: E501
        :type: float
        """

        self._core_id = core_id

    @property
    def http_port(self):
        """Gets the http_port of this HostResourceDataNodes1.  # noqa: E501


        :return: The http_port of this HostResourceDataNodes1.  # noqa: E501
        :rtype: float
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this HostResourceDataNodes1.


        :param http_port: The http_port of this HostResourceDataNodes1.  # noqa: E501
        :type: float
        """

        self._http_port = http_port

    @property
    def dedicate_core(self):
        """Gets the dedicate_core of this HostResourceDataNodes1.  # noqa: E501


        :return: The dedicate_core of this HostResourceDataNodes1.  # noqa: E501
        :rtype: bool
        """
        return self._dedicate_core

    @dedicate_core.setter
    def dedicate_core(self, dedicate_core):
        """Sets the dedicate_core of this HostResourceDataNodes1.


        :param dedicate_core: The dedicate_core of this HostResourceDataNodes1.  # noqa: E501
        :type: bool
        """

        self._dedicate_core = dedicate_core

    @property
    def rpc_port(self):
        """Gets the rpc_port of this HostResourceDataNodes1.  # noqa: E501


        :return: The rpc_port of this HostResourceDataNodes1.  # noqa: E501
        :rtype: float
        """
        return self._rpc_port

    @rpc_port.setter
    def rpc_port(self, rpc_port):
        """Sets the rpc_port of this HostResourceDataNodes1.


        :param rpc_port: The rpc_port of this HostResourceDataNodes1.  # noqa: E501
        :type: float
        """

        self._rpc_port = rpc_port

    @property
    def dedicated_mode(self):
        """Gets the dedicated_mode of this HostResourceDataNodes1.  # noqa: E501


        :return: The dedicated_mode of this HostResourceDataNodes1.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_mode

    @dedicated_mode.setter
    def dedicated_mode(self, dedicated_mode):
        """Sets the dedicated_mode of this HostResourceDataNodes1.


        :param dedicated_mode: The dedicated_mode of this HostResourceDataNodes1.  # noqa: E501
        :type: str
        """

        self._dedicated_mode = dedicated_mode

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
        if issubclass(HostResourceDataNodes1, dict):
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
        if not isinstance(other, HostResourceDataNodes1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

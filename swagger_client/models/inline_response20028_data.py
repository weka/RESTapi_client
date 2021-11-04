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

class InlineResponse20028Data(object):
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
        'enabled': 'bool',
        'group_object_class': 'str',
        'ignore_start_tls_failure': 'bool',
        'group_membership_attribute': 'str',
        'server_timeout_secs': 'float',
        'user_id_attribute': 'str',
        'start_tls': 'bool',
        'protocol_version': 'float',
        'reader_username': 'str',
        'group_id_attribute': 'str',
        'base_dn': 'str',
        'user_object_class': 'str',
        'role_groups': 'InlineResponse20028DataRoleGroups',
        'server_type': 'str',
        'user_revocation_attribute': 'str',
        'domain': 'str',
        'server_uri': 'str'
    }

    attribute_map = {
        'enabled': 'enabled',
        'group_object_class': 'group_object_class',
        'ignore_start_tls_failure': 'ignore_start_tls_failure',
        'group_membership_attribute': 'group_membership_attribute',
        'server_timeout_secs': 'server_timeout_secs',
        'user_id_attribute': 'user_id_attribute',
        'start_tls': 'start_tls',
        'protocol_version': 'protocol_version',
        'reader_username': 'reader_username',
        'group_id_attribute': 'group_id_attribute',
        'base_dn': 'base_dn',
        'user_object_class': 'user_object_class',
        'role_groups': 'role_groups',
        'server_type': 'server_type',
        'user_revocation_attribute': 'user_revocation_attribute',
        'domain': 'domain',
        'server_uri': 'server_uri'
    }

    def __init__(self, enabled=None, group_object_class=None, ignore_start_tls_failure=None, group_membership_attribute=None, server_timeout_secs=None, user_id_attribute=None, start_tls=None, protocol_version=None, reader_username=None, group_id_attribute=None, base_dn=None, user_object_class=None, role_groups=None, server_type=None, user_revocation_attribute=None, domain=None, server_uri=None):  # noqa: E501
        """InlineResponse20028Data - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._group_object_class = None
        self._ignore_start_tls_failure = None
        self._group_membership_attribute = None
        self._server_timeout_secs = None
        self._user_id_attribute = None
        self._start_tls = None
        self._protocol_version = None
        self._reader_username = None
        self._group_id_attribute = None
        self._base_dn = None
        self._user_object_class = None
        self._role_groups = None
        self._server_type = None
        self._user_revocation_attribute = None
        self._domain = None
        self._server_uri = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if group_object_class is not None:
            self.group_object_class = group_object_class
        if ignore_start_tls_failure is not None:
            self.ignore_start_tls_failure = ignore_start_tls_failure
        if group_membership_attribute is not None:
            self.group_membership_attribute = group_membership_attribute
        if server_timeout_secs is not None:
            self.server_timeout_secs = server_timeout_secs
        if user_id_attribute is not None:
            self.user_id_attribute = user_id_attribute
        if start_tls is not None:
            self.start_tls = start_tls
        if protocol_version is not None:
            self.protocol_version = protocol_version
        if reader_username is not None:
            self.reader_username = reader_username
        if group_id_attribute is not None:
            self.group_id_attribute = group_id_attribute
        if base_dn is not None:
            self.base_dn = base_dn
        if user_object_class is not None:
            self.user_object_class = user_object_class
        if role_groups is not None:
            self.role_groups = role_groups
        if server_type is not None:
            self.server_type = server_type
        if user_revocation_attribute is not None:
            self.user_revocation_attribute = user_revocation_attribute
        if domain is not None:
            self.domain = domain
        if server_uri is not None:
            self.server_uri = server_uri

    @property
    def enabled(self):
        """Gets the enabled of this InlineResponse20028Data.  # noqa: E501


        :return: The enabled of this InlineResponse20028Data.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InlineResponse20028Data.


        :param enabled: The enabled of this InlineResponse20028Data.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def group_object_class(self):
        """Gets the group_object_class of this InlineResponse20028Data.  # noqa: E501


        :return: The group_object_class of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._group_object_class

    @group_object_class.setter
    def group_object_class(self, group_object_class):
        """Sets the group_object_class of this InlineResponse20028Data.


        :param group_object_class: The group_object_class of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._group_object_class = group_object_class

    @property
    def ignore_start_tls_failure(self):
        """Gets the ignore_start_tls_failure of this InlineResponse20028Data.  # noqa: E501


        :return: The ignore_start_tls_failure of this InlineResponse20028Data.  # noqa: E501
        :rtype: bool
        """
        return self._ignore_start_tls_failure

    @ignore_start_tls_failure.setter
    def ignore_start_tls_failure(self, ignore_start_tls_failure):
        """Sets the ignore_start_tls_failure of this InlineResponse20028Data.


        :param ignore_start_tls_failure: The ignore_start_tls_failure of this InlineResponse20028Data.  # noqa: E501
        :type: bool
        """

        self._ignore_start_tls_failure = ignore_start_tls_failure

    @property
    def group_membership_attribute(self):
        """Gets the group_membership_attribute of this InlineResponse20028Data.  # noqa: E501


        :return: The group_membership_attribute of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._group_membership_attribute

    @group_membership_attribute.setter
    def group_membership_attribute(self, group_membership_attribute):
        """Sets the group_membership_attribute of this InlineResponse20028Data.


        :param group_membership_attribute: The group_membership_attribute of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._group_membership_attribute = group_membership_attribute

    @property
    def server_timeout_secs(self):
        """Gets the server_timeout_secs of this InlineResponse20028Data.  # noqa: E501


        :return: The server_timeout_secs of this InlineResponse20028Data.  # noqa: E501
        :rtype: float
        """
        return self._server_timeout_secs

    @server_timeout_secs.setter
    def server_timeout_secs(self, server_timeout_secs):
        """Sets the server_timeout_secs of this InlineResponse20028Data.


        :param server_timeout_secs: The server_timeout_secs of this InlineResponse20028Data.  # noqa: E501
        :type: float
        """

        self._server_timeout_secs = server_timeout_secs

    @property
    def user_id_attribute(self):
        """Gets the user_id_attribute of this InlineResponse20028Data.  # noqa: E501


        :return: The user_id_attribute of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._user_id_attribute

    @user_id_attribute.setter
    def user_id_attribute(self, user_id_attribute):
        """Sets the user_id_attribute of this InlineResponse20028Data.


        :param user_id_attribute: The user_id_attribute of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._user_id_attribute = user_id_attribute

    @property
    def start_tls(self):
        """Gets the start_tls of this InlineResponse20028Data.  # noqa: E501


        :return: The start_tls of this InlineResponse20028Data.  # noqa: E501
        :rtype: bool
        """
        return self._start_tls

    @start_tls.setter
    def start_tls(self, start_tls):
        """Sets the start_tls of this InlineResponse20028Data.


        :param start_tls: The start_tls of this InlineResponse20028Data.  # noqa: E501
        :type: bool
        """

        self._start_tls = start_tls

    @property
    def protocol_version(self):
        """Gets the protocol_version of this InlineResponse20028Data.  # noqa: E501


        :return: The protocol_version of this InlineResponse20028Data.  # noqa: E501
        :rtype: float
        """
        return self._protocol_version

    @protocol_version.setter
    def protocol_version(self, protocol_version):
        """Sets the protocol_version of this InlineResponse20028Data.


        :param protocol_version: The protocol_version of this InlineResponse20028Data.  # noqa: E501
        :type: float
        """

        self._protocol_version = protocol_version

    @property
    def reader_username(self):
        """Gets the reader_username of this InlineResponse20028Data.  # noqa: E501


        :return: The reader_username of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._reader_username

    @reader_username.setter
    def reader_username(self, reader_username):
        """Sets the reader_username of this InlineResponse20028Data.


        :param reader_username: The reader_username of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._reader_username = reader_username

    @property
    def group_id_attribute(self):
        """Gets the group_id_attribute of this InlineResponse20028Data.  # noqa: E501


        :return: The group_id_attribute of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._group_id_attribute

    @group_id_attribute.setter
    def group_id_attribute(self, group_id_attribute):
        """Sets the group_id_attribute of this InlineResponse20028Data.


        :param group_id_attribute: The group_id_attribute of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._group_id_attribute = group_id_attribute

    @property
    def base_dn(self):
        """Gets the base_dn of this InlineResponse20028Data.  # noqa: E501


        :return: The base_dn of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._base_dn

    @base_dn.setter
    def base_dn(self, base_dn):
        """Sets the base_dn of this InlineResponse20028Data.


        :param base_dn: The base_dn of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._base_dn = base_dn

    @property
    def user_object_class(self):
        """Gets the user_object_class of this InlineResponse20028Data.  # noqa: E501


        :return: The user_object_class of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._user_object_class

    @user_object_class.setter
    def user_object_class(self, user_object_class):
        """Sets the user_object_class of this InlineResponse20028Data.


        :param user_object_class: The user_object_class of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._user_object_class = user_object_class

    @property
    def role_groups(self):
        """Gets the role_groups of this InlineResponse20028Data.  # noqa: E501


        :return: The role_groups of this InlineResponse20028Data.  # noqa: E501
        :rtype: InlineResponse20028DataRoleGroups
        """
        return self._role_groups

    @role_groups.setter
    def role_groups(self, role_groups):
        """Sets the role_groups of this InlineResponse20028Data.


        :param role_groups: The role_groups of this InlineResponse20028Data.  # noqa: E501
        :type: InlineResponse20028DataRoleGroups
        """

        self._role_groups = role_groups

    @property
    def server_type(self):
        """Gets the server_type of this InlineResponse20028Data.  # noqa: E501


        :return: The server_type of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._server_type

    @server_type.setter
    def server_type(self, server_type):
        """Sets the server_type of this InlineResponse20028Data.


        :param server_type: The server_type of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._server_type = server_type

    @property
    def user_revocation_attribute(self):
        """Gets the user_revocation_attribute of this InlineResponse20028Data.  # noqa: E501


        :return: The user_revocation_attribute of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._user_revocation_attribute

    @user_revocation_attribute.setter
    def user_revocation_attribute(self, user_revocation_attribute):
        """Sets the user_revocation_attribute of this InlineResponse20028Data.


        :param user_revocation_attribute: The user_revocation_attribute of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._user_revocation_attribute = user_revocation_attribute

    @property
    def domain(self):
        """Gets the domain of this InlineResponse20028Data.  # noqa: E501


        :return: The domain of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this InlineResponse20028Data.


        :param domain: The domain of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def server_uri(self):
        """Gets the server_uri of this InlineResponse20028Data.  # noqa: E501


        :return: The server_uri of this InlineResponse20028Data.  # noqa: E501
        :rtype: str
        """
        return self._server_uri

    @server_uri.setter
    def server_uri(self, server_uri):
        """Sets the server_uri of this InlineResponse20028Data.


        :param server_uri: The server_uri of this InlineResponse20028Data.  # noqa: E501
        :type: str
        """

        self._server_uri = server_uri

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
        if issubclass(InlineResponse20028Data, dict):
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
        if not isinstance(other, InlineResponse20028Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

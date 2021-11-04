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

class PermissionsUidBody(object):
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
        'path': 'str',
        'permission_type': 'str',
        'root_squashing': 'bool',
        'anon_uid': 'float',
        'anon_gid': 'float',
        'obs_direct': 'bool'
    }

    attribute_map = {
        'path': 'path',
        'permission_type': 'permission_type',
        'root_squashing': 'root_squashing',
        'anon_uid': 'anon_uid',
        'anon_gid': 'anon_gid',
        'obs_direct': 'obs_direct'
    }

    def __init__(self, path=None, permission_type=None, root_squashing=None, anon_uid=None, anon_gid=None, obs_direct=None):  # noqa: E501
        """PermissionsUidBody - a model defined in Swagger"""  # noqa: E501
        self._path = None
        self._permission_type = None
        self._root_squashing = None
        self._anon_uid = None
        self._anon_gid = None
        self._obs_direct = None
        self.discriminator = None
        if path is not None:
            self.path = path
        if permission_type is not None:
            self.permission_type = permission_type
        if root_squashing is not None:
            self.root_squashing = root_squashing
        if anon_uid is not None:
            self.anon_uid = anon_uid
        if anon_gid is not None:
            self.anon_gid = anon_gid
        if obs_direct is not None:
            self.obs_direct = obs_direct

    @property
    def path(self):
        """Gets the path of this PermissionsUidBody.  # noqa: E501

        path [default -  /]  # noqa: E501

        :return: The path of this PermissionsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this PermissionsUidBody.

        path [default -  /]  # noqa: E501

        :param path: The path of this PermissionsUidBody.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def permission_type(self):
        """Gets the permission_type of this PermissionsUidBody.  # noqa: E501

        Permission type  # noqa: E501

        :return: The permission_type of this PermissionsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._permission_type

    @permission_type.setter
    def permission_type(self, permission_type):
        """Sets the permission_type of this PermissionsUidBody.

        Permission type  # noqa: E501

        :param permission_type: The permission_type of this PermissionsUidBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["RO", "RW"]  # noqa: E501
        if permission_type not in allowed_values:
            raise ValueError(
                "Invalid value for `permission_type` ({0}), must be one of {1}"  # noqa: E501
                .format(permission_type, allowed_values)
            )

        self._permission_type = permission_type

    @property
    def root_squashing(self):
        """Gets the root_squashing of this PermissionsUidBody.  # noqa: E501

        Root squashing  # noqa: E501

        :return: The root_squashing of this PermissionsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._root_squashing

    @root_squashing.setter
    def root_squashing(self, root_squashing):
        """Sets the root_squashing of this PermissionsUidBody.

        Root squashing  # noqa: E501

        :param root_squashing: The root_squashing of this PermissionsUidBody.  # noqa: E501
        :type: bool
        """

        self._root_squashing = root_squashing

    @property
    def anon_uid(self):
        """Gets the anon_uid of this PermissionsUidBody.  # noqa: E501

        Anonymous UID to be used instead of root when root squashing is enabled  # noqa: E501

        :return: The anon_uid of this PermissionsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._anon_uid

    @anon_uid.setter
    def anon_uid(self, anon_uid):
        """Sets the anon_uid of this PermissionsUidBody.

        Anonymous UID to be used instead of root when root squashing is enabled  # noqa: E501

        :param anon_uid: The anon_uid of this PermissionsUidBody.  # noqa: E501
        :type: float
        """

        self._anon_uid = anon_uid

    @property
    def anon_gid(self):
        """Gets the anon_gid of this PermissionsUidBody.  # noqa: E501

        Anonymous GID to be used instead of root when root squashing is enabled  # noqa: E501

        :return: The anon_gid of this PermissionsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._anon_gid

    @anon_gid.setter
    def anon_gid(self, anon_gid):
        """Sets the anon_gid of this PermissionsUidBody.

        Anonymous GID to be used instead of root when root squashing is enabled  # noqa: E501

        :param anon_gid: The anon_gid of this PermissionsUidBody.  # noqa: E501
        :type: float
        """

        self._anon_gid = anon_gid

    @property
    def obs_direct(self):
        """Gets the obs_direct of this PermissionsUidBody.  # noqa: E501

        Obs direct  # noqa: E501

        :return: The obs_direct of this PermissionsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._obs_direct

    @obs_direct.setter
    def obs_direct(self, obs_direct):
        """Sets the obs_direct of this PermissionsUidBody.

        Obs direct  # noqa: E501

        :param obs_direct: The obs_direct of this PermissionsUidBody.  # noqa: E501
        :type: bool
        """

        self._obs_direct = obs_direct

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
        if issubclass(PermissionsUidBody, dict):
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
        if not isinstance(other, PermissionsUidBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

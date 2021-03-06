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

class UsersBody(object):
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
        'password': 'str',
        'posix_gid': 'float',
        'posix_uid': 'float',
        'role': 'str',
        'username': 'str'
    }

    attribute_map = {
        'password': 'password',
        'posix_gid': 'posix_gid',
        'posix_uid': 'posix_uid',
        'role': 'role',
        'username': 'username'
    }

    def __init__(self, password=None, posix_gid=None, posix_uid=None, role=None, username=None):  # noqa: E501
        """UsersBody - a model defined in Swagger"""  # noqa: E501
        self._password = None
        self._posix_gid = None
        self._posix_uid = None
        self._role = None
        self._username = None
        self.discriminator = None
        if password is not None:
            self.password = password
        if posix_gid is not None:
            self.posix_gid = posix_gid
        if posix_uid is not None:
            self.posix_uid = posix_uid
        if role is not None:
            self.role = role
        if username is not None:
            self.username = username

    @property
    def password(self):
        """Gets the password of this UsersBody.  # noqa: E501

        Password for the new user - must contain at least 8 characters, and have at least one uppercase letter, one lowercase letter, and one number or special character. Typing special characters as arguments to this command might require escaping  # noqa: E501

        :return: The password of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UsersBody.

        Password for the new user - must contain at least 8 characters, and have at least one uppercase letter, one lowercase letter, and one number or special character. Typing special characters as arguments to this command might require escaping  # noqa: E501

        :param password: The password of this UsersBody.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def posix_gid(self):
        """Gets the posix_gid of this UsersBody.  # noqa: E501

        (S3 only) POSIX GID for this user's S3 files  # noqa: E501

        :return: The posix_gid of this UsersBody.  # noqa: E501
        :rtype: float
        """
        return self._posix_gid

    @posix_gid.setter
    def posix_gid(self, posix_gid):
        """Sets the posix_gid of this UsersBody.

        (S3 only) POSIX GID for this user's S3 files  # noqa: E501

        :param posix_gid: The posix_gid of this UsersBody.  # noqa: E501
        :type: float
        """

        self._posix_gid = posix_gid

    @property
    def posix_uid(self):
        """Gets the posix_uid of this UsersBody.  # noqa: E501

        (S3 only) POSIX UID for this user's S3 files  # noqa: E501

        :return: The posix_uid of this UsersBody.  # noqa: E501
        :rtype: float
        """
        return self._posix_uid

    @posix_uid.setter
    def posix_uid(self, posix_uid):
        """Sets the posix_uid of this UsersBody.

        (S3 only) POSIX UID for this user's S3 files  # noqa: E501

        :param posix_uid: The posix_uid of this UsersBody.  # noqa: E501
        :type: float
        """

        self._posix_uid = posix_uid

    @property
    def role(self):
        """Gets the role of this UsersBody.  # noqa: E501

        The role of the new user  # noqa: E501

        :return: The role of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UsersBody.

        The role of the new user  # noqa: E501

        :param role: The role of this UsersBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["ClusterAdmin", "OrgAdmin", "ReadOnly", "Regular", "S3"]  # noqa: E501
        if role not in allowed_values:
            raise ValueError(
                "Invalid value for `role` ({0}), must be one of {1}"  # noqa: E501
                .format(role, allowed_values)
            )

        self._role = role

    @property
    def username(self):
        """Gets the username of this UsersBody.  # noqa: E501

        Username of the new user to create  # noqa: E501

        :return: The username of this UsersBody.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UsersBody.

        Username of the new user to create  # noqa: E501

        :param username: The username of this UsersBody.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(UsersBody, dict):
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
        if not isinstance(other, UsersBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

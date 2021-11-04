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

class SmbShare(object):
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
        'inner_path': 'str',
        'file_create_mask': 'str',
        'mount_options': 'str',
        'read_write_users': 'list[str]',
        'read_only': 'bool',
        'valid_users': 'list[str]',
        'invalid_users': 'list[str]',
        'hidden': 'bool',
        'share_name': 'str',
        'read_only_users': 'list[str]',
        'encryption': 'str',
        'uid': 'str',
        'acl': 'bool',
        'additional_share_options': 'list[str]',
        'directory_create_mask': 'str',
        'description': 'str',
        'obs_direct': 'bool',
        'allow_guest_access': 'bool',
        'fs_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'inner_path': 'innerPath',
        'file_create_mask': 'fileCreateMask',
        'mount_options': 'mountOptions',
        'read_write_users': 'readWriteUsers',
        'read_only': 'readOnly',
        'valid_users': 'validUsers',
        'invalid_users': 'invalidUsers',
        'hidden': 'hidden',
        'share_name': 'shareName',
        'read_only_users': 'readOnlyUsers',
        'encryption': 'encryption',
        'uid': 'uid',
        'acl': 'acl',
        'additional_share_options': 'additionalShareOptions',
        'directory_create_mask': 'directoryCreateMask',
        'description': 'description',
        'obs_direct': 'obsDirect',
        'allow_guest_access': 'allowGuestAccess',
        'fs_name': 'fsName'
    }

    def __init__(self, id=None, inner_path=None, file_create_mask=None, mount_options=None, read_write_users=None, read_only=None, valid_users=None, invalid_users=None, hidden=None, share_name=None, read_only_users=None, encryption=None, uid=None, acl=None, additional_share_options=None, directory_create_mask=None, description=None, obs_direct=None, allow_guest_access=None, fs_name=None):  # noqa: E501
        """SmbShare - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._inner_path = None
        self._file_create_mask = None
        self._mount_options = None
        self._read_write_users = None
        self._read_only = None
        self._valid_users = None
        self._invalid_users = None
        self._hidden = None
        self._share_name = None
        self._read_only_users = None
        self._encryption = None
        self._uid = None
        self._acl = None
        self._additional_share_options = None
        self._directory_create_mask = None
        self._description = None
        self._obs_direct = None
        self._allow_guest_access = None
        self._fs_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if inner_path is not None:
            self.inner_path = inner_path
        if file_create_mask is not None:
            self.file_create_mask = file_create_mask
        if mount_options is not None:
            self.mount_options = mount_options
        if read_write_users is not None:
            self.read_write_users = read_write_users
        if read_only is not None:
            self.read_only = read_only
        if valid_users is not None:
            self.valid_users = valid_users
        if invalid_users is not None:
            self.invalid_users = invalid_users
        if hidden is not None:
            self.hidden = hidden
        if share_name is not None:
            self.share_name = share_name
        if read_only_users is not None:
            self.read_only_users = read_only_users
        if encryption is not None:
            self.encryption = encryption
        if uid is not None:
            self.uid = uid
        if acl is not None:
            self.acl = acl
        if additional_share_options is not None:
            self.additional_share_options = additional_share_options
        if directory_create_mask is not None:
            self.directory_create_mask = directory_create_mask
        if description is not None:
            self.description = description
        if obs_direct is not None:
            self.obs_direct = obs_direct
        if allow_guest_access is not None:
            self.allow_guest_access = allow_guest_access
        if fs_name is not None:
            self.fs_name = fs_name

    @property
    def id(self):
        """Gets the id of this SmbShare.  # noqa: E501


        :return: The id of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbShare.


        :param id: The id of this SmbShare.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def inner_path(self):
        """Gets the inner_path of this SmbShare.  # noqa: E501


        :return: The inner_path of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._inner_path

    @inner_path.setter
    def inner_path(self, inner_path):
        """Sets the inner_path of this SmbShare.


        :param inner_path: The inner_path of this SmbShare.  # noqa: E501
        :type: str
        """

        self._inner_path = inner_path

    @property
    def file_create_mask(self):
        """Gets the file_create_mask of this SmbShare.  # noqa: E501


        :return: The file_create_mask of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._file_create_mask

    @file_create_mask.setter
    def file_create_mask(self, file_create_mask):
        """Sets the file_create_mask of this SmbShare.


        :param file_create_mask: The file_create_mask of this SmbShare.  # noqa: E501
        :type: str
        """

        self._file_create_mask = file_create_mask

    @property
    def mount_options(self):
        """Gets the mount_options of this SmbShare.  # noqa: E501


        :return: The mount_options of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """Sets the mount_options of this SmbShare.


        :param mount_options: The mount_options of this SmbShare.  # noqa: E501
        :type: str
        """

        self._mount_options = mount_options

    @property
    def read_write_users(self):
        """Gets the read_write_users of this SmbShare.  # noqa: E501


        :return: The read_write_users of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._read_write_users

    @read_write_users.setter
    def read_write_users(self, read_write_users):
        """Sets the read_write_users of this SmbShare.


        :param read_write_users: The read_write_users of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._read_write_users = read_write_users

    @property
    def read_only(self):
        """Gets the read_only of this SmbShare.  # noqa: E501


        :return: The read_only of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this SmbShare.


        :param read_only: The read_only of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def valid_users(self):
        """Gets the valid_users of this SmbShare.  # noqa: E501


        :return: The valid_users of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._valid_users

    @valid_users.setter
    def valid_users(self, valid_users):
        """Sets the valid_users of this SmbShare.


        :param valid_users: The valid_users of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._valid_users = valid_users

    @property
    def invalid_users(self):
        """Gets the invalid_users of this SmbShare.  # noqa: E501


        :return: The invalid_users of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._invalid_users

    @invalid_users.setter
    def invalid_users(self, invalid_users):
        """Sets the invalid_users of this SmbShare.


        :param invalid_users: The invalid_users of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._invalid_users = invalid_users

    @property
    def hidden(self):
        """Gets the hidden of this SmbShare.  # noqa: E501


        :return: The hidden of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this SmbShare.


        :param hidden: The hidden of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def share_name(self):
        """Gets the share_name of this SmbShare.  # noqa: E501


        :return: The share_name of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._share_name

    @share_name.setter
    def share_name(self, share_name):
        """Sets the share_name of this SmbShare.


        :param share_name: The share_name of this SmbShare.  # noqa: E501
        :type: str
        """

        self._share_name = share_name

    @property
    def read_only_users(self):
        """Gets the read_only_users of this SmbShare.  # noqa: E501


        :return: The read_only_users of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._read_only_users

    @read_only_users.setter
    def read_only_users(self, read_only_users):
        """Sets the read_only_users of this SmbShare.


        :param read_only_users: The read_only_users of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._read_only_users = read_only_users

    @property
    def encryption(self):
        """Gets the encryption of this SmbShare.  # noqa: E501


        :return: The encryption of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """Sets the encryption of this SmbShare.


        :param encryption: The encryption of this SmbShare.  # noqa: E501
        :type: str
        """

        self._encryption = encryption

    @property
    def uid(self):
        """Gets the uid of this SmbShare.  # noqa: E501


        :return: The uid of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SmbShare.


        :param uid: The uid of this SmbShare.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def acl(self):
        """Gets the acl of this SmbShare.  # noqa: E501


        :return: The acl of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._acl

    @acl.setter
    def acl(self, acl):
        """Sets the acl of this SmbShare.


        :param acl: The acl of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._acl = acl

    @property
    def additional_share_options(self):
        """Gets the additional_share_options of this SmbShare.  # noqa: E501


        :return: The additional_share_options of this SmbShare.  # noqa: E501
        :rtype: list[str]
        """
        return self._additional_share_options

    @additional_share_options.setter
    def additional_share_options(self, additional_share_options):
        """Sets the additional_share_options of this SmbShare.


        :param additional_share_options: The additional_share_options of this SmbShare.  # noqa: E501
        :type: list[str]
        """

        self._additional_share_options = additional_share_options

    @property
    def directory_create_mask(self):
        """Gets the directory_create_mask of this SmbShare.  # noqa: E501


        :return: The directory_create_mask of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._directory_create_mask

    @directory_create_mask.setter
    def directory_create_mask(self, directory_create_mask):
        """Sets the directory_create_mask of this SmbShare.


        :param directory_create_mask: The directory_create_mask of this SmbShare.  # noqa: E501
        :type: str
        """

        self._directory_create_mask = directory_create_mask

    @property
    def description(self):
        """Gets the description of this SmbShare.  # noqa: E501


        :return: The description of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SmbShare.


        :param description: The description of this SmbShare.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def obs_direct(self):
        """Gets the obs_direct of this SmbShare.  # noqa: E501


        :return: The obs_direct of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._obs_direct

    @obs_direct.setter
    def obs_direct(self, obs_direct):
        """Sets the obs_direct of this SmbShare.


        :param obs_direct: The obs_direct of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._obs_direct = obs_direct

    @property
    def allow_guest_access(self):
        """Gets the allow_guest_access of this SmbShare.  # noqa: E501


        :return: The allow_guest_access of this SmbShare.  # noqa: E501
        :rtype: bool
        """
        return self._allow_guest_access

    @allow_guest_access.setter
    def allow_guest_access(self, allow_guest_access):
        """Sets the allow_guest_access of this SmbShare.


        :param allow_guest_access: The allow_guest_access of this SmbShare.  # noqa: E501
        :type: bool
        """

        self._allow_guest_access = allow_guest_access

    @property
    def fs_name(self):
        """Gets the fs_name of this SmbShare.  # noqa: E501


        :return: The fs_name of this SmbShare.  # noqa: E501
        :rtype: str
        """
        return self._fs_name

    @fs_name.setter
    def fs_name(self, fs_name):
        """Sets the fs_name of this SmbShare.


        :param fs_name: The fs_name of this SmbShare.  # noqa: E501
        :type: str
        """

        self._fs_name = fs_name

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
        if issubclass(SmbShare, dict):
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
        if not isinstance(other, SmbShare):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
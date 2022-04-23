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

class S3Body1(object):
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
        'all_hosts': 'bool',
        'anonymous_posix_gid': 'float',
        'anonymous_posix_uid': 'float',
        'default_fs_name': 'str',
        'etcd_cluster_size': 'float',
        'host_uids': 'list[str]',
        'key': 'str',
        'mount_options': 'str',
        'port': 'float',
        'secret': 'str'
    }

    attribute_map = {
        'all_hosts': 'all_hosts',
        'anonymous_posix_gid': 'anonymous_posix_gid',
        'anonymous_posix_uid': 'anonymous_posix_uid',
        'default_fs_name': 'default_fs_name',
        'etcd_cluster_size': 'etcd_cluster_size',
        'host_uids': 'host_uids',
        'key': 'key',
        'mount_options': 'mount_options',
        'port': 'port',
        'secret': 'secret'
    }

    def __init__(self, all_hosts=None, anonymous_posix_gid=None, anonymous_posix_uid=None, default_fs_name=None, etcd_cluster_size=None, host_uids=None, key=None, mount_options=None, port=None, secret=None):  # noqa: E501
        """S3Body1 - a model defined in Swagger"""  # noqa: E501
        self._all_hosts = None
        self._anonymous_posix_gid = None
        self._anonymous_posix_uid = None
        self._default_fs_name = None
        self._etcd_cluster_size = None
        self._host_uids = None
        self._key = None
        self._mount_options = None
        self._port = None
        self._secret = None
        self.discriminator = None
        if all_hosts is not None:
            self.all_hosts = all_hosts
        if anonymous_posix_gid is not None:
            self.anonymous_posix_gid = anonymous_posix_gid
        if anonymous_posix_uid is not None:
            self.anonymous_posix_uid = anonymous_posix_uid
        self.default_fs_name = default_fs_name
        if etcd_cluster_size is not None:
            self.etcd_cluster_size = etcd_cluster_size
        if host_uids is not None:
            self.host_uids = host_uids
        self.key = key
        if mount_options is not None:
            self.mount_options = mount_options
        if port is not None:
            self.port = port
        self.secret = secret

    @property
    def all_hosts(self):
        """Gets the all_hosts of this S3Body1.  # noqa: E501


        :return: The all_hosts of this S3Body1.  # noqa: E501
        :rtype: bool
        """
        return self._all_hosts

    @all_hosts.setter
    def all_hosts(self, all_hosts):
        """Sets the all_hosts of this S3Body1.


        :param all_hosts: The all_hosts of this S3Body1.  # noqa: E501
        :type: bool
        """

        self._all_hosts = all_hosts

    @property
    def anonymous_posix_gid(self):
        """Gets the anonymous_posix_gid of this S3Body1.  # noqa: E501

        POSIX GID for anonymous users  # noqa: E501

        :return: The anonymous_posix_gid of this S3Body1.  # noqa: E501
        :rtype: float
        """
        return self._anonymous_posix_gid

    @anonymous_posix_gid.setter
    def anonymous_posix_gid(self, anonymous_posix_gid):
        """Sets the anonymous_posix_gid of this S3Body1.

        POSIX GID for anonymous users  # noqa: E501

        :param anonymous_posix_gid: The anonymous_posix_gid of this S3Body1.  # noqa: E501
        :type: float
        """

        self._anonymous_posix_gid = anonymous_posix_gid

    @property
    def anonymous_posix_uid(self):
        """Gets the anonymous_posix_uid of this S3Body1.  # noqa: E501

        POSIX UID for anonymous users  # noqa: E501

        :return: The anonymous_posix_uid of this S3Body1.  # noqa: E501
        :rtype: float
        """
        return self._anonymous_posix_uid

    @anonymous_posix_uid.setter
    def anonymous_posix_uid(self, anonymous_posix_uid):
        """Sets the anonymous_posix_uid of this S3Body1.

        POSIX UID for anonymous users  # noqa: E501

        :param anonymous_posix_uid: The anonymous_posix_uid of this S3Body1.  # noqa: E501
        :type: float
        """

        self._anonymous_posix_uid = anonymous_posix_uid

    @property
    def default_fs_name(self):
        """Gets the default_fs_name of this S3Body1.  # noqa: E501

        Default file system name  # noqa: E501

        :return: The default_fs_name of this S3Body1.  # noqa: E501
        :rtype: str
        """
        return self._default_fs_name

    @default_fs_name.setter
    def default_fs_name(self, default_fs_name):
        """Sets the default_fs_name of this S3Body1.

        Default file system name  # noqa: E501

        :param default_fs_name: The default_fs_name of this S3Body1.  # noqa: E501
        :type: str
        """
        if default_fs_name is None:
            raise ValueError("Invalid value for `default_fs_name`, must not be `None`")  # noqa: E501

        self._default_fs_name = default_fs_name

    @property
    def etcd_cluster_size(self):
        """Gets the etcd_cluster_size of this S3Body1.  # noqa: E501

        Size of etcd cluster  # noqa: E501

        :return: The etcd_cluster_size of this S3Body1.  # noqa: E501
        :rtype: float
        """
        return self._etcd_cluster_size

    @etcd_cluster_size.setter
    def etcd_cluster_size(self, etcd_cluster_size):
        """Sets the etcd_cluster_size of this S3Body1.

        Size of etcd cluster  # noqa: E501

        :param etcd_cluster_size: The etcd_cluster_size of this S3Body1.  # noqa: E501
        :type: float
        """

        self._etcd_cluster_size = etcd_cluster_size

    @property
    def host_uids(self):
        """Gets the host_uids of this S3Body1.  # noqa: E501

        UIDs of hosts running S3  # noqa: E501

        :return: The host_uids of this S3Body1.  # noqa: E501
        :rtype: list[str]
        """
        return self._host_uids

    @host_uids.setter
    def host_uids(self, host_uids):
        """Sets the host_uids of this S3Body1.

        UIDs of hosts running S3  # noqa: E501

        :param host_uids: The host_uids of this S3Body1.  # noqa: E501
        :type: list[str]
        """

        self._host_uids = host_uids

    @property
    def key(self):
        """Gets the key of this S3Body1.  # noqa: E501

        S3 cluster access key  # noqa: E501

        :return: The key of this S3Body1.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this S3Body1.

        S3 cluster access key  # noqa: E501

        :param key: The key of this S3Body1.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def mount_options(self):
        """Gets the mount_options of this S3Body1.  # noqa: E501

        mount options  # noqa: E501

        :return: The mount_options of this S3Body1.  # noqa: E501
        :rtype: str
        """
        return self._mount_options

    @mount_options.setter
    def mount_options(self, mount_options):
        """Sets the mount_options of this S3Body1.

        mount options  # noqa: E501

        :param mount_options: The mount_options of this S3Body1.  # noqa: E501
        :type: str
        """

        self._mount_options = mount_options

    @property
    def port(self):
        """Gets the port of this S3Body1.  # noqa: E501

        port  # noqa: E501

        :return: The port of this S3Body1.  # noqa: E501
        :rtype: float
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this S3Body1.

        port  # noqa: E501

        :param port: The port of this S3Body1.  # noqa: E501
        :type: float
        """

        self._port = port

    @property
    def secret(self):
        """Gets the secret of this S3Body1.  # noqa: E501

        S3 cluster secret key  # noqa: E501

        :return: The secret of this S3Body1.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this S3Body1.

        S3 cluster secret key  # noqa: E501

        :param secret: The secret of this S3Body1.  # noqa: E501
        :type: str
        """
        if secret is None:
            raise ValueError("Invalid value for `secret`, must not be `None`")  # noqa: E501

        self._secret = secret

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
        if issubclass(S3Body1, dict):
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
        if not isinstance(other, S3Body1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

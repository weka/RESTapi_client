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

class FileSystemsBody(object):
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
        'allow_no_kms': 'bool',
        'auth_required': 'bool',
        'encrypted': 'bool',
        'group_name': 'str',
        'name': 'str',
        'obs_name': 'str',
        'ssd_capacity': 'float',
        'thin_provision_max_ssd': 'float',
        'thin_provision_min_ssd': 'float',
        'total_capacity': 'float'
    }

    attribute_map = {
        'allow_no_kms': 'allow_no_kms',
        'auth_required': 'auth_required',
        'encrypted': 'encrypted',
        'group_name': 'group_name',
        'name': 'name',
        'obs_name': 'obs_name',
        'ssd_capacity': 'ssd_capacity',
        'thin_provision_max_ssd': 'thin_provision_max_ssd',
        'thin_provision_min_ssd': 'thin_provision_min_ssd',
        'total_capacity': 'total_capacity'
    }

    def __init__(self, allow_no_kms=None, auth_required=None, encrypted=None, group_name=None, name=None, obs_name=None, ssd_capacity=None, thin_provision_max_ssd=None, thin_provision_min_ssd=None, total_capacity=None):  # noqa: E501
        """FileSystemsBody - a model defined in Swagger"""  # noqa: E501
        self._allow_no_kms = None
        self._auth_required = None
        self._encrypted = None
        self._group_name = None
        self._name = None
        self._obs_name = None
        self._ssd_capacity = None
        self._thin_provision_max_ssd = None
        self._thin_provision_min_ssd = None
        self._total_capacity = None
        self.discriminator = None
        if allow_no_kms is not None:
            self.allow_no_kms = allow_no_kms
        if auth_required is not None:
            self.auth_required = auth_required
        if encrypted is not None:
            self.encrypted = encrypted
        self.group_name = group_name
        self.name = name
        if obs_name is not None:
            self.obs_name = obs_name
        if ssd_capacity is not None:
            self.ssd_capacity = ssd_capacity
        if thin_provision_max_ssd is not None:
            self.thin_provision_max_ssd = thin_provision_max_ssd
        if thin_provision_min_ssd is not None:
            self.thin_provision_min_ssd = thin_provision_min_ssd
        self.total_capacity = total_capacity

    @property
    def allow_no_kms(self):
        """Gets the allow_no_kms of this FileSystemsBody.  # noqa: E501

        Allow (insecurely) creating an encrypted filesystem without a KMS configured  # noqa: E501

        :return: The allow_no_kms of this FileSystemsBody.  # noqa: E501
        :rtype: bool
        """
        return self._allow_no_kms

    @allow_no_kms.setter
    def allow_no_kms(self, allow_no_kms):
        """Sets the allow_no_kms of this FileSystemsBody.

        Allow (insecurely) creating an encrypted filesystem without a KMS configured  # noqa: E501

        :param allow_no_kms: The allow_no_kms of this FileSystemsBody.  # noqa: E501
        :type: bool
        """

        self._allow_no_kms = allow_no_kms

    @property
    def auth_required(self):
        """Gets the auth_required of this FileSystemsBody.  # noqa: E501

        Require the mounting user to be authenticated for mounting this filesystem. This flag is only effective in the root organization, users in non-root organizations must be authenticated to perform a mount operation  # noqa: E501

        :return: The auth_required of this FileSystemsBody.  # noqa: E501
        :rtype: bool
        """
        return self._auth_required

    @auth_required.setter
    def auth_required(self, auth_required):
        """Sets the auth_required of this FileSystemsBody.

        Require the mounting user to be authenticated for mounting this filesystem. This flag is only effective in the root organization, users in non-root organizations must be authenticated to perform a mount operation  # noqa: E501

        :param auth_required: The auth_required of this FileSystemsBody.  # noqa: E501
        :type: bool
        """

        self._auth_required = auth_required

    @property
    def encrypted(self):
        """Gets the encrypted of this FileSystemsBody.  # noqa: E501

        Creates an encrypted filesystem  # noqa: E501

        :return: The encrypted of this FileSystemsBody.  # noqa: E501
        :rtype: bool
        """
        return self._encrypted

    @encrypted.setter
    def encrypted(self, encrypted):
        """Sets the encrypted of this FileSystemsBody.

        Creates an encrypted filesystem  # noqa: E501

        :param encrypted: The encrypted of this FileSystemsBody.  # noqa: E501
        :type: bool
        """

        self._encrypted = encrypted

    @property
    def group_name(self):
        """Gets the group_name of this FileSystemsBody.  # noqa: E501

        Group name  # noqa: E501

        :return: The group_name of this FileSystemsBody.  # noqa: E501
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this FileSystemsBody.

        Group name  # noqa: E501

        :param group_name: The group_name of this FileSystemsBody.  # noqa: E501
        :type: str
        """
        if group_name is None:
            raise ValueError("Invalid value for `group_name`, must not be `None`")  # noqa: E501

        self._group_name = group_name

    @property
    def name(self):
        """Gets the name of this FileSystemsBody.  # noqa: E501

        Filesystem name  # noqa: E501

        :return: The name of this FileSystemsBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSystemsBody.

        Filesystem name  # noqa: E501

        :param name: The name of this FileSystemsBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def obs_name(self):
        """Gets the obs_name of this FileSystemsBody.  # noqa: E501

        Object store name. Mandatory for tiered filesystems  # noqa: E501

        :return: The obs_name of this FileSystemsBody.  # noqa: E501
        :rtype: str
        """
        return self._obs_name

    @obs_name.setter
    def obs_name(self, obs_name):
        """Sets the obs_name of this FileSystemsBody.

        Object store name. Mandatory for tiered filesystems  # noqa: E501

        :param obs_name: The obs_name of this FileSystemsBody.  # noqa: E501
        :type: str
        """

        self._obs_name = obs_name

    @property
    def ssd_capacity(self):
        """Gets the ssd_capacity of this FileSystemsBody.  # noqa: E501

        SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The ssd_capacity of this FileSystemsBody.  # noqa: E501
        :rtype: float
        """
        return self._ssd_capacity

    @ssd_capacity.setter
    def ssd_capacity(self, ssd_capacity):
        """Sets the ssd_capacity of this FileSystemsBody.

        SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param ssd_capacity: The ssd_capacity of this FileSystemsBody.  # noqa: E501
        :type: float
        """

        self._ssd_capacity = ssd_capacity

    @property
    def thin_provision_max_ssd(self):
        """Gets the thin_provision_max_ssd of this FileSystemsBody.  # noqa: E501

        Thin provisioned maximum SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The thin_provision_max_ssd of this FileSystemsBody.  # noqa: E501
        :rtype: float
        """
        return self._thin_provision_max_ssd

    @thin_provision_max_ssd.setter
    def thin_provision_max_ssd(self, thin_provision_max_ssd):
        """Sets the thin_provision_max_ssd of this FileSystemsBody.

        Thin provisioned maximum SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param thin_provision_max_ssd: The thin_provision_max_ssd of this FileSystemsBody.  # noqa: E501
        :type: float
        """

        self._thin_provision_max_ssd = thin_provision_max_ssd

    @property
    def thin_provision_min_ssd(self):
        """Gets the thin_provision_min_ssd of this FileSystemsBody.  # noqa: E501

        Thin provisioned minimum SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The thin_provision_min_ssd of this FileSystemsBody.  # noqa: E501
        :rtype: float
        """
        return self._thin_provision_min_ssd

    @thin_provision_min_ssd.setter
    def thin_provision_min_ssd(self, thin_provision_min_ssd):
        """Sets the thin_provision_min_ssd of this FileSystemsBody.

        Thin provisioned minimum SSD capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param thin_provision_min_ssd: The thin_provision_min_ssd of this FileSystemsBody.  # noqa: E501
        :type: float
        """

        self._thin_provision_min_ssd = thin_provision_min_ssd

    @property
    def total_capacity(self):
        """Gets the total_capacity of this FileSystemsBody.  # noqa: E501

        Total capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The total_capacity of this FileSystemsBody.  # noqa: E501
        :rtype: float
        """
        return self._total_capacity

    @total_capacity.setter
    def total_capacity(self, total_capacity):
        """Sets the total_capacity of this FileSystemsBody.

        Total capacity (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param total_capacity: The total_capacity of this FileSystemsBody.  # noqa: E501
        :type: float
        """
        if total_capacity is None:
            raise ValueError("Invalid value for `total_capacity`, must not be `None`")  # noqa: E501

        self._total_capacity = total_capacity

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
        if issubclass(FileSystemsBody, dict):
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
        if not isinstance(other, FileSystemsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

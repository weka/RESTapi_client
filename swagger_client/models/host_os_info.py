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

class HostOsInfo(object):
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
        'drivers': 'HostOsInfoDrivers',
        'kernel_name': 'str',
        'kernel_release': 'str',
        'kernel_version': 'str',
        'os_name': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'drivers': 'drivers',
        'kernel_name': 'kernel_name',
        'kernel_release': 'kernel_release',
        'kernel_version': 'kernel_version',
        'os_name': 'os_name',
        'platform': 'platform'
    }

    def __init__(self, drivers=None, kernel_name=None, kernel_release=None, kernel_version=None, os_name=None, platform=None):  # noqa: E501
        """HostOsInfo - a model defined in Swagger"""  # noqa: E501
        self._drivers = None
        self._kernel_name = None
        self._kernel_release = None
        self._kernel_version = None
        self._os_name = None
        self._platform = None
        self.discriminator = None
        if drivers is not None:
            self.drivers = drivers
        if kernel_name is not None:
            self.kernel_name = kernel_name
        if kernel_release is not None:
            self.kernel_release = kernel_release
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if os_name is not None:
            self.os_name = os_name
        if platform is not None:
            self.platform = platform

    @property
    def drivers(self):
        """Gets the drivers of this HostOsInfo.  # noqa: E501


        :return: The drivers of this HostOsInfo.  # noqa: E501
        :rtype: HostOsInfoDrivers
        """
        return self._drivers

    @drivers.setter
    def drivers(self, drivers):
        """Sets the drivers of this HostOsInfo.


        :param drivers: The drivers of this HostOsInfo.  # noqa: E501
        :type: HostOsInfoDrivers
        """

        self._drivers = drivers

    @property
    def kernel_name(self):
        """Gets the kernel_name of this HostOsInfo.  # noqa: E501


        :return: The kernel_name of this HostOsInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel_name

    @kernel_name.setter
    def kernel_name(self, kernel_name):
        """Sets the kernel_name of this HostOsInfo.


        :param kernel_name: The kernel_name of this HostOsInfo.  # noqa: E501
        :type: str
        """

        self._kernel_name = kernel_name

    @property
    def kernel_release(self):
        """Gets the kernel_release of this HostOsInfo.  # noqa: E501


        :return: The kernel_release of this HostOsInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel_release

    @kernel_release.setter
    def kernel_release(self, kernel_release):
        """Sets the kernel_release of this HostOsInfo.


        :param kernel_release: The kernel_release of this HostOsInfo.  # noqa: E501
        :type: str
        """

        self._kernel_release = kernel_release

    @property
    def kernel_version(self):
        """Gets the kernel_version of this HostOsInfo.  # noqa: E501


        :return: The kernel_version of this HostOsInfo.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this HostOsInfo.


        :param kernel_version: The kernel_version of this HostOsInfo.  # noqa: E501
        :type: str
        """

        self._kernel_version = kernel_version

    @property
    def os_name(self):
        """Gets the os_name of this HostOsInfo.  # noqa: E501


        :return: The os_name of this HostOsInfo.  # noqa: E501
        :rtype: str
        """
        return self._os_name

    @os_name.setter
    def os_name(self, os_name):
        """Sets the os_name of this HostOsInfo.


        :param os_name: The os_name of this HostOsInfo.  # noqa: E501
        :type: str
        """

        self._os_name = os_name

    @property
    def platform(self):
        """Gets the platform of this HostOsInfo.  # noqa: E501


        :return: The platform of this HostOsInfo.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this HostOsInfo.


        :param platform: The platform of this HostOsInfo.  # noqa: E501
        :type: str
        """

        self._platform = platform

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
        if issubclass(HostOsInfo, dict):
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
        if not isinstance(other, HostOsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

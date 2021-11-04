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

class HostsUidBody(object):
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
        'failure_domain_type': 'str',
        'failure_domain': 'str',
        'cores': 'float',
        'frontend_dedicated_cores': 'float',
        'drives_dedicated_cores': 'float',
        'cores_ids_type': 'str',
        'memory': 'float',
        'dedicated': 'bool',
        'bandwidth': 'float',
        'auto_remove_timeout': 'float',
        'management_ips': 'list[str]',
        'apply_host': 'bool'
    }

    attribute_map = {
        'failure_domain_type': 'failure_domain_type',
        'failure_domain': 'failure_domain',
        'cores': 'cores',
        'frontend_dedicated_cores': 'frontend_dedicated_cores',
        'drives_dedicated_cores': 'drives_dedicated_cores',
        'cores_ids_type': 'cores_ids_type',
        'memory': 'memory',
        'dedicated': 'dedicated',
        'bandwidth': 'bandwidth',
        'auto_remove_timeout': 'auto_remove_timeout',
        'management_ips': 'management_ips',
        'apply_host': 'apply_host'
    }

    def __init__(self, failure_domain_type=None, failure_domain=None, cores=None, frontend_dedicated_cores=None, drives_dedicated_cores=None, cores_ids_type=None, memory=None, dedicated=None, bandwidth=None, auto_remove_timeout=None, management_ips=None, apply_host=None):  # noqa: E501
        """HostsUidBody - a model defined in Swagger"""  # noqa: E501
        self._failure_domain_type = None
        self._failure_domain = None
        self._cores = None
        self._frontend_dedicated_cores = None
        self._drives_dedicated_cores = None
        self._cores_ids_type = None
        self._memory = None
        self._dedicated = None
        self._bandwidth = None
        self._auto_remove_timeout = None
        self._management_ips = None
        self._apply_host = None
        self.discriminator = None
        if failure_domain_type is not None:
            self.failure_domain_type = failure_domain_type
        if failure_domain is not None:
            self.failure_domain = failure_domain
        if cores is not None:
            self.cores = cores
        if frontend_dedicated_cores is not None:
            self.frontend_dedicated_cores = frontend_dedicated_cores
        if drives_dedicated_cores is not None:
            self.drives_dedicated_cores = drives_dedicated_cores
        if cores_ids_type is not None:
            self.cores_ids_type = cores_ids_type
        if memory is not None:
            self.memory = memory
        if dedicated is not None:
            self.dedicated = dedicated
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if auto_remove_timeout is not None:
            self.auto_remove_timeout = auto_remove_timeout
        if management_ips is not None:
            self.management_ips = management_ips
        if apply_host is not None:
            self.apply_host = apply_host

    @property
    def failure_domain_type(self):
        """Gets the failure_domain_type of this HostsUidBody.  # noqa: E501

        A failure domain type  # noqa: E501

        :return: The failure_domain_type of this HostsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._failure_domain_type

    @failure_domain_type.setter
    def failure_domain_type(self, failure_domain_type):
        """Sets the failure_domain_type of this HostsUidBody.

        A failure domain type  # noqa: E501

        :param failure_domain_type: The failure_domain_type of this HostsUidBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO", "USER", "HA"]  # noqa: E501
        if failure_domain_type not in allowed_values:
            raise ValueError(
                "Invalid value for `failure_domain_type` ({0}), must be one of {1}"  # noqa: E501
                .format(failure_domain_type, allowed_values)
            )

        self._failure_domain_type = failure_domain_type

    @property
    def failure_domain(self):
        """Gets the failure_domain of this HostsUidBody.  # noqa: E501

        Set the host failure domain  # noqa: E501

        :return: The failure_domain of this HostsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._failure_domain

    @failure_domain.setter
    def failure_domain(self, failure_domain):
        """Sets the failure_domain of this HostsUidBody.

        Set the host failure domain  # noqa: E501

        :param failure_domain: The failure_domain of this HostsUidBody.  # noqa: E501
        :type: str
        """

        self._failure_domain = failure_domain

    @property
    def cores(self):
        """Gets the cores of this HostsUidBody.  # noqa: E501

        Dedicate host's cores to weka  # noqa: E501

        :return: The cores of this HostsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this HostsUidBody.

        Dedicate host's cores to weka  # noqa: E501

        :param cores: The cores of this HostsUidBody.  # noqa: E501
        :type: float
        """

        self._cores = cores

    @property
    def frontend_dedicated_cores(self):
        """Gets the frontend_dedicated_cores of this HostsUidBody.  # noqa: E501

        Frontend dedicate cores  # noqa: E501

        :return: The frontend_dedicated_cores of this HostsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._frontend_dedicated_cores

    @frontend_dedicated_cores.setter
    def frontend_dedicated_cores(self, frontend_dedicated_cores):
        """Sets the frontend_dedicated_cores of this HostsUidBody.

        Frontend dedicate cores  # noqa: E501

        :param frontend_dedicated_cores: The frontend_dedicated_cores of this HostsUidBody.  # noqa: E501
        :type: float
        """

        self._frontend_dedicated_cores = frontend_dedicated_cores

    @property
    def drives_dedicated_cores(self):
        """Gets the drives_dedicated_cores of this HostsUidBody.  # noqa: E501

        Drives dedicate cores  # noqa: E501

        :return: The drives_dedicated_cores of this HostsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._drives_dedicated_cores

    @drives_dedicated_cores.setter
    def drives_dedicated_cores(self, drives_dedicated_cores):
        """Sets the drives_dedicated_cores of this HostsUidBody.

        Drives dedicate cores  # noqa: E501

        :param drives_dedicated_cores: The drives_dedicated_cores of this HostsUidBody.  # noqa: E501
        :type: float
        """

        self._drives_dedicated_cores = drives_dedicated_cores

    @property
    def cores_ids_type(self):
        """Gets the cores_ids_type of this HostsUidBody.  # noqa: E501

        A core id type  # noqa: E501

        :return: The cores_ids_type of this HostsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._cores_ids_type

    @cores_ids_type.setter
    def cores_ids_type(self, cores_ids_type):
        """Sets the cores_ids_type of this HostsUidBody.

        A core id type  # noqa: E501

        :param cores_ids_type: The cores_ids_type of this HostsUidBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO", "USER"]  # noqa: E501
        if cores_ids_type not in allowed_values:
            raise ValueError(
                "Invalid value for `cores_ids_type` ({0}), must be one of {1}"  # noqa: E501
                .format(cores_ids_type, allowed_values)
            )

        self._cores_ids_type = cores_ids_type

    @property
    def memory(self):
        """Gets the memory of this HostsUidBody.  # noqa: E501

        Dedicate a set amount of RAM to weka  # noqa: E501

        :return: The memory of this HostsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this HostsUidBody.

        Dedicate a set amount of RAM to weka  # noqa: E501

        :param memory: The memory of this HostsUidBody.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def dedicated(self):
        """Gets the dedicated of this HostsUidBody.  # noqa: E501

        Set the host as dedicated to weka. For example it can be rebooted whenever needed, and configured by weka for optimal performance and stability  # noqa: E501

        :return: The dedicated of this HostsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._dedicated

    @dedicated.setter
    def dedicated(self, dedicated):
        """Sets the dedicated of this HostsUidBody.

        Set the host as dedicated to weka. For example it can be rebooted whenever needed, and configured by weka for optimal performance and stability  # noqa: E501

        :param dedicated: The dedicated of this HostsUidBody.  # noqa: E501
        :type: bool
        """

        self._dedicated = dedicated

    @property
    def bandwidth(self):
        """Gets the bandwidth of this HostsUidBody.  # noqa: E501

        Limit weka's bandwidth for the host  # noqa: E501

        :return: The bandwidth of this HostsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this HostsUidBody.

        Limit weka's bandwidth for the host  # noqa: E501

        :param bandwidth: The bandwidth of this HostsUidBody.  # noqa: E501
        :type: float
        """

        self._bandwidth = bandwidth

    @property
    def auto_remove_timeout(self):
        """Gets the auto_remove_timeout of this HostsUidBody.  # noqa: E501

        Set how long to wait before removing this host if it disconnects from the cluster (for clients only)  # noqa: E501

        :return: The auto_remove_timeout of this HostsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._auto_remove_timeout

    @auto_remove_timeout.setter
    def auto_remove_timeout(self, auto_remove_timeout):
        """Sets the auto_remove_timeout of this HostsUidBody.

        Set how long to wait before removing this host if it disconnects from the cluster (for clients only)  # noqa: E501

        :param auto_remove_timeout: The auto_remove_timeout of this HostsUidBody.  # noqa: E501
        :type: float
        """

        self._auto_remove_timeout = auto_remove_timeout

    @property
    def management_ips(self):
        """Gets the management_ips of this HostsUidBody.  # noqa: E501

        Set the host's management node IPs. Setting 2 IPs will turn this hosts networking into highly-available mode  # noqa: E501

        :return: The management_ips of this HostsUidBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._management_ips

    @management_ips.setter
    def management_ips(self, management_ips):
        """Sets the management_ips of this HostsUidBody.

        Set the host's management node IPs. Setting 2 IPs will turn this hosts networking into highly-available mode  # noqa: E501

        :param management_ips: The management_ips of this HostsUidBody.  # noqa: E501
        :type: list[str]
        """

        self._management_ips = management_ips

    @property
    def apply_host(self):
        """Gets the apply_host of this HostsUidBody.  # noqa: E501

        Apply the host after this change  # noqa: E501

        :return: The apply_host of this HostsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._apply_host

    @apply_host.setter
    def apply_host(self, apply_host):
        """Sets the apply_host of this HostsUidBody.

        Apply the host after this change  # noqa: E501

        :param apply_host: The apply_host of this HostsUidBody.  # noqa: E501
        :type: bool
        """

        self._apply_host = apply_host

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
        if issubclass(HostsUidBody, dict):
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
        if not isinstance(other, HostsUidBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

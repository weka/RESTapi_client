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

class Node(object):
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
        'dpdk_port_info': 'list[NodeDpdkPortInfo]',
        'network_mode': 'str',
        'mode': 'str',
        'lowest_node_path_issue': 'str',
        'last_fencing_reason': 'str',
        'uid': 'str',
        'hostname': 'str',
        'ips': 'list[str]',
        'slot': 'float',
        'is_blacklisted': 'bool',
        'roles': 'list[str]',
        'missing_links': 'str',
        'cpu_is_dedicated': 'bool',
        'cpu_core_id': 'float',
        'host_id': 'str',
        'cpu_numa_node': 'float',
        'cpu_socket_id': 'float',
        'memory': 'float',
        'up_since': 'str',
        'trace_history_in_seconds': 'float',
        'leadership_role': 'str',
        'last_fencing_time': 'str',
        'status': 'str',
        'cpu_model': 'str',
        'dpdk_ip': 'str',
        'dataplane_transfer_mode': 'str',
        'dpdk_socket_info': 'list[str]',
        'last_join_reject_reason': 'str',
        'is_dpdk': 'bool',
        'cpu_id': 'float'
    }

    attribute_map = {
        'id': 'id',
        'dpdk_port_info': 'dpdk_port_info',
        'network_mode': 'network_mode',
        'mode': 'mode',
        'lowest_node_path_issue': 'lowest_node_path_issue',
        'last_fencing_reason': 'last_fencing_reason',
        'uid': 'uid',
        'hostname': 'hostname',
        'ips': 'ips',
        'slot': 'slot',
        'is_blacklisted': 'is_blacklisted',
        'roles': 'roles',
        'missing_links': 'missing_links',
        'cpu_is_dedicated': 'cpu_is_dedicated',
        'cpu_core_id': 'cpu_core_id',
        'host_id': 'host_id',
        'cpu_numa_node': 'cpu_numa_node',
        'cpu_socket_id': 'cpu_socket_id',
        'memory': 'memory',
        'up_since': 'up_since',
        'trace_history_in_seconds': 'trace_history_in_seconds',
        'leadership_role': 'leadership_role',
        'last_fencing_time': 'last_fencing_time',
        'status': 'status',
        'cpu_model': 'cpu_model',
        'dpdk_ip': 'dpdk_ip',
        'dataplane_transfer_mode': 'dataplane_transfer_mode',
        'dpdk_socket_info': 'dpdk_socket_info',
        'last_join_reject_reason': 'last_join_reject_reason',
        'is_dpdk': 'is_dpdk',
        'cpu_id': 'cpu_id'
    }

    def __init__(self, id=None, dpdk_port_info=None, network_mode=None, mode=None, lowest_node_path_issue=None, last_fencing_reason=None, uid=None, hostname=None, ips=None, slot=None, is_blacklisted=None, roles=None, missing_links=None, cpu_is_dedicated=None, cpu_core_id=None, host_id=None, cpu_numa_node=None, cpu_socket_id=None, memory=None, up_since=None, trace_history_in_seconds=None, leadership_role=None, last_fencing_time=None, status=None, cpu_model=None, dpdk_ip=None, dataplane_transfer_mode=None, dpdk_socket_info=None, last_join_reject_reason=None, is_dpdk=None, cpu_id=None):  # noqa: E501
        """Node - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._dpdk_port_info = None
        self._network_mode = None
        self._mode = None
        self._lowest_node_path_issue = None
        self._last_fencing_reason = None
        self._uid = None
        self._hostname = None
        self._ips = None
        self._slot = None
        self._is_blacklisted = None
        self._roles = None
        self._missing_links = None
        self._cpu_is_dedicated = None
        self._cpu_core_id = None
        self._host_id = None
        self._cpu_numa_node = None
        self._cpu_socket_id = None
        self._memory = None
        self._up_since = None
        self._trace_history_in_seconds = None
        self._leadership_role = None
        self._last_fencing_time = None
        self._status = None
        self._cpu_model = None
        self._dpdk_ip = None
        self._dataplane_transfer_mode = None
        self._dpdk_socket_info = None
        self._last_join_reject_reason = None
        self._is_dpdk = None
        self._cpu_id = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if dpdk_port_info is not None:
            self.dpdk_port_info = dpdk_port_info
        if network_mode is not None:
            self.network_mode = network_mode
        if mode is not None:
            self.mode = mode
        if lowest_node_path_issue is not None:
            self.lowest_node_path_issue = lowest_node_path_issue
        if last_fencing_reason is not None:
            self.last_fencing_reason = last_fencing_reason
        if uid is not None:
            self.uid = uid
        if hostname is not None:
            self.hostname = hostname
        if ips is not None:
            self.ips = ips
        if slot is not None:
            self.slot = slot
        if is_blacklisted is not None:
            self.is_blacklisted = is_blacklisted
        if roles is not None:
            self.roles = roles
        if missing_links is not None:
            self.missing_links = missing_links
        if cpu_is_dedicated is not None:
            self.cpu_is_dedicated = cpu_is_dedicated
        if cpu_core_id is not None:
            self.cpu_core_id = cpu_core_id
        if host_id is not None:
            self.host_id = host_id
        if cpu_numa_node is not None:
            self.cpu_numa_node = cpu_numa_node
        if cpu_socket_id is not None:
            self.cpu_socket_id = cpu_socket_id
        if memory is not None:
            self.memory = memory
        if up_since is not None:
            self.up_since = up_since
        if trace_history_in_seconds is not None:
            self.trace_history_in_seconds = trace_history_in_seconds
        if leadership_role is not None:
            self.leadership_role = leadership_role
        if last_fencing_time is not None:
            self.last_fencing_time = last_fencing_time
        if status is not None:
            self.status = status
        if cpu_model is not None:
            self.cpu_model = cpu_model
        if dpdk_ip is not None:
            self.dpdk_ip = dpdk_ip
        if dataplane_transfer_mode is not None:
            self.dataplane_transfer_mode = dataplane_transfer_mode
        if dpdk_socket_info is not None:
            self.dpdk_socket_info = dpdk_socket_info
        if last_join_reject_reason is not None:
            self.last_join_reject_reason = last_join_reject_reason
        if is_dpdk is not None:
            self.is_dpdk = is_dpdk
        if cpu_id is not None:
            self.cpu_id = cpu_id

    @property
    def id(self):
        """Gets the id of this Node.  # noqa: E501


        :return: The id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Node.


        :param id: The id of this Node.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def dpdk_port_info(self):
        """Gets the dpdk_port_info of this Node.  # noqa: E501


        :return: The dpdk_port_info of this Node.  # noqa: E501
        :rtype: list[NodeDpdkPortInfo]
        """
        return self._dpdk_port_info

    @dpdk_port_info.setter
    def dpdk_port_info(self, dpdk_port_info):
        """Sets the dpdk_port_info of this Node.


        :param dpdk_port_info: The dpdk_port_info of this Node.  # noqa: E501
        :type: list[NodeDpdkPortInfo]
        """

        self._dpdk_port_info = dpdk_port_info

    @property
    def network_mode(self):
        """Gets the network_mode of this Node.  # noqa: E501


        :return: The network_mode of this Node.  # noqa: E501
        :rtype: str
        """
        return self._network_mode

    @network_mode.setter
    def network_mode(self, network_mode):
        """Sets the network_mode of this Node.


        :param network_mode: The network_mode of this Node.  # noqa: E501
        :type: str
        """

        self._network_mode = network_mode

    @property
    def mode(self):
        """Gets the mode of this Node.  # noqa: E501


        :return: The mode of this Node.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this Node.


        :param mode: The mode of this Node.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def lowest_node_path_issue(self):
        """Gets the lowest_node_path_issue of this Node.  # noqa: E501


        :return: The lowest_node_path_issue of this Node.  # noqa: E501
        :rtype: str
        """
        return self._lowest_node_path_issue

    @lowest_node_path_issue.setter
    def lowest_node_path_issue(self, lowest_node_path_issue):
        """Sets the lowest_node_path_issue of this Node.


        :param lowest_node_path_issue: The lowest_node_path_issue of this Node.  # noqa: E501
        :type: str
        """

        self._lowest_node_path_issue = lowest_node_path_issue

    @property
    def last_fencing_reason(self):
        """Gets the last_fencing_reason of this Node.  # noqa: E501


        :return: The last_fencing_reason of this Node.  # noqa: E501
        :rtype: str
        """
        return self._last_fencing_reason

    @last_fencing_reason.setter
    def last_fencing_reason(self, last_fencing_reason):
        """Sets the last_fencing_reason of this Node.


        :param last_fencing_reason: The last_fencing_reason of this Node.  # noqa: E501
        :type: str
        """

        self._last_fencing_reason = last_fencing_reason

    @property
    def uid(self):
        """Gets the uid of this Node.  # noqa: E501


        :return: The uid of this Node.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Node.


        :param uid: The uid of this Node.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def hostname(self):
        """Gets the hostname of this Node.  # noqa: E501


        :return: The hostname of this Node.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this Node.


        :param hostname: The hostname of this Node.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def ips(self):
        """Gets the ips of this Node.  # noqa: E501


        :return: The ips of this Node.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this Node.


        :param ips: The ips of this Node.  # noqa: E501
        :type: list[str]
        """

        self._ips = ips

    @property
    def slot(self):
        """Gets the slot of this Node.  # noqa: E501


        :return: The slot of this Node.  # noqa: E501
        :rtype: float
        """
        return self._slot

    @slot.setter
    def slot(self, slot):
        """Sets the slot of this Node.


        :param slot: The slot of this Node.  # noqa: E501
        :type: float
        """

        self._slot = slot

    @property
    def is_blacklisted(self):
        """Gets the is_blacklisted of this Node.  # noqa: E501


        :return: The is_blacklisted of this Node.  # noqa: E501
        :rtype: bool
        """
        return self._is_blacklisted

    @is_blacklisted.setter
    def is_blacklisted(self, is_blacklisted):
        """Sets the is_blacklisted of this Node.


        :param is_blacklisted: The is_blacklisted of this Node.  # noqa: E501
        :type: bool
        """

        self._is_blacklisted = is_blacklisted

    @property
    def roles(self):
        """Gets the roles of this Node.  # noqa: E501


        :return: The roles of this Node.  # noqa: E501
        :rtype: list[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this Node.


        :param roles: The roles of this Node.  # noqa: E501
        :type: list[str]
        """

        self._roles = roles

    @property
    def missing_links(self):
        """Gets the missing_links of this Node.  # noqa: E501


        :return: The missing_links of this Node.  # noqa: E501
        :rtype: str
        """
        return self._missing_links

    @missing_links.setter
    def missing_links(self, missing_links):
        """Sets the missing_links of this Node.


        :param missing_links: The missing_links of this Node.  # noqa: E501
        :type: str
        """

        self._missing_links = missing_links

    @property
    def cpu_is_dedicated(self):
        """Gets the cpu_is_dedicated of this Node.  # noqa: E501


        :return: The cpu_is_dedicated of this Node.  # noqa: E501
        :rtype: bool
        """
        return self._cpu_is_dedicated

    @cpu_is_dedicated.setter
    def cpu_is_dedicated(self, cpu_is_dedicated):
        """Sets the cpu_is_dedicated of this Node.


        :param cpu_is_dedicated: The cpu_is_dedicated of this Node.  # noqa: E501
        :type: bool
        """

        self._cpu_is_dedicated = cpu_is_dedicated

    @property
    def cpu_core_id(self):
        """Gets the cpu_core_id of this Node.  # noqa: E501


        :return: The cpu_core_id of this Node.  # noqa: E501
        :rtype: float
        """
        return self._cpu_core_id

    @cpu_core_id.setter
    def cpu_core_id(self, cpu_core_id):
        """Sets the cpu_core_id of this Node.


        :param cpu_core_id: The cpu_core_id of this Node.  # noqa: E501
        :type: float
        """

        self._cpu_core_id = cpu_core_id

    @property
    def host_id(self):
        """Gets the host_id of this Node.  # noqa: E501


        :return: The host_id of this Node.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this Node.


        :param host_id: The host_id of this Node.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def cpu_numa_node(self):
        """Gets the cpu_numa_node of this Node.  # noqa: E501


        :return: The cpu_numa_node of this Node.  # noqa: E501
        :rtype: float
        """
        return self._cpu_numa_node

    @cpu_numa_node.setter
    def cpu_numa_node(self, cpu_numa_node):
        """Sets the cpu_numa_node of this Node.


        :param cpu_numa_node: The cpu_numa_node of this Node.  # noqa: E501
        :type: float
        """

        self._cpu_numa_node = cpu_numa_node

    @property
    def cpu_socket_id(self):
        """Gets the cpu_socket_id of this Node.  # noqa: E501


        :return: The cpu_socket_id of this Node.  # noqa: E501
        :rtype: float
        """
        return self._cpu_socket_id

    @cpu_socket_id.setter
    def cpu_socket_id(self, cpu_socket_id):
        """Sets the cpu_socket_id of this Node.


        :param cpu_socket_id: The cpu_socket_id of this Node.  # noqa: E501
        :type: float
        """

        self._cpu_socket_id = cpu_socket_id

    @property
    def memory(self):
        """Gets the memory of this Node.  # noqa: E501


        :return: The memory of this Node.  # noqa: E501
        :rtype: float
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this Node.


        :param memory: The memory of this Node.  # noqa: E501
        :type: float
        """

        self._memory = memory

    @property
    def up_since(self):
        """Gets the up_since of this Node.  # noqa: E501


        :return: The up_since of this Node.  # noqa: E501
        :rtype: str
        """
        return self._up_since

    @up_since.setter
    def up_since(self, up_since):
        """Sets the up_since of this Node.


        :param up_since: The up_since of this Node.  # noqa: E501
        :type: str
        """

        self._up_since = up_since

    @property
    def trace_history_in_seconds(self):
        """Gets the trace_history_in_seconds of this Node.  # noqa: E501


        :return: The trace_history_in_seconds of this Node.  # noqa: E501
        :rtype: float
        """
        return self._trace_history_in_seconds

    @trace_history_in_seconds.setter
    def trace_history_in_seconds(self, trace_history_in_seconds):
        """Sets the trace_history_in_seconds of this Node.


        :param trace_history_in_seconds: The trace_history_in_seconds of this Node.  # noqa: E501
        :type: float
        """

        self._trace_history_in_seconds = trace_history_in_seconds

    @property
    def leadership_role(self):
        """Gets the leadership_role of this Node.  # noqa: E501


        :return: The leadership_role of this Node.  # noqa: E501
        :rtype: str
        """
        return self._leadership_role

    @leadership_role.setter
    def leadership_role(self, leadership_role):
        """Sets the leadership_role of this Node.


        :param leadership_role: The leadership_role of this Node.  # noqa: E501
        :type: str
        """

        self._leadership_role = leadership_role

    @property
    def last_fencing_time(self):
        """Gets the last_fencing_time of this Node.  # noqa: E501


        :return: The last_fencing_time of this Node.  # noqa: E501
        :rtype: str
        """
        return self._last_fencing_time

    @last_fencing_time.setter
    def last_fencing_time(self, last_fencing_time):
        """Sets the last_fencing_time of this Node.


        :param last_fencing_time: The last_fencing_time of this Node.  # noqa: E501
        :type: str
        """

        self._last_fencing_time = last_fencing_time

    @property
    def status(self):
        """Gets the status of this Node.  # noqa: E501


        :return: The status of this Node.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Node.


        :param status: The status of this Node.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def cpu_model(self):
        """Gets the cpu_model of this Node.  # noqa: E501


        :return: The cpu_model of this Node.  # noqa: E501
        :rtype: str
        """
        return self._cpu_model

    @cpu_model.setter
    def cpu_model(self, cpu_model):
        """Sets the cpu_model of this Node.


        :param cpu_model: The cpu_model of this Node.  # noqa: E501
        :type: str
        """

        self._cpu_model = cpu_model

    @property
    def dpdk_ip(self):
        """Gets the dpdk_ip of this Node.  # noqa: E501


        :return: The dpdk_ip of this Node.  # noqa: E501
        :rtype: str
        """
        return self._dpdk_ip

    @dpdk_ip.setter
    def dpdk_ip(self, dpdk_ip):
        """Sets the dpdk_ip of this Node.


        :param dpdk_ip: The dpdk_ip of this Node.  # noqa: E501
        :type: str
        """

        self._dpdk_ip = dpdk_ip

    @property
    def dataplane_transfer_mode(self):
        """Gets the dataplane_transfer_mode of this Node.  # noqa: E501


        :return: The dataplane_transfer_mode of this Node.  # noqa: E501
        :rtype: str
        """
        return self._dataplane_transfer_mode

    @dataplane_transfer_mode.setter
    def dataplane_transfer_mode(self, dataplane_transfer_mode):
        """Sets the dataplane_transfer_mode of this Node.


        :param dataplane_transfer_mode: The dataplane_transfer_mode of this Node.  # noqa: E501
        :type: str
        """

        self._dataplane_transfer_mode = dataplane_transfer_mode

    @property
    def dpdk_socket_info(self):
        """Gets the dpdk_socket_info of this Node.  # noqa: E501


        :return: The dpdk_socket_info of this Node.  # noqa: E501
        :rtype: list[str]
        """
        return self._dpdk_socket_info

    @dpdk_socket_info.setter
    def dpdk_socket_info(self, dpdk_socket_info):
        """Sets the dpdk_socket_info of this Node.


        :param dpdk_socket_info: The dpdk_socket_info of this Node.  # noqa: E501
        :type: list[str]
        """

        self._dpdk_socket_info = dpdk_socket_info

    @property
    def last_join_reject_reason(self):
        """Gets the last_join_reject_reason of this Node.  # noqa: E501


        :return: The last_join_reject_reason of this Node.  # noqa: E501
        :rtype: str
        """
        return self._last_join_reject_reason

    @last_join_reject_reason.setter
    def last_join_reject_reason(self, last_join_reject_reason):
        """Sets the last_join_reject_reason of this Node.


        :param last_join_reject_reason: The last_join_reject_reason of this Node.  # noqa: E501
        :type: str
        """

        self._last_join_reject_reason = last_join_reject_reason

    @property
    def is_dpdk(self):
        """Gets the is_dpdk of this Node.  # noqa: E501


        :return: The is_dpdk of this Node.  # noqa: E501
        :rtype: bool
        """
        return self._is_dpdk

    @is_dpdk.setter
    def is_dpdk(self, is_dpdk):
        """Sets the is_dpdk of this Node.


        :param is_dpdk: The is_dpdk of this Node.  # noqa: E501
        :type: bool
        """

        self._is_dpdk = is_dpdk

    @property
    def cpu_id(self):
        """Gets the cpu_id of this Node.  # noqa: E501


        :return: The cpu_id of this Node.  # noqa: E501
        :rtype: float
        """
        return self._cpu_id

    @cpu_id.setter
    def cpu_id(self, cpu_id):
        """Sets the cpu_id of this Node.


        :param cpu_id: The cpu_id of this Node.  # noqa: E501
        :type: float
        """

        self._cpu_id = cpu_id

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
        if issubclass(Node, dict):
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
        if not isinstance(other, Node):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

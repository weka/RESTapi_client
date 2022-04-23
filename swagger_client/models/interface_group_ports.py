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

class InterfaceGroupPorts(object):
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
        'host_id': 'str',
        'host_uid': 'str',
        'port': 'str',
        'status': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'host_uid': 'host_uid',
        'port': 'port',
        'status': 'status'
    }

    def __init__(self, host_id=None, host_uid=None, port=None, status=None):  # noqa: E501
        """InterfaceGroupPorts - a model defined in Swagger"""  # noqa: E501
        self._host_id = None
        self._host_uid = None
        self._port = None
        self._status = None
        self.discriminator = None
        if host_id is not None:
            self.host_id = host_id
        if host_uid is not None:
            self.host_uid = host_uid
        if port is not None:
            self.port = port
        if status is not None:
            self.status = status

    @property
    def host_id(self):
        """Gets the host_id of this InterfaceGroupPorts.  # noqa: E501


        :return: The host_id of this InterfaceGroupPorts.  # noqa: E501
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this InterfaceGroupPorts.


        :param host_id: The host_id of this InterfaceGroupPorts.  # noqa: E501
        :type: str
        """

        self._host_id = host_id

    @property
    def host_uid(self):
        """Gets the host_uid of this InterfaceGroupPorts.  # noqa: E501


        :return: The host_uid of this InterfaceGroupPorts.  # noqa: E501
        :rtype: str
        """
        return self._host_uid

    @host_uid.setter
    def host_uid(self, host_uid):
        """Sets the host_uid of this InterfaceGroupPorts.


        :param host_uid: The host_uid of this InterfaceGroupPorts.  # noqa: E501
        :type: str
        """

        self._host_uid = host_uid

    @property
    def port(self):
        """Gets the port of this InterfaceGroupPorts.  # noqa: E501


        :return: The port of this InterfaceGroupPorts.  # noqa: E501
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this InterfaceGroupPorts.


        :param port: The port of this InterfaceGroupPorts.  # noqa: E501
        :type: str
        """

        self._port = port

    @property
    def status(self):
        """Gets the status of this InterfaceGroupPorts.  # noqa: E501


        :return: The status of this InterfaceGroupPorts.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InterfaceGroupPorts.


        :param status: The status of this InterfaceGroupPorts.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(InterfaceGroupPorts, dict):
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
        if not isinstance(other, InterfaceGroupPorts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class InlineResponse20011EventFields(object):
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
        'node_id': 'float',
        'pid': 'float',
        'sw_release': 'str',
        'sw_version': 'str'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'pid': 'pid',
        'sw_release': 'swRelease',
        'sw_version': 'swVersion'
    }

    def __init__(self, node_id=None, pid=None, sw_release=None, sw_version=None):  # noqa: E501
        """InlineResponse20011EventFields - a model defined in Swagger"""  # noqa: E501
        self._node_id = None
        self._pid = None
        self._sw_release = None
        self._sw_version = None
        self.discriminator = None
        if node_id is not None:
            self.node_id = node_id
        if pid is not None:
            self.pid = pid
        if sw_release is not None:
            self.sw_release = sw_release
        if sw_version is not None:
            self.sw_version = sw_version

    @property
    def node_id(self):
        """Gets the node_id of this InlineResponse20011EventFields.  # noqa: E501


        :return: The node_id of this InlineResponse20011EventFields.  # noqa: E501
        :rtype: float
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this InlineResponse20011EventFields.


        :param node_id: The node_id of this InlineResponse20011EventFields.  # noqa: E501
        :type: float
        """

        self._node_id = node_id

    @property
    def pid(self):
        """Gets the pid of this InlineResponse20011EventFields.  # noqa: E501


        :return: The pid of this InlineResponse20011EventFields.  # noqa: E501
        :rtype: float
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this InlineResponse20011EventFields.


        :param pid: The pid of this InlineResponse20011EventFields.  # noqa: E501
        :type: float
        """

        self._pid = pid

    @property
    def sw_release(self):
        """Gets the sw_release of this InlineResponse20011EventFields.  # noqa: E501


        :return: The sw_release of this InlineResponse20011EventFields.  # noqa: E501
        :rtype: str
        """
        return self._sw_release

    @sw_release.setter
    def sw_release(self, sw_release):
        """Sets the sw_release of this InlineResponse20011EventFields.


        :param sw_release: The sw_release of this InlineResponse20011EventFields.  # noqa: E501
        :type: str
        """

        self._sw_release = sw_release

    @property
    def sw_version(self):
        """Gets the sw_version of this InlineResponse20011EventFields.  # noqa: E501


        :return: The sw_version of this InlineResponse20011EventFields.  # noqa: E501
        :rtype: str
        """
        return self._sw_version

    @sw_version.setter
    def sw_version(self, sw_version):
        """Sets the sw_version of this InlineResponse20011EventFields.


        :param sw_version: The sw_version of this InlineResponse20011EventFields.  # noqa: E501
        :type: str
        """

        self._sw_version = sw_version

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
        if issubclass(InlineResponse20011EventFields, dict):
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
        if not isinstance(other, InlineResponse20011EventFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

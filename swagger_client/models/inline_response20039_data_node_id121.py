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

class InlineResponse20039DataNodeId121(object):
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
        'chan_type': 'str',
        'info': 'InlineResponse20039DataInfo',
        'op_phase': 'str'
    }

    attribute_map = {
        'chan_type': 'chanType',
        'info': 'info',
        'op_phase': 'opPhase'
    }

    def __init__(self, chan_type=None, info=None, op_phase=None):  # noqa: E501
        """InlineResponse20039DataNodeId121 - a model defined in Swagger"""  # noqa: E501
        self._chan_type = None
        self._info = None
        self._op_phase = None
        self.discriminator = None
        if chan_type is not None:
            self.chan_type = chan_type
        if info is not None:
            self.info = info
        if op_phase is not None:
            self.op_phase = op_phase

    @property
    def chan_type(self):
        """Gets the chan_type of this InlineResponse20039DataNodeId121.  # noqa: E501


        :return: The chan_type of this InlineResponse20039DataNodeId121.  # noqa: E501
        :rtype: str
        """
        return self._chan_type

    @chan_type.setter
    def chan_type(self, chan_type):
        """Sets the chan_type of this InlineResponse20039DataNodeId121.


        :param chan_type: The chan_type of this InlineResponse20039DataNodeId121.  # noqa: E501
        :type: str
        """

        self._chan_type = chan_type

    @property
    def info(self):
        """Gets the info of this InlineResponse20039DataNodeId121.  # noqa: E501


        :return: The info of this InlineResponse20039DataNodeId121.  # noqa: E501
        :rtype: InlineResponse20039DataInfo
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this InlineResponse20039DataNodeId121.


        :param info: The info of this InlineResponse20039DataNodeId121.  # noqa: E501
        :type: InlineResponse20039DataInfo
        """

        self._info = info

    @property
    def op_phase(self):
        """Gets the op_phase of this InlineResponse20039DataNodeId121.  # noqa: E501


        :return: The op_phase of this InlineResponse20039DataNodeId121.  # noqa: E501
        :rtype: str
        """
        return self._op_phase

    @op_phase.setter
    def op_phase(self, op_phase):
        """Sets the op_phase of this InlineResponse20039DataNodeId121.


        :param op_phase: The op_phase of this InlineResponse20039DataNodeId121.  # noqa: E501
        :type: str
        """

        self._op_phase = op_phase

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
        if issubclass(InlineResponse20039DataNodeId121, dict):
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
        if not isinstance(other, InlineResponse20039DataNodeId121):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

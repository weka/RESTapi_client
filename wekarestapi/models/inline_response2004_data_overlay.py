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

class InlineResponse2004DataOverlay(object):
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
        'branching_factor': 'float',
        'client_nodes_at_risk': 'float',
        'client_nodes_not_supported': 'float',
        'client_nodes_safety_histogram': 'list[InlineResponse2004DataOverlayClientNodesSafetyHistogram]',
        'clients_branching_factor': 'float'
    }

    attribute_map = {
        'branching_factor': 'branching_factor',
        'client_nodes_at_risk': 'client_nodes_at_risk',
        'client_nodes_not_supported': 'client_nodes_not_supported',
        'client_nodes_safety_histogram': 'client_nodes_safety_histogram',
        'clients_branching_factor': 'clients_branching_factor'
    }

    def __init__(self, branching_factor=None, client_nodes_at_risk=None, client_nodes_not_supported=None, client_nodes_safety_histogram=None, clients_branching_factor=None):  # noqa: E501
        """InlineResponse2004DataOverlay - a model defined in Swagger"""  # noqa: E501
        self._branching_factor = None
        self._client_nodes_at_risk = None
        self._client_nodes_not_supported = None
        self._client_nodes_safety_histogram = None
        self._clients_branching_factor = None
        self.discriminator = None
        if branching_factor is not None:
            self.branching_factor = branching_factor
        if client_nodes_at_risk is not None:
            self.client_nodes_at_risk = client_nodes_at_risk
        if client_nodes_not_supported is not None:
            self.client_nodes_not_supported = client_nodes_not_supported
        if client_nodes_safety_histogram is not None:
            self.client_nodes_safety_histogram = client_nodes_safety_histogram
        if clients_branching_factor is not None:
            self.clients_branching_factor = clients_branching_factor

    @property
    def branching_factor(self):
        """Gets the branching_factor of this InlineResponse2004DataOverlay.  # noqa: E501


        :return: The branching_factor of this InlineResponse2004DataOverlay.  # noqa: E501
        :rtype: float
        """
        return self._branching_factor

    @branching_factor.setter
    def branching_factor(self, branching_factor):
        """Sets the branching_factor of this InlineResponse2004DataOverlay.


        :param branching_factor: The branching_factor of this InlineResponse2004DataOverlay.  # noqa: E501
        :type: float
        """

        self._branching_factor = branching_factor

    @property
    def client_nodes_at_risk(self):
        """Gets the client_nodes_at_risk of this InlineResponse2004DataOverlay.  # noqa: E501


        :return: The client_nodes_at_risk of this InlineResponse2004DataOverlay.  # noqa: E501
        :rtype: float
        """
        return self._client_nodes_at_risk

    @client_nodes_at_risk.setter
    def client_nodes_at_risk(self, client_nodes_at_risk):
        """Sets the client_nodes_at_risk of this InlineResponse2004DataOverlay.


        :param client_nodes_at_risk: The client_nodes_at_risk of this InlineResponse2004DataOverlay.  # noqa: E501
        :type: float
        """

        self._client_nodes_at_risk = client_nodes_at_risk

    @property
    def client_nodes_not_supported(self):
        """Gets the client_nodes_not_supported of this InlineResponse2004DataOverlay.  # noqa: E501


        :return: The client_nodes_not_supported of this InlineResponse2004DataOverlay.  # noqa: E501
        :rtype: float
        """
        return self._client_nodes_not_supported

    @client_nodes_not_supported.setter
    def client_nodes_not_supported(self, client_nodes_not_supported):
        """Sets the client_nodes_not_supported of this InlineResponse2004DataOverlay.


        :param client_nodes_not_supported: The client_nodes_not_supported of this InlineResponse2004DataOverlay.  # noqa: E501
        :type: float
        """

        self._client_nodes_not_supported = client_nodes_not_supported

    @property
    def client_nodes_safety_histogram(self):
        """Gets the client_nodes_safety_histogram of this InlineResponse2004DataOverlay.  # noqa: E501


        :return: The client_nodes_safety_histogram of this InlineResponse2004DataOverlay.  # noqa: E501
        :rtype: list[InlineResponse2004DataOverlayClientNodesSafetyHistogram]
        """
        return self._client_nodes_safety_histogram

    @client_nodes_safety_histogram.setter
    def client_nodes_safety_histogram(self, client_nodes_safety_histogram):
        """Sets the client_nodes_safety_histogram of this InlineResponse2004DataOverlay.


        :param client_nodes_safety_histogram: The client_nodes_safety_histogram of this InlineResponse2004DataOverlay.  # noqa: E501
        :type: list[InlineResponse2004DataOverlayClientNodesSafetyHistogram]
        """

        self._client_nodes_safety_histogram = client_nodes_safety_histogram

    @property
    def clients_branching_factor(self):
        """Gets the clients_branching_factor of this InlineResponse2004DataOverlay.  # noqa: E501


        :return: The clients_branching_factor of this InlineResponse2004DataOverlay.  # noqa: E501
        :rtype: float
        """
        return self._clients_branching_factor

    @clients_branching_factor.setter
    def clients_branching_factor(self, clients_branching_factor):
        """Sets the clients_branching_factor of this InlineResponse2004DataOverlay.


        :param clients_branching_factor: The clients_branching_factor of this InlineResponse2004DataOverlay.  # noqa: E501
        :type: float
        """

        self._clients_branching_factor = clients_branching_factor

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
        if issubclass(InlineResponse2004DataOverlay, dict):
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
        if not isinstance(other, InlineResponse2004DataOverlay):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

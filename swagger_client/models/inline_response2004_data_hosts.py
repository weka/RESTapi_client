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

class InlineResponse2004DataHosts(object):
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
        'active_count': 'float',
        'backends': 'InlineResponse2004DataDrives',
        'clients': 'InlineResponse2004DataHostsClients',
        'total_count': 'float'
    }

    attribute_map = {
        'active_count': 'active_count',
        'backends': 'backends',
        'clients': 'clients',
        'total_count': 'total_count'
    }

    def __init__(self, active_count=None, backends=None, clients=None, total_count=None):  # noqa: E501
        """InlineResponse2004DataHosts - a model defined in Swagger"""  # noqa: E501
        self._active_count = None
        self._backends = None
        self._clients = None
        self._total_count = None
        self.discriminator = None
        if active_count is not None:
            self.active_count = active_count
        if backends is not None:
            self.backends = backends
        if clients is not None:
            self.clients = clients
        if total_count is not None:
            self.total_count = total_count

    @property
    def active_count(self):
        """Gets the active_count of this InlineResponse2004DataHosts.  # noqa: E501


        :return: The active_count of this InlineResponse2004DataHosts.  # noqa: E501
        :rtype: float
        """
        return self._active_count

    @active_count.setter
    def active_count(self, active_count):
        """Sets the active_count of this InlineResponse2004DataHosts.


        :param active_count: The active_count of this InlineResponse2004DataHosts.  # noqa: E501
        :type: float
        """

        self._active_count = active_count

    @property
    def backends(self):
        """Gets the backends of this InlineResponse2004DataHosts.  # noqa: E501


        :return: The backends of this InlineResponse2004DataHosts.  # noqa: E501
        :rtype: InlineResponse2004DataDrives
        """
        return self._backends

    @backends.setter
    def backends(self, backends):
        """Sets the backends of this InlineResponse2004DataHosts.


        :param backends: The backends of this InlineResponse2004DataHosts.  # noqa: E501
        :type: InlineResponse2004DataDrives
        """

        self._backends = backends

    @property
    def clients(self):
        """Gets the clients of this InlineResponse2004DataHosts.  # noqa: E501


        :return: The clients of this InlineResponse2004DataHosts.  # noqa: E501
        :rtype: InlineResponse2004DataHostsClients
        """
        return self._clients

    @clients.setter
    def clients(self, clients):
        """Sets the clients of this InlineResponse2004DataHosts.


        :param clients: The clients of this InlineResponse2004DataHosts.  # noqa: E501
        :type: InlineResponse2004DataHostsClients
        """

        self._clients = clients

    @property
    def total_count(self):
        """Gets the total_count of this InlineResponse2004DataHosts.  # noqa: E501


        :return: The total_count of this InlineResponse2004DataHosts.  # noqa: E501
        :rtype: float
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this InlineResponse2004DataHosts.


        :param total_count: The total_count of this InlineResponse2004DataHosts.  # noqa: E501
        :type: float
        """

        self._total_count = total_count

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
        if issubclass(InlineResponse2004DataHosts, dict):
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
        if not isinstance(other, InlineResponse2004DataHosts):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

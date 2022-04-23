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

class InlineResponse2004DataBuckets(object):
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
        'active': 'float',
        'flush_finished': 'float',
        'global_flush_generation': 'float',
        'global_flush_status': 'str',
        'shutdown_finished': 'float',
        'total': 'float'
    }

    attribute_map = {
        'active': 'active',
        'flush_finished': 'flush_finished',
        'global_flush_generation': 'global_flush_generation',
        'global_flush_status': 'global_flush_status',
        'shutdown_finished': 'shutdown_finished',
        'total': 'total'
    }

    def __init__(self, active=None, flush_finished=None, global_flush_generation=None, global_flush_status=None, shutdown_finished=None, total=None):  # noqa: E501
        """InlineResponse2004DataBuckets - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._flush_finished = None
        self._global_flush_generation = None
        self._global_flush_status = None
        self._shutdown_finished = None
        self._total = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if flush_finished is not None:
            self.flush_finished = flush_finished
        if global_flush_generation is not None:
            self.global_flush_generation = global_flush_generation
        if global_flush_status is not None:
            self.global_flush_status = global_flush_status
        if shutdown_finished is not None:
            self.shutdown_finished = shutdown_finished
        if total is not None:
            self.total = total

    @property
    def active(self):
        """Gets the active of this InlineResponse2004DataBuckets.  # noqa: E501


        :return: The active of this InlineResponse2004DataBuckets.  # noqa: E501
        :rtype: float
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this InlineResponse2004DataBuckets.


        :param active: The active of this InlineResponse2004DataBuckets.  # noqa: E501
        :type: float
        """

        self._active = active

    @property
    def flush_finished(self):
        """Gets the flush_finished of this InlineResponse2004DataBuckets.  # noqa: E501


        :return: The flush_finished of this InlineResponse2004DataBuckets.  # noqa: E501
        :rtype: float
        """
        return self._flush_finished

    @flush_finished.setter
    def flush_finished(self, flush_finished):
        """Sets the flush_finished of this InlineResponse2004DataBuckets.


        :param flush_finished: The flush_finished of this InlineResponse2004DataBuckets.  # noqa: E501
        :type: float
        """

        self._flush_finished = flush_finished

    @property
    def global_flush_generation(self):
        """Gets the global_flush_generation of this InlineResponse2004DataBuckets.  # noqa: E501


        :return: The global_flush_generation of this InlineResponse2004DataBuckets.  # noqa: E501
        :rtype: float
        """
        return self._global_flush_generation

    @global_flush_generation.setter
    def global_flush_generation(self, global_flush_generation):
        """Sets the global_flush_generation of this InlineResponse2004DataBuckets.


        :param global_flush_generation: The global_flush_generation of this InlineResponse2004DataBuckets.  # noqa: E501
        :type: float
        """

        self._global_flush_generation = global_flush_generation

    @property
    def global_flush_status(self):
        """Gets the global_flush_status of this InlineResponse2004DataBuckets.  # noqa: E501


        :return: The global_flush_status of this InlineResponse2004DataBuckets.  # noqa: E501
        :rtype: str
        """
        return self._global_flush_status

    @global_flush_status.setter
    def global_flush_status(self, global_flush_status):
        """Sets the global_flush_status of this InlineResponse2004DataBuckets.


        :param global_flush_status: The global_flush_status of this InlineResponse2004DataBuckets.  # noqa: E501
        :type: str
        """

        self._global_flush_status = global_flush_status

    @property
    def shutdown_finished(self):
        """Gets the shutdown_finished of this InlineResponse2004DataBuckets.  # noqa: E501


        :return: The shutdown_finished of this InlineResponse2004DataBuckets.  # noqa: E501
        :rtype: float
        """
        return self._shutdown_finished

    @shutdown_finished.setter
    def shutdown_finished(self, shutdown_finished):
        """Sets the shutdown_finished of this InlineResponse2004DataBuckets.


        :param shutdown_finished: The shutdown_finished of this InlineResponse2004DataBuckets.  # noqa: E501
        :type: float
        """

        self._shutdown_finished = shutdown_finished

    @property
    def total(self):
        """Gets the total of this InlineResponse2004DataBuckets.  # noqa: E501


        :return: The total of this InlineResponse2004DataBuckets.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this InlineResponse2004DataBuckets.


        :param total: The total of this InlineResponse2004DataBuckets.  # noqa: E501
        :type: float
        """

        self._total = total

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
        if issubclass(InlineResponse2004DataBuckets, dict):
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
        if not isinstance(other, InlineResponse2004DataBuckets):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

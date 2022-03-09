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

class InlineResponse2008DataHangingIos(object):
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
        'event_driver_frontend_threshold_secs': 'float',
        'last_emitted_backend_no_longer_detected_event': 'str',
        'alerts_threshold_secs': 'float',
        'last_emitted_backend_event': 'str',
        'event_backend_threshold_secs': 'float',
        'last_emitted_driver_frontend_no_longer_detected_event': 'str',
        'last_emitted_driver_frontend_event': 'str',
        'event_nfs_frontend_threshold_secs': 'float',
        'last_emitted_nfs_frontend_event': 'str',
        'last_emitted_nfs_frontend_no_longer_detected_event': 'str'
    }

    attribute_map = {
        'event_driver_frontend_threshold_secs': 'event_driver_frontend_threshold_secs',
        'last_emitted_backend_no_longer_detected_event': 'last_emitted_backend_no_longer_detected_event',
        'alerts_threshold_secs': 'alerts_threshold_secs',
        'last_emitted_backend_event': 'last_emitted_backend_event',
        'event_backend_threshold_secs': 'event_backend_threshold_secs',
        'last_emitted_driver_frontend_no_longer_detected_event': 'last_emitted_driver_frontend_no_longer_detected_event',
        'last_emitted_driver_frontend_event': 'last_emitted_driver_frontend_event',
        'event_nfs_frontend_threshold_secs': 'event_nfs_frontend_threshold_secs',
        'last_emitted_nfs_frontend_event': 'last_emitted_nfs_frontend_event',
        'last_emitted_nfs_frontend_no_longer_detected_event': 'last_emitted_nfs_frontend_no_longer_detected_event'
    }

    def __init__(self, event_driver_frontend_threshold_secs=None, last_emitted_backend_no_longer_detected_event=None, alerts_threshold_secs=None, last_emitted_backend_event=None, event_backend_threshold_secs=None, last_emitted_driver_frontend_no_longer_detected_event=None, last_emitted_driver_frontend_event=None, event_nfs_frontend_threshold_secs=None, last_emitted_nfs_frontend_event=None, last_emitted_nfs_frontend_no_longer_detected_event=None):  # noqa: E501
        """InlineResponse2008DataHangingIos - a model defined in Swagger"""  # noqa: E501
        self._event_driver_frontend_threshold_secs = None
        self._last_emitted_backend_no_longer_detected_event = None
        self._alerts_threshold_secs = None
        self._last_emitted_backend_event = None
        self._event_backend_threshold_secs = None
        self._last_emitted_driver_frontend_no_longer_detected_event = None
        self._last_emitted_driver_frontend_event = None
        self._event_nfs_frontend_threshold_secs = None
        self._last_emitted_nfs_frontend_event = None
        self._last_emitted_nfs_frontend_no_longer_detected_event = None
        self.discriminator = None
        if event_driver_frontend_threshold_secs is not None:
            self.event_driver_frontend_threshold_secs = event_driver_frontend_threshold_secs
        if last_emitted_backend_no_longer_detected_event is not None:
            self.last_emitted_backend_no_longer_detected_event = last_emitted_backend_no_longer_detected_event
        if alerts_threshold_secs is not None:
            self.alerts_threshold_secs = alerts_threshold_secs
        if last_emitted_backend_event is not None:
            self.last_emitted_backend_event = last_emitted_backend_event
        if event_backend_threshold_secs is not None:
            self.event_backend_threshold_secs = event_backend_threshold_secs
        if last_emitted_driver_frontend_no_longer_detected_event is not None:
            self.last_emitted_driver_frontend_no_longer_detected_event = last_emitted_driver_frontend_no_longer_detected_event
        if last_emitted_driver_frontend_event is not None:
            self.last_emitted_driver_frontend_event = last_emitted_driver_frontend_event
        if event_nfs_frontend_threshold_secs is not None:
            self.event_nfs_frontend_threshold_secs = event_nfs_frontend_threshold_secs
        if last_emitted_nfs_frontend_event is not None:
            self.last_emitted_nfs_frontend_event = last_emitted_nfs_frontend_event
        if last_emitted_nfs_frontend_no_longer_detected_event is not None:
            self.last_emitted_nfs_frontend_no_longer_detected_event = last_emitted_nfs_frontend_no_longer_detected_event

    @property
    def event_driver_frontend_threshold_secs(self):
        """Gets the event_driver_frontend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The event_driver_frontend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: float
        """
        return self._event_driver_frontend_threshold_secs

    @event_driver_frontend_threshold_secs.setter
    def event_driver_frontend_threshold_secs(self, event_driver_frontend_threshold_secs):
        """Sets the event_driver_frontend_threshold_secs of this InlineResponse2008DataHangingIos.


        :param event_driver_frontend_threshold_secs: The event_driver_frontend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: float
        """

        self._event_driver_frontend_threshold_secs = event_driver_frontend_threshold_secs

    @property
    def last_emitted_backend_no_longer_detected_event(self):
        """Gets the last_emitted_backend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The last_emitted_backend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: str
        """
        return self._last_emitted_backend_no_longer_detected_event

    @last_emitted_backend_no_longer_detected_event.setter
    def last_emitted_backend_no_longer_detected_event(self, last_emitted_backend_no_longer_detected_event):
        """Sets the last_emitted_backend_no_longer_detected_event of this InlineResponse2008DataHangingIos.


        :param last_emitted_backend_no_longer_detected_event: The last_emitted_backend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: str
        """

        self._last_emitted_backend_no_longer_detected_event = last_emitted_backend_no_longer_detected_event

    @property
    def alerts_threshold_secs(self):
        """Gets the alerts_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The alerts_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: float
        """
        return self._alerts_threshold_secs

    @alerts_threshold_secs.setter
    def alerts_threshold_secs(self, alerts_threshold_secs):
        """Sets the alerts_threshold_secs of this InlineResponse2008DataHangingIos.


        :param alerts_threshold_secs: The alerts_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: float
        """

        self._alerts_threshold_secs = alerts_threshold_secs

    @property
    def last_emitted_backend_event(self):
        """Gets the last_emitted_backend_event of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The last_emitted_backend_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: str
        """
        return self._last_emitted_backend_event

    @last_emitted_backend_event.setter
    def last_emitted_backend_event(self, last_emitted_backend_event):
        """Sets the last_emitted_backend_event of this InlineResponse2008DataHangingIos.


        :param last_emitted_backend_event: The last_emitted_backend_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: str
        """

        self._last_emitted_backend_event = last_emitted_backend_event

    @property
    def event_backend_threshold_secs(self):
        """Gets the event_backend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The event_backend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: float
        """
        return self._event_backend_threshold_secs

    @event_backend_threshold_secs.setter
    def event_backend_threshold_secs(self, event_backend_threshold_secs):
        """Sets the event_backend_threshold_secs of this InlineResponse2008DataHangingIos.


        :param event_backend_threshold_secs: The event_backend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: float
        """

        self._event_backend_threshold_secs = event_backend_threshold_secs

    @property
    def last_emitted_driver_frontend_no_longer_detected_event(self):
        """Gets the last_emitted_driver_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The last_emitted_driver_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: str
        """
        return self._last_emitted_driver_frontend_no_longer_detected_event

    @last_emitted_driver_frontend_no_longer_detected_event.setter
    def last_emitted_driver_frontend_no_longer_detected_event(self, last_emitted_driver_frontend_no_longer_detected_event):
        """Sets the last_emitted_driver_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.


        :param last_emitted_driver_frontend_no_longer_detected_event: The last_emitted_driver_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: str
        """

        self._last_emitted_driver_frontend_no_longer_detected_event = last_emitted_driver_frontend_no_longer_detected_event

    @property
    def last_emitted_driver_frontend_event(self):
        """Gets the last_emitted_driver_frontend_event of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The last_emitted_driver_frontend_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: str
        """
        return self._last_emitted_driver_frontend_event

    @last_emitted_driver_frontend_event.setter
    def last_emitted_driver_frontend_event(self, last_emitted_driver_frontend_event):
        """Sets the last_emitted_driver_frontend_event of this InlineResponse2008DataHangingIos.


        :param last_emitted_driver_frontend_event: The last_emitted_driver_frontend_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: str
        """

        self._last_emitted_driver_frontend_event = last_emitted_driver_frontend_event

    @property
    def event_nfs_frontend_threshold_secs(self):
        """Gets the event_nfs_frontend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The event_nfs_frontend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: float
        """
        return self._event_nfs_frontend_threshold_secs

    @event_nfs_frontend_threshold_secs.setter
    def event_nfs_frontend_threshold_secs(self, event_nfs_frontend_threshold_secs):
        """Sets the event_nfs_frontend_threshold_secs of this InlineResponse2008DataHangingIos.


        :param event_nfs_frontend_threshold_secs: The event_nfs_frontend_threshold_secs of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: float
        """

        self._event_nfs_frontend_threshold_secs = event_nfs_frontend_threshold_secs

    @property
    def last_emitted_nfs_frontend_event(self):
        """Gets the last_emitted_nfs_frontend_event of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The last_emitted_nfs_frontend_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: str
        """
        return self._last_emitted_nfs_frontend_event

    @last_emitted_nfs_frontend_event.setter
    def last_emitted_nfs_frontend_event(self, last_emitted_nfs_frontend_event):
        """Sets the last_emitted_nfs_frontend_event of this InlineResponse2008DataHangingIos.


        :param last_emitted_nfs_frontend_event: The last_emitted_nfs_frontend_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: str
        """

        self._last_emitted_nfs_frontend_event = last_emitted_nfs_frontend_event

    @property
    def last_emitted_nfs_frontend_no_longer_detected_event(self):
        """Gets the last_emitted_nfs_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501


        :return: The last_emitted_nfs_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :rtype: str
        """
        return self._last_emitted_nfs_frontend_no_longer_detected_event

    @last_emitted_nfs_frontend_no_longer_detected_event.setter
    def last_emitted_nfs_frontend_no_longer_detected_event(self, last_emitted_nfs_frontend_no_longer_detected_event):
        """Sets the last_emitted_nfs_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.


        :param last_emitted_nfs_frontend_no_longer_detected_event: The last_emitted_nfs_frontend_no_longer_detected_event of this InlineResponse2008DataHangingIos.  # noqa: E501
        :type: str
        """

        self._last_emitted_nfs_frontend_no_longer_detected_event = last_emitted_nfs_frontend_no_longer_detected_event

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
        if issubclass(InlineResponse2008DataHangingIos, dict):
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
        if not isinstance(other, InlineResponse2008DataHangingIos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

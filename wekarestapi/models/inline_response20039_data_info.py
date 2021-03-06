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

class InlineResponse20039DataInfo(object):
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
        'concurrency_at_end': 'float',
        'execution_time_u_secs': 'float',
        'key': 'str',
        'concurrency_at_start': 'float',
        'size': 'float',
        'last_curl_error': 'str',
        'last_latency_u_secs': 'float',
        'fs_id': 'str',
        'last_http_resp_code': 'str',
        'curl_error_str': 'str',
        'start_time': 'InlineResponse20039DataInfoStartTime',
        'extent_spec': 'InlineResponse20039DataInfoExtentSpec',
        'counts': 'InlineResponse20039DataInfoCounts'
    }

    attribute_map = {
        'concurrency_at_end': 'concurrencyAtEnd',
        'execution_time_u_secs': 'executionTimeUSecs',
        'key': 'key',
        'concurrency_at_start': 'concurrencyAtStart',
        'size': 'size',
        'last_curl_error': 'lastCurlError',
        'last_latency_u_secs': 'lastLatencyUSecs',
        'fs_id': 'fsId',
        'last_http_resp_code': 'lastHTTPRespCode',
        'curl_error_str': 'curlErrorStr',
        'start_time': 'startTime',
        'extent_spec': 'extentSpec',
        'counts': 'counts'
    }

    def __init__(self, concurrency_at_end=None, execution_time_u_secs=None, key=None, concurrency_at_start=None, size=None, last_curl_error=None, last_latency_u_secs=None, fs_id=None, last_http_resp_code=None, curl_error_str=None, start_time=None, extent_spec=None, counts=None):  # noqa: E501
        """InlineResponse20039DataInfo - a model defined in Swagger"""  # noqa: E501
        self._concurrency_at_end = None
        self._execution_time_u_secs = None
        self._key = None
        self._concurrency_at_start = None
        self._size = None
        self._last_curl_error = None
        self._last_latency_u_secs = None
        self._fs_id = None
        self._last_http_resp_code = None
        self._curl_error_str = None
        self._start_time = None
        self._extent_spec = None
        self._counts = None
        self.discriminator = None
        if concurrency_at_end is not None:
            self.concurrency_at_end = concurrency_at_end
        if execution_time_u_secs is not None:
            self.execution_time_u_secs = execution_time_u_secs
        if key is not None:
            self.key = key
        if concurrency_at_start is not None:
            self.concurrency_at_start = concurrency_at_start
        if size is not None:
            self.size = size
        if last_curl_error is not None:
            self.last_curl_error = last_curl_error
        if last_latency_u_secs is not None:
            self.last_latency_u_secs = last_latency_u_secs
        if fs_id is not None:
            self.fs_id = fs_id
        if last_http_resp_code is not None:
            self.last_http_resp_code = last_http_resp_code
        if curl_error_str is not None:
            self.curl_error_str = curl_error_str
        if start_time is not None:
            self.start_time = start_time
        if extent_spec is not None:
            self.extent_spec = extent_spec
        if counts is not None:
            self.counts = counts

    @property
    def concurrency_at_end(self):
        """Gets the concurrency_at_end of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The concurrency_at_end of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: float
        """
        return self._concurrency_at_end

    @concurrency_at_end.setter
    def concurrency_at_end(self, concurrency_at_end):
        """Sets the concurrency_at_end of this InlineResponse20039DataInfo.


        :param concurrency_at_end: The concurrency_at_end of this InlineResponse20039DataInfo.  # noqa: E501
        :type: float
        """

        self._concurrency_at_end = concurrency_at_end

    @property
    def execution_time_u_secs(self):
        """Gets the execution_time_u_secs of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The execution_time_u_secs of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: float
        """
        return self._execution_time_u_secs

    @execution_time_u_secs.setter
    def execution_time_u_secs(self, execution_time_u_secs):
        """Sets the execution_time_u_secs of this InlineResponse20039DataInfo.


        :param execution_time_u_secs: The execution_time_u_secs of this InlineResponse20039DataInfo.  # noqa: E501
        :type: float
        """

        self._execution_time_u_secs = execution_time_u_secs

    @property
    def key(self):
        """Gets the key of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The key of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InlineResponse20039DataInfo.


        :param key: The key of this InlineResponse20039DataInfo.  # noqa: E501
        :type: str
        """

        self._key = key

    @property
    def concurrency_at_start(self):
        """Gets the concurrency_at_start of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The concurrency_at_start of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: float
        """
        return self._concurrency_at_start

    @concurrency_at_start.setter
    def concurrency_at_start(self, concurrency_at_start):
        """Sets the concurrency_at_start of this InlineResponse20039DataInfo.


        :param concurrency_at_start: The concurrency_at_start of this InlineResponse20039DataInfo.  # noqa: E501
        :type: float
        """

        self._concurrency_at_start = concurrency_at_start

    @property
    def size(self):
        """Gets the size of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The size of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InlineResponse20039DataInfo.


        :param size: The size of this InlineResponse20039DataInfo.  # noqa: E501
        :type: float
        """

        self._size = size

    @property
    def last_curl_error(self):
        """Gets the last_curl_error of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The last_curl_error of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_curl_error

    @last_curl_error.setter
    def last_curl_error(self, last_curl_error):
        """Sets the last_curl_error of this InlineResponse20039DataInfo.


        :param last_curl_error: The last_curl_error of this InlineResponse20039DataInfo.  # noqa: E501
        :type: str
        """

        self._last_curl_error = last_curl_error

    @property
    def last_latency_u_secs(self):
        """Gets the last_latency_u_secs of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The last_latency_u_secs of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: float
        """
        return self._last_latency_u_secs

    @last_latency_u_secs.setter
    def last_latency_u_secs(self, last_latency_u_secs):
        """Sets the last_latency_u_secs of this InlineResponse20039DataInfo.


        :param last_latency_u_secs: The last_latency_u_secs of this InlineResponse20039DataInfo.  # noqa: E501
        :type: float
        """

        self._last_latency_u_secs = last_latency_u_secs

    @property
    def fs_id(self):
        """Gets the fs_id of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The fs_id of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: str
        """
        return self._fs_id

    @fs_id.setter
    def fs_id(self, fs_id):
        """Sets the fs_id of this InlineResponse20039DataInfo.


        :param fs_id: The fs_id of this InlineResponse20039DataInfo.  # noqa: E501
        :type: str
        """

        self._fs_id = fs_id

    @property
    def last_http_resp_code(self):
        """Gets the last_http_resp_code of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The last_http_resp_code of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_http_resp_code

    @last_http_resp_code.setter
    def last_http_resp_code(self, last_http_resp_code):
        """Sets the last_http_resp_code of this InlineResponse20039DataInfo.


        :param last_http_resp_code: The last_http_resp_code of this InlineResponse20039DataInfo.  # noqa: E501
        :type: str
        """

        self._last_http_resp_code = last_http_resp_code

    @property
    def curl_error_str(self):
        """Gets the curl_error_str of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The curl_error_str of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: str
        """
        return self._curl_error_str

    @curl_error_str.setter
    def curl_error_str(self, curl_error_str):
        """Sets the curl_error_str of this InlineResponse20039DataInfo.


        :param curl_error_str: The curl_error_str of this InlineResponse20039DataInfo.  # noqa: E501
        :type: str
        """

        self._curl_error_str = curl_error_str

    @property
    def start_time(self):
        """Gets the start_time of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The start_time of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: InlineResponse20039DataInfoStartTime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this InlineResponse20039DataInfo.


        :param start_time: The start_time of this InlineResponse20039DataInfo.  # noqa: E501
        :type: InlineResponse20039DataInfoStartTime
        """

        self._start_time = start_time

    @property
    def extent_spec(self):
        """Gets the extent_spec of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The extent_spec of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: InlineResponse20039DataInfoExtentSpec
        """
        return self._extent_spec

    @extent_spec.setter
    def extent_spec(self, extent_spec):
        """Sets the extent_spec of this InlineResponse20039DataInfo.


        :param extent_spec: The extent_spec of this InlineResponse20039DataInfo.  # noqa: E501
        :type: InlineResponse20039DataInfoExtentSpec
        """

        self._extent_spec = extent_spec

    @property
    def counts(self):
        """Gets the counts of this InlineResponse20039DataInfo.  # noqa: E501


        :return: The counts of this InlineResponse20039DataInfo.  # noqa: E501
        :rtype: InlineResponse20039DataInfoCounts
        """
        return self._counts

    @counts.setter
    def counts(self, counts):
        """Sets the counts of this InlineResponse20039DataInfo.


        :param counts: The counts of this InlineResponse20039DataInfo.  # noqa: E501
        :type: InlineResponse20039DataInfoCounts
        """

        self._counts = counts

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
        if issubclass(InlineResponse20039DataInfo, dict):
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
        if not isinstance(other, InlineResponse20039DataInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

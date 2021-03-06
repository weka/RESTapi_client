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

class WekaHomeEnableBody(object):
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
        'cloud_url': 'str',
        'enable_cloud_stats': 'bool'
    }

    attribute_map = {
        'cloud_url': 'cloud_url',
        'enable_cloud_stats': 'enable_cloud_stats'
    }

    def __init__(self, cloud_url=None, enable_cloud_stats=None):  # noqa: E501
        """WekaHomeEnableBody - a model defined in Swagger"""  # noqa: E501
        self._cloud_url = None
        self._enable_cloud_stats = None
        self.discriminator = None
        if cloud_url is not None:
            self.cloud_url = cloud_url
        if enable_cloud_stats is not None:
            self.enable_cloud_stats = enable_cloud_stats

    @property
    def cloud_url(self):
        """Gets the cloud_url of this WekaHomeEnableBody.  # noqa: E501

        The base url of the cloud service  # noqa: E501

        :return: The cloud_url of this WekaHomeEnableBody.  # noqa: E501
        :rtype: str
        """
        return self._cloud_url

    @cloud_url.setter
    def cloud_url(self, cloud_url):
        """Sets the cloud_url of this WekaHomeEnableBody.

        The base url of the cloud service  # noqa: E501

        :param cloud_url: The cloud_url of this WekaHomeEnableBody.  # noqa: E501
        :type: str
        """

        self._cloud_url = cloud_url

    @property
    def enable_cloud_stats(self):
        """Gets the enable_cloud_stats of this WekaHomeEnableBody.  # noqa: E501

        Enable or disable uploading stats to the cloud  # noqa: E501

        :return: The enable_cloud_stats of this WekaHomeEnableBody.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cloud_stats

    @enable_cloud_stats.setter
    def enable_cloud_stats(self, enable_cloud_stats):
        """Sets the enable_cloud_stats of this WekaHomeEnableBody.

        Enable or disable uploading stats to the cloud  # noqa: E501

        :param enable_cloud_stats: The enable_cloud_stats of this WekaHomeEnableBody.  # noqa: E501
        :type: bool
        """

        self._enable_cloud_stats = enable_cloud_stats

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
        if issubclass(WekaHomeEnableBody, dict):
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
        if not isinstance(other, WekaHomeEnableBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

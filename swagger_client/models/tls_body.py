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

class TlsBody(object):
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
        'tls_cert_pem': 'str',
        'tls_key_pem': 'str'
    }

    attribute_map = {
        'tls_cert_pem': 'tls_cert_pem',
        'tls_key_pem': 'tls_key_pem'
    }

    def __init__(self, tls_cert_pem=None, tls_key_pem=None):  # noqa: E501
        """TlsBody - a model defined in Swagger"""  # noqa: E501
        self._tls_cert_pem = None
        self._tls_key_pem = None
        self.discriminator = None
        self.tls_cert_pem = tls_cert_pem
        self.tls_key_pem = tls_key_pem

    @property
    def tls_cert_pem(self):
        """Gets the tls_cert_pem of this TlsBody.  # noqa: E501


        :return: The tls_cert_pem of this TlsBody.  # noqa: E501
        :rtype: str
        """
        return self._tls_cert_pem

    @tls_cert_pem.setter
    def tls_cert_pem(self, tls_cert_pem):
        """Sets the tls_cert_pem of this TlsBody.


        :param tls_cert_pem: The tls_cert_pem of this TlsBody.  # noqa: E501
        :type: str
        """
        if tls_cert_pem is None:
            raise ValueError("Invalid value for `tls_cert_pem`, must not be `None`")  # noqa: E501

        self._tls_cert_pem = tls_cert_pem

    @property
    def tls_key_pem(self):
        """Gets the tls_key_pem of this TlsBody.  # noqa: E501


        :return: The tls_key_pem of this TlsBody.  # noqa: E501
        :rtype: str
        """
        return self._tls_key_pem

    @tls_key_pem.setter
    def tls_key_pem(self, tls_key_pem):
        """Sets the tls_key_pem of this TlsBody.


        :param tls_key_pem: The tls_key_pem of this TlsBody.  # noqa: E501
        :type: str
        """
        if tls_key_pem is None:
            raise ValueError("Invalid value for `tls_key_pem`, must not be `None`")  # noqa: E501

        self._tls_key_pem = tls_key_pem

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
        if issubclass(TlsBody, dict):
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
        if not isinstance(other, TlsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

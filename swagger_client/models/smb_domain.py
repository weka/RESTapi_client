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

class SmbDomain(object):
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
        'id': 'str',
        'uid': 'str',
        'idmap_backend': 'str',
        'mapping_from_id': 'float',
        'mapping_to_id': 'float',
        'domain_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'uid': 'uid',
        'idmap_backend': 'idmapBackend',
        'mapping_from_id': 'mappingFromId',
        'mapping_to_id': 'mappingToId',
        'domain_name': 'domainName'
    }

    def __init__(self, id=None, uid=None, idmap_backend=None, mapping_from_id=None, mapping_to_id=None, domain_name=None):  # noqa: E501
        """SmbDomain - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._uid = None
        self._idmap_backend = None
        self._mapping_from_id = None
        self._mapping_to_id = None
        self._domain_name = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if uid is not None:
            self.uid = uid
        if idmap_backend is not None:
            self.idmap_backend = idmap_backend
        if mapping_from_id is not None:
            self.mapping_from_id = mapping_from_id
        if mapping_to_id is not None:
            self.mapping_to_id = mapping_to_id
        if domain_name is not None:
            self.domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this SmbDomain.  # noqa: E501


        :return: The id of this SmbDomain.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SmbDomain.


        :param id: The id of this SmbDomain.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uid(self):
        """Gets the uid of this SmbDomain.  # noqa: E501


        :return: The uid of this SmbDomain.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this SmbDomain.


        :param uid: The uid of this SmbDomain.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def idmap_backend(self):
        """Gets the idmap_backend of this SmbDomain.  # noqa: E501


        :return: The idmap_backend of this SmbDomain.  # noqa: E501
        :rtype: str
        """
        return self._idmap_backend

    @idmap_backend.setter
    def idmap_backend(self, idmap_backend):
        """Sets the idmap_backend of this SmbDomain.


        :param idmap_backend: The idmap_backend of this SmbDomain.  # noqa: E501
        :type: str
        """

        self._idmap_backend = idmap_backend

    @property
    def mapping_from_id(self):
        """Gets the mapping_from_id of this SmbDomain.  # noqa: E501


        :return: The mapping_from_id of this SmbDomain.  # noqa: E501
        :rtype: float
        """
        return self._mapping_from_id

    @mapping_from_id.setter
    def mapping_from_id(self, mapping_from_id):
        """Sets the mapping_from_id of this SmbDomain.


        :param mapping_from_id: The mapping_from_id of this SmbDomain.  # noqa: E501
        :type: float
        """

        self._mapping_from_id = mapping_from_id

    @property
    def mapping_to_id(self):
        """Gets the mapping_to_id of this SmbDomain.  # noqa: E501


        :return: The mapping_to_id of this SmbDomain.  # noqa: E501
        :rtype: float
        """
        return self._mapping_to_id

    @mapping_to_id.setter
    def mapping_to_id(self, mapping_to_id):
        """Sets the mapping_to_id of this SmbDomain.


        :param mapping_to_id: The mapping_to_id of this SmbDomain.  # noqa: E501
        :type: float
        """

        self._mapping_to_id = mapping_to_id

    @property
    def domain_name(self):
        """Gets the domain_name of this SmbDomain.  # noqa: E501


        :return: The domain_name of this SmbDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this SmbDomain.


        :param domain_name: The domain_name of this SmbDomain.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

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
        if issubclass(SmbDomain, dict):
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
        if not isinstance(other, SmbDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

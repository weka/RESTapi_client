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

class SnapshotsBody(object):
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
        'fs_uid': 'str',
        'name': 'str',
        'access_point': 'str',
        'source_snap_uid': 'str',
        'is_writable': 'bool'
    }

    attribute_map = {
        'fs_uid': 'fs_uid',
        'name': 'name',
        'access_point': 'access_point',
        'source_snap_uid': 'source_snap_uid',
        'is_writable': 'is_writable'
    }

    def __init__(self, fs_uid=None, name=None, access_point=None, source_snap_uid=None, is_writable=None):  # noqa: E501
        """SnapshotsBody - a model defined in Swagger"""  # noqa: E501
        self._fs_uid = None
        self._name = None
        self._access_point = None
        self._source_snap_uid = None
        self._is_writable = None
        self.discriminator = None
        self.fs_uid = fs_uid
        self.name = name
        self.access_point = access_point
        if source_snap_uid is not None:
            self.source_snap_uid = source_snap_uid
        if is_writable is not None:
            self.is_writable = is_writable

    @property
    def fs_uid(self):
        """Gets the fs_uid of this SnapshotsBody.  # noqa: E501

        File system uid for creating the snapshot  # noqa: E501

        :return: The fs_uid of this SnapshotsBody.  # noqa: E501
        :rtype: str
        """
        return self._fs_uid

    @fs_uid.setter
    def fs_uid(self, fs_uid):
        """Sets the fs_uid of this SnapshotsBody.

        File system uid for creating the snapshot  # noqa: E501

        :param fs_uid: The fs_uid of this SnapshotsBody.  # noqa: E501
        :type: str
        """
        if fs_uid is None:
            raise ValueError("Invalid value for `fs_uid`, must not be `None`")  # noqa: E501

        self._fs_uid = fs_uid

    @property
    def name(self):
        """Gets the name of this SnapshotsBody.  # noqa: E501

        Target Snapshot name  # noqa: E501

        :return: The name of this SnapshotsBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SnapshotsBody.

        Target Snapshot name  # noqa: E501

        :param name: The name of this SnapshotsBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def access_point(self):
        """Gets the access_point of this SnapshotsBody.  # noqa: E501

        Access point  # noqa: E501

        :return: The access_point of this SnapshotsBody.  # noqa: E501
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this SnapshotsBody.

        Access point  # noqa: E501

        :param access_point: The access_point of this SnapshotsBody.  # noqa: E501
        :type: str
        """
        if access_point is None:
            raise ValueError("Invalid value for `access_point`, must not be `None`")  # noqa: E501

        self._access_point = access_point

    @property
    def source_snap_uid(self):
        """Gets the source_snap_uid of this SnapshotsBody.  # noqa: E501

        Source snapshot uid for copy a snapshot  # noqa: E501

        :return: The source_snap_uid of this SnapshotsBody.  # noqa: E501
        :rtype: str
        """
        return self._source_snap_uid

    @source_snap_uid.setter
    def source_snap_uid(self, source_snap_uid):
        """Sets the source_snap_uid of this SnapshotsBody.

        Source snapshot uid for copy a snapshot  # noqa: E501

        :param source_snap_uid: The source_snap_uid of this SnapshotsBody.  # noqa: E501
        :type: str
        """

        self._source_snap_uid = source_snap_uid

    @property
    def is_writable(self):
        """Gets the is_writable of this SnapshotsBody.  # noqa: E501

        Writable  # noqa: E501

        :return: The is_writable of this SnapshotsBody.  # noqa: E501
        :rtype: bool
        """
        return self._is_writable

    @is_writable.setter
    def is_writable(self, is_writable):
        """Sets the is_writable of this SnapshotsBody.

        Writable  # noqa: E501

        :param is_writable: The is_writable of this SnapshotsBody.  # noqa: E501
        :type: bool
        """

        self._is_writable = is_writable

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
        if issubclass(SnapshotsBody, dict):
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
        if not isinstance(other, SnapshotsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

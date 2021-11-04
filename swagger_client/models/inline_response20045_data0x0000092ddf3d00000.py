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

class InlineResponse20045Data0x0000092ddf3d00000(object):
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
        'inode_id': 'float',
        'total_bytes': 'float',
        'owner': 'str',
        'data_blocks': 'float',
        'grace_seconds': 'float',
        'hard_limit_bytes': 'float',
        'snap_view_id': 'float',
        'metadata_blocks': 'float',
        'soft_limit_bytes': 'float',
        'status': 'str'
    }

    attribute_map = {
        'inode_id': 'inodeId',
        'total_bytes': 'totalBytes',
        'owner': 'owner',
        'data_blocks': 'dataBlocks',
        'grace_seconds': 'graceSeconds',
        'hard_limit_bytes': 'hardLimitBytes',
        'snap_view_id': 'snapViewId',
        'metadata_blocks': 'metadataBlocks',
        'soft_limit_bytes': 'softLimitBytes',
        'status': 'status'
    }

    def __init__(self, inode_id=None, total_bytes=None, owner=None, data_blocks=None, grace_seconds=None, hard_limit_bytes=None, snap_view_id=None, metadata_blocks=None, soft_limit_bytes=None, status=None):  # noqa: E501
        """InlineResponse20045Data0x0000092ddf3d00000 - a model defined in Swagger"""  # noqa: E501
        self._inode_id = None
        self._total_bytes = None
        self._owner = None
        self._data_blocks = None
        self._grace_seconds = None
        self._hard_limit_bytes = None
        self._snap_view_id = None
        self._metadata_blocks = None
        self._soft_limit_bytes = None
        self._status = None
        self.discriminator = None
        if inode_id is not None:
            self.inode_id = inode_id
        if total_bytes is not None:
            self.total_bytes = total_bytes
        if owner is not None:
            self.owner = owner
        if data_blocks is not None:
            self.data_blocks = data_blocks
        if grace_seconds is not None:
            self.grace_seconds = grace_seconds
        if hard_limit_bytes is not None:
            self.hard_limit_bytes = hard_limit_bytes
        if snap_view_id is not None:
            self.snap_view_id = snap_view_id
        if metadata_blocks is not None:
            self.metadata_blocks = metadata_blocks
        if soft_limit_bytes is not None:
            self.soft_limit_bytes = soft_limit_bytes
        if status is not None:
            self.status = status

    @property
    def inode_id(self):
        """Gets the inode_id of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The inode_id of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._inode_id

    @inode_id.setter
    def inode_id(self, inode_id):
        """Sets the inode_id of this InlineResponse20045Data0x0000092ddf3d00000.


        :param inode_id: The inode_id of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._inode_id = inode_id

    @property
    def total_bytes(self):
        """Gets the total_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The total_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._total_bytes

    @total_bytes.setter
    def total_bytes(self, total_bytes):
        """Sets the total_bytes of this InlineResponse20045Data0x0000092ddf3d00000.


        :param total_bytes: The total_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._total_bytes = total_bytes

    @property
    def owner(self):
        """Gets the owner of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The owner of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this InlineResponse20045Data0x0000092ddf3d00000.


        :param owner: The owner of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: str
        """

        self._owner = owner

    @property
    def data_blocks(self):
        """Gets the data_blocks of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The data_blocks of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._data_blocks

    @data_blocks.setter
    def data_blocks(self, data_blocks):
        """Sets the data_blocks of this InlineResponse20045Data0x0000092ddf3d00000.


        :param data_blocks: The data_blocks of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._data_blocks = data_blocks

    @property
    def grace_seconds(self):
        """Gets the grace_seconds of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The grace_seconds of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._grace_seconds

    @grace_seconds.setter
    def grace_seconds(self, grace_seconds):
        """Sets the grace_seconds of this InlineResponse20045Data0x0000092ddf3d00000.


        :param grace_seconds: The grace_seconds of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._grace_seconds = grace_seconds

    @property
    def hard_limit_bytes(self):
        """Gets the hard_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The hard_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._hard_limit_bytes

    @hard_limit_bytes.setter
    def hard_limit_bytes(self, hard_limit_bytes):
        """Sets the hard_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.


        :param hard_limit_bytes: The hard_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._hard_limit_bytes = hard_limit_bytes

    @property
    def snap_view_id(self):
        """Gets the snap_view_id of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The snap_view_id of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._snap_view_id

    @snap_view_id.setter
    def snap_view_id(self, snap_view_id):
        """Sets the snap_view_id of this InlineResponse20045Data0x0000092ddf3d00000.


        :param snap_view_id: The snap_view_id of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._snap_view_id = snap_view_id

    @property
    def metadata_blocks(self):
        """Gets the metadata_blocks of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The metadata_blocks of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._metadata_blocks

    @metadata_blocks.setter
    def metadata_blocks(self, metadata_blocks):
        """Sets the metadata_blocks of this InlineResponse20045Data0x0000092ddf3d00000.


        :param metadata_blocks: The metadata_blocks of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._metadata_blocks = metadata_blocks

    @property
    def soft_limit_bytes(self):
        """Gets the soft_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The soft_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: float
        """
        return self._soft_limit_bytes

    @soft_limit_bytes.setter
    def soft_limit_bytes(self, soft_limit_bytes):
        """Sets the soft_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.


        :param soft_limit_bytes: The soft_limit_bytes of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: float
        """

        self._soft_limit_bytes = soft_limit_bytes

    @property
    def status(self):
        """Gets the status of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501


        :return: The status of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20045Data0x0000092ddf3d00000.


        :param status: The status of this InlineResponse20045Data0x0000092ddf3d00000.  # noqa: E501
        :type: str
        """

        self._status = status

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
        if issubclass(InlineResponse20045Data0x0000092ddf3d00000, dict):
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
        if not isinstance(other, InlineResponse20045Data0x0000092ddf3d00000):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

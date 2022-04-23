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

class Snapshot(object):
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
        'access_point': 'str',
        'creation_time': 'str',
        'filesystem': 'str',
        'filesystem_id': 'str',
        'filesystem_uid': 'str',
        'id': 'str',
        'is_removing': 'bool',
        'is_writable': 'bool',
        'locator': 'str',
        'multi_obs': 'bool',
        'name': 'str',
        'progress': 'float',
        'stow_status': 'str',
        'type': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'access_point': 'accessPoint',
        'creation_time': 'creationTime',
        'filesystem': 'filesystem',
        'filesystem_id': 'filesystemId',
        'filesystem_uid': 'filesystemUid',
        'id': 'id',
        'is_removing': 'isRemoving',
        'is_writable': 'isWritable',
        'locator': 'locator',
        'multi_obs': 'multiObs',
        'name': 'name',
        'progress': 'progress',
        'stow_status': 'stowStatus',
        'type': 'type',
        'uid': 'uid'
    }

    def __init__(self, access_point=None, creation_time=None, filesystem=None, filesystem_id=None, filesystem_uid=None, id=None, is_removing=None, is_writable=None, locator=None, multi_obs=None, name=None, progress=None, stow_status=None, type=None, uid=None):  # noqa: E501
        """Snapshot - a model defined in Swagger"""  # noqa: E501
        self._access_point = None
        self._creation_time = None
        self._filesystem = None
        self._filesystem_id = None
        self._filesystem_uid = None
        self._id = None
        self._is_removing = None
        self._is_writable = None
        self._locator = None
        self._multi_obs = None
        self._name = None
        self._progress = None
        self._stow_status = None
        self._type = None
        self._uid = None
        self.discriminator = None
        if access_point is not None:
            self.access_point = access_point
        if creation_time is not None:
            self.creation_time = creation_time
        if filesystem is not None:
            self.filesystem = filesystem
        if filesystem_id is not None:
            self.filesystem_id = filesystem_id
        if filesystem_uid is not None:
            self.filesystem_uid = filesystem_uid
        if id is not None:
            self.id = id
        if is_removing is not None:
            self.is_removing = is_removing
        if is_writable is not None:
            self.is_writable = is_writable
        if locator is not None:
            self.locator = locator
        if multi_obs is not None:
            self.multi_obs = multi_obs
        if name is not None:
            self.name = name
        if progress is not None:
            self.progress = progress
        if stow_status is not None:
            self.stow_status = stow_status
        if type is not None:
            self.type = type
        if uid is not None:
            self.uid = uid

    @property
    def access_point(self):
        """Gets the access_point of this Snapshot.  # noqa: E501


        :return: The access_point of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._access_point

    @access_point.setter
    def access_point(self, access_point):
        """Sets the access_point of this Snapshot.


        :param access_point: The access_point of this Snapshot.  # noqa: E501
        :type: str
        """

        self._access_point = access_point

    @property
    def creation_time(self):
        """Gets the creation_time of this Snapshot.  # noqa: E501


        :return: The creation_time of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this Snapshot.


        :param creation_time: The creation_time of this Snapshot.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def filesystem(self):
        """Gets the filesystem of this Snapshot.  # noqa: E501


        :return: The filesystem of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._filesystem

    @filesystem.setter
    def filesystem(self, filesystem):
        """Sets the filesystem of this Snapshot.


        :param filesystem: The filesystem of this Snapshot.  # noqa: E501
        :type: str
        """

        self._filesystem = filesystem

    @property
    def filesystem_id(self):
        """Gets the filesystem_id of this Snapshot.  # noqa: E501


        :return: The filesystem_id of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._filesystem_id

    @filesystem_id.setter
    def filesystem_id(self, filesystem_id):
        """Sets the filesystem_id of this Snapshot.


        :param filesystem_id: The filesystem_id of this Snapshot.  # noqa: E501
        :type: str
        """

        self._filesystem_id = filesystem_id

    @property
    def filesystem_uid(self):
        """Gets the filesystem_uid of this Snapshot.  # noqa: E501


        :return: The filesystem_uid of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._filesystem_uid

    @filesystem_uid.setter
    def filesystem_uid(self, filesystem_uid):
        """Sets the filesystem_uid of this Snapshot.


        :param filesystem_uid: The filesystem_uid of this Snapshot.  # noqa: E501
        :type: str
        """

        self._filesystem_uid = filesystem_uid

    @property
    def id(self):
        """Gets the id of this Snapshot.  # noqa: E501


        :return: The id of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Snapshot.


        :param id: The id of this Snapshot.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_removing(self):
        """Gets the is_removing of this Snapshot.  # noqa: E501


        :return: The is_removing of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_removing

    @is_removing.setter
    def is_removing(self, is_removing):
        """Sets the is_removing of this Snapshot.


        :param is_removing: The is_removing of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._is_removing = is_removing

    @property
    def is_writable(self):
        """Gets the is_writable of this Snapshot.  # noqa: E501


        :return: The is_writable of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._is_writable

    @is_writable.setter
    def is_writable(self, is_writable):
        """Sets the is_writable of this Snapshot.


        :param is_writable: The is_writable of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._is_writable = is_writable

    @property
    def locator(self):
        """Gets the locator of this Snapshot.  # noqa: E501


        :return: The locator of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._locator

    @locator.setter
    def locator(self, locator):
        """Sets the locator of this Snapshot.


        :param locator: The locator of this Snapshot.  # noqa: E501
        :type: str
        """

        self._locator = locator

    @property
    def multi_obs(self):
        """Gets the multi_obs of this Snapshot.  # noqa: E501


        :return: The multi_obs of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._multi_obs

    @multi_obs.setter
    def multi_obs(self, multi_obs):
        """Sets the multi_obs of this Snapshot.


        :param multi_obs: The multi_obs of this Snapshot.  # noqa: E501
        :type: bool
        """

        self._multi_obs = multi_obs

    @property
    def name(self):
        """Gets the name of this Snapshot.  # noqa: E501


        :return: The name of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Snapshot.


        :param name: The name of this Snapshot.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def progress(self):
        """Gets the progress of this Snapshot.  # noqa: E501


        :return: The progress of this Snapshot.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Snapshot.


        :param progress: The progress of this Snapshot.  # noqa: E501
        :type: float
        """

        self._progress = progress

    @property
    def stow_status(self):
        """Gets the stow_status of this Snapshot.  # noqa: E501


        :return: The stow_status of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._stow_status

    @stow_status.setter
    def stow_status(self, stow_status):
        """Sets the stow_status of this Snapshot.


        :param stow_status: The stow_status of this Snapshot.  # noqa: E501
        :type: str
        """

        self._stow_status = stow_status

    @property
    def type(self):
        """Gets the type of this Snapshot.  # noqa: E501


        :return: The type of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Snapshot.


        :param type: The type of this Snapshot.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def uid(self):
        """Gets the uid of this Snapshot.  # noqa: E501


        :return: The uid of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Snapshot.


        :param uid: The uid of this Snapshot.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(Snapshot, dict):
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
        if not isinstance(other, Snapshot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

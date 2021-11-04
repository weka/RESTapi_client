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

class ObjectStore(object):
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
        'secret_key': 'str',
        'bandwidth': 'ObjectStoreBandwidth',
        'name': 'str',
        'obs_site': 'str',
        'uid': 'str',
        'hostname': 'str',
        'auth_method': 'str',
        'max_concurrent_removals': 'float',
        'max_extents_in_data_blob': 'float',
        'max_blocks_in_data_blob': 'float',
        'upload_bandwidth': 'ObjectStoreUploadBandwidth',
        'access_key_id': 'str',
        'port': 'float',
        'max_concurrent_downloads': 'float',
        'region': 'str',
        'protocol': 'str',
        'upload_memory_blocks_limit': 'float',
        'enable_upload_tags': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'secret_key': 'secret_key',
        'bandwidth': 'bandwidth',
        'name': 'name',
        'obs_site': 'obs_site',
        'uid': 'uid',
        'hostname': 'hostname',
        'auth_method': 'auth_method',
        'max_concurrent_removals': 'max_concurrent_removals',
        'max_extents_in_data_blob': 'max_extents_in_data_blob',
        'max_blocks_in_data_blob': 'max_blocks_in_data_blob',
        'upload_bandwidth': 'uploadBandwidth',
        'access_key_id': 'access_key_id',
        'port': 'port',
        'max_concurrent_downloads': 'max_concurrent_downloads',
        'region': 'region',
        'protocol': 'protocol',
        'upload_memory_blocks_limit': 'upload_memory_blocks_limit',
        'enable_upload_tags': 'enable_upload_tags'
    }

    def __init__(self, id=None, secret_key=None, bandwidth=None, name=None, obs_site=None, uid=None, hostname=None, auth_method=None, max_concurrent_removals=None, max_extents_in_data_blob=None, max_blocks_in_data_blob=None, upload_bandwidth=None, access_key_id=None, port=None, max_concurrent_downloads=None, region=None, protocol=None, upload_memory_blocks_limit=None, enable_upload_tags=None):  # noqa: E501
        """ObjectStore - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._secret_key = None
        self._bandwidth = None
        self._name = None
        self._obs_site = None
        self._uid = None
        self._hostname = None
        self._auth_method = None
        self._max_concurrent_removals = None
        self._max_extents_in_data_blob = None
        self._max_blocks_in_data_blob = None
        self._upload_bandwidth = None
        self._access_key_id = None
        self._port = None
        self._max_concurrent_downloads = None
        self._region = None
        self._protocol = None
        self._upload_memory_blocks_limit = None
        self._enable_upload_tags = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if secret_key is not None:
            self.secret_key = secret_key
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if name is not None:
            self.name = name
        if obs_site is not None:
            self.obs_site = obs_site
        if uid is not None:
            self.uid = uid
        if hostname is not None:
            self.hostname = hostname
        if auth_method is not None:
            self.auth_method = auth_method
        if max_concurrent_removals is not None:
            self.max_concurrent_removals = max_concurrent_removals
        if max_extents_in_data_blob is not None:
            self.max_extents_in_data_blob = max_extents_in_data_blob
        if max_blocks_in_data_blob is not None:
            self.max_blocks_in_data_blob = max_blocks_in_data_blob
        if upload_bandwidth is not None:
            self.upload_bandwidth = upload_bandwidth
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if port is not None:
            self.port = port
        if max_concurrent_downloads is not None:
            self.max_concurrent_downloads = max_concurrent_downloads
        if region is not None:
            self.region = region
        if protocol is not None:
            self.protocol = protocol
        if upload_memory_blocks_limit is not None:
            self.upload_memory_blocks_limit = upload_memory_blocks_limit
        if enable_upload_tags is not None:
            self.enable_upload_tags = enable_upload_tags

    @property
    def id(self):
        """Gets the id of this ObjectStore.  # noqa: E501


        :return: The id of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ObjectStore.


        :param id: The id of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def secret_key(self):
        """Gets the secret_key of this ObjectStore.  # noqa: E501


        :return: The secret_key of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ObjectStore.


        :param secret_key: The secret_key of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ObjectStore.  # noqa: E501


        :return: The bandwidth of this ObjectStore.  # noqa: E501
        :rtype: ObjectStoreBandwidth
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ObjectStore.


        :param bandwidth: The bandwidth of this ObjectStore.  # noqa: E501
        :type: ObjectStoreBandwidth
        """

        self._bandwidth = bandwidth

    @property
    def name(self):
        """Gets the name of this ObjectStore.  # noqa: E501


        :return: The name of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ObjectStore.


        :param name: The name of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def obs_site(self):
        """Gets the obs_site of this ObjectStore.  # noqa: E501


        :return: The obs_site of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._obs_site

    @obs_site.setter
    def obs_site(self, obs_site):
        """Sets the obs_site of this ObjectStore.


        :param obs_site: The obs_site of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._obs_site = obs_site

    @property
    def uid(self):
        """Gets the uid of this ObjectStore.  # noqa: E501


        :return: The uid of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ObjectStore.


        :param uid: The uid of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def hostname(self):
        """Gets the hostname of this ObjectStore.  # noqa: E501


        :return: The hostname of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ObjectStore.


        :param hostname: The hostname of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def auth_method(self):
        """Gets the auth_method of this ObjectStore.  # noqa: E501


        :return: The auth_method of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this ObjectStore.


        :param auth_method: The auth_method of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._auth_method = auth_method

    @property
    def max_concurrent_removals(self):
        """Gets the max_concurrent_removals of this ObjectStore.  # noqa: E501


        :return: The max_concurrent_removals of this ObjectStore.  # noqa: E501
        :rtype: float
        """
        return self._max_concurrent_removals

    @max_concurrent_removals.setter
    def max_concurrent_removals(self, max_concurrent_removals):
        """Sets the max_concurrent_removals of this ObjectStore.


        :param max_concurrent_removals: The max_concurrent_removals of this ObjectStore.  # noqa: E501
        :type: float
        """

        self._max_concurrent_removals = max_concurrent_removals

    @property
    def max_extents_in_data_blob(self):
        """Gets the max_extents_in_data_blob of this ObjectStore.  # noqa: E501


        :return: The max_extents_in_data_blob of this ObjectStore.  # noqa: E501
        :rtype: float
        """
        return self._max_extents_in_data_blob

    @max_extents_in_data_blob.setter
    def max_extents_in_data_blob(self, max_extents_in_data_blob):
        """Sets the max_extents_in_data_blob of this ObjectStore.


        :param max_extents_in_data_blob: The max_extents_in_data_blob of this ObjectStore.  # noqa: E501
        :type: float
        """

        self._max_extents_in_data_blob = max_extents_in_data_blob

    @property
    def max_blocks_in_data_blob(self):
        """Gets the max_blocks_in_data_blob of this ObjectStore.  # noqa: E501


        :return: The max_blocks_in_data_blob of this ObjectStore.  # noqa: E501
        :rtype: float
        """
        return self._max_blocks_in_data_blob

    @max_blocks_in_data_blob.setter
    def max_blocks_in_data_blob(self, max_blocks_in_data_blob):
        """Sets the max_blocks_in_data_blob of this ObjectStore.


        :param max_blocks_in_data_blob: The max_blocks_in_data_blob of this ObjectStore.  # noqa: E501
        :type: float
        """

        self._max_blocks_in_data_blob = max_blocks_in_data_blob

    @property
    def upload_bandwidth(self):
        """Gets the upload_bandwidth of this ObjectStore.  # noqa: E501


        :return: The upload_bandwidth of this ObjectStore.  # noqa: E501
        :rtype: ObjectStoreUploadBandwidth
        """
        return self._upload_bandwidth

    @upload_bandwidth.setter
    def upload_bandwidth(self, upload_bandwidth):
        """Sets the upload_bandwidth of this ObjectStore.


        :param upload_bandwidth: The upload_bandwidth of this ObjectStore.  # noqa: E501
        :type: ObjectStoreUploadBandwidth
        """

        self._upload_bandwidth = upload_bandwidth

    @property
    def access_key_id(self):
        """Gets the access_key_id of this ObjectStore.  # noqa: E501


        :return: The access_key_id of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this ObjectStore.


        :param access_key_id: The access_key_id of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def port(self):
        """Gets the port of this ObjectStore.  # noqa: E501


        :return: The port of this ObjectStore.  # noqa: E501
        :rtype: float
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ObjectStore.


        :param port: The port of this ObjectStore.  # noqa: E501
        :type: float
        """

        self._port = port

    @property
    def max_concurrent_downloads(self):
        """Gets the max_concurrent_downloads of this ObjectStore.  # noqa: E501


        :return: The max_concurrent_downloads of this ObjectStore.  # noqa: E501
        :rtype: float
        """
        return self._max_concurrent_downloads

    @max_concurrent_downloads.setter
    def max_concurrent_downloads(self, max_concurrent_downloads):
        """Sets the max_concurrent_downloads of this ObjectStore.


        :param max_concurrent_downloads: The max_concurrent_downloads of this ObjectStore.  # noqa: E501
        :type: float
        """

        self._max_concurrent_downloads = max_concurrent_downloads

    @property
    def region(self):
        """Gets the region of this ObjectStore.  # noqa: E501


        :return: The region of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ObjectStore.


        :param region: The region of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def protocol(self):
        """Gets the protocol of this ObjectStore.  # noqa: E501


        :return: The protocol of this ObjectStore.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ObjectStore.


        :param protocol: The protocol of this ObjectStore.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def upload_memory_blocks_limit(self):
        """Gets the upload_memory_blocks_limit of this ObjectStore.  # noqa: E501


        :return: The upload_memory_blocks_limit of this ObjectStore.  # noqa: E501
        :rtype: float
        """
        return self._upload_memory_blocks_limit

    @upload_memory_blocks_limit.setter
    def upload_memory_blocks_limit(self, upload_memory_blocks_limit):
        """Sets the upload_memory_blocks_limit of this ObjectStore.


        :param upload_memory_blocks_limit: The upload_memory_blocks_limit of this ObjectStore.  # noqa: E501
        :type: float
        """

        self._upload_memory_blocks_limit = upload_memory_blocks_limit

    @property
    def enable_upload_tags(self):
        """Gets the enable_upload_tags of this ObjectStore.  # noqa: E501


        :return: The enable_upload_tags of this ObjectStore.  # noqa: E501
        :rtype: bool
        """
        return self._enable_upload_tags

    @enable_upload_tags.setter
    def enable_upload_tags(self, enable_upload_tags):
        """Sets the enable_upload_tags of this ObjectStore.


        :param enable_upload_tags: The enable_upload_tags of this ObjectStore.  # noqa: E501
        :type: bool
        """

        self._enable_upload_tags = enable_upload_tags

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
        if issubclass(ObjectStore, dict):
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
        if not isinstance(other, ObjectStore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

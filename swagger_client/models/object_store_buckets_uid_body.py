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

class ObjectStoreBucketsUidBody(object):
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
        'new_name': 'str',
        'new_obs_name': 'str',
        'protocol': 'str',
        'hostname': 'str',
        'port': 'float',
        'bucket': 'str',
        'auth_method': 'str',
        'region': 'str',
        'access_key_id': 'str',
        'secret_key': 'str',
        'dry_run': 'bool',
        'skip_verification': 'bool',
        'bandwidth': 'float',
        'verbose_errors': 'bool',
        'errors_timeout': 'str',
        'prefetch_mib': 'float',
        'max_concurrent_downloads': 'float',
        'max_concurrent_uploads': 'float',
        'max_concurrent_removals': 'float',
        'max_extents_in_data_blob': 'float',
        'max_blocks_in_data_blob': 'float'
    }

    attribute_map = {
        'new_name': 'new_name',
        'new_obs_name': 'new_obs_name',
        'protocol': 'protocol',
        'hostname': 'hostname',
        'port': 'port',
        'bucket': 'bucket',
        'auth_method': 'auth_method',
        'region': 'region',
        'access_key_id': 'access_key_id',
        'secret_key': 'secret_key',
        'dry_run': 'dry_run',
        'skip_verification': 'skip_verification',
        'bandwidth': 'bandwidth',
        'verbose_errors': 'verbose_errors',
        'errors_timeout': 'errors_timeout',
        'prefetch_mib': 'prefetch_mib',
        'max_concurrent_downloads': 'max_concurrent_downloads',
        'max_concurrent_uploads': 'max_concurrent_uploads',
        'max_concurrent_removals': 'max_concurrent_removals',
        'max_extents_in_data_blob': 'max_extents_in_data_blob',
        'max_blocks_in_data_blob': 'max_blocks_in_data_blob'
    }

    def __init__(self, new_name=None, new_obs_name=None, protocol=None, hostname=None, port=None, bucket=None, auth_method=None, region=None, access_key_id=None, secret_key=None, dry_run=None, skip_verification=None, bandwidth=None, verbose_errors=None, errors_timeout=None, prefetch_mib=None, max_concurrent_downloads=None, max_concurrent_uploads=None, max_concurrent_removals=None, max_extents_in_data_blob=None, max_blocks_in_data_blob=None):  # noqa: E501
        """ObjectStoreBucketsUidBody - a model defined in Swagger"""  # noqa: E501
        self._new_name = None
        self._new_obs_name = None
        self._protocol = None
        self._hostname = None
        self._port = None
        self._bucket = None
        self._auth_method = None
        self._region = None
        self._access_key_id = None
        self._secret_key = None
        self._dry_run = None
        self._skip_verification = None
        self._bandwidth = None
        self._verbose_errors = None
        self._errors_timeout = None
        self._prefetch_mib = None
        self._max_concurrent_downloads = None
        self._max_concurrent_uploads = None
        self._max_concurrent_removals = None
        self._max_extents_in_data_blob = None
        self._max_blocks_in_data_blob = None
        self.discriminator = None
        if new_name is not None:
            self.new_name = new_name
        if new_obs_name is not None:
            self.new_obs_name = new_obs_name
        if protocol is not None:
            self.protocol = protocol
        if hostname is not None:
            self.hostname = hostname
        if port is not None:
            self.port = port
        if bucket is not None:
            self.bucket = bucket
        if auth_method is not None:
            self.auth_method = auth_method
        if region is not None:
            self.region = region
        if access_key_id is not None:
            self.access_key_id = access_key_id
        if secret_key is not None:
            self.secret_key = secret_key
        if dry_run is not None:
            self.dry_run = dry_run
        if skip_verification is not None:
            self.skip_verification = skip_verification
        if bandwidth is not None:
            self.bandwidth = bandwidth
        if verbose_errors is not None:
            self.verbose_errors = verbose_errors
        if errors_timeout is not None:
            self.errors_timeout = errors_timeout
        if prefetch_mib is not None:
            self.prefetch_mib = prefetch_mib
        if max_concurrent_downloads is not None:
            self.max_concurrent_downloads = max_concurrent_downloads
        if max_concurrent_uploads is not None:
            self.max_concurrent_uploads = max_concurrent_uploads
        if max_concurrent_removals is not None:
            self.max_concurrent_removals = max_concurrent_removals
        if max_extents_in_data_blob is not None:
            self.max_extents_in_data_blob = max_extents_in_data_blob
        if max_blocks_in_data_blob is not None:
            self.max_blocks_in_data_blob = max_blocks_in_data_blob

    @property
    def new_name(self):
        """Gets the new_name of this ObjectStoreBucketsUidBody.  # noqa: E501

        Name of the Object Store Bucket  # noqa: E501

        :return: The new_name of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._new_name

    @new_name.setter
    def new_name(self, new_name):
        """Sets the new_name of this ObjectStoreBucketsUidBody.

        Name of the Object Store Bucket  # noqa: E501

        :param new_name: The new_name of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._new_name = new_name

    @property
    def new_obs_name(self):
        """Gets the new_obs_name of this ObjectStoreBucketsUidBody.  # noqa: E501

        Name of the Object Store  # noqa: E501

        :return: The new_obs_name of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._new_obs_name

    @new_obs_name.setter
    def new_obs_name(self, new_obs_name):
        """Sets the new_obs_name of this ObjectStoreBucketsUidBody.

        Name of the Object Store  # noqa: E501

        :param new_obs_name: The new_obs_name of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._new_obs_name = new_obs_name

    @property
    def protocol(self):
        """Gets the protocol of this ObjectStoreBucketsUidBody.  # noqa: E501

        One of - HTTP (default), HTTPS, HTTPS_UNVERIFIED  # noqa: E501

        :return: The protocol of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ObjectStoreBucketsUidBody.

        One of - HTTP (default), HTTPS, HTTPS_UNVERIFIED  # noqa: E501

        :param protocol: The protocol of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["HTTP", "HTTPS", "HTTPS_UNVERIFIED"]  # noqa: E501
        if protocol not in allowed_values:
            raise ValueError(
                "Invalid value for `protocol` ({0}), must be one of {1}"  # noqa: E501
                .format(protocol, allowed_values)
            )

        self._protocol = protocol

    @property
    def hostname(self):
        """Gets the hostname of this ObjectStoreBucketsUidBody.  # noqa: E501

        Hostname (or IP) of the entrypoint to the object store  # noqa: E501

        :return: The hostname of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this ObjectStoreBucketsUidBody.

        Hostname (or IP) of the entrypoint to the object store  # noqa: E501

        :param hostname: The hostname of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._hostname = hostname

    @property
    def port(self):
        """Gets the port of this ObjectStoreBucketsUidBody.  # noqa: E501

        Port of the entrypoint to S3 (single Accesser or Load-Balancer)  # noqa: E501

        :return: The port of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this ObjectStoreBucketsUidBody.

        Port of the entrypoint to S3 (single Accesser or Load-Balancer)  # noqa: E501

        :param port: The port of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._port = port

    @property
    def bucket(self):
        """Gets the bucket of this ObjectStoreBucketsUidBody.  # noqa: E501

        Name of the bucket we are assigned to work with  # noqa: E501

        :return: The bucket of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this ObjectStoreBucketsUidBody.

        Name of the bucket we are assigned to work with  # noqa: E501

        :param bucket: The bucket of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._bucket = bucket

    @property
    def auth_method(self):
        """Gets the auth_method of this ObjectStoreBucketsUidBody.  # noqa: E501

        Authentication method S3AuthMethod can be None, AWSSignature2 or AWSSignature4  # noqa: E501

        :return: The auth_method of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._auth_method

    @auth_method.setter
    def auth_method(self, auth_method):
        """Sets the auth_method of this ObjectStoreBucketsUidBody.

        Authentication method S3AuthMethod can be None, AWSSignature2 or AWSSignature4  # noqa: E501

        :param auth_method: The auth_method of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """
        allowed_values = ["None", "AWSSignature2", "AWSSignature4"]  # noqa: E501
        if auth_method not in allowed_values:
            raise ValueError(
                "Invalid value for `auth_method` ({0}), must be one of {1}"  # noqa: E501
                .format(auth_method, allowed_values)
            )

        self._auth_method = auth_method

    @property
    def region(self):
        """Gets the region of this ObjectStoreBucketsUidBody.  # noqa: E501

        Name of the region we are assigned to work with (usually empty)  # noqa: E501

        :return: The region of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ObjectStoreBucketsUidBody.

        Name of the region we are assigned to work with (usually empty)  # noqa: E501

        :param region: The region of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def access_key_id(self):
        """Gets the access_key_id of this ObjectStoreBucketsUidBody.  # noqa: E501

        Access Key ID for AWS Signature authentications  # noqa: E501

        :return: The access_key_id of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this ObjectStoreBucketsUidBody.

        Access Key ID for AWS Signature authentications  # noqa: E501

        :param access_key_id: The access_key_id of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def secret_key(self):
        """Gets the secret_key of this ObjectStoreBucketsUidBody.  # noqa: E501

        Secret Key for AWS Signature authentications  # noqa: E501

        :return: The secret_key of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this ObjectStoreBucketsUidBody.

        Secret Key for AWS Signature authentications  # noqa: E501

        :param secret_key: The secret_key of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

    @property
    def dry_run(self):
        """Gets the dry_run of this ObjectStoreBucketsUidBody.  # noqa: E501

        Only test the command, don't affect the system  # noqa: E501

        :return: The dry_run of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this ObjectStoreBucketsUidBody.

        Only test the command, don't affect the system  # noqa: E501

        :param dry_run: The dry_run of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def skip_verification(self):
        """Gets the skip_verification of this ObjectStoreBucketsUidBody.  # noqa: E501

        Don't verify the connection to the given store  # noqa: E501

        :return: The skip_verification of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._skip_verification

    @skip_verification.setter
    def skip_verification(self, skip_verification):
        """Sets the skip_verification of this ObjectStoreBucketsUidBody.

        Don't verify the connection to the given store  # noqa: E501

        :param skip_verification: The skip_verification of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: bool
        """

        self._skip_verification = skip_verification

    @property
    def bandwidth(self):
        """Gets the bandwidth of this ObjectStoreBucketsUidBody.  # noqa: E501

        Bandwidth limitation per core (Mbps)  # noqa: E501

        :return: The bandwidth of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._bandwidth

    @bandwidth.setter
    def bandwidth(self, bandwidth):
        """Sets the bandwidth of this ObjectStoreBucketsUidBody.

        Bandwidth limitation per core (Mbps)  # noqa: E501

        :param bandwidth: The bandwidth of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._bandwidth = bandwidth

    @property
    def verbose_errors(self):
        """Gets the verbose_errors of this ObjectStoreBucketsUidBody.  # noqa: E501

        Dump HTTP info on error  # noqa: E501

        :return: The verbose_errors of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: bool
        """
        return self._verbose_errors

    @verbose_errors.setter
    def verbose_errors(self, verbose_errors):
        """Sets the verbose_errors of this ObjectStoreBucketsUidBody.

        Dump HTTP info on error  # noqa: E501

        :param verbose_errors: The verbose_errors of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: bool
        """

        self._verbose_errors = verbose_errors

    @property
    def errors_timeout(self):
        """Gets the errors_timeout of this ObjectStoreBucketsUidBody.  # noqa: E501

        If the OBS link is down for longer than this, all IOs that need data return with an error (format - duration between 1 minute and 15 minutes)  # noqa: E501

        :return: The errors_timeout of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: str
        """
        return self._errors_timeout

    @errors_timeout.setter
    def errors_timeout(self, errors_timeout):
        """Sets the errors_timeout of this ObjectStoreBucketsUidBody.

        If the OBS link is down for longer than this, all IOs that need data return with an error (format - duration between 1 minute and 15 minutes)  # noqa: E501

        :param errors_timeout: The errors_timeout of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: str
        """

        self._errors_timeout = errors_timeout

    @property
    def prefetch_mib(self):
        """Gets the prefetch_mib of this ObjectStoreBucketsUidBody.  # noqa: E501

        How many MiB of data to prefetch when reading a whole MiB on object store (format - 0..600)  # noqa: E501

        :return: The prefetch_mib of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._prefetch_mib

    @prefetch_mib.setter
    def prefetch_mib(self, prefetch_mib):
        """Sets the prefetch_mib of this ObjectStoreBucketsUidBody.

        How many MiB of data to prefetch when reading a whole MiB on object store (format - 0..600)  # noqa: E501

        :param prefetch_mib: The prefetch_mib of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._prefetch_mib = prefetch_mib

    @property
    def max_concurrent_downloads(self):
        """Gets the max_concurrent_downloads of this ObjectStoreBucketsUidBody.  # noqa: E501

        Maximum number of downloads we concurrently perform on this object store in a single IO node (format - 1..64)  # noqa: E501

        :return: The max_concurrent_downloads of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._max_concurrent_downloads

    @max_concurrent_downloads.setter
    def max_concurrent_downloads(self, max_concurrent_downloads):
        """Sets the max_concurrent_downloads of this ObjectStoreBucketsUidBody.

        Maximum number of downloads we concurrently perform on this object store in a single IO node (format - 1..64)  # noqa: E501

        :param max_concurrent_downloads: The max_concurrent_downloads of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._max_concurrent_downloads = max_concurrent_downloads

    @property
    def max_concurrent_uploads(self):
        """Gets the max_concurrent_uploads of this ObjectStoreBucketsUidBody.  # noqa: E501

        Maximum number of uploads we concurrently perform on this object store in a single IO node (format - 1..64)  # noqa: E501

        :return: The max_concurrent_uploads of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._max_concurrent_uploads

    @max_concurrent_uploads.setter
    def max_concurrent_uploads(self, max_concurrent_uploads):
        """Sets the max_concurrent_uploads of this ObjectStoreBucketsUidBody.

        Maximum number of uploads we concurrently perform on this object store in a single IO node (format - 1..64)  # noqa: E501

        :param max_concurrent_uploads: The max_concurrent_uploads of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._max_concurrent_uploads = max_concurrent_uploads

    @property
    def max_concurrent_removals(self):
        """Gets the max_concurrent_removals of this ObjectStoreBucketsUidBody.  # noqa: E501

        Maximum number of removals we concurrently perform on this object store in a single IO node (format -  1..64)  # noqa: E501

        :return: The max_concurrent_removals of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._max_concurrent_removals

    @max_concurrent_removals.setter
    def max_concurrent_removals(self, max_concurrent_removals):
        """Sets the max_concurrent_removals of this ObjectStoreBucketsUidBody.

        Maximum number of removals we concurrently perform on this object store in a single IO node (format -  1..64)  # noqa: E501

        :param max_concurrent_removals: The max_concurrent_removals of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._max_concurrent_removals = max_concurrent_removals

    @property
    def max_extents_in_data_blob(self):
        """Gets the max_extents_in_data_blob of this ObjectStoreBucketsUidBody.  # noqa: E501

        Maximum number of extents data to upload to an object store data blob  # noqa: E501

        :return: The max_extents_in_data_blob of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._max_extents_in_data_blob

    @max_extents_in_data_blob.setter
    def max_extents_in_data_blob(self, max_extents_in_data_blob):
        """Sets the max_extents_in_data_blob of this ObjectStoreBucketsUidBody.

        Maximum number of extents data to upload to an object store data blob  # noqa: E501

        :param max_extents_in_data_blob: The max_extents_in_data_blob of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._max_extents_in_data_blob = max_extents_in_data_blob

    @property
    def max_blocks_in_data_blob(self):
        """Gets the max_blocks_in_data_blob of this ObjectStoreBucketsUidBody.  # noqa: E501

        Maximum size to upload to an object store data blob (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :return: The max_blocks_in_data_blob of this ObjectStoreBucketsUidBody.  # noqa: E501
        :rtype: float
        """
        return self._max_blocks_in_data_blob

    @max_blocks_in_data_blob.setter
    def max_blocks_in_data_blob(self, max_blocks_in_data_blob):
        """Sets the max_blocks_in_data_blob of this ObjectStoreBucketsUidBody.

        Maximum size to upload to an object store data blob (format - capacity in decimal or binary units - 11B, 1KB, 1MB, 1GB, 1TB, 1PB, 1EB, 1KiB, 1MiB, 1GiB, 1TiB, 1PiB, 1EiB)  # noqa: E501

        :param max_blocks_in_data_blob: The max_blocks_in_data_blob of this ObjectStoreBucketsUidBody.  # noqa: E501
        :type: float
        """

        self._max_blocks_in_data_blob = max_blocks_in_data_blob

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
        if issubclass(ObjectStoreBucketsUidBody, dict):
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
        if not isinstance(other, ObjectStoreBucketsUidBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

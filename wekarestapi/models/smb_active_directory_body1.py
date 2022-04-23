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

class SmbActiveDirectoryBody1(object):
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
        'asynchronous': 'bool',
        'create_computer_ou': 'str',
        'debug_mode': 'bool',
        'extra_options': 'str',
        'password': 'str',
        'poll': 'bool',
        'server': 'str',
        'task_id': 'str',
        'timeout': 'str',
        'username': 'str'
    }

    attribute_map = {
        'asynchronous': 'asynchronous',
        'create_computer_ou': 'create_computerOU',
        'debug_mode': 'debug_mode',
        'extra_options': 'extra_options',
        'password': 'password',
        'poll': 'poll',
        'server': 'server',
        'task_id': 'task_id',
        'timeout': 'timeout',
        'username': 'username'
    }

    def __init__(self, asynchronous=None, create_computer_ou=None, debug_mode=None, extra_options=None, password=None, poll=None, server=None, task_id=None, timeout=None, username=None):  # noqa: E501
        """SmbActiveDirectoryBody1 - a model defined in Swagger"""  # noqa: E501
        self._asynchronous = None
        self._create_computer_ou = None
        self._debug_mode = None
        self._extra_options = None
        self._password = None
        self._poll = None
        self._server = None
        self._task_id = None
        self._timeout = None
        self._username = None
        self.discriminator = None
        if asynchronous is not None:
            self.asynchronous = asynchronous
        if create_computer_ou is not None:
            self.create_computer_ou = create_computer_ou
        if debug_mode is not None:
            self.debug_mode = debug_mode
        if extra_options is not None:
            self.extra_options = extra_options
        self.password = password
        if poll is not None:
            self.poll = poll
        if server is not None:
            self.server = server
        if task_id is not None:
            self.task_id = task_id
        if timeout is not None:
            self.timeout = timeout
        self.username = username

    @property
    def asynchronous(self):
        """Gets the asynchronous of this SmbActiveDirectoryBody1.  # noqa: E501


        :return: The asynchronous of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: bool
        """
        return self._asynchronous

    @asynchronous.setter
    def asynchronous(self, asynchronous):
        """Sets the asynchronous of this SmbActiveDirectoryBody1.


        :param asynchronous: The asynchronous of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: bool
        """

        self._asynchronous = asynchronous

    @property
    def create_computer_ou(self):
        """Gets the create_computer_ou of this SmbActiveDirectoryBody1.  # noqa: E501

        Precreate the computer account in a specific OU  # noqa: E501

        :return: The create_computer_ou of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._create_computer_ou

    @create_computer_ou.setter
    def create_computer_ou(self, create_computer_ou):
        """Sets the create_computer_ou of this SmbActiveDirectoryBody1.

        Precreate the computer account in a specific OU  # noqa: E501

        :param create_computer_ou: The create_computer_ou of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """

        self._create_computer_ou = create_computer_ou

    @property
    def debug_mode(self):
        """Gets the debug_mode of this SmbActiveDirectoryBody1.  # noqa: E501

        Run the command in debug mode  # noqa: E501

        :return: The debug_mode of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: bool
        """
        return self._debug_mode

    @debug_mode.setter
    def debug_mode(self, debug_mode):
        """Sets the debug_mode of this SmbActiveDirectoryBody1.

        Run the command in debug mode  # noqa: E501

        :param debug_mode: The debug_mode of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: bool
        """

        self._debug_mode = debug_mode

    @property
    def extra_options(self):
        """Gets the extra_options of this SmbActiveDirectoryBody1.  # noqa: E501


        :return: The extra_options of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._extra_options

    @extra_options.setter
    def extra_options(self, extra_options):
        """Sets the extra_options of this SmbActiveDirectoryBody1.


        :param extra_options: The extra_options of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """

        self._extra_options = extra_options

    @property
    def password(self):
        """Gets the password of this SmbActiveDirectoryBody1.  # noqa: E501

        The administrator user password  # noqa: E501

        :return: The password of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this SmbActiveDirectoryBody1.

        The administrator user password  # noqa: E501

        :param password: The password of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def poll(self):
        """Gets the poll of this SmbActiveDirectoryBody1.  # noqa: E501


        :return: The poll of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: bool
        """
        return self._poll

    @poll.setter
    def poll(self, poll):
        """Sets the poll of this SmbActiveDirectoryBody1.


        :param poll: The poll of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: bool
        """

        self._poll = poll

    @property
    def server(self):
        """Gets the server of this SmbActiveDirectoryBody1.  # noqa: E501

        The domain controller server  # noqa: E501

        :return: The server of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this SmbActiveDirectoryBody1.

        The domain controller server  # noqa: E501

        :param server: The server of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def task_id(self):
        """Gets the task_id of this SmbActiveDirectoryBody1.  # noqa: E501


        :return: The task_id of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this SmbActiveDirectoryBody1.


        :param task_id: The task_id of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """

        self._task_id = task_id

    @property
    def timeout(self):
        """Gets the timeout of this SmbActiveDirectoryBody1.  # noqa: E501

        Join command timeout in seconds (format - 3s, 2h, 4m, 1d, 1d5h, 1w, infinite/unlimited)  # noqa: E501

        :return: The timeout of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this SmbActiveDirectoryBody1.

        Join command timeout in seconds (format - 3s, 2h, 4m, 1d, 1d5h, 1w, infinite/unlimited)  # noqa: E501

        :param timeout: The timeout of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """

        self._timeout = timeout

    @property
    def username(self):
        """Gets the username of this SmbActiveDirectoryBody1.  # noqa: E501

        The name of the administrator user to join the domain using it  # noqa: E501

        :return: The username of this SmbActiveDirectoryBody1.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this SmbActiveDirectoryBody1.

        The name of the administrator user to join the domain using it  # noqa: E501

        :param username: The username of this SmbActiveDirectoryBody1.  # noqa: E501
        :type: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

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
        if issubclass(SmbActiveDirectoryBody1, dict):
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
        if not isinstance(other, SmbActiveDirectoryBody1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
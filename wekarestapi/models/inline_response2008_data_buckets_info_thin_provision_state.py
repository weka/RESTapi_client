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

class InlineResponse2008DataBucketsInfoThinProvisionState(object):
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
        'usable_writable': 'float',
        'total_ssd_budgets': 'float',
        'shrinkage_factor': 'InlineResponse2008DataBucketsInfoThinProvisionStateShrinkageFactor'
    }

    attribute_map = {
        'usable_writable': 'usableWritable',
        'total_ssd_budgets': 'totalSSDBudgets',
        'shrinkage_factor': 'shrinkageFactor'
    }

    def __init__(self, usable_writable=None, total_ssd_budgets=None, shrinkage_factor=None):  # noqa: E501
        """InlineResponse2008DataBucketsInfoThinProvisionState - a model defined in Swagger"""  # noqa: E501
        self._usable_writable = None
        self._total_ssd_budgets = None
        self._shrinkage_factor = None
        self.discriminator = None
        if usable_writable is not None:
            self.usable_writable = usable_writable
        if total_ssd_budgets is not None:
            self.total_ssd_budgets = total_ssd_budgets
        if shrinkage_factor is not None:
            self.shrinkage_factor = shrinkage_factor

    @property
    def usable_writable(self):
        """Gets the usable_writable of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501


        :return: The usable_writable of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501
        :rtype: float
        """
        return self._usable_writable

    @usable_writable.setter
    def usable_writable(self, usable_writable):
        """Sets the usable_writable of this InlineResponse2008DataBucketsInfoThinProvisionState.


        :param usable_writable: The usable_writable of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501
        :type: float
        """

        self._usable_writable = usable_writable

    @property
    def total_ssd_budgets(self):
        """Gets the total_ssd_budgets of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501


        :return: The total_ssd_budgets of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501
        :rtype: float
        """
        return self._total_ssd_budgets

    @total_ssd_budgets.setter
    def total_ssd_budgets(self, total_ssd_budgets):
        """Sets the total_ssd_budgets of this InlineResponse2008DataBucketsInfoThinProvisionState.


        :param total_ssd_budgets: The total_ssd_budgets of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501
        :type: float
        """

        self._total_ssd_budgets = total_ssd_budgets

    @property
    def shrinkage_factor(self):
        """Gets the shrinkage_factor of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501


        :return: The shrinkage_factor of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501
        :rtype: InlineResponse2008DataBucketsInfoThinProvisionStateShrinkageFactor
        """
        return self._shrinkage_factor

    @shrinkage_factor.setter
    def shrinkage_factor(self, shrinkage_factor):
        """Sets the shrinkage_factor of this InlineResponse2008DataBucketsInfoThinProvisionState.


        :param shrinkage_factor: The shrinkage_factor of this InlineResponse2008DataBucketsInfoThinProvisionState.  # noqa: E501
        :type: InlineResponse2008DataBucketsInfoThinProvisionStateShrinkageFactor
        """

        self._shrinkage_factor = shrinkage_factor

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
        if issubclass(InlineResponse2008DataBucketsInfoThinProvisionState, dict):
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
        if not isinstance(other, InlineResponse2008DataBucketsInfoThinProvisionState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
# coding: utf-8

"""
    Pietsmiet.de API

    OpenAPI spec generated from HAR data for www.pietsmiet.de on 2024-09-03T03:22:16.459Z  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Datum12(object):
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
        'braintree_id': 'str',
        'braintree_plan': 'BraintreePlan',
        'details': 'Details',
        'enabled': 'bool',
        'id': 'str',
        'options': 'Options1',
        'support_add_on': 'AnyOfDatum12SupportAddOn',
        'type': 'str'
    }

    attribute_map = {
        'braintree_id': 'braintree_id',
        'braintree_plan': 'braintree_plan',
        'details': 'details',
        'enabled': 'enabled',
        'id': 'id',
        'options': 'options',
        'support_add_on': 'support_add_on',
        'type': 'type'
    }

    def __init__(self, braintree_id=None, braintree_plan=None, details=None, enabled=None, id=None, options=None, support_add_on=None, type=None):  # noqa: E501
        """Datum12 - a model defined in Swagger"""  # noqa: E501
        self._braintree_id = None
        self._braintree_plan = None
        self._details = None
        self._enabled = None
        self._id = None
        self._options = None
        self._support_add_on = None
        self._type = None
        self.discriminator = None
        if braintree_id is not None:
            self.braintree_id = braintree_id
        if braintree_plan is not None:
            self.braintree_plan = braintree_plan
        if details is not None:
            self.details = details
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if options is not None:
            self.options = options
        if support_add_on is not None:
            self.support_add_on = support_add_on
        if type is not None:
            self.type = type

    @property
    def braintree_id(self):
        """Gets the braintree_id of this Datum12.  # noqa: E501


        :return: The braintree_id of this Datum12.  # noqa: E501
        :rtype: str
        """
        return self._braintree_id

    @braintree_id.setter
    def braintree_id(self, braintree_id):
        """Sets the braintree_id of this Datum12.


        :param braintree_id: The braintree_id of this Datum12.  # noqa: E501
        :type: str
        """

        self._braintree_id = braintree_id

    @property
    def braintree_plan(self):
        """Gets the braintree_plan of this Datum12.  # noqa: E501


        :return: The braintree_plan of this Datum12.  # noqa: E501
        :rtype: BraintreePlan
        """
        return self._braintree_plan

    @braintree_plan.setter
    def braintree_plan(self, braintree_plan):
        """Sets the braintree_plan of this Datum12.


        :param braintree_plan: The braintree_plan of this Datum12.  # noqa: E501
        :type: BraintreePlan
        """

        self._braintree_plan = braintree_plan

    @property
    def details(self):
        """Gets the details of this Datum12.  # noqa: E501


        :return: The details of this Datum12.  # noqa: E501
        :rtype: Details
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Datum12.


        :param details: The details of this Datum12.  # noqa: E501
        :type: Details
        """

        self._details = details

    @property
    def enabled(self):
        """Gets the enabled of this Datum12.  # noqa: E501


        :return: The enabled of this Datum12.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this Datum12.


        :param enabled: The enabled of this Datum12.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this Datum12.  # noqa: E501


        :return: The id of this Datum12.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Datum12.


        :param id: The id of this Datum12.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def options(self):
        """Gets the options of this Datum12.  # noqa: E501


        :return: The options of this Datum12.  # noqa: E501
        :rtype: Options1
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this Datum12.


        :param options: The options of this Datum12.  # noqa: E501
        :type: Options1
        """

        self._options = options

    @property
    def support_add_on(self):
        """Gets the support_add_on of this Datum12.  # noqa: E501


        :return: The support_add_on of this Datum12.  # noqa: E501
        :rtype: AnyOfDatum12SupportAddOn
        """
        return self._support_add_on

    @support_add_on.setter
    def support_add_on(self, support_add_on):
        """Sets the support_add_on of this Datum12.


        :param support_add_on: The support_add_on of this Datum12.  # noqa: E501
        :type: AnyOfDatum12SupportAddOn
        """

        self._support_add_on = support_add_on

    @property
    def type(self):
        """Gets the type of this Datum12.  # noqa: E501


        :return: The type of this Datum12.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Datum12.


        :param type: The type of this Datum12.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Datum12, dict):
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
        if not isinstance(other, Datum12):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

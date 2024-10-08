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

class BraintreePlan(object):
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
        'add_ons': 'list[object]',
        'billing_day_of_month': 'object',
        'billing_frequency': 'int',
        'created_at': 'AtedAt',
        'currency_iso_code': 'str',
        'description': 'object',
        'discounts': 'list[object]',
        'id': 'str',
        'merchant_id': 'str',
        'name': 'str',
        'number_of_billing_cycles': 'object',
        'plans': 'list[object]',
        'price': 'str',
        'trial_duration': 'object',
        'trial_duration_unit': 'object',
        'trial_period': 'bool',
        'updated_at': 'AtedAt'
    }

    attribute_map = {
        'add_ons': 'addOns',
        'billing_day_of_month': 'billingDayOfMonth',
        'billing_frequency': 'billingFrequency',
        'created_at': 'createdAt',
        'currency_iso_code': 'currencyIsoCode',
        'description': 'description',
        'discounts': 'discounts',
        'id': 'id',
        'merchant_id': 'merchantId',
        'name': 'name',
        'number_of_billing_cycles': 'numberOfBillingCycles',
        'plans': 'plans',
        'price': 'price',
        'trial_duration': 'trialDuration',
        'trial_duration_unit': 'trialDurationUnit',
        'trial_period': 'trialPeriod',
        'updated_at': 'updatedAt'
    }

    def __init__(self, add_ons=None, billing_day_of_month=None, billing_frequency=None, created_at=None, currency_iso_code=None, description=None, discounts=None, id=None, merchant_id=None, name=None, number_of_billing_cycles=None, plans=None, price=None, trial_duration=None, trial_duration_unit=None, trial_period=None, updated_at=None):  # noqa: E501
        """BraintreePlan - a model defined in Swagger"""  # noqa: E501
        self._add_ons = None
        self._billing_day_of_month = None
        self._billing_frequency = None
        self._created_at = None
        self._currency_iso_code = None
        self._description = None
        self._discounts = None
        self._id = None
        self._merchant_id = None
        self._name = None
        self._number_of_billing_cycles = None
        self._plans = None
        self._price = None
        self._trial_duration = None
        self._trial_duration_unit = None
        self._trial_period = None
        self._updated_at = None
        self.discriminator = None
        if add_ons is not None:
            self.add_ons = add_ons
        if billing_day_of_month is not None:
            self.billing_day_of_month = billing_day_of_month
        if billing_frequency is not None:
            self.billing_frequency = billing_frequency
        if created_at is not None:
            self.created_at = created_at
        if currency_iso_code is not None:
            self.currency_iso_code = currency_iso_code
        if description is not None:
            self.description = description
        if discounts is not None:
            self.discounts = discounts
        if id is not None:
            self.id = id
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if name is not None:
            self.name = name
        if number_of_billing_cycles is not None:
            self.number_of_billing_cycles = number_of_billing_cycles
        if plans is not None:
            self.plans = plans
        if price is not None:
            self.price = price
        if trial_duration is not None:
            self.trial_duration = trial_duration
        if trial_duration_unit is not None:
            self.trial_duration_unit = trial_duration_unit
        if trial_period is not None:
            self.trial_period = trial_period
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def add_ons(self):
        """Gets the add_ons of this BraintreePlan.  # noqa: E501


        :return: The add_ons of this BraintreePlan.  # noqa: E501
        :rtype: list[object]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """Sets the add_ons of this BraintreePlan.


        :param add_ons: The add_ons of this BraintreePlan.  # noqa: E501
        :type: list[object]
        """

        self._add_ons = add_ons

    @property
    def billing_day_of_month(self):
        """Gets the billing_day_of_month of this BraintreePlan.  # noqa: E501


        :return: The billing_day_of_month of this BraintreePlan.  # noqa: E501
        :rtype: object
        """
        return self._billing_day_of_month

    @billing_day_of_month.setter
    def billing_day_of_month(self, billing_day_of_month):
        """Sets the billing_day_of_month of this BraintreePlan.


        :param billing_day_of_month: The billing_day_of_month of this BraintreePlan.  # noqa: E501
        :type: object
        """

        self._billing_day_of_month = billing_day_of_month

    @property
    def billing_frequency(self):
        """Gets the billing_frequency of this BraintreePlan.  # noqa: E501


        :return: The billing_frequency of this BraintreePlan.  # noqa: E501
        :rtype: int
        """
        return self._billing_frequency

    @billing_frequency.setter
    def billing_frequency(self, billing_frequency):
        """Sets the billing_frequency of this BraintreePlan.


        :param billing_frequency: The billing_frequency of this BraintreePlan.  # noqa: E501
        :type: int
        """

        self._billing_frequency = billing_frequency

    @property
    def created_at(self):
        """Gets the created_at of this BraintreePlan.  # noqa: E501


        :return: The created_at of this BraintreePlan.  # noqa: E501
        :rtype: AtedAt
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this BraintreePlan.


        :param created_at: The created_at of this BraintreePlan.  # noqa: E501
        :type: AtedAt
        """

        self._created_at = created_at

    @property
    def currency_iso_code(self):
        """Gets the currency_iso_code of this BraintreePlan.  # noqa: E501


        :return: The currency_iso_code of this BraintreePlan.  # noqa: E501
        :rtype: str
        """
        return self._currency_iso_code

    @currency_iso_code.setter
    def currency_iso_code(self, currency_iso_code):
        """Sets the currency_iso_code of this BraintreePlan.


        :param currency_iso_code: The currency_iso_code of this BraintreePlan.  # noqa: E501
        :type: str
        """

        self._currency_iso_code = currency_iso_code

    @property
    def description(self):
        """Gets the description of this BraintreePlan.  # noqa: E501


        :return: The description of this BraintreePlan.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BraintreePlan.


        :param description: The description of this BraintreePlan.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def discounts(self):
        """Gets the discounts of this BraintreePlan.  # noqa: E501


        :return: The discounts of this BraintreePlan.  # noqa: E501
        :rtype: list[object]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this BraintreePlan.


        :param discounts: The discounts of this BraintreePlan.  # noqa: E501
        :type: list[object]
        """

        self._discounts = discounts

    @property
    def id(self):
        """Gets the id of this BraintreePlan.  # noqa: E501


        :return: The id of this BraintreePlan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BraintreePlan.


        :param id: The id of this BraintreePlan.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def merchant_id(self):
        """Gets the merchant_id of this BraintreePlan.  # noqa: E501


        :return: The merchant_id of this BraintreePlan.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this BraintreePlan.


        :param merchant_id: The merchant_id of this BraintreePlan.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def name(self):
        """Gets the name of this BraintreePlan.  # noqa: E501


        :return: The name of this BraintreePlan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BraintreePlan.


        :param name: The name of this BraintreePlan.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def number_of_billing_cycles(self):
        """Gets the number_of_billing_cycles of this BraintreePlan.  # noqa: E501


        :return: The number_of_billing_cycles of this BraintreePlan.  # noqa: E501
        :rtype: object
        """
        return self._number_of_billing_cycles

    @number_of_billing_cycles.setter
    def number_of_billing_cycles(self, number_of_billing_cycles):
        """Sets the number_of_billing_cycles of this BraintreePlan.


        :param number_of_billing_cycles: The number_of_billing_cycles of this BraintreePlan.  # noqa: E501
        :type: object
        """

        self._number_of_billing_cycles = number_of_billing_cycles

    @property
    def plans(self):
        """Gets the plans of this BraintreePlan.  # noqa: E501


        :return: The plans of this BraintreePlan.  # noqa: E501
        :rtype: list[object]
        """
        return self._plans

    @plans.setter
    def plans(self, plans):
        """Sets the plans of this BraintreePlan.


        :param plans: The plans of this BraintreePlan.  # noqa: E501
        :type: list[object]
        """

        self._plans = plans

    @property
    def price(self):
        """Gets the price of this BraintreePlan.  # noqa: E501


        :return: The price of this BraintreePlan.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BraintreePlan.


        :param price: The price of this BraintreePlan.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def trial_duration(self):
        """Gets the trial_duration of this BraintreePlan.  # noqa: E501


        :return: The trial_duration of this BraintreePlan.  # noqa: E501
        :rtype: object
        """
        return self._trial_duration

    @trial_duration.setter
    def trial_duration(self, trial_duration):
        """Sets the trial_duration of this BraintreePlan.


        :param trial_duration: The trial_duration of this BraintreePlan.  # noqa: E501
        :type: object
        """

        self._trial_duration = trial_duration

    @property
    def trial_duration_unit(self):
        """Gets the trial_duration_unit of this BraintreePlan.  # noqa: E501


        :return: The trial_duration_unit of this BraintreePlan.  # noqa: E501
        :rtype: object
        """
        return self._trial_duration_unit

    @trial_duration_unit.setter
    def trial_duration_unit(self, trial_duration_unit):
        """Sets the trial_duration_unit of this BraintreePlan.


        :param trial_duration_unit: The trial_duration_unit of this BraintreePlan.  # noqa: E501
        :type: object
        """

        self._trial_duration_unit = trial_duration_unit

    @property
    def trial_period(self):
        """Gets the trial_period of this BraintreePlan.  # noqa: E501


        :return: The trial_period of this BraintreePlan.  # noqa: E501
        :rtype: bool
        """
        return self._trial_period

    @trial_period.setter
    def trial_period(self, trial_period):
        """Sets the trial_period of this BraintreePlan.


        :param trial_period: The trial_period of this BraintreePlan.  # noqa: E501
        :type: bool
        """

        self._trial_period = trial_period

    @property
    def updated_at(self):
        """Gets the updated_at of this BraintreePlan.  # noqa: E501


        :return: The updated_at of this BraintreePlan.  # noqa: E501
        :rtype: AtedAt
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this BraintreePlan.


        :param updated_at: The updated_at of this BraintreePlan.  # noqa: E501
        :type: AtedAt
        """

        self._updated_at = updated_at

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
        if issubclass(BraintreePlan, dict):
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
        if not isinstance(other, BraintreePlan):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

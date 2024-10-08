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

class Braintree(object):
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
        'billing_day_of_month': 'int',
        'billing_period_end_date': 'datetime',
        'billing_period_start_date': 'datetime',
        'current_billing_cycle': 'int',
        'days_past_due': 'object',
        'discounts': 'list[Discount]',
        'failure_count': 'int',
        'first_billing_date': 'datetime',
        'never_expires': 'bool',
        'next_bill_amount': 'str',
        'next_billing_date': 'datetime',
        'next_billing_period_amount': 'str',
        'number_of_billing_cycles': 'object',
        'price': 'str',
        'status': 'str'
    }

    attribute_map = {
        'add_ons': 'add_ons',
        'billing_day_of_month': 'billing_day_of_month',
        'billing_period_end_date': 'billing_period_end_date',
        'billing_period_start_date': 'billing_period_start_date',
        'current_billing_cycle': 'current_billing_cycle',
        'days_past_due': 'days_past_due',
        'discounts': 'discounts',
        'failure_count': 'failure_count',
        'first_billing_date': 'first_billing_date',
        'never_expires': 'never_expires',
        'next_bill_amount': 'next_bill_amount',
        'next_billing_date': 'next_billing_date',
        'next_billing_period_amount': 'next_billing_period_amount',
        'number_of_billing_cycles': 'number_of_billing_cycles',
        'price': 'price',
        'status': 'status'
    }

    def __init__(self, add_ons=None, billing_day_of_month=None, billing_period_end_date=None, billing_period_start_date=None, current_billing_cycle=None, days_past_due=None, discounts=None, failure_count=None, first_billing_date=None, never_expires=None, next_bill_amount=None, next_billing_date=None, next_billing_period_amount=None, number_of_billing_cycles=None, price=None, status=None):  # noqa: E501
        """Braintree - a model defined in Swagger"""  # noqa: E501
        self._add_ons = None
        self._billing_day_of_month = None
        self._billing_period_end_date = None
        self._billing_period_start_date = None
        self._current_billing_cycle = None
        self._days_past_due = None
        self._discounts = None
        self._failure_count = None
        self._first_billing_date = None
        self._never_expires = None
        self._next_bill_amount = None
        self._next_billing_date = None
        self._next_billing_period_amount = None
        self._number_of_billing_cycles = None
        self._price = None
        self._status = None
        self.discriminator = None
        if add_ons is not None:
            self.add_ons = add_ons
        if billing_day_of_month is not None:
            self.billing_day_of_month = billing_day_of_month
        if billing_period_end_date is not None:
            self.billing_period_end_date = billing_period_end_date
        if billing_period_start_date is not None:
            self.billing_period_start_date = billing_period_start_date
        if current_billing_cycle is not None:
            self.current_billing_cycle = current_billing_cycle
        if days_past_due is not None:
            self.days_past_due = days_past_due
        if discounts is not None:
            self.discounts = discounts
        if failure_count is not None:
            self.failure_count = failure_count
        if first_billing_date is not None:
            self.first_billing_date = first_billing_date
        if never_expires is not None:
            self.never_expires = never_expires
        if next_bill_amount is not None:
            self.next_bill_amount = next_bill_amount
        if next_billing_date is not None:
            self.next_billing_date = next_billing_date
        if next_billing_period_amount is not None:
            self.next_billing_period_amount = next_billing_period_amount
        if number_of_billing_cycles is not None:
            self.number_of_billing_cycles = number_of_billing_cycles
        if price is not None:
            self.price = price
        if status is not None:
            self.status = status

    @property
    def add_ons(self):
        """Gets the add_ons of this Braintree.  # noqa: E501


        :return: The add_ons of this Braintree.  # noqa: E501
        :rtype: list[object]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons):
        """Sets the add_ons of this Braintree.


        :param add_ons: The add_ons of this Braintree.  # noqa: E501
        :type: list[object]
        """

        self._add_ons = add_ons

    @property
    def billing_day_of_month(self):
        """Gets the billing_day_of_month of this Braintree.  # noqa: E501


        :return: The billing_day_of_month of this Braintree.  # noqa: E501
        :rtype: int
        """
        return self._billing_day_of_month

    @billing_day_of_month.setter
    def billing_day_of_month(self, billing_day_of_month):
        """Sets the billing_day_of_month of this Braintree.


        :param billing_day_of_month: The billing_day_of_month of this Braintree.  # noqa: E501
        :type: int
        """

        self._billing_day_of_month = billing_day_of_month

    @property
    def billing_period_end_date(self):
        """Gets the billing_period_end_date of this Braintree.  # noqa: E501


        :return: The billing_period_end_date of this Braintree.  # noqa: E501
        :rtype: datetime
        """
        return self._billing_period_end_date

    @billing_period_end_date.setter
    def billing_period_end_date(self, billing_period_end_date):
        """Sets the billing_period_end_date of this Braintree.


        :param billing_period_end_date: The billing_period_end_date of this Braintree.  # noqa: E501
        :type: datetime
        """

        self._billing_period_end_date = billing_period_end_date

    @property
    def billing_period_start_date(self):
        """Gets the billing_period_start_date of this Braintree.  # noqa: E501


        :return: The billing_period_start_date of this Braintree.  # noqa: E501
        :rtype: datetime
        """
        return self._billing_period_start_date

    @billing_period_start_date.setter
    def billing_period_start_date(self, billing_period_start_date):
        """Sets the billing_period_start_date of this Braintree.


        :param billing_period_start_date: The billing_period_start_date of this Braintree.  # noqa: E501
        :type: datetime
        """

        self._billing_period_start_date = billing_period_start_date

    @property
    def current_billing_cycle(self):
        """Gets the current_billing_cycle of this Braintree.  # noqa: E501


        :return: The current_billing_cycle of this Braintree.  # noqa: E501
        :rtype: int
        """
        return self._current_billing_cycle

    @current_billing_cycle.setter
    def current_billing_cycle(self, current_billing_cycle):
        """Sets the current_billing_cycle of this Braintree.


        :param current_billing_cycle: The current_billing_cycle of this Braintree.  # noqa: E501
        :type: int
        """

        self._current_billing_cycle = current_billing_cycle

    @property
    def days_past_due(self):
        """Gets the days_past_due of this Braintree.  # noqa: E501


        :return: The days_past_due of this Braintree.  # noqa: E501
        :rtype: object
        """
        return self._days_past_due

    @days_past_due.setter
    def days_past_due(self, days_past_due):
        """Sets the days_past_due of this Braintree.


        :param days_past_due: The days_past_due of this Braintree.  # noqa: E501
        :type: object
        """

        self._days_past_due = days_past_due

    @property
    def discounts(self):
        """Gets the discounts of this Braintree.  # noqa: E501


        :return: The discounts of this Braintree.  # noqa: E501
        :rtype: list[Discount]
        """
        return self._discounts

    @discounts.setter
    def discounts(self, discounts):
        """Sets the discounts of this Braintree.


        :param discounts: The discounts of this Braintree.  # noqa: E501
        :type: list[Discount]
        """

        self._discounts = discounts

    @property
    def failure_count(self):
        """Gets the failure_count of this Braintree.  # noqa: E501


        :return: The failure_count of this Braintree.  # noqa: E501
        :rtype: int
        """
        return self._failure_count

    @failure_count.setter
    def failure_count(self, failure_count):
        """Sets the failure_count of this Braintree.


        :param failure_count: The failure_count of this Braintree.  # noqa: E501
        :type: int
        """

        self._failure_count = failure_count

    @property
    def first_billing_date(self):
        """Gets the first_billing_date of this Braintree.  # noqa: E501


        :return: The first_billing_date of this Braintree.  # noqa: E501
        :rtype: datetime
        """
        return self._first_billing_date

    @first_billing_date.setter
    def first_billing_date(self, first_billing_date):
        """Sets the first_billing_date of this Braintree.


        :param first_billing_date: The first_billing_date of this Braintree.  # noqa: E501
        :type: datetime
        """

        self._first_billing_date = first_billing_date

    @property
    def never_expires(self):
        """Gets the never_expires of this Braintree.  # noqa: E501


        :return: The never_expires of this Braintree.  # noqa: E501
        :rtype: bool
        """
        return self._never_expires

    @never_expires.setter
    def never_expires(self, never_expires):
        """Sets the never_expires of this Braintree.


        :param never_expires: The never_expires of this Braintree.  # noqa: E501
        :type: bool
        """

        self._never_expires = never_expires

    @property
    def next_bill_amount(self):
        """Gets the next_bill_amount of this Braintree.  # noqa: E501


        :return: The next_bill_amount of this Braintree.  # noqa: E501
        :rtype: str
        """
        return self._next_bill_amount

    @next_bill_amount.setter
    def next_bill_amount(self, next_bill_amount):
        """Sets the next_bill_amount of this Braintree.


        :param next_bill_amount: The next_bill_amount of this Braintree.  # noqa: E501
        :type: str
        """

        self._next_bill_amount = next_bill_amount

    @property
    def next_billing_date(self):
        """Gets the next_billing_date of this Braintree.  # noqa: E501


        :return: The next_billing_date of this Braintree.  # noqa: E501
        :rtype: datetime
        """
        return self._next_billing_date

    @next_billing_date.setter
    def next_billing_date(self, next_billing_date):
        """Sets the next_billing_date of this Braintree.


        :param next_billing_date: The next_billing_date of this Braintree.  # noqa: E501
        :type: datetime
        """

        self._next_billing_date = next_billing_date

    @property
    def next_billing_period_amount(self):
        """Gets the next_billing_period_amount of this Braintree.  # noqa: E501


        :return: The next_billing_period_amount of this Braintree.  # noqa: E501
        :rtype: str
        """
        return self._next_billing_period_amount

    @next_billing_period_amount.setter
    def next_billing_period_amount(self, next_billing_period_amount):
        """Sets the next_billing_period_amount of this Braintree.


        :param next_billing_period_amount: The next_billing_period_amount of this Braintree.  # noqa: E501
        :type: str
        """

        self._next_billing_period_amount = next_billing_period_amount

    @property
    def number_of_billing_cycles(self):
        """Gets the number_of_billing_cycles of this Braintree.  # noqa: E501


        :return: The number_of_billing_cycles of this Braintree.  # noqa: E501
        :rtype: object
        """
        return self._number_of_billing_cycles

    @number_of_billing_cycles.setter
    def number_of_billing_cycles(self, number_of_billing_cycles):
        """Sets the number_of_billing_cycles of this Braintree.


        :param number_of_billing_cycles: The number_of_billing_cycles of this Braintree.  # noqa: E501
        :type: object
        """

        self._number_of_billing_cycles = number_of_billing_cycles

    @property
    def price(self):
        """Gets the price of this Braintree.  # noqa: E501


        :return: The price of this Braintree.  # noqa: E501
        :rtype: str
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this Braintree.


        :param price: The price of this Braintree.  # noqa: E501
        :type: str
        """

        self._price = price

    @property
    def status(self):
        """Gets the status of this Braintree.  # noqa: E501


        :return: The status of this Braintree.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Braintree.


        :param status: The status of this Braintree.  # noqa: E501
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
        if issubclass(Braintree, dict):
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
        if not isinstance(other, Braintree):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

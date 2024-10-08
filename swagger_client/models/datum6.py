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

class Datum6(object):
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
        'active': 'bool',
        'braintree': 'Braintree',
        'cancelled': 'bool',
        'created_at': 'datetime',
        'ends_at': 'datetime',
        'gifted': 'bool',
        'id': 'int',
        'name': 'object',
        'on_grace_period': 'bool',
        'on_trial': 'bool',
        'product': 'Product',
        'sponsored': 'bool',
        'trial_ends_at': 'object',
        'updated_at': 'datetime',
        'valid': 'bool'
    }

    attribute_map = {
        'active': 'active',
        'braintree': 'braintree',
        'cancelled': 'cancelled',
        'created_at': 'created_at',
        'ends_at': 'ends_at',
        'gifted': 'gifted',
        'id': 'id',
        'name': 'name',
        'on_grace_period': 'on_grace_period',
        'on_trial': 'on_trial',
        'product': 'product',
        'sponsored': 'sponsored',
        'trial_ends_at': 'trial_ends_at',
        'updated_at': 'updated_at',
        'valid': 'valid'
    }

    def __init__(self, active=None, braintree=None, cancelled=None, created_at=None, ends_at=None, gifted=None, id=None, name=None, on_grace_period=None, on_trial=None, product=None, sponsored=None, trial_ends_at=None, updated_at=None, valid=None):  # noqa: E501
        """Datum6 - a model defined in Swagger"""  # noqa: E501
        self._active = None
        self._braintree = None
        self._cancelled = None
        self._created_at = None
        self._ends_at = None
        self._gifted = None
        self._id = None
        self._name = None
        self._on_grace_period = None
        self._on_trial = None
        self._product = None
        self._sponsored = None
        self._trial_ends_at = None
        self._updated_at = None
        self._valid = None
        self.discriminator = None
        if active is not None:
            self.active = active
        if braintree is not None:
            self.braintree = braintree
        if cancelled is not None:
            self.cancelled = cancelled
        if created_at is not None:
            self.created_at = created_at
        if ends_at is not None:
            self.ends_at = ends_at
        if gifted is not None:
            self.gifted = gifted
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if on_grace_period is not None:
            self.on_grace_period = on_grace_period
        if on_trial is not None:
            self.on_trial = on_trial
        if product is not None:
            self.product = product
        if sponsored is not None:
            self.sponsored = sponsored
        if trial_ends_at is not None:
            self.trial_ends_at = trial_ends_at
        if updated_at is not None:
            self.updated_at = updated_at
        if valid is not None:
            self.valid = valid

    @property
    def active(self):
        """Gets the active of this Datum6.  # noqa: E501


        :return: The active of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Datum6.


        :param active: The active of this Datum6.  # noqa: E501
        :type: bool
        """

        self._active = active

    @property
    def braintree(self):
        """Gets the braintree of this Datum6.  # noqa: E501


        :return: The braintree of this Datum6.  # noqa: E501
        :rtype: Braintree
        """
        return self._braintree

    @braintree.setter
    def braintree(self, braintree):
        """Sets the braintree of this Datum6.


        :param braintree: The braintree of this Datum6.  # noqa: E501
        :type: Braintree
        """

        self._braintree = braintree

    @property
    def cancelled(self):
        """Gets the cancelled of this Datum6.  # noqa: E501


        :return: The cancelled of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._cancelled

    @cancelled.setter
    def cancelled(self, cancelled):
        """Sets the cancelled of this Datum6.


        :param cancelled: The cancelled of this Datum6.  # noqa: E501
        :type: bool
        """

        self._cancelled = cancelled

    @property
    def created_at(self):
        """Gets the created_at of this Datum6.  # noqa: E501


        :return: The created_at of this Datum6.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Datum6.


        :param created_at: The created_at of this Datum6.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def ends_at(self):
        """Gets the ends_at of this Datum6.  # noqa: E501


        :return: The ends_at of this Datum6.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this Datum6.


        :param ends_at: The ends_at of this Datum6.  # noqa: E501
        :type: datetime
        """

        self._ends_at = ends_at

    @property
    def gifted(self):
        """Gets the gifted of this Datum6.  # noqa: E501


        :return: The gifted of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._gifted

    @gifted.setter
    def gifted(self, gifted):
        """Sets the gifted of this Datum6.


        :param gifted: The gifted of this Datum6.  # noqa: E501
        :type: bool
        """

        self._gifted = gifted

    @property
    def id(self):
        """Gets the id of this Datum6.  # noqa: E501


        :return: The id of this Datum6.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Datum6.


        :param id: The id of this Datum6.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Datum6.  # noqa: E501


        :return: The name of this Datum6.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Datum6.


        :param name: The name of this Datum6.  # noqa: E501
        :type: object
        """

        self._name = name

    @property
    def on_grace_period(self):
        """Gets the on_grace_period of this Datum6.  # noqa: E501


        :return: The on_grace_period of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._on_grace_period

    @on_grace_period.setter
    def on_grace_period(self, on_grace_period):
        """Sets the on_grace_period of this Datum6.


        :param on_grace_period: The on_grace_period of this Datum6.  # noqa: E501
        :type: bool
        """

        self._on_grace_period = on_grace_period

    @property
    def on_trial(self):
        """Gets the on_trial of this Datum6.  # noqa: E501


        :return: The on_trial of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._on_trial

    @on_trial.setter
    def on_trial(self, on_trial):
        """Sets the on_trial of this Datum6.


        :param on_trial: The on_trial of this Datum6.  # noqa: E501
        :type: bool
        """

        self._on_trial = on_trial

    @property
    def product(self):
        """Gets the product of this Datum6.  # noqa: E501


        :return: The product of this Datum6.  # noqa: E501
        :rtype: Product
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this Datum6.


        :param product: The product of this Datum6.  # noqa: E501
        :type: Product
        """

        self._product = product

    @property
    def sponsored(self):
        """Gets the sponsored of this Datum6.  # noqa: E501


        :return: The sponsored of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._sponsored

    @sponsored.setter
    def sponsored(self, sponsored):
        """Sets the sponsored of this Datum6.


        :param sponsored: The sponsored of this Datum6.  # noqa: E501
        :type: bool
        """

        self._sponsored = sponsored

    @property
    def trial_ends_at(self):
        """Gets the trial_ends_at of this Datum6.  # noqa: E501


        :return: The trial_ends_at of this Datum6.  # noqa: E501
        :rtype: object
        """
        return self._trial_ends_at

    @trial_ends_at.setter
    def trial_ends_at(self, trial_ends_at):
        """Sets the trial_ends_at of this Datum6.


        :param trial_ends_at: The trial_ends_at of this Datum6.  # noqa: E501
        :type: object
        """

        self._trial_ends_at = trial_ends_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Datum6.  # noqa: E501


        :return: The updated_at of this Datum6.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Datum6.


        :param updated_at: The updated_at of this Datum6.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def valid(self):
        """Gets the valid of this Datum6.  # noqa: E501


        :return: The valid of this Datum6.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this Datum6.


        :param valid: The valid of this Datum6.  # noqa: E501
        :type: bool
        """

        self._valid = valid

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
        if issubclass(Datum6, dict):
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
        if not isinstance(other, Datum6):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

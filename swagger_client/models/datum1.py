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

class Datum1(object):
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
        'code': 'str',
        'flat_url': 'str',
        'localized_name': 'str',
        'name': 'str',
        'tax': 'int'
    }

    attribute_map = {
        'code': 'code',
        'flat_url': 'flat_url',
        'localized_name': 'localized_name',
        'name': 'name',
        'tax': 'tax'
    }

    def __init__(self, code=None, flat_url=None, localized_name=None, name=None, tax=None):  # noqa: E501
        """Datum1 - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._flat_url = None
        self._localized_name = None
        self._name = None
        self._tax = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if flat_url is not None:
            self.flat_url = flat_url
        if localized_name is not None:
            self.localized_name = localized_name
        if name is not None:
            self.name = name
        if tax is not None:
            self.tax = tax

    @property
    def code(self):
        """Gets the code of this Datum1.  # noqa: E501


        :return: The code of this Datum1.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this Datum1.


        :param code: The code of this Datum1.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def flat_url(self):
        """Gets the flat_url of this Datum1.  # noqa: E501


        :return: The flat_url of this Datum1.  # noqa: E501
        :rtype: str
        """
        return self._flat_url

    @flat_url.setter
    def flat_url(self, flat_url):
        """Sets the flat_url of this Datum1.


        :param flat_url: The flat_url of this Datum1.  # noqa: E501
        :type: str
        """

        self._flat_url = flat_url

    @property
    def localized_name(self):
        """Gets the localized_name of this Datum1.  # noqa: E501


        :return: The localized_name of this Datum1.  # noqa: E501
        :rtype: str
        """
        return self._localized_name

    @localized_name.setter
    def localized_name(self, localized_name):
        """Sets the localized_name of this Datum1.


        :param localized_name: The localized_name of this Datum1.  # noqa: E501
        :type: str
        """

        self._localized_name = localized_name

    @property
    def name(self):
        """Gets the name of this Datum1.  # noqa: E501


        :return: The name of this Datum1.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Datum1.


        :param name: The name of this Datum1.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def tax(self):
        """Gets the tax of this Datum1.  # noqa: E501


        :return: The tax of this Datum1.  # noqa: E501
        :rtype: int
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this Datum1.


        :param tax: The tax of this Datum1.  # noqa: E501
        :type: int
        """

        self._tax = tax

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
        if issubclass(Datum1, dict):
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
        if not isinstance(other, Datum1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

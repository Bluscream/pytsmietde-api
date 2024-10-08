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

class AtedAt(object):
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
        '_date': 'datetime',
        'timezone': 'str',
        'timezone_type': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'timezone': 'timezone',
        'timezone_type': 'timezone_type'
    }

    def __init__(self, _date=None, timezone=None, timezone_type=None):  # noqa: E501
        """AtedAt - a model defined in Swagger"""  # noqa: E501
        self.__date = None
        self._timezone = None
        self._timezone_type = None
        self.discriminator = None
        if _date is not None:
            self._date = _date
        if timezone is not None:
            self.timezone = timezone
        if timezone_type is not None:
            self.timezone_type = timezone_type

    @property
    def _date(self):
        """Gets the _date of this AtedAt.  # noqa: E501


        :return: The _date of this AtedAt.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this AtedAt.


        :param _date: The _date of this AtedAt.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def timezone(self):
        """Gets the timezone of this AtedAt.  # noqa: E501


        :return: The timezone of this AtedAt.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this AtedAt.


        :param timezone: The timezone of this AtedAt.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def timezone_type(self):
        """Gets the timezone_type of this AtedAt.  # noqa: E501


        :return: The timezone_type of this AtedAt.  # noqa: E501
        :rtype: int
        """
        return self._timezone_type

    @timezone_type.setter
    def timezone_type(self, timezone_type):
        """Sets the timezone_type of this AtedAt.


        :param timezone_type: The timezone_type of this AtedAt.  # noqa: E501
        :type: int
        """

        self._timezone_type = timezone_type

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
        if issubclass(AtedAt, dict):
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
        if not isinstance(other, AtedAt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

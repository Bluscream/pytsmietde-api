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

class Options1(object):
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
        'max': 'int',
        'months': 'int'
    }

    attribute_map = {
        'max': 'max',
        'months': 'months'
    }

    def __init__(self, max=None, months=None):  # noqa: E501
        """Options1 - a model defined in Swagger"""  # noqa: E501
        self._max = None
        self._months = None
        self.discriminator = None
        if max is not None:
            self.max = max
        if months is not None:
            self.months = months

    @property
    def max(self):
        """Gets the max of this Options1.  # noqa: E501


        :return: The max of this Options1.  # noqa: E501
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this Options1.


        :param max: The max of this Options1.  # noqa: E501
        :type: int
        """

        self._max = max

    @property
    def months(self):
        """Gets the months of this Options1.  # noqa: E501


        :return: The months of this Options1.  # noqa: E501
        :rtype: int
        """
        return self._months

    @months.setter
    def months(self, months):
        """Sets the months of this Options1.


        :param months: The months of this Options1.  # noqa: E501
        :type: int
        """

        self._months = months

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
        if issubclass(Options1, dict):
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
        if not isinstance(other, Options1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

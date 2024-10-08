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

class Advertising(object):
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
        'nugg': 'bool',
        'played': 'bool',
        'tag': 'str',
        'time': 'int'
    }

    attribute_map = {
        'nugg': 'nugg',
        'played': 'played',
        'tag': 'tag',
        'time': 'time'
    }

    def __init__(self, nugg=None, played=None, tag=None, time=None):  # noqa: E501
        """Advertising - a model defined in Swagger"""  # noqa: E501
        self._nugg = None
        self._played = None
        self._tag = None
        self._time = None
        self.discriminator = None
        if nugg is not None:
            self.nugg = nugg
        if played is not None:
            self.played = played
        if tag is not None:
            self.tag = tag
        if time is not None:
            self.time = time

    @property
    def nugg(self):
        """Gets the nugg of this Advertising.  # noqa: E501


        :return: The nugg of this Advertising.  # noqa: E501
        :rtype: bool
        """
        return self._nugg

    @nugg.setter
    def nugg(self, nugg):
        """Sets the nugg of this Advertising.


        :param nugg: The nugg of this Advertising.  # noqa: E501
        :type: bool
        """

        self._nugg = nugg

    @property
    def played(self):
        """Gets the played of this Advertising.  # noqa: E501


        :return: The played of this Advertising.  # noqa: E501
        :rtype: bool
        """
        return self._played

    @played.setter
    def played(self, played):
        """Sets the played of this Advertising.


        :param played: The played of this Advertising.  # noqa: E501
        :type: bool
        """

        self._played = played

    @property
    def tag(self):
        """Gets the tag of this Advertising.  # noqa: E501


        :return: The tag of this Advertising.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this Advertising.


        :param tag: The tag of this Advertising.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def time(self):
        """Gets the time of this Advertising.  # noqa: E501


        :return: The time of this Advertising.  # noqa: E501
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Advertising.


        :param time: The time of this Advertising.  # noqa: E501
        :type: int
        """

        self._time = time

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
        if issubclass(Advertising, dict):
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
        if not isinstance(other, Advertising):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

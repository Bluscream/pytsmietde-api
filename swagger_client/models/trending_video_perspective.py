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

class TrendingVideoPerspective(object):
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
        'id': 'int',
        'main': 'bool',
        'title': 'AnyOfTrendingVideoPerspectiveTitle',
        'title_pluralized': 'str'
    }

    attribute_map = {
        'id': 'id',
        'main': 'main',
        'title': 'title',
        'title_pluralized': 'title_pluralized'
    }

    def __init__(self, id=None, main=None, title=None, title_pluralized=None):  # noqa: E501
        """TrendingVideoPerspective - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._main = None
        self._title = None
        self._title_pluralized = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if main is not None:
            self.main = main
        if title is not None:
            self.title = title
        if title_pluralized is not None:
            self.title_pluralized = title_pluralized

    @property
    def id(self):
        """Gets the id of this TrendingVideoPerspective.  # noqa: E501


        :return: The id of this TrendingVideoPerspective.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TrendingVideoPerspective.


        :param id: The id of this TrendingVideoPerspective.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def main(self):
        """Gets the main of this TrendingVideoPerspective.  # noqa: E501


        :return: The main of this TrendingVideoPerspective.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this TrendingVideoPerspective.


        :param main: The main of this TrendingVideoPerspective.  # noqa: E501
        :type: bool
        """

        self._main = main

    @property
    def title(self):
        """Gets the title of this TrendingVideoPerspective.  # noqa: E501


        :return: The title of this TrendingVideoPerspective.  # noqa: E501
        :rtype: AnyOfTrendingVideoPerspectiveTitle
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TrendingVideoPerspective.


        :param title: The title of this TrendingVideoPerspective.  # noqa: E501
        :type: AnyOfTrendingVideoPerspectiveTitle
        """

        self._title = title

    @property
    def title_pluralized(self):
        """Gets the title_pluralized of this TrendingVideoPerspective.  # noqa: E501


        :return: The title_pluralized of this TrendingVideoPerspective.  # noqa: E501
        :rtype: str
        """
        return self._title_pluralized

    @title_pluralized.setter
    def title_pluralized(self, title_pluralized):
        """Sets the title_pluralized of this TrendingVideoPerspective.


        :param title_pluralized: The title_pluralized of this TrendingVideoPerspective.  # noqa: E501
        :type: str
        """

        self._title_pluralized = title_pluralized

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
        if issubclass(TrendingVideoPerspective, dict):
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
        if not isinstance(other, TrendingVideoPerspective):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

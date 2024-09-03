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

class Track(object):
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
        'full_title': 'str',
        'id': 'int',
        'main': 'bool',
        'pluralized_title': 'str',
        'qualities': 'list[Quality]',
        'sources': 'Sources',
        'title': 'object'
    }

    attribute_map = {
        'full_title': 'full_title',
        'id': 'id',
        'main': 'main',
        'pluralized_title': 'pluralized_title',
        'qualities': 'qualities',
        'sources': 'sources',
        'title': 'title'
    }

    def __init__(self, full_title=None, id=None, main=None, pluralized_title=None, qualities=None, sources=None, title=None):  # noqa: E501
        """Track - a model defined in Swagger"""  # noqa: E501
        self._full_title = None
        self._id = None
        self._main = None
        self._pluralized_title = None
        self._qualities = None
        self._sources = None
        self._title = None
        self.discriminator = None
        if full_title is not None:
            self.full_title = full_title
        if id is not None:
            self.id = id
        if main is not None:
            self.main = main
        if pluralized_title is not None:
            self.pluralized_title = pluralized_title
        if qualities is not None:
            self.qualities = qualities
        if sources is not None:
            self.sources = sources
        if title is not None:
            self.title = title

    @property
    def full_title(self):
        """Gets the full_title of this Track.  # noqa: E501


        :return: The full_title of this Track.  # noqa: E501
        :rtype: str
        """
        return self._full_title

    @full_title.setter
    def full_title(self, full_title):
        """Sets the full_title of this Track.


        :param full_title: The full_title of this Track.  # noqa: E501
        :type: str
        """

        self._full_title = full_title

    @property
    def id(self):
        """Gets the id of this Track.  # noqa: E501


        :return: The id of this Track.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Track.


        :param id: The id of this Track.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def main(self):
        """Gets the main of this Track.  # noqa: E501


        :return: The main of this Track.  # noqa: E501
        :rtype: bool
        """
        return self._main

    @main.setter
    def main(self, main):
        """Sets the main of this Track.


        :param main: The main of this Track.  # noqa: E501
        :type: bool
        """

        self._main = main

    @property
    def pluralized_title(self):
        """Gets the pluralized_title of this Track.  # noqa: E501


        :return: The pluralized_title of this Track.  # noqa: E501
        :rtype: str
        """
        return self._pluralized_title

    @pluralized_title.setter
    def pluralized_title(self, pluralized_title):
        """Sets the pluralized_title of this Track.


        :param pluralized_title: The pluralized_title of this Track.  # noqa: E501
        :type: str
        """

        self._pluralized_title = pluralized_title

    @property
    def qualities(self):
        """Gets the qualities of this Track.  # noqa: E501


        :return: The qualities of this Track.  # noqa: E501
        :rtype: list[Quality]
        """
        return self._qualities

    @qualities.setter
    def qualities(self, qualities):
        """Sets the qualities of this Track.


        :param qualities: The qualities of this Track.  # noqa: E501
        :type: list[Quality]
        """

        self._qualities = qualities

    @property
    def sources(self):
        """Gets the sources of this Track.  # noqa: E501


        :return: The sources of this Track.  # noqa: E501
        :rtype: Sources
        """
        return self._sources

    @sources.setter
    def sources(self, sources):
        """Sets the sources of this Track.


        :param sources: The sources of this Track.  # noqa: E501
        :type: Sources
        """

        self._sources = sources

    @property
    def title(self):
        """Gets the title of this Track.  # noqa: E501


        :return: The title of this Track.  # noqa: E501
        :rtype: object
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Track.


        :param title: The title of this Track.  # noqa: E501
        :type: object
        """

        self._title = title

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
        if issubclass(Track, dict):
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
        if not isinstance(other, Track):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

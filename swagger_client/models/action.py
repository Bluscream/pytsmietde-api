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

class Action(object):
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
        'title': 'str',
        'url': 'str'
    }

    attribute_map = {
        'title': 'title',
        'url': 'url'
    }

    def __init__(self, title=None, url=None):  # noqa: E501
        """Action - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._url = None
        self.discriminator = None
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url

    @property
    def title(self):
        """Gets the title of this Action.  # noqa: E501


        :return: The title of this Action.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Action.


        :param title: The title of this Action.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this Action.  # noqa: E501


        :return: The url of this Action.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Action.


        :param url: The url of this Action.  # noqa: E501
        :type: str
        """

        self._url = url

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
        if issubclass(Action, dict):
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
        if not isinstance(other, Action):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

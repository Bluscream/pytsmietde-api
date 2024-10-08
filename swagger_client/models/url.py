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

class URL(object):
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
        'href': 'str',
        'replace': 'str',
        'search': 'str'
    }

    attribute_map = {
        'href': 'href',
        'replace': 'replace',
        'search': 'search'
    }

    def __init__(self, href=None, replace=None, search=None):  # noqa: E501
        """URL - a model defined in Swagger"""  # noqa: E501
        self._href = None
        self._replace = None
        self._search = None
        self.discriminator = None
        if href is not None:
            self.href = href
        if replace is not None:
            self.replace = replace
        if search is not None:
            self.search = search

    @property
    def href(self):
        """Gets the href of this URL.  # noqa: E501


        :return: The href of this URL.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this URL.


        :param href: The href of this URL.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def replace(self):
        """Gets the replace of this URL.  # noqa: E501


        :return: The replace of this URL.  # noqa: E501
        :rtype: str
        """
        return self._replace

    @replace.setter
    def replace(self, replace):
        """Sets the replace of this URL.


        :param replace: The replace of this URL.  # noqa: E501
        :type: str
        """

        self._replace = replace

    @property
    def search(self):
        """Gets the search of this URL.  # noqa: E501


        :return: The search of this URL.  # noqa: E501
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        """Sets the search of this URL.


        :param search: The search of this URL.  # noqa: E501
        :type: str
        """

        self._search = search

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
        if issubclass(URL, dict):
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
        if not isinstance(other, URL):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

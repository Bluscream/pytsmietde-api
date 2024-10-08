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

class Meta(object):
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
        'current_page': 'int',
        '_from': 'int',
        'last_page': 'int',
        'links': 'list[Link]',
        'path': 'str',
        'per_page': 'int',
        'to': 'int',
        'total': 'int'
    }

    attribute_map = {
        'current_page': 'current_page',
        '_from': 'from',
        'last_page': 'last_page',
        'links': 'links',
        'path': 'path',
        'per_page': 'per_page',
        'to': 'to',
        'total': 'total'
    }

    def __init__(self, current_page=None, _from=None, last_page=None, links=None, path=None, per_page=None, to=None, total=None):  # noqa: E501
        """Meta - a model defined in Swagger"""  # noqa: E501
        self._current_page = None
        self.__from = None
        self._last_page = None
        self._links = None
        self._path = None
        self._per_page = None
        self._to = None
        self._total = None
        self.discriminator = None
        if current_page is not None:
            self.current_page = current_page
        if _from is not None:
            self._from = _from
        if last_page is not None:
            self.last_page = last_page
        if links is not None:
            self.links = links
        if path is not None:
            self.path = path
        if per_page is not None:
            self.per_page = per_page
        if to is not None:
            self.to = to
        if total is not None:
            self.total = total

    @property
    def current_page(self):
        """Gets the current_page of this Meta.  # noqa: E501


        :return: The current_page of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this Meta.


        :param current_page: The current_page of this Meta.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def _from(self):
        """Gets the _from of this Meta.  # noqa: E501


        :return: The _from of this Meta.  # noqa: E501
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Meta.


        :param _from: The _from of this Meta.  # noqa: E501
        :type: int
        """

        self.__from = _from

    @property
    def last_page(self):
        """Gets the last_page of this Meta.  # noqa: E501


        :return: The last_page of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._last_page

    @last_page.setter
    def last_page(self, last_page):
        """Sets the last_page of this Meta.


        :param last_page: The last_page of this Meta.  # noqa: E501
        :type: int
        """

        self._last_page = last_page

    @property
    def links(self):
        """Gets the links of this Meta.  # noqa: E501


        :return: The links of this Meta.  # noqa: E501
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Meta.


        :param links: The links of this Meta.  # noqa: E501
        :type: list[Link]
        """

        self._links = links

    @property
    def path(self):
        """Gets the path of this Meta.  # noqa: E501


        :return: The path of this Meta.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this Meta.


        :param path: The path of this Meta.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def per_page(self):
        """Gets the per_page of this Meta.  # noqa: E501


        :return: The per_page of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        """Sets the per_page of this Meta.


        :param per_page: The per_page of this Meta.  # noqa: E501
        :type: int
        """

        self._per_page = per_page

    @property
    def to(self):
        """Gets the to of this Meta.  # noqa: E501


        :return: The to of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Meta.


        :param to: The to of this Meta.  # noqa: E501
        :type: int
        """

        self._to = to

    @property
    def total(self):
        """Gets the total of this Meta.  # noqa: E501


        :return: The total of this Meta.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Meta.


        :param total: The total of this Meta.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(Meta, dict):
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
        if not isinstance(other, Meta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

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

class UsersIDViewsGetRequest(object):
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
        'data': 'list[Datum17]',
        'links': 'Links',
        'meta': 'Meta',
        'success': 'bool'
    }

    attribute_map = {
        'data': 'data',
        'links': 'links',
        'meta': 'meta',
        'success': 'success'
    }

    def __init__(self, data=None, links=None, meta=None, success=None):  # noqa: E501
        """UsersIDViewsGetRequest - a model defined in Swagger"""  # noqa: E501
        self._data = None
        self._links = None
        self._meta = None
        self._success = None
        self.discriminator = None
        if data is not None:
            self.data = data
        if links is not None:
            self.links = links
        if meta is not None:
            self.meta = meta
        if success is not None:
            self.success = success

    @property
    def data(self):
        """Gets the data of this UsersIDViewsGetRequest.  # noqa: E501


        :return: The data of this UsersIDViewsGetRequest.  # noqa: E501
        :rtype: list[Datum17]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UsersIDViewsGetRequest.


        :param data: The data of this UsersIDViewsGetRequest.  # noqa: E501
        :type: list[Datum17]
        """

        self._data = data

    @property
    def links(self):
        """Gets the links of this UsersIDViewsGetRequest.  # noqa: E501


        :return: The links of this UsersIDViewsGetRequest.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this UsersIDViewsGetRequest.


        :param links: The links of this UsersIDViewsGetRequest.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def meta(self):
        """Gets the meta of this UsersIDViewsGetRequest.  # noqa: E501


        :return: The meta of this UsersIDViewsGetRequest.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this UsersIDViewsGetRequest.


        :param meta: The meta of this UsersIDViewsGetRequest.  # noqa: E501
        :type: Meta
        """

        self._meta = meta

    @property
    def success(self):
        """Gets the success of this UsersIDViewsGetRequest.  # noqa: E501


        :return: The success of this UsersIDViewsGetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UsersIDViewsGetRequest.


        :param success: The success of this UsersIDViewsGetRequest.  # noqa: E501
        :type: bool
        """

        self._success = success

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
        if issubclass(UsersIDViewsGetRequest, dict):
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
        if not isinstance(other, UsersIDViewsGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

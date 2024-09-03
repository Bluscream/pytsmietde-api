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

class Datum4(object):
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
        'created_at': 'datetime',
        'extra': 'list[object]',
        'icon': 'str',
        'id': 'int',
        'title': 'str',
        'type': 'int',
        'updated_at': 'datetime',
        'user_id': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'extra': 'extra',
        'icon': 'icon',
        'id': 'id',
        'title': 'title',
        'type': 'type',
        'updated_at': 'updated_at',
        'user_id': 'user_id'
    }

    def __init__(self, created_at=None, extra=None, icon=None, id=None, title=None, type=None, updated_at=None, user_id=None):  # noqa: E501
        """Datum4 - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._extra = None
        self._icon = None
        self._id = None
        self._title = None
        self._type = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if extra is not None:
            self.extra = extra
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this Datum4.  # noqa: E501


        :return: The created_at of this Datum4.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Datum4.


        :param created_at: The created_at of this Datum4.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def extra(self):
        """Gets the extra of this Datum4.  # noqa: E501


        :return: The extra of this Datum4.  # noqa: E501
        :rtype: list[object]
        """
        return self._extra

    @extra.setter
    def extra(self, extra):
        """Sets the extra of this Datum4.


        :param extra: The extra of this Datum4.  # noqa: E501
        :type: list[object]
        """

        self._extra = extra

    @property
    def icon(self):
        """Gets the icon of this Datum4.  # noqa: E501


        :return: The icon of this Datum4.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this Datum4.


        :param icon: The icon of this Datum4.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this Datum4.  # noqa: E501


        :return: The id of this Datum4.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Datum4.


        :param id: The id of this Datum4.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Datum4.  # noqa: E501


        :return: The title of this Datum4.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Datum4.


        :param title: The title of this Datum4.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def type(self):
        """Gets the type of this Datum4.  # noqa: E501


        :return: The type of this Datum4.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Datum4.


        :param type: The type of this Datum4.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def updated_at(self):
        """Gets the updated_at of this Datum4.  # noqa: E501


        :return: The updated_at of this Datum4.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Datum4.


        :param updated_at: The updated_at of this Datum4.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this Datum4.  # noqa: E501


        :return: The user_id of this Datum4.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Datum4.


        :param user_id: The user_id of this Datum4.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(Datum4, dict):
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
        if not isinstance(other, Datum4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

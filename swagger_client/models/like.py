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

class Like(object):
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
        'id': 'int',
        'subject_id': 'int',
        'subject_type': 'str',
        'updated_at': 'datetime',
        'user_id': 'int'
    }

    attribute_map = {
        'created_at': 'created_at',
        'id': 'id',
        'subject_id': 'subject_id',
        'subject_type': 'subject_type',
        'updated_at': 'updated_at',
        'user_id': 'user_id'
    }

    def __init__(self, created_at=None, id=None, subject_id=None, subject_type=None, updated_at=None, user_id=None):  # noqa: E501
        """Like - a model defined in Swagger"""  # noqa: E501
        self._created_at = None
        self._id = None
        self._subject_id = None
        self._subject_type = None
        self._updated_at = None
        self._user_id = None
        self.discriminator = None
        if created_at is not None:
            self.created_at = created_at
        if id is not None:
            self.id = id
        if subject_id is not None:
            self.subject_id = subject_id
        if subject_type is not None:
            self.subject_type = subject_type
        if updated_at is not None:
            self.updated_at = updated_at
        if user_id is not None:
            self.user_id = user_id

    @property
    def created_at(self):
        """Gets the created_at of this Like.  # noqa: E501


        :return: The created_at of this Like.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Like.


        :param created_at: The created_at of this Like.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this Like.  # noqa: E501


        :return: The id of this Like.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Like.


        :param id: The id of this Like.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def subject_id(self):
        """Gets the subject_id of this Like.  # noqa: E501


        :return: The subject_id of this Like.  # noqa: E501
        :rtype: int
        """
        return self._subject_id

    @subject_id.setter
    def subject_id(self, subject_id):
        """Sets the subject_id of this Like.


        :param subject_id: The subject_id of this Like.  # noqa: E501
        :type: int
        """

        self._subject_id = subject_id

    @property
    def subject_type(self):
        """Gets the subject_type of this Like.  # noqa: E501


        :return: The subject_type of this Like.  # noqa: E501
        :rtype: str
        """
        return self._subject_type

    @subject_type.setter
    def subject_type(self, subject_type):
        """Sets the subject_type of this Like.


        :param subject_type: The subject_type of this Like.  # noqa: E501
        :type: str
        """

        self._subject_type = subject_type

    @property
    def updated_at(self):
        """Gets the updated_at of this Like.  # noqa: E501


        :return: The updated_at of this Like.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Like.


        :param updated_at: The updated_at of this Like.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def user_id(self):
        """Gets the user_id of this Like.  # noqa: E501


        :return: The user_id of this Like.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Like.


        :param user_id: The user_id of this Like.  # noqa: E501
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
        if issubclass(Like, dict):
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
        if not isinstance(other, Like):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

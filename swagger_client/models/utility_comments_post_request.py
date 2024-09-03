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

class UtilityCommentsPostRequest(object):
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
        'reply': 'int',
        'text': 'str',
        'timestamp': 'float',
        'type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'reply': 'reply',
        'text': 'text',
        'timestamp': 'timestamp',
        'type': 'type'
    }

    def __init__(self, id=None, reply=None, text=None, timestamp=None, type=None):  # noqa: E501
        """UtilityCommentsPostRequest - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._reply = None
        self._text = None
        self._timestamp = None
        self._type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if reply is not None:
            self.reply = reply
        if text is not None:
            self.text = text
        if timestamp is not None:
            self.timestamp = timestamp
        if type is not None:
            self.type = type

    @property
    def id(self):
        """Gets the id of this UtilityCommentsPostRequest.  # noqa: E501


        :return: The id of this UtilityCommentsPostRequest.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UtilityCommentsPostRequest.


        :param id: The id of this UtilityCommentsPostRequest.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def reply(self):
        """Gets the reply of this UtilityCommentsPostRequest.  # noqa: E501


        :return: The reply of this UtilityCommentsPostRequest.  # noqa: E501
        :rtype: int
        """
        return self._reply

    @reply.setter
    def reply(self, reply):
        """Sets the reply of this UtilityCommentsPostRequest.


        :param reply: The reply of this UtilityCommentsPostRequest.  # noqa: E501
        :type: int
        """

        self._reply = reply

    @property
    def text(self):
        """Gets the text of this UtilityCommentsPostRequest.  # noqa: E501


        :return: The text of this UtilityCommentsPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this UtilityCommentsPostRequest.


        :param text: The text of this UtilityCommentsPostRequest.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def timestamp(self):
        """Gets the timestamp of this UtilityCommentsPostRequest.  # noqa: E501


        :return: The timestamp of this UtilityCommentsPostRequest.  # noqa: E501
        :rtype: float
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UtilityCommentsPostRequest.


        :param timestamp: The timestamp of this UtilityCommentsPostRequest.  # noqa: E501
        :type: float
        """

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this UtilityCommentsPostRequest.  # noqa: E501


        :return: The type of this UtilityCommentsPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UtilityCommentsPostRequest.


        :param type: The type of this UtilityCommentsPostRequest.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(UtilityCommentsPostRequest, dict):
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
        if not isinstance(other, UtilityCommentsPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

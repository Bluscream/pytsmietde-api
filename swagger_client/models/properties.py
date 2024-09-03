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

class Properties(object):
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
        '_from': 'ModelFrom',
        'id': 'int',
        'timestamp': 'int',
        'to': 'To',
        'type': 'str',
        'video': 'int'
    }

    attribute_map = {
        '_from': 'from',
        'id': 'id',
        'timestamp': 'timestamp',
        'to': 'to',
        'type': 'type',
        'video': 'video'
    }

    def __init__(self, _from=None, id=None, timestamp=None, to=None, type=None, video=None):  # noqa: E501
        """Properties - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._id = None
        self._timestamp = None
        self._to = None
        self._type = None
        self._video = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if id is not None:
            self.id = id
        if timestamp is not None:
            self.timestamp = timestamp
        if to is not None:
            self.to = to
        if type is not None:
            self.type = type
        if video is not None:
            self.video = video

    @property
    def _from(self):
        """Gets the _from of this Properties.  # noqa: E501


        :return: The _from of this Properties.  # noqa: E501
        :rtype: ModelFrom
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this Properties.


        :param _from: The _from of this Properties.  # noqa: E501
        :type: ModelFrom
        """

        self.__from = _from

    @property
    def id(self):
        """Gets the id of this Properties.  # noqa: E501


        :return: The id of this Properties.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Properties.


        :param id: The id of this Properties.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def timestamp(self):
        """Gets the timestamp of this Properties.  # noqa: E501


        :return: The timestamp of this Properties.  # noqa: E501
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Properties.


        :param timestamp: The timestamp of this Properties.  # noqa: E501
        :type: int
        """

        self._timestamp = timestamp

    @property
    def to(self):
        """Gets the to of this Properties.  # noqa: E501


        :return: The to of this Properties.  # noqa: E501
        :rtype: To
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this Properties.


        :param to: The to of this Properties.  # noqa: E501
        :type: To
        """

        self._to = to

    @property
    def type(self):
        """Gets the type of this Properties.  # noqa: E501


        :return: The type of this Properties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Properties.


        :param type: The type of this Properties.  # noqa: E501
        :type: str
        """
        allowed_values = ["video", "podcastEpisode", "newsArticle", "videoPlaylist"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def video(self):
        """Gets the video of this Properties.  # noqa: E501


        :return: The video of this Properties.  # noqa: E501
        :rtype: int
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this Properties.


        :param video: The video of this Properties.  # noqa: E501
        :type: int
        """

        self._video = video

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
        if issubclass(Properties, dict):
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
        if not isinstance(other, Properties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

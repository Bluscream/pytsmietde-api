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

class PodcastEpisodesIDGetRequest(object):
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
        'episode': 'Episode',
        'success': 'bool'
    }

    attribute_map = {
        'episode': 'episode',
        'success': 'success'
    }

    def __init__(self, episode=None, success=None):  # noqa: E501
        """PodcastEpisodesIDGetRequest - a model defined in Swagger"""  # noqa: E501
        self._episode = None
        self._success = None
        self.discriminator = None
        if episode is not None:
            self.episode = episode
        if success is not None:
            self.success = success

    @property
    def episode(self):
        """Gets the episode of this PodcastEpisodesIDGetRequest.  # noqa: E501


        :return: The episode of this PodcastEpisodesIDGetRequest.  # noqa: E501
        :rtype: Episode
        """
        return self._episode

    @episode.setter
    def episode(self, episode):
        """Sets the episode of this PodcastEpisodesIDGetRequest.


        :param episode: The episode of this PodcastEpisodesIDGetRequest.  # noqa: E501
        :type: Episode
        """

        self._episode = episode

    @property
    def success(self):
        """Gets the success of this PodcastEpisodesIDGetRequest.  # noqa: E501


        :return: The success of this PodcastEpisodesIDGetRequest.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this PodcastEpisodesIDGetRequest.


        :param success: The success of this PodcastEpisodesIDGetRequest.  # noqa: E501
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
        if issubclass(PodcastEpisodesIDGetRequest, dict):
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
        if not isinstance(other, PodcastEpisodesIDGetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

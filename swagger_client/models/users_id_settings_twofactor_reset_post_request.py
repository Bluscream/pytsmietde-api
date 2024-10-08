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

class UsersIDSettingsTwofactorResetPostRequest(object):
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
        'otp': 'str'
    }

    attribute_map = {
        'otp': 'otp'
    }

    def __init__(self, otp=None):  # noqa: E501
        """UsersIDSettingsTwofactorResetPostRequest - a model defined in Swagger"""  # noqa: E501
        self._otp = None
        self.discriminator = None
        if otp is not None:
            self.otp = otp

    @property
    def otp(self):
        """Gets the otp of this UsersIDSettingsTwofactorResetPostRequest.  # noqa: E501


        :return: The otp of this UsersIDSettingsTwofactorResetPostRequest.  # noqa: E501
        :rtype: str
        """
        return self._otp

    @otp.setter
    def otp(self, otp):
        """Sets the otp of this UsersIDSettingsTwofactorResetPostRequest.


        :param otp: The otp of this UsersIDSettingsTwofactorResetPostRequest.  # noqa: E501
        :type: str
        """

        self._otp = otp

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
        if issubclass(UsersIDSettingsTwofactorResetPostRequest, dict):
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
        if not isinstance(other, UsersIDSettingsTwofactorResetPostRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

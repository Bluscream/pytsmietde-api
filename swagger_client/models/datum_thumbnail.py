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

class DatumThumbnail(object):
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
        'collection': 'str',
        'id': 'int',
        'remote_url': 'object',
        'variations': 'list[Variation]'
    }

    attribute_map = {
        'collection': 'collection',
        'id': 'id',
        'remote_url': 'remote_url',
        'variations': 'variations'
    }

    def __init__(self, collection=None, id=None, remote_url=None, variations=None):  # noqa: E501
        """DatumThumbnail - a model defined in Swagger"""  # noqa: E501
        self._collection = None
        self._id = None
        self._remote_url = None
        self._variations = None
        self.discriminator = None
        if collection is not None:
            self.collection = collection
        if id is not None:
            self.id = id
        if remote_url is not None:
            self.remote_url = remote_url
        if variations is not None:
            self.variations = variations

    @property
    def collection(self):
        """Gets the collection of this DatumThumbnail.  # noqa: E501


        :return: The collection of this DatumThumbnail.  # noqa: E501
        :rtype: str
        """
        return self._collection

    @collection.setter
    def collection(self, collection):
        """Sets the collection of this DatumThumbnail.


        :param collection: The collection of this DatumThumbnail.  # noqa: E501
        :type: str
        """
        allowed_values = ["thumbnail"]  # noqa: E501
        if collection not in allowed_values:
            raise ValueError(
                "Invalid value for `collection` ({0}), must be one of {1}"  # noqa: E501
                .format(collection, allowed_values)
            )

        self._collection = collection

    @property
    def id(self):
        """Gets the id of this DatumThumbnail.  # noqa: E501


        :return: The id of this DatumThumbnail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatumThumbnail.


        :param id: The id of this DatumThumbnail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def remote_url(self):
        """Gets the remote_url of this DatumThumbnail.  # noqa: E501


        :return: The remote_url of this DatumThumbnail.  # noqa: E501
        :rtype: object
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        """Sets the remote_url of this DatumThumbnail.


        :param remote_url: The remote_url of this DatumThumbnail.  # noqa: E501
        :type: object
        """

        self._remote_url = remote_url

    @property
    def variations(self):
        """Gets the variations of this DatumThumbnail.  # noqa: E501


        :return: The variations of this DatumThumbnail.  # noqa: E501
        :rtype: list[Variation]
        """
        return self._variations

    @variations.setter
    def variations(self, variations):
        """Sets the variations of this DatumThumbnail.


        :param variations: The variations of this DatumThumbnail.  # noqa: E501
        :type: list[Variation]
        """

        self._variations = variations

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
        if issubclass(DatumThumbnail, dict):
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
        if not isinstance(other, DatumThumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

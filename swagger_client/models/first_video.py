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

class FirstVideo(object):
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
        'comments_count': 'object',
        'description': 'object',
        'featured': 'bool',
        'id': 'int',
        'likes_count': 'object',
        'preferences': 'LatestArticlePreferences',
        'publish_date': 'datetime',
        'remote': 'bool',
        'remote_url': 'object',
        'short_url': 'str',
        'slug': 'str',
        'thumbnail': 'FirstVideoThumbnail',
        'title': 'str',
        'url': 'str',
        'url_slug': 'str'
    }

    attribute_map = {
        'comments_count': 'comments_count',
        'description': 'description',
        'featured': 'featured',
        'id': 'id',
        'likes_count': 'likes_count',
        'preferences': 'preferences',
        'publish_date': 'publish_date',
        'remote': 'remote',
        'remote_url': 'remote_url',
        'short_url': 'short_url',
        'slug': 'slug',
        'thumbnail': 'thumbnail',
        'title': 'title',
        'url': 'url',
        'url_slug': 'url_slug'
    }

    def __init__(self, comments_count=None, description=None, featured=None, id=None, likes_count=None, preferences=None, publish_date=None, remote=None, remote_url=None, short_url=None, slug=None, thumbnail=None, title=None, url=None, url_slug=None):  # noqa: E501
        """FirstVideo - a model defined in Swagger"""  # noqa: E501
        self._comments_count = None
        self._description = None
        self._featured = None
        self._id = None
        self._likes_count = None
        self._preferences = None
        self._publish_date = None
        self._remote = None
        self._remote_url = None
        self._short_url = None
        self._slug = None
        self._thumbnail = None
        self._title = None
        self._url = None
        self._url_slug = None
        self.discriminator = None
        if comments_count is not None:
            self.comments_count = comments_count
        if description is not None:
            self.description = description
        if featured is not None:
            self.featured = featured
        if id is not None:
            self.id = id
        if likes_count is not None:
            self.likes_count = likes_count
        if preferences is not None:
            self.preferences = preferences
        if publish_date is not None:
            self.publish_date = publish_date
        if remote is not None:
            self.remote = remote
        if remote_url is not None:
            self.remote_url = remote_url
        if short_url is not None:
            self.short_url = short_url
        if slug is not None:
            self.slug = slug
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if url_slug is not None:
            self.url_slug = url_slug

    @property
    def comments_count(self):
        """Gets the comments_count of this FirstVideo.  # noqa: E501


        :return: The comments_count of this FirstVideo.  # noqa: E501
        :rtype: object
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this FirstVideo.


        :param comments_count: The comments_count of this FirstVideo.  # noqa: E501
        :type: object
        """

        self._comments_count = comments_count

    @property
    def description(self):
        """Gets the description of this FirstVideo.  # noqa: E501


        :return: The description of this FirstVideo.  # noqa: E501
        :rtype: object
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FirstVideo.


        :param description: The description of this FirstVideo.  # noqa: E501
        :type: object
        """

        self._description = description

    @property
    def featured(self):
        """Gets the featured of this FirstVideo.  # noqa: E501


        :return: The featured of this FirstVideo.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this FirstVideo.


        :param featured: The featured of this FirstVideo.  # noqa: E501
        :type: bool
        """

        self._featured = featured

    @property
    def id(self):
        """Gets the id of this FirstVideo.  # noqa: E501


        :return: The id of this FirstVideo.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FirstVideo.


        :param id: The id of this FirstVideo.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def likes_count(self):
        """Gets the likes_count of this FirstVideo.  # noqa: E501


        :return: The likes_count of this FirstVideo.  # noqa: E501
        :rtype: object
        """
        return self._likes_count

    @likes_count.setter
    def likes_count(self, likes_count):
        """Sets the likes_count of this FirstVideo.


        :param likes_count: The likes_count of this FirstVideo.  # noqa: E501
        :type: object
        """

        self._likes_count = likes_count

    @property
    def preferences(self):
        """Gets the preferences of this FirstVideo.  # noqa: E501


        :return: The preferences of this FirstVideo.  # noqa: E501
        :rtype: LatestArticlePreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this FirstVideo.


        :param preferences: The preferences of this FirstVideo.  # noqa: E501
        :type: LatestArticlePreferences
        """

        self._preferences = preferences

    @property
    def publish_date(self):
        """Gets the publish_date of this FirstVideo.  # noqa: E501


        :return: The publish_date of this FirstVideo.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """Sets the publish_date of this FirstVideo.


        :param publish_date: The publish_date of this FirstVideo.  # noqa: E501
        :type: datetime
        """

        self._publish_date = publish_date

    @property
    def remote(self):
        """Gets the remote of this FirstVideo.  # noqa: E501


        :return: The remote of this FirstVideo.  # noqa: E501
        :rtype: bool
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this FirstVideo.


        :param remote: The remote of this FirstVideo.  # noqa: E501
        :type: bool
        """

        self._remote = remote

    @property
    def remote_url(self):
        """Gets the remote_url of this FirstVideo.  # noqa: E501


        :return: The remote_url of this FirstVideo.  # noqa: E501
        :rtype: object
        """
        return self._remote_url

    @remote_url.setter
    def remote_url(self, remote_url):
        """Sets the remote_url of this FirstVideo.


        :param remote_url: The remote_url of this FirstVideo.  # noqa: E501
        :type: object
        """

        self._remote_url = remote_url

    @property
    def short_url(self):
        """Gets the short_url of this FirstVideo.  # noqa: E501


        :return: The short_url of this FirstVideo.  # noqa: E501
        :rtype: str
        """
        return self._short_url

    @short_url.setter
    def short_url(self, short_url):
        """Sets the short_url of this FirstVideo.


        :param short_url: The short_url of this FirstVideo.  # noqa: E501
        :type: str
        """

        self._short_url = short_url

    @property
    def slug(self):
        """Gets the slug of this FirstVideo.  # noqa: E501


        :return: The slug of this FirstVideo.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this FirstVideo.


        :param slug: The slug of this FirstVideo.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def thumbnail(self):
        """Gets the thumbnail of this FirstVideo.  # noqa: E501


        :return: The thumbnail of this FirstVideo.  # noqa: E501
        :rtype: FirstVideoThumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this FirstVideo.


        :param thumbnail: The thumbnail of this FirstVideo.  # noqa: E501
        :type: FirstVideoThumbnail
        """

        self._thumbnail = thumbnail

    @property
    def title(self):
        """Gets the title of this FirstVideo.  # noqa: E501


        :return: The title of this FirstVideo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this FirstVideo.


        :param title: The title of this FirstVideo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this FirstVideo.  # noqa: E501


        :return: The url of this FirstVideo.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this FirstVideo.


        :param url: The url of this FirstVideo.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def url_slug(self):
        """Gets the url_slug of this FirstVideo.  # noqa: E501


        :return: The url_slug of this FirstVideo.  # noqa: E501
        :rtype: str
        """
        return self._url_slug

    @url_slug.setter
    def url_slug(self, url_slug):
        """Sets the url_slug of this FirstVideo.


        :param url_slug: The url_slug of this FirstVideo.  # noqa: E501
        :type: str
        """

        self._url_slug = url_slug

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
        if issubclass(FirstVideo, dict):
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
        if not isinstance(other, FirstVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

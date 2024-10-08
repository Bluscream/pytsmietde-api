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

class LatestArticle(object):
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
        'author': 'Author',
        'categories': 'list[Category]',
        'comments_count': 'object',
        'featured': 'bool',
        'id': 'int',
        'intro': 'str',
        'preferences': 'LatestArticlePreferences',
        'publish_date': 'datetime',
        'slug': 'str',
        'text': 'object',
        'thumbnail': 'LatestArticleThumbnail',
        'title': 'str',
        'url': 'str',
        'url_slug': 'str'
    }

    attribute_map = {
        'author': 'author',
        'categories': 'categories',
        'comments_count': 'comments_count',
        'featured': 'featured',
        'id': 'id',
        'intro': 'intro',
        'preferences': 'preferences',
        'publish_date': 'publish_date',
        'slug': 'slug',
        'text': 'text',
        'thumbnail': 'thumbnail',
        'title': 'title',
        'url': 'url',
        'url_slug': 'url_slug'
    }

    def __init__(self, author=None, categories=None, comments_count=None, featured=None, id=None, intro=None, preferences=None, publish_date=None, slug=None, text=None, thumbnail=None, title=None, url=None, url_slug=None):  # noqa: E501
        """LatestArticle - a model defined in Swagger"""  # noqa: E501
        self._author = None
        self._categories = None
        self._comments_count = None
        self._featured = None
        self._id = None
        self._intro = None
        self._preferences = None
        self._publish_date = None
        self._slug = None
        self._text = None
        self._thumbnail = None
        self._title = None
        self._url = None
        self._url_slug = None
        self.discriminator = None
        if author is not None:
            self.author = author
        if categories is not None:
            self.categories = categories
        if comments_count is not None:
            self.comments_count = comments_count
        if featured is not None:
            self.featured = featured
        if id is not None:
            self.id = id
        if intro is not None:
            self.intro = intro
        if preferences is not None:
            self.preferences = preferences
        if publish_date is not None:
            self.publish_date = publish_date
        if slug is not None:
            self.slug = slug
        if text is not None:
            self.text = text
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if title is not None:
            self.title = title
        if url is not None:
            self.url = url
        if url_slug is not None:
            self.url_slug = url_slug

    @property
    def author(self):
        """Gets the author of this LatestArticle.  # noqa: E501


        :return: The author of this LatestArticle.  # noqa: E501
        :rtype: Author
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this LatestArticle.


        :param author: The author of this LatestArticle.  # noqa: E501
        :type: Author
        """

        self._author = author

    @property
    def categories(self):
        """Gets the categories of this LatestArticle.  # noqa: E501


        :return: The categories of this LatestArticle.  # noqa: E501
        :rtype: list[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this LatestArticle.


        :param categories: The categories of this LatestArticle.  # noqa: E501
        :type: list[Category]
        """

        self._categories = categories

    @property
    def comments_count(self):
        """Gets the comments_count of this LatestArticle.  # noqa: E501


        :return: The comments_count of this LatestArticle.  # noqa: E501
        :rtype: object
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this LatestArticle.


        :param comments_count: The comments_count of this LatestArticle.  # noqa: E501
        :type: object
        """

        self._comments_count = comments_count

    @property
    def featured(self):
        """Gets the featured of this LatestArticle.  # noqa: E501


        :return: The featured of this LatestArticle.  # noqa: E501
        :rtype: bool
        """
        return self._featured

    @featured.setter
    def featured(self, featured):
        """Sets the featured of this LatestArticle.


        :param featured: The featured of this LatestArticle.  # noqa: E501
        :type: bool
        """

        self._featured = featured

    @property
    def id(self):
        """Gets the id of this LatestArticle.  # noqa: E501


        :return: The id of this LatestArticle.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LatestArticle.


        :param id: The id of this LatestArticle.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def intro(self):
        """Gets the intro of this LatestArticle.  # noqa: E501


        :return: The intro of this LatestArticle.  # noqa: E501
        :rtype: str
        """
        return self._intro

    @intro.setter
    def intro(self, intro):
        """Sets the intro of this LatestArticle.


        :param intro: The intro of this LatestArticle.  # noqa: E501
        :type: str
        """

        self._intro = intro

    @property
    def preferences(self):
        """Gets the preferences of this LatestArticle.  # noqa: E501


        :return: The preferences of this LatestArticle.  # noqa: E501
        :rtype: LatestArticlePreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this LatestArticle.


        :param preferences: The preferences of this LatestArticle.  # noqa: E501
        :type: LatestArticlePreferences
        """

        self._preferences = preferences

    @property
    def publish_date(self):
        """Gets the publish_date of this LatestArticle.  # noqa: E501


        :return: The publish_date of this LatestArticle.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """Sets the publish_date of this LatestArticle.


        :param publish_date: The publish_date of this LatestArticle.  # noqa: E501
        :type: datetime
        """

        self._publish_date = publish_date

    @property
    def slug(self):
        """Gets the slug of this LatestArticle.  # noqa: E501


        :return: The slug of this LatestArticle.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this LatestArticle.


        :param slug: The slug of this LatestArticle.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def text(self):
        """Gets the text of this LatestArticle.  # noqa: E501


        :return: The text of this LatestArticle.  # noqa: E501
        :rtype: object
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this LatestArticle.


        :param text: The text of this LatestArticle.  # noqa: E501
        :type: object
        """

        self._text = text

    @property
    def thumbnail(self):
        """Gets the thumbnail of this LatestArticle.  # noqa: E501


        :return: The thumbnail of this LatestArticle.  # noqa: E501
        :rtype: LatestArticleThumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this LatestArticle.


        :param thumbnail: The thumbnail of this LatestArticle.  # noqa: E501
        :type: LatestArticleThumbnail
        """

        self._thumbnail = thumbnail

    @property
    def title(self):
        """Gets the title of this LatestArticle.  # noqa: E501


        :return: The title of this LatestArticle.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this LatestArticle.


        :param title: The title of this LatestArticle.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url(self):
        """Gets the url of this LatestArticle.  # noqa: E501


        :return: The url of this LatestArticle.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this LatestArticle.


        :param url: The url of this LatestArticle.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def url_slug(self):
        """Gets the url_slug of this LatestArticle.  # noqa: E501


        :return: The url_slug of this LatestArticle.  # noqa: E501
        :rtype: str
        """
        return self._url_slug

    @url_slug.setter
    def url_slug(self, url_slug):
        """Sets the url_slug of this LatestArticle.


        :param url_slug: The url_slug of this LatestArticle.  # noqa: E501
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
        if issubclass(LatestArticle, dict):
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
        if not isinstance(other, LatestArticle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

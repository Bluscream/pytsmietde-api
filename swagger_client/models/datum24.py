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

class Datum24(object):
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
        'category': 'OtherCategory',
        'comments_count': 'int',
        'description': 'str',
        'duration': 'int',
        'duration_pretty': 'object',
        'id': 'int',
        'meta_tags': 'object',
        'mime': 'str',
        'publish_date': 'datetime',
        'size': 'int',
        'slug': 'str',
        'source_url': 'str',
        'thumbnail': 'Thumbnail',
        'title': 'str',
        'url_slug': 'str'
    }

    attribute_map = {
        'category': 'category',
        'comments_count': 'comments_count',
        'description': 'description',
        'duration': 'duration',
        'duration_pretty': 'duration_pretty',
        'id': 'id',
        'meta_tags': 'meta_tags',
        'mime': 'mime',
        'publish_date': 'publish_date',
        'size': 'size',
        'slug': 'slug',
        'source_url': 'source_url',
        'thumbnail': 'thumbnail',
        'title': 'title',
        'url_slug': 'url_slug'
    }

    def __init__(self, category=None, comments_count=None, description=None, duration=None, duration_pretty=None, id=None, meta_tags=None, mime=None, publish_date=None, size=None, slug=None, source_url=None, thumbnail=None, title=None, url_slug=None):  # noqa: E501
        """Datum24 - a model defined in Swagger"""  # noqa: E501
        self._category = None
        self._comments_count = None
        self._description = None
        self._duration = None
        self._duration_pretty = None
        self._id = None
        self._meta_tags = None
        self._mime = None
        self._publish_date = None
        self._size = None
        self._slug = None
        self._source_url = None
        self._thumbnail = None
        self._title = None
        self._url_slug = None
        self.discriminator = None
        if category is not None:
            self.category = category
        if comments_count is not None:
            self.comments_count = comments_count
        if description is not None:
            self.description = description
        if duration is not None:
            self.duration = duration
        if duration_pretty is not None:
            self.duration_pretty = duration_pretty
        if id is not None:
            self.id = id
        if meta_tags is not None:
            self.meta_tags = meta_tags
        if mime is not None:
            self.mime = mime
        if publish_date is not None:
            self.publish_date = publish_date
        if size is not None:
            self.size = size
        if slug is not None:
            self.slug = slug
        if source_url is not None:
            self.source_url = source_url
        if thumbnail is not None:
            self.thumbnail = thumbnail
        if title is not None:
            self.title = title
        if url_slug is not None:
            self.url_slug = url_slug

    @property
    def category(self):
        """Gets the category of this Datum24.  # noqa: E501


        :return: The category of this Datum24.  # noqa: E501
        :rtype: OtherCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Datum24.


        :param category: The category of this Datum24.  # noqa: E501
        :type: OtherCategory
        """

        self._category = category

    @property
    def comments_count(self):
        """Gets the comments_count of this Datum24.  # noqa: E501


        :return: The comments_count of this Datum24.  # noqa: E501
        :rtype: int
        """
        return self._comments_count

    @comments_count.setter
    def comments_count(self, comments_count):
        """Sets the comments_count of this Datum24.


        :param comments_count: The comments_count of this Datum24.  # noqa: E501
        :type: int
        """

        self._comments_count = comments_count

    @property
    def description(self):
        """Gets the description of this Datum24.  # noqa: E501


        :return: The description of this Datum24.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Datum24.


        :param description: The description of this Datum24.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def duration(self):
        """Gets the duration of this Datum24.  # noqa: E501


        :return: The duration of this Datum24.  # noqa: E501
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Datum24.


        :param duration: The duration of this Datum24.  # noqa: E501
        :type: int
        """

        self._duration = duration

    @property
    def duration_pretty(self):
        """Gets the duration_pretty of this Datum24.  # noqa: E501


        :return: The duration_pretty of this Datum24.  # noqa: E501
        :rtype: object
        """
        return self._duration_pretty

    @duration_pretty.setter
    def duration_pretty(self, duration_pretty):
        """Sets the duration_pretty of this Datum24.


        :param duration_pretty: The duration_pretty of this Datum24.  # noqa: E501
        :type: object
        """

        self._duration_pretty = duration_pretty

    @property
    def id(self):
        """Gets the id of this Datum24.  # noqa: E501


        :return: The id of this Datum24.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Datum24.


        :param id: The id of this Datum24.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def meta_tags(self):
        """Gets the meta_tags of this Datum24.  # noqa: E501


        :return: The meta_tags of this Datum24.  # noqa: E501
        :rtype: object
        """
        return self._meta_tags

    @meta_tags.setter
    def meta_tags(self, meta_tags):
        """Sets the meta_tags of this Datum24.


        :param meta_tags: The meta_tags of this Datum24.  # noqa: E501
        :type: object
        """

        self._meta_tags = meta_tags

    @property
    def mime(self):
        """Gets the mime of this Datum24.  # noqa: E501


        :return: The mime of this Datum24.  # noqa: E501
        :rtype: str
        """
        return self._mime

    @mime.setter
    def mime(self, mime):
        """Sets the mime of this Datum24.


        :param mime: The mime of this Datum24.  # noqa: E501
        :type: str
        """

        self._mime = mime

    @property
    def publish_date(self):
        """Gets the publish_date of this Datum24.  # noqa: E501


        :return: The publish_date of this Datum24.  # noqa: E501
        :rtype: datetime
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """Sets the publish_date of this Datum24.


        :param publish_date: The publish_date of this Datum24.  # noqa: E501
        :type: datetime
        """

        self._publish_date = publish_date

    @property
    def size(self):
        """Gets the size of this Datum24.  # noqa: E501


        :return: The size of this Datum24.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Datum24.


        :param size: The size of this Datum24.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def slug(self):
        """Gets the slug of this Datum24.  # noqa: E501


        :return: The slug of this Datum24.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Datum24.


        :param slug: The slug of this Datum24.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def source_url(self):
        """Gets the source_url of this Datum24.  # noqa: E501


        :return: The source_url of this Datum24.  # noqa: E501
        :rtype: str
        """
        return self._source_url

    @source_url.setter
    def source_url(self, source_url):
        """Sets the source_url of this Datum24.


        :param source_url: The source_url of this Datum24.  # noqa: E501
        :type: str
        """

        self._source_url = source_url

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Datum24.  # noqa: E501


        :return: The thumbnail of this Datum24.  # noqa: E501
        :rtype: Thumbnail
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Datum24.


        :param thumbnail: The thumbnail of this Datum24.  # noqa: E501
        :type: Thumbnail
        """

        self._thumbnail = thumbnail

    @property
    def title(self):
        """Gets the title of this Datum24.  # noqa: E501


        :return: The title of this Datum24.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Datum24.


        :param title: The title of this Datum24.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def url_slug(self):
        """Gets the url_slug of this Datum24.  # noqa: E501


        :return: The url_slug of this Datum24.  # noqa: E501
        :rtype: str
        """
        return self._url_slug

    @url_slug.setter
    def url_slug(self, url_slug):
        """Sets the url_slug of this Datum24.


        :param url_slug: The url_slug of this Datum24.  # noqa: E501
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
        if issubclass(Datum24, dict):
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
        if not isinstance(other, Datum24):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

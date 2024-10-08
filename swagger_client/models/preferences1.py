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

class Preferences1(object):
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
        'comments_order_own_first': 'bool',
        'comments_order_popular': 'bool',
        'country': 'str',
        'enable_darkmode': 'bool',
        'enable_darkmode_schedule': 'bool',
        'enable_spoilers': 'bool',
        'public_profile': 'bool',
        'scroll_top_route_change': 'bool',
        'show_in_presence': 'bool',
        'show_in_subscribed_users': 'bool',
        'subscribe_newsletter': 'bool',
        'subscription_enable_identification': 'bool',
        'subscription_keep_ads': 'bool',
        'timezone': 'str',
        'use_gravatar': 'bool',
        'videos_autocontinue': 'bool',
        'videos_autoplay': 'bool',
        'videos_player_floating': 'bool'
    }

    attribute_map = {
        'comments_order_own_first': 'comments_order_own_first',
        'comments_order_popular': 'comments_order_popular',
        'country': 'country',
        'enable_darkmode': 'enable_darkmode',
        'enable_darkmode_schedule': 'enable_darkmode_schedule',
        'enable_spoilers': 'enable_spoilers',
        'public_profile': 'public_profile',
        'scroll_top_route_change': 'scroll_top_route_change',
        'show_in_presence': 'show_in_presence',
        'show_in_subscribed_users': 'show_in_subscribed_users',
        'subscribe_newsletter': 'subscribe_newsletter',
        'subscription_enable_identification': 'subscription_enable_identification',
        'subscription_keep_ads': 'subscription_keep_ads',
        'timezone': 'timezone',
        'use_gravatar': 'use_gravatar',
        'videos_autocontinue': 'videos_autocontinue',
        'videos_autoplay': 'videos_autoplay',
        'videos_player_floating': 'videos_player_floating'
    }

    def __init__(self, comments_order_own_first=None, comments_order_popular=None, country=None, enable_darkmode=None, enable_darkmode_schedule=None, enable_spoilers=None, public_profile=None, scroll_top_route_change=None, show_in_presence=None, show_in_subscribed_users=None, subscribe_newsletter=None, subscription_enable_identification=None, subscription_keep_ads=None, timezone=None, use_gravatar=None, videos_autocontinue=None, videos_autoplay=None, videos_player_floating=None):  # noqa: E501
        """Preferences1 - a model defined in Swagger"""  # noqa: E501
        self._comments_order_own_first = None
        self._comments_order_popular = None
        self._country = None
        self._enable_darkmode = None
        self._enable_darkmode_schedule = None
        self._enable_spoilers = None
        self._public_profile = None
        self._scroll_top_route_change = None
        self._show_in_presence = None
        self._show_in_subscribed_users = None
        self._subscribe_newsletter = None
        self._subscription_enable_identification = None
        self._subscription_keep_ads = None
        self._timezone = None
        self._use_gravatar = None
        self._videos_autocontinue = None
        self._videos_autoplay = None
        self._videos_player_floating = None
        self.discriminator = None
        if comments_order_own_first is not None:
            self.comments_order_own_first = comments_order_own_first
        if comments_order_popular is not None:
            self.comments_order_popular = comments_order_popular
        if country is not None:
            self.country = country
        if enable_darkmode is not None:
            self.enable_darkmode = enable_darkmode
        if enable_darkmode_schedule is not None:
            self.enable_darkmode_schedule = enable_darkmode_schedule
        if enable_spoilers is not None:
            self.enable_spoilers = enable_spoilers
        if public_profile is not None:
            self.public_profile = public_profile
        if scroll_top_route_change is not None:
            self.scroll_top_route_change = scroll_top_route_change
        if show_in_presence is not None:
            self.show_in_presence = show_in_presence
        if show_in_subscribed_users is not None:
            self.show_in_subscribed_users = show_in_subscribed_users
        if subscribe_newsletter is not None:
            self.subscribe_newsletter = subscribe_newsletter
        if subscription_enable_identification is not None:
            self.subscription_enable_identification = subscription_enable_identification
        if subscription_keep_ads is not None:
            self.subscription_keep_ads = subscription_keep_ads
        if timezone is not None:
            self.timezone = timezone
        if use_gravatar is not None:
            self.use_gravatar = use_gravatar
        if videos_autocontinue is not None:
            self.videos_autocontinue = videos_autocontinue
        if videos_autoplay is not None:
            self.videos_autoplay = videos_autoplay
        if videos_player_floating is not None:
            self.videos_player_floating = videos_player_floating

    @property
    def comments_order_own_first(self):
        """Gets the comments_order_own_first of this Preferences1.  # noqa: E501


        :return: The comments_order_own_first of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._comments_order_own_first

    @comments_order_own_first.setter
    def comments_order_own_first(self, comments_order_own_first):
        """Sets the comments_order_own_first of this Preferences1.


        :param comments_order_own_first: The comments_order_own_first of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._comments_order_own_first = comments_order_own_first

    @property
    def comments_order_popular(self):
        """Gets the comments_order_popular of this Preferences1.  # noqa: E501


        :return: The comments_order_popular of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._comments_order_popular

    @comments_order_popular.setter
    def comments_order_popular(self, comments_order_popular):
        """Sets the comments_order_popular of this Preferences1.


        :param comments_order_popular: The comments_order_popular of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._comments_order_popular = comments_order_popular

    @property
    def country(self):
        """Gets the country of this Preferences1.  # noqa: E501


        :return: The country of this Preferences1.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Preferences1.


        :param country: The country of this Preferences1.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def enable_darkmode(self):
        """Gets the enable_darkmode of this Preferences1.  # noqa: E501


        :return: The enable_darkmode of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._enable_darkmode

    @enable_darkmode.setter
    def enable_darkmode(self, enable_darkmode):
        """Sets the enable_darkmode of this Preferences1.


        :param enable_darkmode: The enable_darkmode of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._enable_darkmode = enable_darkmode

    @property
    def enable_darkmode_schedule(self):
        """Gets the enable_darkmode_schedule of this Preferences1.  # noqa: E501


        :return: The enable_darkmode_schedule of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._enable_darkmode_schedule

    @enable_darkmode_schedule.setter
    def enable_darkmode_schedule(self, enable_darkmode_schedule):
        """Sets the enable_darkmode_schedule of this Preferences1.


        :param enable_darkmode_schedule: The enable_darkmode_schedule of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._enable_darkmode_schedule = enable_darkmode_schedule

    @property
    def enable_spoilers(self):
        """Gets the enable_spoilers of this Preferences1.  # noqa: E501


        :return: The enable_spoilers of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._enable_spoilers

    @enable_spoilers.setter
    def enable_spoilers(self, enable_spoilers):
        """Sets the enable_spoilers of this Preferences1.


        :param enable_spoilers: The enable_spoilers of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._enable_spoilers = enable_spoilers

    @property
    def public_profile(self):
        """Gets the public_profile of this Preferences1.  # noqa: E501


        :return: The public_profile of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._public_profile

    @public_profile.setter
    def public_profile(self, public_profile):
        """Sets the public_profile of this Preferences1.


        :param public_profile: The public_profile of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._public_profile = public_profile

    @property
    def scroll_top_route_change(self):
        """Gets the scroll_top_route_change of this Preferences1.  # noqa: E501


        :return: The scroll_top_route_change of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._scroll_top_route_change

    @scroll_top_route_change.setter
    def scroll_top_route_change(self, scroll_top_route_change):
        """Sets the scroll_top_route_change of this Preferences1.


        :param scroll_top_route_change: The scroll_top_route_change of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._scroll_top_route_change = scroll_top_route_change

    @property
    def show_in_presence(self):
        """Gets the show_in_presence of this Preferences1.  # noqa: E501


        :return: The show_in_presence of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_presence

    @show_in_presence.setter
    def show_in_presence(self, show_in_presence):
        """Sets the show_in_presence of this Preferences1.


        :param show_in_presence: The show_in_presence of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._show_in_presence = show_in_presence

    @property
    def show_in_subscribed_users(self):
        """Gets the show_in_subscribed_users of this Preferences1.  # noqa: E501


        :return: The show_in_subscribed_users of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._show_in_subscribed_users

    @show_in_subscribed_users.setter
    def show_in_subscribed_users(self, show_in_subscribed_users):
        """Sets the show_in_subscribed_users of this Preferences1.


        :param show_in_subscribed_users: The show_in_subscribed_users of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._show_in_subscribed_users = show_in_subscribed_users

    @property
    def subscribe_newsletter(self):
        """Gets the subscribe_newsletter of this Preferences1.  # noqa: E501


        :return: The subscribe_newsletter of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe_newsletter

    @subscribe_newsletter.setter
    def subscribe_newsletter(self, subscribe_newsletter):
        """Sets the subscribe_newsletter of this Preferences1.


        :param subscribe_newsletter: The subscribe_newsletter of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._subscribe_newsletter = subscribe_newsletter

    @property
    def subscription_enable_identification(self):
        """Gets the subscription_enable_identification of this Preferences1.  # noqa: E501


        :return: The subscription_enable_identification of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._subscription_enable_identification

    @subscription_enable_identification.setter
    def subscription_enable_identification(self, subscription_enable_identification):
        """Sets the subscription_enable_identification of this Preferences1.


        :param subscription_enable_identification: The subscription_enable_identification of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._subscription_enable_identification = subscription_enable_identification

    @property
    def subscription_keep_ads(self):
        """Gets the subscription_keep_ads of this Preferences1.  # noqa: E501


        :return: The subscription_keep_ads of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._subscription_keep_ads

    @subscription_keep_ads.setter
    def subscription_keep_ads(self, subscription_keep_ads):
        """Sets the subscription_keep_ads of this Preferences1.


        :param subscription_keep_ads: The subscription_keep_ads of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._subscription_keep_ads = subscription_keep_ads

    @property
    def timezone(self):
        """Gets the timezone of this Preferences1.  # noqa: E501


        :return: The timezone of this Preferences1.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this Preferences1.


        :param timezone: The timezone of this Preferences1.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def use_gravatar(self):
        """Gets the use_gravatar of this Preferences1.  # noqa: E501


        :return: The use_gravatar of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._use_gravatar

    @use_gravatar.setter
    def use_gravatar(self, use_gravatar):
        """Sets the use_gravatar of this Preferences1.


        :param use_gravatar: The use_gravatar of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._use_gravatar = use_gravatar

    @property
    def videos_autocontinue(self):
        """Gets the videos_autocontinue of this Preferences1.  # noqa: E501


        :return: The videos_autocontinue of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._videos_autocontinue

    @videos_autocontinue.setter
    def videos_autocontinue(self, videos_autocontinue):
        """Sets the videos_autocontinue of this Preferences1.


        :param videos_autocontinue: The videos_autocontinue of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._videos_autocontinue = videos_autocontinue

    @property
    def videos_autoplay(self):
        """Gets the videos_autoplay of this Preferences1.  # noqa: E501


        :return: The videos_autoplay of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._videos_autoplay

    @videos_autoplay.setter
    def videos_autoplay(self, videos_autoplay):
        """Sets the videos_autoplay of this Preferences1.


        :param videos_autoplay: The videos_autoplay of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._videos_autoplay = videos_autoplay

    @property
    def videos_player_floating(self):
        """Gets the videos_player_floating of this Preferences1.  # noqa: E501


        :return: The videos_player_floating of this Preferences1.  # noqa: E501
        :rtype: bool
        """
        return self._videos_player_floating

    @videos_player_floating.setter
    def videos_player_floating(self, videos_player_floating):
        """Sets the videos_player_floating of this Preferences1.


        :param videos_player_floating: The videos_player_floating of this Preferences1.  # noqa: E501
        :type: bool
        """

        self._videos_player_floating = videos_player_floating

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
        if issubclass(Preferences1, dict):
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
        if not isinstance(other, Preferences1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

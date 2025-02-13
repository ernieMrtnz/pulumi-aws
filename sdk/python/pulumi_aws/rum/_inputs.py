# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'AppMonitorAppMonitorConfigurationArgs',
    'AppMonitorCustomEventsArgs',
]

@pulumi.input_type
class AppMonitorAppMonitorConfigurationArgs:
    def __init__(__self__, *,
                 allow_cookies: Optional[pulumi.Input[bool]] = None,
                 enable_xray: Optional[pulumi.Input[bool]] = None,
                 excluded_pages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 favorite_pages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 guest_role_arn: Optional[pulumi.Input[str]] = None,
                 identity_pool_id: Optional[pulumi.Input[str]] = None,
                 included_pages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 session_sample_rate: Optional[pulumi.Input[float]] = None,
                 telemetries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[bool] allow_cookies: If you set this to `true`, RUM web client sets two cookies, a session cookie  and a user cookie. The cookies allow the RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.
        :param pulumi.Input[bool] enable_xray: If you set this to `true`, RUM enables X-Ray tracing for the user sessions  that RUM samples. RUM adds an X-Ray trace header to allowed HTTP requests. It also records an X-Ray segment for allowed HTTP requests.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] excluded_pages: A list of URLs in your website or application to exclude from RUM data collection.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] favorite_pages: A list of pages in the CloudWatch RUM console that are to be displayed with a "favorite" icon.
        :param pulumi.Input[str] guest_role_arn: The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.
        :param pulumi.Input[str] identity_pool_id: The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] included_pages: If this app monitor is to collect data from only certain pages in your application, this structure lists those pages.
        :param pulumi.Input[float] session_sample_rate: Specifies the percentage of user sessions to use for RUM data collection. Choosing a higher percentage gives you more data but also incurs more costs. The number you specify is the percentage of user sessions that will be used. Default value is `0.1`.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] telemetries: An array that lists the types of telemetry data that this app monitor is to collect. Valid values are `errors`, `performance`, and `http`.
        """
        AppMonitorAppMonitorConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allow_cookies=allow_cookies,
            enable_xray=enable_xray,
            excluded_pages=excluded_pages,
            favorite_pages=favorite_pages,
            guest_role_arn=guest_role_arn,
            identity_pool_id=identity_pool_id,
            included_pages=included_pages,
            session_sample_rate=session_sample_rate,
            telemetries=telemetries,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allow_cookies: Optional[pulumi.Input[bool]] = None,
             enable_xray: Optional[pulumi.Input[bool]] = None,
             excluded_pages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             favorite_pages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             guest_role_arn: Optional[pulumi.Input[str]] = None,
             identity_pool_id: Optional[pulumi.Input[str]] = None,
             included_pages: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             session_sample_rate: Optional[pulumi.Input[float]] = None,
             telemetries: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if allow_cookies is None and 'allowCookies' in kwargs:
            allow_cookies = kwargs['allowCookies']
        if enable_xray is None and 'enableXray' in kwargs:
            enable_xray = kwargs['enableXray']
        if excluded_pages is None and 'excludedPages' in kwargs:
            excluded_pages = kwargs['excludedPages']
        if favorite_pages is None and 'favoritePages' in kwargs:
            favorite_pages = kwargs['favoritePages']
        if guest_role_arn is None and 'guestRoleArn' in kwargs:
            guest_role_arn = kwargs['guestRoleArn']
        if identity_pool_id is None and 'identityPoolId' in kwargs:
            identity_pool_id = kwargs['identityPoolId']
        if included_pages is None and 'includedPages' in kwargs:
            included_pages = kwargs['includedPages']
        if session_sample_rate is None and 'sessionSampleRate' in kwargs:
            session_sample_rate = kwargs['sessionSampleRate']

        if allow_cookies is not None:
            _setter("allow_cookies", allow_cookies)
        if enable_xray is not None:
            _setter("enable_xray", enable_xray)
        if excluded_pages is not None:
            _setter("excluded_pages", excluded_pages)
        if favorite_pages is not None:
            _setter("favorite_pages", favorite_pages)
        if guest_role_arn is not None:
            _setter("guest_role_arn", guest_role_arn)
        if identity_pool_id is not None:
            _setter("identity_pool_id", identity_pool_id)
        if included_pages is not None:
            _setter("included_pages", included_pages)
        if session_sample_rate is not None:
            _setter("session_sample_rate", session_sample_rate)
        if telemetries is not None:
            _setter("telemetries", telemetries)

    @property
    @pulumi.getter(name="allowCookies")
    def allow_cookies(self) -> Optional[pulumi.Input[bool]]:
        """
        If you set this to `true`, RUM web client sets two cookies, a session cookie  and a user cookie. The cookies allow the RUM web client to collect data relating to the number of users an application has and the behavior of the application across a sequence of events. Cookies are stored in the top-level domain of the current page.
        """
        return pulumi.get(self, "allow_cookies")

    @allow_cookies.setter
    def allow_cookies(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "allow_cookies", value)

    @property
    @pulumi.getter(name="enableXray")
    def enable_xray(self) -> Optional[pulumi.Input[bool]]:
        """
        If you set this to `true`, RUM enables X-Ray tracing for the user sessions  that RUM samples. RUM adds an X-Ray trace header to allowed HTTP requests. It also records an X-Ray segment for allowed HTTP requests.
        """
        return pulumi.get(self, "enable_xray")

    @enable_xray.setter
    def enable_xray(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_xray", value)

    @property
    @pulumi.getter(name="excludedPages")
    def excluded_pages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of URLs in your website or application to exclude from RUM data collection.
        """
        return pulumi.get(self, "excluded_pages")

    @excluded_pages.setter
    def excluded_pages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "excluded_pages", value)

    @property
    @pulumi.getter(name="favoritePages")
    def favorite_pages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of pages in the CloudWatch RUM console that are to be displayed with a "favorite" icon.
        """
        return pulumi.get(self, "favorite_pages")

    @favorite_pages.setter
    def favorite_pages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "favorite_pages", value)

    @property
    @pulumi.getter(name="guestRoleArn")
    def guest_role_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the guest IAM role that is attached to the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.
        """
        return pulumi.get(self, "guest_role_arn")

    @guest_role_arn.setter
    def guest_role_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "guest_role_arn", value)

    @property
    @pulumi.getter(name="identityPoolId")
    def identity_pool_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Amazon Cognito identity pool that is used to authorize the sending of data to RUM.
        """
        return pulumi.get(self, "identity_pool_id")

    @identity_pool_id.setter
    def identity_pool_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_pool_id", value)

    @property
    @pulumi.getter(name="includedPages")
    def included_pages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        If this app monitor is to collect data from only certain pages in your application, this structure lists those pages.
        """
        return pulumi.get(self, "included_pages")

    @included_pages.setter
    def included_pages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "included_pages", value)

    @property
    @pulumi.getter(name="sessionSampleRate")
    def session_sample_rate(self) -> Optional[pulumi.Input[float]]:
        """
        Specifies the percentage of user sessions to use for RUM data collection. Choosing a higher percentage gives you more data but also incurs more costs. The number you specify is the percentage of user sessions that will be used. Default value is `0.1`.
        """
        return pulumi.get(self, "session_sample_rate")

    @session_sample_rate.setter
    def session_sample_rate(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "session_sample_rate", value)

    @property
    @pulumi.getter
    def telemetries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        An array that lists the types of telemetry data that this app monitor is to collect. Valid values are `errors`, `performance`, and `http`.
        """
        return pulumi.get(self, "telemetries")

    @telemetries.setter
    def telemetries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "telemetries", value)


@pulumi.input_type
class AppMonitorCustomEventsArgs:
    def __init__(__self__, *,
                 status: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] status: Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be `DISABLED`. Valid values are `DISABLED` and `ENABLED`.
        """
        AppMonitorCustomEventsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether this app monitor allows the web client to define and send custom events. The default is for custom events to be `DISABLED`. Valid values are `DISABLED` and `ENABLED`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)



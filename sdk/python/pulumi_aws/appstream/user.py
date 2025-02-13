# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 authentication_type: pulumi.Input[str],
                 user_name: pulumi.Input[str],
                 enabled: Optional[pulumi.Input[bool]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 send_email_notification: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] authentication_type: Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        :param pulumi.Input[str] user_name: Email address of the user.
               
               The following arguments are optional:
        :param pulumi.Input[bool] enabled: Whether the user in the user pool is enabled.
        :param pulumi.Input[str] first_name: First name, or given name, of the user.
        :param pulumi.Input[str] last_name: Last name, or surname, of the user.
        :param pulumi.Input[bool] send_email_notification: Send an email notification.
        """
        UserArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            authentication_type=authentication_type,
            user_name=user_name,
            enabled=enabled,
            first_name=first_name,
            last_name=last_name,
            send_email_notification=send_email_notification,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             authentication_type: Optional[pulumi.Input[str]] = None,
             user_name: Optional[pulumi.Input[str]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             first_name: Optional[pulumi.Input[str]] = None,
             last_name: Optional[pulumi.Input[str]] = None,
             send_email_notification: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if authentication_type is None and 'authenticationType' in kwargs:
            authentication_type = kwargs['authenticationType']
        if authentication_type is None:
            raise TypeError("Missing 'authentication_type' argument")
        if user_name is None and 'userName' in kwargs:
            user_name = kwargs['userName']
        if user_name is None:
            raise TypeError("Missing 'user_name' argument")
        if first_name is None and 'firstName' in kwargs:
            first_name = kwargs['firstName']
        if last_name is None and 'lastName' in kwargs:
            last_name = kwargs['lastName']
        if send_email_notification is None and 'sendEmailNotification' in kwargs:
            send_email_notification = kwargs['sendEmailNotification']

        _setter("authentication_type", authentication_type)
        _setter("user_name", user_name)
        if enabled is not None:
            _setter("enabled", enabled)
        if first_name is not None:
            _setter("first_name", first_name)
        if last_name is not None:
            _setter("last_name", last_name)
        if send_email_notification is not None:
            _setter("send_email_notification", send_email_notification)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Input[str]:
        """
        Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[str]:
        """
        Email address of the user.

        The following arguments are optional:
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_name", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the user in the user pool is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name, or given name, of the user.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name, or surname, of the user.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="sendEmailNotification")
    def send_email_notification(self) -> Optional[pulumi.Input[bool]]:
        """
        Send an email notification.
        """
        return pulumi.get(self, "send_email_notification")

    @send_email_notification.setter
    def send_email_notification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_email_notification", value)


@pulumi.input_type
class _UserState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 send_email_notification: Optional[pulumi.Input[bool]] = None,
                 user_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering User resources.
        :param pulumi.Input[str] arn: ARN of the appstream user.
        :param pulumi.Input[str] authentication_type: Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        :param pulumi.Input[str] created_time: Date and time, in UTC and extended RFC 3339 format, when the user was created.
        :param pulumi.Input[bool] enabled: Whether the user in the user pool is enabled.
        :param pulumi.Input[str] first_name: First name, or given name, of the user.
        :param pulumi.Input[str] last_name: Last name, or surname, of the user.
        :param pulumi.Input[bool] send_email_notification: Send an email notification.
        :param pulumi.Input[str] user_name: Email address of the user.
               
               The following arguments are optional:
        """
        _UserState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            authentication_type=authentication_type,
            created_time=created_time,
            enabled=enabled,
            first_name=first_name,
            last_name=last_name,
            send_email_notification=send_email_notification,
            user_name=user_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[pulumi.Input[str]] = None,
             authentication_type: Optional[pulumi.Input[str]] = None,
             created_time: Optional[pulumi.Input[str]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             first_name: Optional[pulumi.Input[str]] = None,
             last_name: Optional[pulumi.Input[str]] = None,
             send_email_notification: Optional[pulumi.Input[bool]] = None,
             user_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if authentication_type is None and 'authenticationType' in kwargs:
            authentication_type = kwargs['authenticationType']
        if created_time is None and 'createdTime' in kwargs:
            created_time = kwargs['createdTime']
        if first_name is None and 'firstName' in kwargs:
            first_name = kwargs['firstName']
        if last_name is None and 'lastName' in kwargs:
            last_name = kwargs['lastName']
        if send_email_notification is None and 'sendEmailNotification' in kwargs:
            send_email_notification = kwargs['sendEmailNotification']
        if user_name is None and 'userName' in kwargs:
            user_name = kwargs['userName']

        if arn is not None:
            _setter("arn", arn)
        if authentication_type is not None:
            _setter("authentication_type", authentication_type)
        if created_time is not None:
            _setter("created_time", created_time)
        if enabled is not None:
            _setter("enabled", enabled)
        if first_name is not None:
            _setter("first_name", first_name)
        if last_name is not None:
            _setter("last_name", last_name)
        if send_email_notification is not None:
            _setter("send_email_notification", send_email_notification)
        if user_name is not None:
            _setter("user_name", user_name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the appstream user.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> Optional[pulumi.Input[str]]:
        """
        Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        """
        return pulumi.get(self, "authentication_type")

    @authentication_type.setter
    def authentication_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_type", value)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time, in UTC and extended RFC 3339 format, when the user was created.
        """
        return pulumi.get(self, "created_time")

    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_time", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the user in the user pool is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name, or given name, of the user.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name, or surname, of the user.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="sendEmailNotification")
    def send_email_notification(self) -> Optional[pulumi.Input[bool]]:
        """
        Send an email notification.
        """
        return pulumi.get(self, "send_email_notification")

    @send_email_notification.setter
    def send_email_notification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "send_email_notification", value)

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the user.

        The following arguments are optional:
        """
        return pulumi.get(self, "user_name")

    @user_name.setter
    def user_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_name", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 send_email_notification: Optional[pulumi.Input[bool]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an AppStream user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appstream.User("example",
            authentication_type="USERPOOL",
            first_name="FIRST NAME",
            last_name="LAST NAME",
            user_name="EMAIL")
        ```

        ## Import

        Using `pulumi import`, import `aws_appstream_user` using the `user_name` and `authentication_type` separated by a slash (`/`). For example:

        ```sh
         $ pulumi import aws:appstream/user:User example UserName/AuthenticationType
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_type: Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        :param pulumi.Input[bool] enabled: Whether the user in the user pool is enabled.
        :param pulumi.Input[str] first_name: First name, or given name, of the user.
        :param pulumi.Input[str] last_name: Last name, or surname, of the user.
        :param pulumi.Input[bool] send_email_notification: Send an email notification.
        :param pulumi.Input[str] user_name: Email address of the user.
               
               The following arguments are optional:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an AppStream user.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.appstream.User("example",
            authentication_type="USERPOOL",
            first_name="FIRST NAME",
            last_name="LAST NAME",
            user_name="EMAIL")
        ```

        ## Import

        Using `pulumi import`, import `aws_appstream_user` using the `user_name` and `authentication_type` separated by a slash (`/`). For example:

        ```sh
         $ pulumi import aws:appstream/user:User example UserName/AuthenticationType
        ```

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            UserArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_type: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 send_email_notification: Optional[pulumi.Input[bool]] = None,
                 user_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            if authentication_type is None and not opts.urn:
                raise TypeError("Missing required property 'authentication_type'")
            __props__.__dict__["authentication_type"] = authentication_type
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["first_name"] = first_name
            __props__.__dict__["last_name"] = last_name
            __props__.__dict__["send_email_notification"] = send_email_notification
            if user_name is None and not opts.urn:
                raise TypeError("Missing required property 'user_name'")
            __props__.__dict__["user_name"] = user_name
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
        super(User, __self__).__init__(
            'aws:appstream/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            authentication_type: Optional[pulumi.Input[str]] = None,
            created_time: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            first_name: Optional[pulumi.Input[str]] = None,
            last_name: Optional[pulumi.Input[str]] = None,
            send_email_notification: Optional[pulumi.Input[bool]] = None,
            user_name: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: ARN of the appstream user.
        :param pulumi.Input[str] authentication_type: Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        :param pulumi.Input[str] created_time: Date and time, in UTC and extended RFC 3339 format, when the user was created.
        :param pulumi.Input[bool] enabled: Whether the user in the user pool is enabled.
        :param pulumi.Input[str] first_name: First name, or given name, of the user.
        :param pulumi.Input[str] last_name: Last name, or surname, of the user.
        :param pulumi.Input[bool] send_email_notification: Send an email notification.
        :param pulumi.Input[str] user_name: Email address of the user.
               
               The following arguments are optional:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserState.__new__(_UserState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["authentication_type"] = authentication_type
        __props__.__dict__["created_time"] = created_time
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["first_name"] = first_name
        __props__.__dict__["last_name"] = last_name
        __props__.__dict__["send_email_notification"] = send_email_notification
        __props__.__dict__["user_name"] = user_name
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN of the appstream user.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="authenticationType")
    def authentication_type(self) -> pulumi.Output[str]:
        """
        Authentication type for the user. You must specify USERPOOL. Valid values: `API`, `SAML`, `USERPOOL`
        """
        return pulumi.get(self, "authentication_type")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        Date and time, in UTC and extended RFC 3339 format, when the user was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the user in the user pool is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> pulumi.Output[Optional[str]]:
        """
        First name, or given name, of the user.
        """
        return pulumi.get(self, "first_name")

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> pulumi.Output[Optional[str]]:
        """
        Last name, or surname, of the user.
        """
        return pulumi.get(self, "last_name")

    @property
    @pulumi.getter(name="sendEmailNotification")
    def send_email_notification(self) -> pulumi.Output[Optional[bool]]:
        """
        Send an email notification.
        """
        return pulumi.get(self, "send_email_notification")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Output[str]:
        """
        Email address of the user.

        The following arguments are optional:
        """
        return pulumi.get(self, "user_name")


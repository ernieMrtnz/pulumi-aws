# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['MemberArgs', 'Member']

@pulumi.input_type
class MemberArgs:
    def __init__(__self__, *,
                 account_id: pulumi.Input[str],
                 email_address: pulumi.Input[str],
                 graph_arn: pulumi.Input[str],
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 message: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Member resource.
        :param pulumi.Input[str] account_id: AWS account ID for the account.
        :param pulumi.Input[str] email_address: Email address for the account.
        :param pulumi.Input[str] graph_arn: ARN of the behavior graph to invite the member accounts to contribute their data to.
        :param pulumi.Input[bool] disable_email_notification: If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        :param pulumi.Input[str] message: A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        """
        MemberArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            email_address=email_address,
            graph_arn=graph_arn,
            disable_email_notification=disable_email_notification,
            message=message,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             email_address: Optional[pulumi.Input[str]] = None,
             graph_arn: Optional[pulumi.Input[str]] = None,
             disable_email_notification: Optional[pulumi.Input[bool]] = None,
             message: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if account_id is None and 'accountId' in kwargs:
            account_id = kwargs['accountId']
        if account_id is None:
            raise TypeError("Missing 'account_id' argument")
        if email_address is None and 'emailAddress' in kwargs:
            email_address = kwargs['emailAddress']
        if email_address is None:
            raise TypeError("Missing 'email_address' argument")
        if graph_arn is None and 'graphArn' in kwargs:
            graph_arn = kwargs['graphArn']
        if graph_arn is None:
            raise TypeError("Missing 'graph_arn' argument")
        if disable_email_notification is None and 'disableEmailNotification' in kwargs:
            disable_email_notification = kwargs['disableEmailNotification']

        _setter("account_id", account_id)
        _setter("email_address", email_address)
        _setter("graph_arn", graph_arn)
        if disable_email_notification is not None:
            _setter("disable_email_notification", disable_email_notification)
        if message is not None:
            _setter("message", message)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Input[str]:
        """
        AWS account ID for the account.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[str]:
        """
        Email address for the account.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Input[str]:
        """
        ARN of the behavior graph to invite the member accounts to contribute their data to.
        """
        return pulumi.get(self, "graph_arn")

    @graph_arn.setter
    def graph_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "graph_arn", value)

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        """
        return pulumi.get(self, "disable_email_notification")

    @disable_email_notification.setter
    def disable_email_notification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_email_notification", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)


@pulumi.input_type
class _MemberState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 administrator_id: Optional[pulumi.Input[str]] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 disabled_reason: Optional[pulumi.Input[str]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 graph_arn: Optional[pulumi.Input[str]] = None,
                 invited_time: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 updated_time: Optional[pulumi.Input[str]] = None,
                 volume_usage_in_bytes: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Member resources.
        :param pulumi.Input[str] account_id: AWS account ID for the account.
        :param pulumi.Input[str] administrator_id: AWS account ID for the administrator account.
        :param pulumi.Input[bool] disable_email_notification: If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        :param pulumi.Input[str] email_address: Email address for the account.
        :param pulumi.Input[str] graph_arn: ARN of the behavior graph to invite the member accounts to contribute their data to.
        :param pulumi.Input[str] invited_time: Date and time, in UTC and extended RFC 3339 format, when an Amazon Detective membership invitation was last sent to the account.
        :param pulumi.Input[str] message: A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        :param pulumi.Input[str] status: Current membership status of the member account.
        :param pulumi.Input[str] updated_time: Date and time, in UTC and extended RFC 3339 format, of the most recent change to the member account's status.
        :param pulumi.Input[str] volume_usage_in_bytes: Data volume in bytes per day for the member account.
        """
        _MemberState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            administrator_id=administrator_id,
            disable_email_notification=disable_email_notification,
            disabled_reason=disabled_reason,
            email_address=email_address,
            graph_arn=graph_arn,
            invited_time=invited_time,
            message=message,
            status=status,
            updated_time=updated_time,
            volume_usage_in_bytes=volume_usage_in_bytes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             administrator_id: Optional[pulumi.Input[str]] = None,
             disable_email_notification: Optional[pulumi.Input[bool]] = None,
             disabled_reason: Optional[pulumi.Input[str]] = None,
             email_address: Optional[pulumi.Input[str]] = None,
             graph_arn: Optional[pulumi.Input[str]] = None,
             invited_time: Optional[pulumi.Input[str]] = None,
             message: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             updated_time: Optional[pulumi.Input[str]] = None,
             volume_usage_in_bytes: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if account_id is None and 'accountId' in kwargs:
            account_id = kwargs['accountId']
        if administrator_id is None and 'administratorId' in kwargs:
            administrator_id = kwargs['administratorId']
        if disable_email_notification is None and 'disableEmailNotification' in kwargs:
            disable_email_notification = kwargs['disableEmailNotification']
        if disabled_reason is None and 'disabledReason' in kwargs:
            disabled_reason = kwargs['disabledReason']
        if email_address is None and 'emailAddress' in kwargs:
            email_address = kwargs['emailAddress']
        if graph_arn is None and 'graphArn' in kwargs:
            graph_arn = kwargs['graphArn']
        if invited_time is None and 'invitedTime' in kwargs:
            invited_time = kwargs['invitedTime']
        if updated_time is None and 'updatedTime' in kwargs:
            updated_time = kwargs['updatedTime']
        if volume_usage_in_bytes is None and 'volumeUsageInBytes' in kwargs:
            volume_usage_in_bytes = kwargs['volumeUsageInBytes']

        if account_id is not None:
            _setter("account_id", account_id)
        if administrator_id is not None:
            _setter("administrator_id", administrator_id)
        if disable_email_notification is not None:
            _setter("disable_email_notification", disable_email_notification)
        if disabled_reason is not None:
            _setter("disabled_reason", disabled_reason)
        if email_address is not None:
            _setter("email_address", email_address)
        if graph_arn is not None:
            _setter("graph_arn", graph_arn)
        if invited_time is not None:
            _setter("invited_time", invited_time)
        if message is not None:
            _setter("message", message)
        if status is not None:
            _setter("status", status)
        if updated_time is not None:
            _setter("updated_time", updated_time)
        if volume_usage_in_bytes is not None:
            _setter("volume_usage_in_bytes", volume_usage_in_bytes)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID for the account.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter(name="administratorId")
    def administrator_id(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID for the administrator account.
        """
        return pulumi.get(self, "administrator_id")

    @administrator_id.setter
    def administrator_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "administrator_id", value)

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        """
        return pulumi.get(self, "disable_email_notification")

    @disable_email_notification.setter
    def disable_email_notification(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_email_notification", value)

    @property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "disabled_reason")

    @disabled_reason.setter
    def disabled_reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disabled_reason", value)

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> Optional[pulumi.Input[str]]:
        """
        Email address for the account.
        """
        return pulumi.get(self, "email_address")

    @email_address.setter
    def email_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email_address", value)

    @property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the behavior graph to invite the member accounts to contribute their data to.
        """
        return pulumi.get(self, "graph_arn")

    @graph_arn.setter
    def graph_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "graph_arn", value)

    @property
    @pulumi.getter(name="invitedTime")
    def invited_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time, in UTC and extended RFC 3339 format, when an Amazon Detective membership invitation was last sent to the account.
        """
        return pulumi.get(self, "invited_time")

    @invited_time.setter
    def invited_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "invited_time", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Current membership status of the member account.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time, in UTC and extended RFC 3339 format, of the most recent change to the member account's status.
        """
        return pulumi.get(self, "updated_time")

    @updated_time.setter
    def updated_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_time", value)

    @property
    @pulumi.getter(name="volumeUsageInBytes")
    def volume_usage_in_bytes(self) -> Optional[pulumi.Input[str]]:
        """
        Data volume in bytes per day for the member account.
        """
        return pulumi.get(self, "volume_usage_in_bytes")

    @volume_usage_in_bytes.setter
    def volume_usage_in_bytes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_usage_in_bytes", value)


class Member(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 graph_arn: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource to manage an [Amazon Detective Member](https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateMembers.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_graph = aws.detective.Graph("exampleGraph")
        example_member = aws.detective.Member("exampleMember",
            account_id="AWS ACCOUNT ID",
            email_address="EMAIL",
            graph_arn=example_graph.id,
            message="Message of the invitation",
            disable_email_notification=True)
        ```

        ## Import

        Using `pulumi import`, import `aws_detective_member` using the ARN of the graph followed by the account ID of the member account. For example:

        ```sh
         $ pulumi import aws:detective/member:Member example arn:aws:detective:us-east-1:123456789101:graph:231684d34gh74g4bae1dbc7bd807d02d/123456789012
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: AWS account ID for the account.
        :param pulumi.Input[bool] disable_email_notification: If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        :param pulumi.Input[str] email_address: Email address for the account.
        :param pulumi.Input[str] graph_arn: ARN of the behavior graph to invite the member accounts to contribute their data to.
        :param pulumi.Input[str] message: A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage an [Amazon Detective Member](https://docs.aws.amazon.com/detective/latest/APIReference/API_CreateMembers.html).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_graph = aws.detective.Graph("exampleGraph")
        example_member = aws.detective.Member("exampleMember",
            account_id="AWS ACCOUNT ID",
            email_address="EMAIL",
            graph_arn=example_graph.id,
            message="Message of the invitation",
            disable_email_notification=True)
        ```

        ## Import

        Using `pulumi import`, import `aws_detective_member` using the ARN of the graph followed by the account ID of the member account. For example:

        ```sh
         $ pulumi import aws:detective/member:Member example arn:aws:detective:us-east-1:123456789101:graph:231684d34gh74g4bae1dbc7bd807d02d/123456789012
        ```

        :param str resource_name: The name of the resource.
        :param MemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MemberArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 disable_email_notification: Optional[pulumi.Input[bool]] = None,
                 email_address: Optional[pulumi.Input[str]] = None,
                 graph_arn: Optional[pulumi.Input[str]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MemberArgs.__new__(MemberArgs)

            if account_id is None and not opts.urn:
                raise TypeError("Missing required property 'account_id'")
            __props__.__dict__["account_id"] = account_id
            __props__.__dict__["disable_email_notification"] = disable_email_notification
            if email_address is None and not opts.urn:
                raise TypeError("Missing required property 'email_address'")
            __props__.__dict__["email_address"] = email_address
            if graph_arn is None and not opts.urn:
                raise TypeError("Missing required property 'graph_arn'")
            __props__.__dict__["graph_arn"] = graph_arn
            __props__.__dict__["message"] = message
            __props__.__dict__["administrator_id"] = None
            __props__.__dict__["disabled_reason"] = None
            __props__.__dict__["invited_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["updated_time"] = None
            __props__.__dict__["volume_usage_in_bytes"] = None
        super(Member, __self__).__init__(
            'aws:detective/member:Member',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            administrator_id: Optional[pulumi.Input[str]] = None,
            disable_email_notification: Optional[pulumi.Input[bool]] = None,
            disabled_reason: Optional[pulumi.Input[str]] = None,
            email_address: Optional[pulumi.Input[str]] = None,
            graph_arn: Optional[pulumi.Input[str]] = None,
            invited_time: Optional[pulumi.Input[str]] = None,
            message: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            updated_time: Optional[pulumi.Input[str]] = None,
            volume_usage_in_bytes: Optional[pulumi.Input[str]] = None) -> 'Member':
        """
        Get an existing Member resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: AWS account ID for the account.
        :param pulumi.Input[str] administrator_id: AWS account ID for the administrator account.
        :param pulumi.Input[bool] disable_email_notification: If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        :param pulumi.Input[str] email_address: Email address for the account.
        :param pulumi.Input[str] graph_arn: ARN of the behavior graph to invite the member accounts to contribute their data to.
        :param pulumi.Input[str] invited_time: Date and time, in UTC and extended RFC 3339 format, when an Amazon Detective membership invitation was last sent to the account.
        :param pulumi.Input[str] message: A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        :param pulumi.Input[str] status: Current membership status of the member account.
        :param pulumi.Input[str] updated_time: Date and time, in UTC and extended RFC 3339 format, of the most recent change to the member account's status.
        :param pulumi.Input[str] volume_usage_in_bytes: Data volume in bytes per day for the member account.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MemberState.__new__(_MemberState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["administrator_id"] = administrator_id
        __props__.__dict__["disable_email_notification"] = disable_email_notification
        __props__.__dict__["disabled_reason"] = disabled_reason
        __props__.__dict__["email_address"] = email_address
        __props__.__dict__["graph_arn"] = graph_arn
        __props__.__dict__["invited_time"] = invited_time
        __props__.__dict__["message"] = message
        __props__.__dict__["status"] = status
        __props__.__dict__["updated_time"] = updated_time
        __props__.__dict__["volume_usage_in_bytes"] = volume_usage_in_bytes
        return Member(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        AWS account ID for the account.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter(name="administratorId")
    def administrator_id(self) -> pulumi.Output[str]:
        """
        AWS account ID for the administrator account.
        """
        return pulumi.get(self, "administrator_id")

    @property
    @pulumi.getter(name="disableEmailNotification")
    def disable_email_notification(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to true, then the root user of the invited account will _not_ receive an email notification. This notification is in addition to an alert that the root user receives in AWS Personal Health Dashboard. By default, this is set to `false`.
        """
        return pulumi.get(self, "disable_email_notification")

    @property
    @pulumi.getter(name="disabledReason")
    def disabled_reason(self) -> pulumi.Output[str]:
        return pulumi.get(self, "disabled_reason")

    @property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Output[str]:
        """
        Email address for the account.
        """
        return pulumi.get(self, "email_address")

    @property
    @pulumi.getter(name="graphArn")
    def graph_arn(self) -> pulumi.Output[str]:
        """
        ARN of the behavior graph to invite the member accounts to contribute their data to.
        """
        return pulumi.get(self, "graph_arn")

    @property
    @pulumi.getter(name="invitedTime")
    def invited_time(self) -> pulumi.Output[str]:
        """
        Date and time, in UTC and extended RFC 3339 format, when an Amazon Detective membership invitation was last sent to the account.
        """
        return pulumi.get(self, "invited_time")

    @property
    @pulumi.getter
    def message(self) -> pulumi.Output[Optional[str]]:
        """
        A custom message to include in the invitation. Amazon Detective adds this message to the standard content that it sends for an invitation.
        """
        return pulumi.get(self, "message")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Current membership status of the member account.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> pulumi.Output[str]:
        """
        Date and time, in UTC and extended RFC 3339 format, of the most recent change to the member account's status.
        """
        return pulumi.get(self, "updated_time")

    @property
    @pulumi.getter(name="volumeUsageInBytes")
    def volume_usage_in_bytes(self) -> pulumi.Output[str]:
        """
        Data volume in bytes per day for the member account.
        """
        return pulumi.get(self, "volume_usage_in_bytes")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['AccountAssignmentArgs', 'AccountAssignment']

@pulumi.input_type
class AccountAssignmentArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 permission_set_arn: pulumi.Input[str],
                 principal_id: pulumi.Input[str],
                 principal_type: pulumi.Input[str],
                 target_id: pulumi.Input[str],
                 target_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AccountAssignment resource.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the SSO Instance.
        :param pulumi.Input[str] permission_set_arn: The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        :param pulumi.Input[str] principal_id: An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        :param pulumi.Input[str] principal_type: The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        :param pulumi.Input[str] target_id: An AWS account identifier, typically a 10-12 digit string.
        :param pulumi.Input[str] target_type: The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        AccountAssignmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_arn=instance_arn,
            permission_set_arn=permission_set_arn,
            principal_id=principal_id,
            principal_type=principal_type,
            target_id=target_id,
            target_type=target_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_arn: Optional[pulumi.Input[str]] = None,
             permission_set_arn: Optional[pulumi.Input[str]] = None,
             principal_id: Optional[pulumi.Input[str]] = None,
             principal_type: Optional[pulumi.Input[str]] = None,
             target_id: Optional[pulumi.Input[str]] = None,
             target_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if instance_arn is None and 'instanceArn' in kwargs:
            instance_arn = kwargs['instanceArn']
        if instance_arn is None:
            raise TypeError("Missing 'instance_arn' argument")
        if permission_set_arn is None and 'permissionSetArn' in kwargs:
            permission_set_arn = kwargs['permissionSetArn']
        if permission_set_arn is None:
            raise TypeError("Missing 'permission_set_arn' argument")
        if principal_id is None and 'principalId' in kwargs:
            principal_id = kwargs['principalId']
        if principal_id is None:
            raise TypeError("Missing 'principal_id' argument")
        if principal_type is None and 'principalType' in kwargs:
            principal_type = kwargs['principalType']
        if principal_type is None:
            raise TypeError("Missing 'principal_type' argument")
        if target_id is None and 'targetId' in kwargs:
            target_id = kwargs['targetId']
        if target_id is None:
            raise TypeError("Missing 'target_id' argument")
        if target_type is None and 'targetType' in kwargs:
            target_type = kwargs['targetType']

        _setter("instance_arn", instance_arn)
        _setter("permission_set_arn", permission_set_arn)
        _setter("principal_id", principal_id)
        _setter("principal_type", principal_type)
        _setter("target_id", target_id)
        if target_type is not None:
            _setter("target_type", target_type)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the SSO Instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        """
        return pulumi.get(self, "permission_set_arn")

    @permission_set_arn.setter
    def permission_set_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "permission_set_arn", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[str]:
        """
        The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        """
        return pulumi.get(self, "principal_type")

    @principal_type.setter
    def principal_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_type", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Input[str]:
        """
        An AWS account identifier, typically a 10-12 digit string.
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_id", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[str]]:
        """
        The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_type", value)


@pulumi.input_type
class _AccountAssignmentState:
    def __init__(__self__, *,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 permission_set_arn: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering AccountAssignment resources.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the SSO Instance.
        :param pulumi.Input[str] permission_set_arn: The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        :param pulumi.Input[str] principal_id: An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        :param pulumi.Input[str] principal_type: The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        :param pulumi.Input[str] target_id: An AWS account identifier, typically a 10-12 digit string.
        :param pulumi.Input[str] target_type: The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        _AccountAssignmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            instance_arn=instance_arn,
            permission_set_arn=permission_set_arn,
            principal_id=principal_id,
            principal_type=principal_type,
            target_id=target_id,
            target_type=target_type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             instance_arn: Optional[pulumi.Input[str]] = None,
             permission_set_arn: Optional[pulumi.Input[str]] = None,
             principal_id: Optional[pulumi.Input[str]] = None,
             principal_type: Optional[pulumi.Input[str]] = None,
             target_id: Optional[pulumi.Input[str]] = None,
             target_type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if instance_arn is None and 'instanceArn' in kwargs:
            instance_arn = kwargs['instanceArn']
        if permission_set_arn is None and 'permissionSetArn' in kwargs:
            permission_set_arn = kwargs['permissionSetArn']
        if principal_id is None and 'principalId' in kwargs:
            principal_id = kwargs['principalId']
        if principal_type is None and 'principalType' in kwargs:
            principal_type = kwargs['principalType']
        if target_id is None and 'targetId' in kwargs:
            target_id = kwargs['targetId']
        if target_type is None and 'targetType' in kwargs:
            target_type = kwargs['targetType']

        if instance_arn is not None:
            _setter("instance_arn", instance_arn)
        if permission_set_arn is not None:
            _setter("permission_set_arn", permission_set_arn)
        if principal_id is not None:
            _setter("principal_id", principal_id)
        if principal_type is not None:
            _setter("principal_type", principal_type)
        if target_id is not None:
            _setter("target_id", target_id)
        if target_type is not None:
            _setter("target_type", target_type)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the SSO Instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        """
        return pulumi.get(self, "permission_set_arn")

    @permission_set_arn.setter
    def permission_set_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "permission_set_arn", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> Optional[pulumi.Input[str]]:
        """
        An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> Optional[pulumi.Input[str]]:
        """
        The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        """
        return pulumi.get(self, "principal_type")

    @principal_type.setter
    def principal_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_type", value)

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> Optional[pulumi.Input[str]]:
        """
        An AWS account identifier, typically a 10-12 digit string.
        """
        return pulumi.get(self, "target_id")

    @target_id.setter
    def target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_id", value)

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> Optional[pulumi.Input[str]]:
        """
        The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        return pulumi.get(self, "target_type")

    @target_type.setter
    def target_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_type", value)


class AccountAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 permission_set_arn: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Single Sign-On (SSO) Account Assignment resource

        ## Import

        Using `pulumi import`, import SSO Account Assignments using the `principal_id`, `principal_type`, `target_id`, `target_type`, `permission_set_arn`, `instance_arn` separated by commas (`,`). For example:

        ```sh
         $ pulumi import aws:ssoadmin/accountAssignment:AccountAssignment example f81d4fae-7dec-11d0-a765-00a0c91e6bf6,GROUP,1234567890,AWS_ACCOUNT,arn:aws:sso:::permissionSet/ssoins-0123456789abcdef/ps-0123456789abcdef,arn:aws:sso:::instance/ssoins-0123456789abcdef
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the SSO Instance.
        :param pulumi.Input[str] permission_set_arn: The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        :param pulumi.Input[str] principal_id: An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        :param pulumi.Input[str] principal_type: The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        :param pulumi.Input[str] target_id: An AWS account identifier, typically a 10-12 digit string.
        :param pulumi.Input[str] target_type: The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AccountAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Single Sign-On (SSO) Account Assignment resource

        ## Import

        Using `pulumi import`, import SSO Account Assignments using the `principal_id`, `principal_type`, `target_id`, `target_type`, `permission_set_arn`, `instance_arn` separated by commas (`,`). For example:

        ```sh
         $ pulumi import aws:ssoadmin/accountAssignment:AccountAssignment example f81d4fae-7dec-11d0-a765-00a0c91e6bf6,GROUP,1234567890,AWS_ACCOUNT,arn:aws:sso:::permissionSet/ssoins-0123456789abcdef/ps-0123456789abcdef,arn:aws:sso:::instance/ssoins-0123456789abcdef
        ```

        :param str resource_name: The name of the resource.
        :param AccountAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AccountAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            AccountAssignmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 permission_set_arn: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[str]] = None,
                 target_id: Optional[pulumi.Input[str]] = None,
                 target_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AccountAssignmentArgs.__new__(AccountAssignmentArgs)

            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            if permission_set_arn is None and not opts.urn:
                raise TypeError("Missing required property 'permission_set_arn'")
            __props__.__dict__["permission_set_arn"] = permission_set_arn
            if principal_id is None and not opts.urn:
                raise TypeError("Missing required property 'principal_id'")
            __props__.__dict__["principal_id"] = principal_id
            if principal_type is None and not opts.urn:
                raise TypeError("Missing required property 'principal_type'")
            __props__.__dict__["principal_type"] = principal_type
            if target_id is None and not opts.urn:
                raise TypeError("Missing required property 'target_id'")
            __props__.__dict__["target_id"] = target_id
            __props__.__dict__["target_type"] = target_type
        super(AccountAssignment, __self__).__init__(
            'aws:ssoadmin/accountAssignment:AccountAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            instance_arn: Optional[pulumi.Input[str]] = None,
            permission_set_arn: Optional[pulumi.Input[str]] = None,
            principal_id: Optional[pulumi.Input[str]] = None,
            principal_type: Optional[pulumi.Input[str]] = None,
            target_id: Optional[pulumi.Input[str]] = None,
            target_type: Optional[pulumi.Input[str]] = None) -> 'AccountAssignment':
        """
        Get an existing AccountAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] instance_arn: The Amazon Resource Name (ARN) of the SSO Instance.
        :param pulumi.Input[str] permission_set_arn: The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        :param pulumi.Input[str] principal_id: An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        :param pulumi.Input[str] principal_type: The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        :param pulumi.Input[str] target_id: An AWS account identifier, typically a 10-12 digit string.
        :param pulumi.Input[str] target_type: The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _AccountAssignmentState.__new__(_AccountAssignmentState)

        __props__.__dict__["instance_arn"] = instance_arn
        __props__.__dict__["permission_set_arn"] = permission_set_arn
        __props__.__dict__["principal_id"] = principal_id
        __props__.__dict__["principal_type"] = principal_type
        __props__.__dict__["target_id"] = target_id
        __props__.__dict__["target_type"] = target_type
        return AccountAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the SSO Instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="permissionSetArn")
    def permission_set_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the Permission Set that the admin wants to grant the principal access to.
        """
        return pulumi.get(self, "permission_set_arn")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        An identifier for an object in SSO, such as a user or group. PrincipalIds are GUIDs (For example, `f81d4fae-7dec-11d0-a765-00a0c91e6bf6`).
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[str]:
        """
        The entity type for which the assignment will be created. Valid values: `USER`, `GROUP`.
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="targetId")
    def target_id(self) -> pulumi.Output[str]:
        """
        An AWS account identifier, typically a 10-12 digit string.
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="targetType")
    def target_type(self) -> pulumi.Output[Optional[str]]:
        """
        The entity type for which the assignment will be created. Valid values: `AWS_ACCOUNT`.
        """
        return pulumi.get(self, "target_type")


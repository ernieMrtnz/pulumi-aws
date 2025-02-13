# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ResolverQueryLogConfigAssociationArgs', 'ResolverQueryLogConfigAssociation']

@pulumi.input_type
class ResolverQueryLogConfigAssociationArgs:
    def __init__(__self__, *,
                 resolver_query_log_config_id: pulumi.Input[str],
                 resource_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a ResolverQueryLogConfigAssociation resource.
        :param pulumi.Input[str] resolver_query_log_config_id: The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        :param pulumi.Input[str] resource_id: The ID of a VPC that you want this query logging configuration to log queries for.
        """
        ResolverQueryLogConfigAssociationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resolver_query_log_config_id=resolver_query_log_config_id,
            resource_id=resource_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
             resource_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if resolver_query_log_config_id is None and 'resolverQueryLogConfigId' in kwargs:
            resolver_query_log_config_id = kwargs['resolverQueryLogConfigId']
        if resolver_query_log_config_id is None:
            raise TypeError("Missing 'resolver_query_log_config_id' argument")
        if resource_id is None and 'resourceId' in kwargs:
            resource_id = kwargs['resourceId']
        if resource_id is None:
            raise TypeError("Missing 'resource_id' argument")

        _setter("resolver_query_log_config_id", resolver_query_log_config_id)
        _setter("resource_id", resource_id)

    @property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> pulumi.Input[str]:
        """
        The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        """
        return pulumi.get(self, "resolver_query_log_config_id")

    @resolver_query_log_config_id.setter
    def resolver_query_log_config_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resolver_query_log_config_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Input[str]:
        """
        The ID of a VPC that you want this query logging configuration to log queries for.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_id", value)


@pulumi.input_type
class _ResolverQueryLogConfigAssociationState:
    def __init__(__self__, *,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ResolverQueryLogConfigAssociation resources.
        :param pulumi.Input[str] resolver_query_log_config_id: The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        :param pulumi.Input[str] resource_id: The ID of a VPC that you want this query logging configuration to log queries for.
        """
        _ResolverQueryLogConfigAssociationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            resolver_query_log_config_id=resolver_query_log_config_id,
            resource_id=resource_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
             resource_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if resolver_query_log_config_id is None and 'resolverQueryLogConfigId' in kwargs:
            resolver_query_log_config_id = kwargs['resolverQueryLogConfigId']
        if resource_id is None and 'resourceId' in kwargs:
            resource_id = kwargs['resourceId']

        if resolver_query_log_config_id is not None:
            _setter("resolver_query_log_config_id", resolver_query_log_config_id)
        if resource_id is not None:
            _setter("resource_id", resource_id)

    @property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        """
        return pulumi.get(self, "resolver_query_log_config_id")

    @resolver_query_log_config_id.setter
    def resolver_query_log_config_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resolver_query_log_config_id", value)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of a VPC that you want this query logging configuration to log queries for.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


class ResolverQueryLogConfigAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Route 53 Resolver query logging configuration association resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53.ResolverQueryLogConfigAssociation("example",
            resolver_query_log_config_id=aws_route53_resolver_query_log_config["example"]["id"],
            resource_id=aws_vpc["example"]["id"])
        ```

        ## Import

        Using `pulumi import`, import

        Route 53 Resolver query logging configuration associations using the Route 53 Resolver query logging configuration association ID. For example:

        ```sh
         $ pulumi import aws:route53/resolverQueryLogConfigAssociation:ResolverQueryLogConfigAssociation example rqlca-b320624fef3c4d70
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resolver_query_log_config_id: The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        :param pulumi.Input[str] resource_id: The ID of a VPC that you want this query logging configuration to log queries for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResolverQueryLogConfigAssociationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Route 53 Resolver query logging configuration association resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.route53.ResolverQueryLogConfigAssociation("example",
            resolver_query_log_config_id=aws_route53_resolver_query_log_config["example"]["id"],
            resource_id=aws_vpc["example"]["id"])
        ```

        ## Import

        Using `pulumi import`, import

        Route 53 Resolver query logging configuration associations using the Route 53 Resolver query logging configuration association ID. For example:

        ```sh
         $ pulumi import aws:route53/resolverQueryLogConfigAssociation:ResolverQueryLogConfigAssociation example rqlca-b320624fef3c4d70
        ```

        :param str resource_name: The name of the resource.
        :param ResolverQueryLogConfigAssociationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResolverQueryLogConfigAssociationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResolverQueryLogConfigAssociationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResolverQueryLogConfigAssociationArgs.__new__(ResolverQueryLogConfigAssociationArgs)

            if resolver_query_log_config_id is None and not opts.urn:
                raise TypeError("Missing required property 'resolver_query_log_config_id'")
            __props__.__dict__["resolver_query_log_config_id"] = resolver_query_log_config_id
            if resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'resource_id'")
            __props__.__dict__["resource_id"] = resource_id
        super(ResolverQueryLogConfigAssociation, __self__).__init__(
            'aws:route53/resolverQueryLogConfigAssociation:ResolverQueryLogConfigAssociation',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            resolver_query_log_config_id: Optional[pulumi.Input[str]] = None,
            resource_id: Optional[pulumi.Input[str]] = None) -> 'ResolverQueryLogConfigAssociation':
        """
        Get an existing ResolverQueryLogConfigAssociation resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] resolver_query_log_config_id: The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        :param pulumi.Input[str] resource_id: The ID of a VPC that you want this query logging configuration to log queries for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResolverQueryLogConfigAssociationState.__new__(_ResolverQueryLogConfigAssociationState)

        __props__.__dict__["resolver_query_log_config_id"] = resolver_query_log_config_id
        __props__.__dict__["resource_id"] = resource_id
        return ResolverQueryLogConfigAssociation(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="resolverQueryLogConfigId")
    def resolver_query_log_config_id(self) -> pulumi.Output[str]:
        """
        The ID of the Route 53 Resolver query logging configuration that you want to associate a VPC with.
        """
        return pulumi.get(self, "resolver_query_log_config_id")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[str]:
        """
        The ID of a VPC that you want this query logging configuration to log queries for.
        """
        return pulumi.get(self, "resource_id")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['MultiRegionAccessPointPolicyArgs', 'MultiRegionAccessPointPolicy']

@pulumi.input_type
class MultiRegionAccessPointPolicyArgs:
    def __init__(__self__, *,
                 details: pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs'],
                 account_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a MultiRegionAccessPointPolicy resource.
        :param pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs'] details: A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        :param pulumi.Input[str] account_id: The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        """
        MultiRegionAccessPointPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            details=details,
            account_id=account_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             details: Optional[pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']] = None,
             account_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if details is None:
            raise TypeError("Missing 'details' argument")
        if account_id is None and 'accountId' in kwargs:
            account_id = kwargs['accountId']

        _setter("details", details)
        if account_id is not None:
            _setter("account_id", account_id)

    @property
    @pulumi.getter
    def details(self) -> pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']:
        """
        A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)


@pulumi.input_type
class _MultiRegionAccessPointPolicyState:
    def __init__(__self__, *,
                 account_id: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']] = None,
                 established: Optional[pulumi.Input[str]] = None,
                 proposed: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering MultiRegionAccessPointPolicy resources.
        :param pulumi.Input[str] account_id: The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs'] details: A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        :param pulumi.Input[str] established: The last established policy for the Multi-Region Access Point.
        :param pulumi.Input[str] proposed: The proposed policy for the Multi-Region Access Point.
        """
        _MultiRegionAccessPointPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            account_id=account_id,
            details=details,
            established=established,
            proposed=proposed,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             account_id: Optional[pulumi.Input[str]] = None,
             details: Optional[pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']] = None,
             established: Optional[pulumi.Input[str]] = None,
             proposed: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if account_id is None and 'accountId' in kwargs:
            account_id = kwargs['accountId']

        if account_id is not None:
            _setter("account_id", account_id)
        if details is not None:
            _setter("details", details)
        if established is not None:
            _setter("established", established)
        if proposed is not None:
            _setter("proposed", proposed)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        """
        return pulumi.get(self, "account_id")

    @account_id.setter
    def account_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "account_id", value)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']]:
        """
        A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input['MultiRegionAccessPointPolicyDetailsArgs']]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter
    def established(self) -> Optional[pulumi.Input[str]]:
        """
        The last established policy for the Multi-Region Access Point.
        """
        return pulumi.get(self, "established")

    @established.setter
    def established(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "established", value)

    @property
    @pulumi.getter
    def proposed(self) -> Optional[pulumi.Input[str]]:
        """
        The proposed policy for the Multi-Region Access Point.
        """
        return pulumi.get(self, "proposed")

    @proposed.setter
    def proposed(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "proposed", value)


class MultiRegionAccessPointPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[pulumi.InputType['MultiRegionAccessPointPolicyDetailsArgs']]] = None,
                 __props__=None):
        """
        Provides a resource to manage an S3 Multi-Region Access Point access control policy.

        ## Example Usage
        ### Basic Example

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        current_caller_identity = aws.get_caller_identity()
        current_partition = aws.get_partition()
        foo_bucket = aws.s3.BucketV2("fooBucket")
        example_multi_region_access_point = aws.s3control.MultiRegionAccessPoint("exampleMultiRegionAccessPoint", details=aws.s3control.MultiRegionAccessPointDetailsArgs(
            name="example",
            regions=[aws.s3control.MultiRegionAccessPointDetailsRegionArgs(
                bucket=foo_bucket.id,
            )],
        ))
        example_multi_region_access_point_policy = aws.s3control.MultiRegionAccessPointPolicy("exampleMultiRegionAccessPointPolicy", details=aws.s3control.MultiRegionAccessPointPolicyDetailsArgs(
            name=example_multi_region_access_point.id.apply(lambda id: id.split(":"))[1],
            policy=example_multi_region_access_point.alias.apply(lambda alias: json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Sid": "Example",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": current_caller_identity.account_id,
                    },
                    "Action": [
                        "s3:GetObject",
                        "s3:PutObject",
                    ],
                    "Resource": f"arn:{current_partition.partition}:s3::{current_caller_identity.account_id}:accesspoint/{alias}/object/*",
                }],
            })),
        ))
        ```

        ## Import

        Using `pulumi import`, import Multi-Region Access Point Policies using the `account_id` and `name` of the Multi-Region Access Point separated by a colon (`:`). For example:

        ```sh
         $ pulumi import aws:s3control/multiRegionAccessPointPolicy:MultiRegionAccessPointPolicy example 123456789012:example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input[pulumi.InputType['MultiRegionAccessPointPolicyDetailsArgs']] details: A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: MultiRegionAccessPointPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource to manage an S3 Multi-Region Access Point access control policy.

        ## Example Usage
        ### Basic Example

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        current_caller_identity = aws.get_caller_identity()
        current_partition = aws.get_partition()
        foo_bucket = aws.s3.BucketV2("fooBucket")
        example_multi_region_access_point = aws.s3control.MultiRegionAccessPoint("exampleMultiRegionAccessPoint", details=aws.s3control.MultiRegionAccessPointDetailsArgs(
            name="example",
            regions=[aws.s3control.MultiRegionAccessPointDetailsRegionArgs(
                bucket=foo_bucket.id,
            )],
        ))
        example_multi_region_access_point_policy = aws.s3control.MultiRegionAccessPointPolicy("exampleMultiRegionAccessPointPolicy", details=aws.s3control.MultiRegionAccessPointPolicyDetailsArgs(
            name=example_multi_region_access_point.id.apply(lambda id: id.split(":"))[1],
            policy=example_multi_region_access_point.alias.apply(lambda alias: json.dumps({
                "Version": "2012-10-17",
                "Statement": [{
                    "Sid": "Example",
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": current_caller_identity.account_id,
                    },
                    "Action": [
                        "s3:GetObject",
                        "s3:PutObject",
                    ],
                    "Resource": f"arn:{current_partition.partition}:s3::{current_caller_identity.account_id}:accesspoint/{alias}/object/*",
                }],
            })),
        ))
        ```

        ## Import

        Using `pulumi import`, import Multi-Region Access Point Policies using the `account_id` and `name` of the Multi-Region Access Point separated by a colon (`:`). For example:

        ```sh
         $ pulumi import aws:s3control/multiRegionAccessPointPolicy:MultiRegionAccessPointPolicy example 123456789012:example
        ```

        :param str resource_name: The name of the resource.
        :param MultiRegionAccessPointPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(MultiRegionAccessPointPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            MultiRegionAccessPointPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_id: Optional[pulumi.Input[str]] = None,
                 details: Optional[pulumi.Input[pulumi.InputType['MultiRegionAccessPointPolicyDetailsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = MultiRegionAccessPointPolicyArgs.__new__(MultiRegionAccessPointPolicyArgs)

            __props__.__dict__["account_id"] = account_id
            details = _utilities.configure(details, MultiRegionAccessPointPolicyDetailsArgs, True)
            if details is None and not opts.urn:
                raise TypeError("Missing required property 'details'")
            __props__.__dict__["details"] = details
            __props__.__dict__["established"] = None
            __props__.__dict__["proposed"] = None
        super(MultiRegionAccessPointPolicy, __self__).__init__(
            'aws:s3control/multiRegionAccessPointPolicy:MultiRegionAccessPointPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            account_id: Optional[pulumi.Input[str]] = None,
            details: Optional[pulumi.Input[pulumi.InputType['MultiRegionAccessPointPolicyDetailsArgs']]] = None,
            established: Optional[pulumi.Input[str]] = None,
            proposed: Optional[pulumi.Input[str]] = None) -> 'MultiRegionAccessPointPolicy':
        """
        Get an existing MultiRegionAccessPointPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_id: The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        :param pulumi.Input[pulumi.InputType['MultiRegionAccessPointPolicyDetailsArgs']] details: A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        :param pulumi.Input[str] established: The last established policy for the Multi-Region Access Point.
        :param pulumi.Input[str] proposed: The proposed policy for the Multi-Region Access Point.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _MultiRegionAccessPointPolicyState.__new__(_MultiRegionAccessPointPolicyState)

        __props__.__dict__["account_id"] = account_id
        __props__.__dict__["details"] = details
        __props__.__dict__["established"] = established
        __props__.__dict__["proposed"] = proposed
        return MultiRegionAccessPointPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> pulumi.Output[str]:
        """
        The AWS account ID for the owner of the Multi-Region Access Point. Defaults to automatically determined account ID of the AWS provider.
        """
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def details(self) -> pulumi.Output['outputs.MultiRegionAccessPointPolicyDetails']:
        """
        A configuration block containing details about the policy for the Multi-Region Access Point. See Details Configuration Block below for more details
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter
    def established(self) -> pulumi.Output[str]:
        """
        The last established policy for the Multi-Region Access Point.
        """
        return pulumi.get(self, "established")

    @property
    @pulumi.getter
    def proposed(self) -> pulumi.Output[str]:
        """
        The proposed policy for the Multi-Region Access Point.
        """
        return pulumi.get(self, "proposed")


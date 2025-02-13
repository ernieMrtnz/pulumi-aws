# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BucketResourceAccessArgs', 'BucketResourceAccess']

@pulumi.input_type
class BucketResourceAccessArgs:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a BucketResourceAccess resource.
        :param pulumi.Input[str] bucket_name: The name of the bucket to grant access to.
        :param pulumi.Input[str] resource_name: The name of the resource to be granted bucket access.
        """
        BucketResourceAccessArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_name=bucket_name,
            resource_name=resource_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_name: Optional[pulumi.Input[str]] = None,
             resource_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if bucket_name is None and 'bucketName' in kwargs:
            bucket_name = kwargs['bucketName']
        if bucket_name is None:
            raise TypeError("Missing 'bucket_name' argument")
        if resource_name is None and 'resourceName' in kwargs:
            resource_name = kwargs['resourceName']
        if resource_name is None:
            raise TypeError("Missing 'resource_name' argument")

        _setter("bucket_name", bucket_name)
        _setter("resource_name", resource_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        The name of the bucket to grant access to.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the resource to be granted bucket access.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)


@pulumi.input_type
class _BucketResourceAccessState:
    def __init__(__self__, *,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 resource_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BucketResourceAccess resources.
        :param pulumi.Input[str] bucket_name: The name of the bucket to grant access to.
        :param pulumi.Input[str] resource_name: The name of the resource to be granted bucket access.
        """
        _BucketResourceAccessState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_name=bucket_name,
            resource_name=resource_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_name: Optional[pulumi.Input[str]] = None,
             resource_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if bucket_name is None and 'bucketName' in kwargs:
            bucket_name = kwargs['bucketName']
        if resource_name is None and 'resourceName' in kwargs:
            resource_name = kwargs['resourceName']

        if bucket_name is not None:
            _setter("bucket_name", bucket_name)
        if resource_name is not None:
            _setter("resource_name", resource_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the bucket to grant access to.
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource to be granted bucket access.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_name", value)


class BucketResourceAccess(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a lightsail resource access to a bucket.

        ## Import

        Using `pulumi import`, import `aws_lightsail_bucket_resource_access` using the `id` attribute. For example:

        ```sh
         $ pulumi import aws:lightsail/bucketResourceAccess:BucketResourceAccess test example-bucket,example-instance
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: The name of the bucket to grant access to.
        :param pulumi.Input[str] resource_name_: The name of the resource to be granted bucket access.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketResourceAccessArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a lightsail resource access to a bucket.

        ## Import

        Using `pulumi import`, import `aws_lightsail_bucket_resource_access` using the `id` attribute. For example:

        ```sh
         $ pulumi import aws:lightsail/bucketResourceAccess:BucketResourceAccess test example-bucket,example-instance
        ```

        :param str resource_name: The name of the resource.
        :param BucketResourceAccessArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketResourceAccessArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BucketResourceAccessArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BucketResourceAccessArgs.__new__(BucketResourceAccessArgs)

            if bucket_name is None and not opts.urn:
                raise TypeError("Missing required property 'bucket_name'")
            __props__.__dict__["bucket_name"] = bucket_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
        super(BucketResourceAccess, __self__).__init__(
            'aws:lightsail/bucketResourceAccess:BucketResourceAccess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket_name: Optional[pulumi.Input[str]] = None,
            resource_name_: Optional[pulumi.Input[str]] = None) -> 'BucketResourceAccess':
        """
        Get an existing BucketResourceAccess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket_name: The name of the bucket to grant access to.
        :param pulumi.Input[str] resource_name_: The name of the resource to be granted bucket access.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketResourceAccessState.__new__(_BucketResourceAccessState)

        __props__.__dict__["bucket_name"] = bucket_name
        __props__.__dict__["resource_name"] = resource_name_
        return BucketResourceAccess(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[str]:
        """
        The name of the bucket to grant access to.
        """
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Output[str]:
        """
        The name of the resource to be granted bucket access.
        """
        return pulumi.get(self, "resource_name")


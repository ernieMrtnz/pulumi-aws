# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ImageBlockPublicAccessArgs', 'ImageBlockPublicAccess']

@pulumi.input_type
class ImageBlockPublicAccessArgs:
    def __init__(__self__, *,
                 state: pulumi.Input[str]):
        """
        The set of arguments for constructing a ImageBlockPublicAccess resource.
        :param pulumi.Input[str] state: The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        ImageBlockPublicAccessArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            state=state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             state: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if state is None:
            raise TypeError("Missing 'state' argument")

        _setter("state", state)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Input[str]:
        """
        The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: pulumi.Input[str]):
        pulumi.set(self, "state", value)


@pulumi.input_type
class _ImageBlockPublicAccessState:
    def __init__(__self__, *,
                 state: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ImageBlockPublicAccess resources.
        :param pulumi.Input[str] state: The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        _ImageBlockPublicAccessState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            state=state,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             state: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if state is not None:
            _setter("state", state)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)


class ImageBlockPublicAccess(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a regional public access block for AMIs. This prevents AMIs from being made publicly accessible.
        If you already have public AMIs, they will remain publicly available.

        > **NOTE:** Deleting this resource does not change the block public access value, the resource in simply removed from state instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Prevent making AMIs publicly accessible in the region and account for which the provider is configured
        test = aws.ec2.ImageBlockPublicAccess("test", state="block-new-sharing")
        ```

        ## Import

        You cannot import this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] state: The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageBlockPublicAccessArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a regional public access block for AMIs. This prevents AMIs from being made publicly accessible.
        If you already have public AMIs, they will remain publicly available.

        > **NOTE:** Deleting this resource does not change the block public access value, the resource in simply removed from state instead.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        # Prevent making AMIs publicly accessible in the region and account for which the provider is configured
        test = aws.ec2.ImageBlockPublicAccess("test", state="block-new-sharing")
        ```

        ## Import

        You cannot import this resource.

        :param str resource_name: The name of the resource.
        :param ImageBlockPublicAccessArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageBlockPublicAccessArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ImageBlockPublicAccessArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageBlockPublicAccessArgs.__new__(ImageBlockPublicAccessArgs)

            if state is None and not opts.urn:
                raise TypeError("Missing required property 'state'")
            __props__.__dict__["state"] = state
        super(ImageBlockPublicAccess, __self__).__init__(
            'aws:ec2/imageBlockPublicAccess:ImageBlockPublicAccess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            state: Optional[pulumi.Input[str]] = None) -> 'ImageBlockPublicAccess':
        """
        Get an existing ImageBlockPublicAccess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] state: The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ImageBlockPublicAccessState.__new__(_ImageBlockPublicAccessState)

        __props__.__dict__["state"] = state
        return ImageBlockPublicAccess(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of block public access for AMIs at the account level in the configured AWS Region. Valid values: `unblocked` and `block-new-sharing`.
        """
        return pulumi.get(self, "state")


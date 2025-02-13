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

__all__ = ['CustomRoutingListenerArgs', 'CustomRoutingListener']

@pulumi.input_type
class CustomRoutingListenerArgs:
    def __init__(__self__, *,
                 accelerator_arn: pulumi.Input[str],
                 port_ranges: pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]):
        """
        The set of arguments for constructing a CustomRoutingListener resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of a custom routing accelerator.
        :param pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        CustomRoutingListenerArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerator_arn=accelerator_arn,
            port_ranges=port_ranges,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerator_arn: Optional[pulumi.Input[str]] = None,
             port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if accelerator_arn is None and 'acceleratorArn' in kwargs:
            accelerator_arn = kwargs['acceleratorArn']
        if accelerator_arn is None:
            raise TypeError("Missing 'accelerator_arn' argument")
        if port_ranges is None and 'portRanges' in kwargs:
            port_ranges = kwargs['portRanges']
        if port_ranges is None:
            raise TypeError("Missing 'port_ranges' argument")

        _setter("accelerator_arn", accelerator_arn)
        _setter("port_ranges", port_ranges)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of a custom routing accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @accelerator_arn.setter
    def accelerator_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "accelerator_arn", value)

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]:
        """
        The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        return pulumi.get(self, "port_ranges")

    @port_ranges.setter
    def port_ranges(self, value: pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]):
        pulumi.set(self, "port_ranges", value)


@pulumi.input_type
class _CustomRoutingListenerState:
    def __init__(__self__, *,
                 accelerator_arn: Optional[pulumi.Input[str]] = None,
                 port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]] = None):
        """
        Input properties used for looking up and filtering CustomRoutingListener resources.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of a custom routing accelerator.
        :param pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        _CustomRoutingListenerState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accelerator_arn=accelerator_arn,
            port_ranges=port_ranges,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accelerator_arn: Optional[pulumi.Input[str]] = None,
             port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if accelerator_arn is None and 'acceleratorArn' in kwargs:
            accelerator_arn = kwargs['acceleratorArn']
        if port_ranges is None and 'portRanges' in kwargs:
            port_ranges = kwargs['portRanges']

        if accelerator_arn is not None:
            _setter("accelerator_arn", accelerator_arn)
        if port_ranges is not None:
            _setter("port_ranges", port_ranges)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of a custom routing accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @accelerator_arn.setter
    def accelerator_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "accelerator_arn", value)

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]]:
        """
        The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        return pulumi.get(self, "port_ranges")

    @port_ranges.setter
    def port_ranges(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['CustomRoutingListenerPortRangeArgs']]]]):
        pulumi.set(self, "port_ranges", value)


class CustomRoutingListener(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_arn: Optional[pulumi.Input[str]] = None,
                 port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRoutingListenerPortRangeArgs']]]]] = None,
                 __props__=None):
        """
        Provides a Global Accelerator custom routing listener.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_custom_routing_accelerator = aws.globalaccelerator.CustomRoutingAccelerator("exampleCustomRoutingAccelerator",
            ip_address_type="IPV4",
            enabled=True,
            attributes=aws.globalaccelerator.CustomRoutingAcceleratorAttributesArgs(
                flow_logs_enabled=True,
                flow_logs_s3_bucket="example-bucket",
                flow_logs_s3_prefix="flow-logs/",
            ))
        example_custom_routing_listener = aws.globalaccelerator.CustomRoutingListener("exampleCustomRoutingListener",
            accelerator_arn=example_custom_routing_accelerator.id,
            port_ranges=[aws.globalaccelerator.CustomRoutingListenerPortRangeArgs(
                from_port=80,
                to_port=80,
            )])
        ```

        ## Import

        Using `pulumi import`, import Global Accelerator custom routing listeners using the `id`. For example:

        ```sh
         $ pulumi import aws:globalaccelerator/customRoutingListener:CustomRoutingListener example arn:aws:globalaccelerator::111111111111:accelerator/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/listener/xxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of a custom routing accelerator.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRoutingListenerPortRangeArgs']]]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomRoutingListenerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Global Accelerator custom routing listener.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_custom_routing_accelerator = aws.globalaccelerator.CustomRoutingAccelerator("exampleCustomRoutingAccelerator",
            ip_address_type="IPV4",
            enabled=True,
            attributes=aws.globalaccelerator.CustomRoutingAcceleratorAttributesArgs(
                flow_logs_enabled=True,
                flow_logs_s3_bucket="example-bucket",
                flow_logs_s3_prefix="flow-logs/",
            ))
        example_custom_routing_listener = aws.globalaccelerator.CustomRoutingListener("exampleCustomRoutingListener",
            accelerator_arn=example_custom_routing_accelerator.id,
            port_ranges=[aws.globalaccelerator.CustomRoutingListenerPortRangeArgs(
                from_port=80,
                to_port=80,
            )])
        ```

        ## Import

        Using `pulumi import`, import Global Accelerator custom routing listeners using the `id`. For example:

        ```sh
         $ pulumi import aws:globalaccelerator/customRoutingListener:CustomRoutingListener example arn:aws:globalaccelerator::111111111111:accelerator/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/listener/xxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param CustomRoutingListenerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomRoutingListenerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            CustomRoutingListenerArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 accelerator_arn: Optional[pulumi.Input[str]] = None,
                 port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRoutingListenerPortRangeArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomRoutingListenerArgs.__new__(CustomRoutingListenerArgs)

            if accelerator_arn is None and not opts.urn:
                raise TypeError("Missing required property 'accelerator_arn'")
            __props__.__dict__["accelerator_arn"] = accelerator_arn
            if port_ranges is None and not opts.urn:
                raise TypeError("Missing required property 'port_ranges'")
            __props__.__dict__["port_ranges"] = port_ranges
        super(CustomRoutingListener, __self__).__init__(
            'aws:globalaccelerator/customRoutingListener:CustomRoutingListener',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            accelerator_arn: Optional[pulumi.Input[str]] = None,
            port_ranges: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRoutingListenerPortRangeArgs']]]]] = None) -> 'CustomRoutingListener':
        """
        Get an existing CustomRoutingListener resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] accelerator_arn: The Amazon Resource Name (ARN) of a custom routing accelerator.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['CustomRoutingListenerPortRangeArgs']]]] port_ranges: The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _CustomRoutingListenerState.__new__(_CustomRoutingListenerState)

        __props__.__dict__["accelerator_arn"] = accelerator_arn
        __props__.__dict__["port_ranges"] = port_ranges
        return CustomRoutingListener(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="acceleratorArn")
    def accelerator_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of a custom routing accelerator.
        """
        return pulumi.get(self, "accelerator_arn")

    @property
    @pulumi.getter(name="portRanges")
    def port_ranges(self) -> pulumi.Output[Sequence['outputs.CustomRoutingListenerPortRange']]:
        """
        The list of port ranges for the connections from clients to the accelerator. Fields documented below.
        """
        return pulumi.get(self, "port_ranges")


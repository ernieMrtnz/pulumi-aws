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

__all__ = ['DeviceArgs', 'Device']

@pulumi.input_type
class DeviceArgs:
    def __init__(__self__, *,
                 global_network_id: pulumi.Input[str],
                 aws_location: Optional[pulumi.Input['DeviceAwsLocationArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input['DeviceLocationArgs']] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Device resource.
        :param pulumi.Input[str] global_network_id: The ID of the global network.
        :param pulumi.Input['DeviceAwsLocationArgs'] aws_location: The AWS location of the device. Documented below.
        :param pulumi.Input[str] description: A description of the device.
        :param pulumi.Input['DeviceLocationArgs'] location: The location of the device. Documented below.
        :param pulumi.Input[str] model: The model of device.
        :param pulumi.Input[str] serial_number: The serial number of the device.
        :param pulumi.Input[str] site_id: The ID of the site.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] type: The type of device.
        :param pulumi.Input[str] vendor: The vendor of the device.
        """
        DeviceArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            global_network_id=global_network_id,
            aws_location=aws_location,
            description=description,
            location=location,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            tags=tags,
            type=type,
            vendor=vendor,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             global_network_id: Optional[pulumi.Input[str]] = None,
             aws_location: Optional[pulumi.Input['DeviceAwsLocationArgs']] = None,
             description: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input['DeviceLocationArgs']] = None,
             model: Optional[pulumi.Input[str]] = None,
             serial_number: Optional[pulumi.Input[str]] = None,
             site_id: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             type: Optional[pulumi.Input[str]] = None,
             vendor: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if global_network_id is None and 'globalNetworkId' in kwargs:
            global_network_id = kwargs['globalNetworkId']
        if global_network_id is None:
            raise TypeError("Missing 'global_network_id' argument")
        if aws_location is None and 'awsLocation' in kwargs:
            aws_location = kwargs['awsLocation']
        if serial_number is None and 'serialNumber' in kwargs:
            serial_number = kwargs['serialNumber']
        if site_id is None and 'siteId' in kwargs:
            site_id = kwargs['siteId']

        _setter("global_network_id", global_network_id)
        if aws_location is not None:
            _setter("aws_location", aws_location)
        if description is not None:
            _setter("description", description)
        if location is not None:
            _setter("location", location)
        if model is not None:
            _setter("model", model)
        if serial_number is not None:
            _setter("serial_number", serial_number)
        if site_id is not None:
            _setter("site_id", site_id)
        if tags is not None:
            _setter("tags", tags)
        if type is not None:
            _setter("type", type)
        if vendor is not None:
            _setter("vendor", vendor)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Input[str]:
        """
        The ID of the global network.
        """
        return pulumi.get(self, "global_network_id")

    @global_network_id.setter
    def global_network_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "global_network_id", value)

    @property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> Optional[pulumi.Input['DeviceAwsLocationArgs']]:
        """
        The AWS location of the device. Documented below.
        """
        return pulumi.get(self, "aws_location")

    @aws_location.setter
    def aws_location(self, value: Optional[pulumi.Input['DeviceAwsLocationArgs']]):
        pulumi.set(self, "aws_location", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the device.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input['DeviceLocationArgs']]:
        """
        The location of the device. Documented below.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input['DeviceLocationArgs']]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        The model of device.
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[str]]:
        """
        The serial number of the device.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the site.
        """
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of device.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[str]]:
        """
        The vendor of the device.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vendor", value)


@pulumi.input_type
class _DeviceState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 aws_location: Optional[pulumi.Input['DeviceAwsLocationArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input['DeviceLocationArgs']] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Device resources.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the device.
        :param pulumi.Input['DeviceAwsLocationArgs'] aws_location: The AWS location of the device. Documented below.
        :param pulumi.Input[str] description: A description of the device.
        :param pulumi.Input[str] global_network_id: The ID of the global network.
        :param pulumi.Input['DeviceLocationArgs'] location: The location of the device. Documented below.
        :param pulumi.Input[str] model: The model of device.
        :param pulumi.Input[str] serial_number: The serial number of the device.
        :param pulumi.Input[str] site_id: The ID of the site.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] type: The type of device.
        :param pulumi.Input[str] vendor: The vendor of the device.
        """
        _DeviceState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            aws_location=aws_location,
            description=description,
            global_network_id=global_network_id,
            location=location,
            model=model,
            serial_number=serial_number,
            site_id=site_id,
            tags=tags,
            tags_all=tags_all,
            type=type,
            vendor=vendor,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[pulumi.Input[str]] = None,
             aws_location: Optional[pulumi.Input['DeviceAwsLocationArgs']] = None,
             description: Optional[pulumi.Input[str]] = None,
             global_network_id: Optional[pulumi.Input[str]] = None,
             location: Optional[pulumi.Input['DeviceLocationArgs']] = None,
             model: Optional[pulumi.Input[str]] = None,
             serial_number: Optional[pulumi.Input[str]] = None,
             site_id: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             type: Optional[pulumi.Input[str]] = None,
             vendor: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if aws_location is None and 'awsLocation' in kwargs:
            aws_location = kwargs['awsLocation']
        if global_network_id is None and 'globalNetworkId' in kwargs:
            global_network_id = kwargs['globalNetworkId']
        if serial_number is None and 'serialNumber' in kwargs:
            serial_number = kwargs['serialNumber']
        if site_id is None and 'siteId' in kwargs:
            site_id = kwargs['siteId']
        if tags_all is None and 'tagsAll' in kwargs:
            tags_all = kwargs['tagsAll']

        if arn is not None:
            _setter("arn", arn)
        if aws_location is not None:
            _setter("aws_location", aws_location)
        if description is not None:
            _setter("description", description)
        if global_network_id is not None:
            _setter("global_network_id", global_network_id)
        if location is not None:
            _setter("location", location)
        if model is not None:
            _setter("model", model)
        if serial_number is not None:
            _setter("serial_number", serial_number)
        if site_id is not None:
            _setter("site_id", site_id)
        if tags is not None:
            _setter("tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            _setter("tags_all", tags_all)
        if type is not None:
            _setter("type", type)
        if vendor is not None:
            _setter("vendor", vendor)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the device.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> Optional[pulumi.Input['DeviceAwsLocationArgs']]:
        """
        The AWS location of the device. Documented below.
        """
        return pulumi.get(self, "aws_location")

    @aws_location.setter
    def aws_location(self, value: Optional[pulumi.Input['DeviceAwsLocationArgs']]):
        pulumi.set(self, "aws_location", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the device.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the global network.
        """
        return pulumi.get(self, "global_network_id")

    @global_network_id.setter
    def global_network_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_network_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input['DeviceLocationArgs']]:
        """
        The location of the device. Documented below.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input['DeviceLocationArgs']]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[str]]:
        """
        The model of device.
        """
        return pulumi.get(self, "model")

    @model.setter
    def model(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> Optional[pulumi.Input[str]]:
        """
        The serial number of the device.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the site.
        """
        return pulumi.get(self, "site_id")

    @site_id.setter
    def site_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
        pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")

        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of device.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def vendor(self) -> Optional[pulumi.Input[str]]:
        """
        The vendor of the device.
        """
        return pulumi.get(self, "vendor")

    @vendor.setter
    def vendor(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vendor", value)


class Device(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_location: Optional[pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['DeviceLocationArgs']]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a device in a global network. If you specify both a site ID and a location,
        the location of the site is used for visualization in the Network Manager console.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.Device("example",
            global_network_id=aws_networkmanager_global_network["example"]["id"],
            site_id=aws_networkmanager_site["example"]["id"])
        ```

        ## Import

        Using `pulumi import`, import `aws_networkmanager_device` using the device ARN. For example:

        ```sh
         $ pulumi import aws:networkmanager/device:Device example arn:aws:networkmanager::123456789012:device/global-network-0d47f6t230mz46dy4/device-07f6fd08867abc123
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']] aws_location: The AWS location of the device. Documented below.
        :param pulumi.Input[str] description: A description of the device.
        :param pulumi.Input[str] global_network_id: The ID of the global network.
        :param pulumi.Input[pulumi.InputType['DeviceLocationArgs']] location: The location of the device. Documented below.
        :param pulumi.Input[str] model: The model of device.
        :param pulumi.Input[str] serial_number: The serial number of the device.
        :param pulumi.Input[str] site_id: The ID of the site.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[str] type: The type of device.
        :param pulumi.Input[str] vendor: The vendor of the device.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeviceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a device in a global network. If you specify both a site ID and a location,
        the location of the site is used for visualization in the Network Manager console.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.networkmanager.Device("example",
            global_network_id=aws_networkmanager_global_network["example"]["id"],
            site_id=aws_networkmanager_site["example"]["id"])
        ```

        ## Import

        Using `pulumi import`, import `aws_networkmanager_device` using the device ARN. For example:

        ```sh
         $ pulumi import aws:networkmanager/device:Device example arn:aws:networkmanager::123456789012:device/global-network-0d47f6t230mz46dy4/device-07f6fd08867abc123
        ```

        :param str resource_name: The name of the resource.
        :param DeviceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeviceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DeviceArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aws_location: Optional[pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 global_network_id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[pulumi.InputType['DeviceLocationArgs']]] = None,
                 model: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 site_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vendor: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeviceArgs.__new__(DeviceArgs)

            aws_location = _utilities.configure(aws_location, DeviceAwsLocationArgs, True)
            __props__.__dict__["aws_location"] = aws_location
            __props__.__dict__["description"] = description
            if global_network_id is None and not opts.urn:
                raise TypeError("Missing required property 'global_network_id'")
            __props__.__dict__["global_network_id"] = global_network_id
            location = _utilities.configure(location, DeviceLocationArgs, True)
            __props__.__dict__["location"] = location
            __props__.__dict__["model"] = model
            __props__.__dict__["serial_number"] = serial_number
            __props__.__dict__["site_id"] = site_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            __props__.__dict__["vendor"] = vendor
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["tagsAll"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Device, __self__).__init__(
            'aws:networkmanager/device:Device',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            aws_location: Optional[pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']]] = None,
            description: Optional[pulumi.Input[str]] = None,
            global_network_id: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[pulumi.InputType['DeviceLocationArgs']]] = None,
            model: Optional[pulumi.Input[str]] = None,
            serial_number: Optional[pulumi.Input[str]] = None,
            site_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vendor: Optional[pulumi.Input[str]] = None) -> 'Device':
        """
        Get an existing Device resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the device.
        :param pulumi.Input[pulumi.InputType['DeviceAwsLocationArgs']] aws_location: The AWS location of the device. Documented below.
        :param pulumi.Input[str] description: A description of the device.
        :param pulumi.Input[str] global_network_id: The ID of the global network.
        :param pulumi.Input[pulumi.InputType['DeviceLocationArgs']] location: The location of the device. Documented below.
        :param pulumi.Input[str] model: The model of device.
        :param pulumi.Input[str] serial_number: The serial number of the device.
        :param pulumi.Input[str] site_id: The ID of the site.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        :param pulumi.Input[str] type: The type of device.
        :param pulumi.Input[str] vendor: The vendor of the device.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DeviceState.__new__(_DeviceState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["aws_location"] = aws_location
        __props__.__dict__["description"] = description
        __props__.__dict__["global_network_id"] = global_network_id
        __props__.__dict__["location"] = location
        __props__.__dict__["model"] = model
        __props__.__dict__["serial_number"] = serial_number
        __props__.__dict__["site_id"] = site_id
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        __props__.__dict__["type"] = type
        __props__.__dict__["vendor"] = vendor
        return Device(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the device.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="awsLocation")
    def aws_location(self) -> pulumi.Output[Optional['outputs.DeviceAwsLocation']]:
        """
        The AWS location of the device. Documented below.
        """
        return pulumi.get(self, "aws_location")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the device.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="globalNetworkId")
    def global_network_id(self) -> pulumi.Output[str]:
        """
        The ID of the global network.
        """
        return pulumi.get(self, "global_network_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional['outputs.DeviceLocation']]:
        """
        The location of the device. Documented below.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def model(self) -> pulumi.Output[Optional[str]]:
        """
        The model of device.
        """
        return pulumi.get(self, "model")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[Optional[str]]:
        """
        The serial number of the device.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the site.
        """
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Key-value tags for the device. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
        pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")

        return pulumi.get(self, "tags_all")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of device.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def vendor(self) -> pulumi.Output[Optional[str]]:
        """
        The vendor of the device.
        """
        return pulumi.get(self, "vendor")


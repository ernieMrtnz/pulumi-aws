# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['InstanceTrustProviderAttachmentArgs', 'InstanceTrustProviderAttachment']

@pulumi.input_type
class InstanceTrustProviderAttachmentArgs:
    def __init__(__self__, *,
                 verifiedaccess_instance_id: pulumi.Input[str],
                 verifiedaccess_trust_provider_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a InstanceTrustProviderAttachment resource.
        :param pulumi.Input[str] verifiedaccess_instance_id: The ID of the Verified Access instance to attach the Trust Provider to.
        :param pulumi.Input[str] verifiedaccess_trust_provider_id: The ID of the Verified Access trust provider.
        """
        InstanceTrustProviderAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            verifiedaccess_instance_id=verifiedaccess_instance_id,
            verifiedaccess_trust_provider_id=verifiedaccess_trust_provider_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             verifiedaccess_instance_id: Optional[pulumi.Input[str]] = None,
             verifiedaccess_trust_provider_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if verifiedaccess_instance_id is None and 'verifiedaccessInstanceId' in kwargs:
            verifiedaccess_instance_id = kwargs['verifiedaccessInstanceId']
        if verifiedaccess_instance_id is None:
            raise TypeError("Missing 'verifiedaccess_instance_id' argument")
        if verifiedaccess_trust_provider_id is None and 'verifiedaccessTrustProviderId' in kwargs:
            verifiedaccess_trust_provider_id = kwargs['verifiedaccessTrustProviderId']
        if verifiedaccess_trust_provider_id is None:
            raise TypeError("Missing 'verifiedaccess_trust_provider_id' argument")

        _setter("verifiedaccess_instance_id", verifiedaccess_instance_id)
        _setter("verifiedaccess_trust_provider_id", verifiedaccess_trust_provider_id)

    @property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> pulumi.Input[str]:
        """
        The ID of the Verified Access instance to attach the Trust Provider to.
        """
        return pulumi.get(self, "verifiedaccess_instance_id")

    @verifiedaccess_instance_id.setter
    def verifiedaccess_instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "verifiedaccess_instance_id", value)

    @property
    @pulumi.getter(name="verifiedaccessTrustProviderId")
    def verifiedaccess_trust_provider_id(self) -> pulumi.Input[str]:
        """
        The ID of the Verified Access trust provider.
        """
        return pulumi.get(self, "verifiedaccess_trust_provider_id")

    @verifiedaccess_trust_provider_id.setter
    def verifiedaccess_trust_provider_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "verifiedaccess_trust_provider_id", value)


@pulumi.input_type
class _InstanceTrustProviderAttachmentState:
    def __init__(__self__, *,
                 verifiedaccess_instance_id: Optional[pulumi.Input[str]] = None,
                 verifiedaccess_trust_provider_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering InstanceTrustProviderAttachment resources.
        :param pulumi.Input[str] verifiedaccess_instance_id: The ID of the Verified Access instance to attach the Trust Provider to.
        :param pulumi.Input[str] verifiedaccess_trust_provider_id: The ID of the Verified Access trust provider.
        """
        _InstanceTrustProviderAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            verifiedaccess_instance_id=verifiedaccess_instance_id,
            verifiedaccess_trust_provider_id=verifiedaccess_trust_provider_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             verifiedaccess_instance_id: Optional[pulumi.Input[str]] = None,
             verifiedaccess_trust_provider_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if verifiedaccess_instance_id is None and 'verifiedaccessInstanceId' in kwargs:
            verifiedaccess_instance_id = kwargs['verifiedaccessInstanceId']
        if verifiedaccess_trust_provider_id is None and 'verifiedaccessTrustProviderId' in kwargs:
            verifiedaccess_trust_provider_id = kwargs['verifiedaccessTrustProviderId']

        if verifiedaccess_instance_id is not None:
            _setter("verifiedaccess_instance_id", verifiedaccess_instance_id)
        if verifiedaccess_trust_provider_id is not None:
            _setter("verifiedaccess_trust_provider_id", verifiedaccess_trust_provider_id)

    @property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Verified Access instance to attach the Trust Provider to.
        """
        return pulumi.get(self, "verifiedaccess_instance_id")

    @verifiedaccess_instance_id.setter
    def verifiedaccess_instance_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verifiedaccess_instance_id", value)

    @property
    @pulumi.getter(name="verifiedaccessTrustProviderId")
    def verifiedaccess_trust_provider_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Verified Access trust provider.
        """
        return pulumi.get(self, "verifiedaccess_trust_provider_id")

    @verifiedaccess_trust_provider_id.setter
    def verifiedaccess_trust_provider_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "verifiedaccess_trust_provider_id", value)


class InstanceTrustProviderAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 verifiedaccess_instance_id: Optional[pulumi.Input[str]] = None,
                 verifiedaccess_trust_provider_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource for managing a Verified Access Instance Trust Provider Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_instance = aws.verifiedaccess.Instance("exampleInstance")
        example_trust_provider = aws.verifiedaccess.TrustProvider("exampleTrustProvider",
            device_trust_provider_type="jamf",
            policy_reference_name="example",
            trust_provider_type="device",
            device_options=aws.verifiedaccess.TrustProviderDeviceOptionsArgs(
                tenant_id="example",
            ))
        example_instance_trust_provider_attachment = aws.verifiedaccess.InstanceTrustProviderAttachment("exampleInstanceTrustProviderAttachment",
            verifiedaccess_instance_id=example_instance.id,
            verifiedaccess_trust_provider_id=example_trust_provider.id)
        ```

        ## Import

        Using `pulumi import`, import Verified Access Instance Trust Provider Attachments using the `verifiedaccess_instance_id` and `verifiedaccess_trust_provider_id` separated by a forward slash (`/`). For example:

        ```sh
         $ pulumi import aws:verifiedaccess/instanceTrustProviderAttachment:InstanceTrustProviderAttachment example vai-1234567890abcdef0/vatp-8012925589
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] verifiedaccess_instance_id: The ID of the Verified Access instance to attach the Trust Provider to.
        :param pulumi.Input[str] verifiedaccess_trust_provider_id: The ID of the Verified Access trust provider.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InstanceTrustProviderAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource for managing a Verified Access Instance Trust Provider Attachment.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_instance = aws.verifiedaccess.Instance("exampleInstance")
        example_trust_provider = aws.verifiedaccess.TrustProvider("exampleTrustProvider",
            device_trust_provider_type="jamf",
            policy_reference_name="example",
            trust_provider_type="device",
            device_options=aws.verifiedaccess.TrustProviderDeviceOptionsArgs(
                tenant_id="example",
            ))
        example_instance_trust_provider_attachment = aws.verifiedaccess.InstanceTrustProviderAttachment("exampleInstanceTrustProviderAttachment",
            verifiedaccess_instance_id=example_instance.id,
            verifiedaccess_trust_provider_id=example_trust_provider.id)
        ```

        ## Import

        Using `pulumi import`, import Verified Access Instance Trust Provider Attachments using the `verifiedaccess_instance_id` and `verifiedaccess_trust_provider_id` separated by a forward slash (`/`). For example:

        ```sh
         $ pulumi import aws:verifiedaccess/instanceTrustProviderAttachment:InstanceTrustProviderAttachment example vai-1234567890abcdef0/vatp-8012925589
        ```

        :param str resource_name: The name of the resource.
        :param InstanceTrustProviderAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InstanceTrustProviderAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            InstanceTrustProviderAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 verifiedaccess_instance_id: Optional[pulumi.Input[str]] = None,
                 verifiedaccess_trust_provider_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InstanceTrustProviderAttachmentArgs.__new__(InstanceTrustProviderAttachmentArgs)

            if verifiedaccess_instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'verifiedaccess_instance_id'")
            __props__.__dict__["verifiedaccess_instance_id"] = verifiedaccess_instance_id
            if verifiedaccess_trust_provider_id is None and not opts.urn:
                raise TypeError("Missing required property 'verifiedaccess_trust_provider_id'")
            __props__.__dict__["verifiedaccess_trust_provider_id"] = verifiedaccess_trust_provider_id
        super(InstanceTrustProviderAttachment, __self__).__init__(
            'aws:verifiedaccess/instanceTrustProviderAttachment:InstanceTrustProviderAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            verifiedaccess_instance_id: Optional[pulumi.Input[str]] = None,
            verifiedaccess_trust_provider_id: Optional[pulumi.Input[str]] = None) -> 'InstanceTrustProviderAttachment':
        """
        Get an existing InstanceTrustProviderAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] verifiedaccess_instance_id: The ID of the Verified Access instance to attach the Trust Provider to.
        :param pulumi.Input[str] verifiedaccess_trust_provider_id: The ID of the Verified Access trust provider.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _InstanceTrustProviderAttachmentState.__new__(_InstanceTrustProviderAttachmentState)

        __props__.__dict__["verifiedaccess_instance_id"] = verifiedaccess_instance_id
        __props__.__dict__["verifiedaccess_trust_provider_id"] = verifiedaccess_trust_provider_id
        return InstanceTrustProviderAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="verifiedaccessInstanceId")
    def verifiedaccess_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the Verified Access instance to attach the Trust Provider to.
        """
        return pulumi.get(self, "verifiedaccess_instance_id")

    @property
    @pulumi.getter(name="verifiedaccessTrustProviderId")
    def verifiedaccess_trust_provider_id(self) -> pulumi.Output[str]:
        """
        The ID of the Verified Access trust provider.
        """
        return pulumi.get(self, "verifiedaccess_trust_provider_id")


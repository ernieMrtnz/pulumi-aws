# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['EncryptionConfigArgs', 'EncryptionConfig']

@pulumi.input_type
class EncryptionConfigArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 key_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a EncryptionConfig resource.
        :param pulumi.Input[str] type: The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        :param pulumi.Input[str] key_id: An AWS KMS customer master key (CMK) ARN.
        """
        EncryptionConfigArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            type=type,
            key_id=key_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             type: Optional[pulumi.Input[str]] = None,
             key_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if type is None:
            raise TypeError("Missing 'type' argument")
        if key_id is None and 'keyId' in kwargs:
            key_id = kwargs['keyId']

        _setter("type", type)
        if key_id is not None:
            _setter("key_id", key_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[str]]:
        """
        An AWS KMS customer master key (CMK) ARN.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_id", value)


@pulumi.input_type
class _EncryptionConfigState:
    def __init__(__self__, *,
                 key_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering EncryptionConfig resources.
        :param pulumi.Input[str] key_id: An AWS KMS customer master key (CMK) ARN.
        :param pulumi.Input[str] type: The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        """
        _EncryptionConfigState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key_id=key_id,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key_id: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if key_id is None and 'keyId' in kwargs:
            key_id = kwargs['keyId']

        if key_id is not None:
            _setter("key_id", key_id)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[str]]:
        """
        An AWS KMS customer master key (CMK) ARN.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class EncryptionConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates and manages an AWS XRay Encryption Config.

        > **NOTE:** Removing this resource from the provider has no effect to the encryption configuration within X-Ray.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.xray.EncryptionConfig("example", type="NONE")
        ```
        ### With KMS Key

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_caller_identity()
        example_policy_document = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            sid="Enable IAM User Permissions",
            effect="Allow",
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="AWS",
                identifiers=[f"arn:aws:iam::{current.account_id}:root"],
            )],
            actions=["kms:*"],
            resources=["*"],
        )])
        example_key = aws.kms.Key("exampleKey",
            description="Some Key",
            deletion_window_in_days=7,
            policy=example_policy_document.json)
        example_encryption_config = aws.xray.EncryptionConfig("exampleEncryptionConfig",
            type="KMS",
            key_id=example_key.arn)
        ```

        ## Import

        Using `pulumi import`, import XRay Encryption Config using the region name. For example:

        ```sh
         $ pulumi import aws:xray/encryptionConfig:EncryptionConfig example us-west-2
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_id: An AWS KMS customer master key (CMK) ARN.
        :param pulumi.Input[str] type: The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EncryptionConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates and manages an AWS XRay Encryption Config.

        > **NOTE:** Removing this resource from the provider has no effect to the encryption configuration within X-Ray.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.xray.EncryptionConfig("example", type="NONE")
        ```
        ### With KMS Key

        ```python
        import pulumi
        import pulumi_aws as aws

        current = aws.get_caller_identity()
        example_policy_document = aws.iam.get_policy_document(statements=[aws.iam.GetPolicyDocumentStatementArgs(
            sid="Enable IAM User Permissions",
            effect="Allow",
            principals=[aws.iam.GetPolicyDocumentStatementPrincipalArgs(
                type="AWS",
                identifiers=[f"arn:aws:iam::{current.account_id}:root"],
            )],
            actions=["kms:*"],
            resources=["*"],
        )])
        example_key = aws.kms.Key("exampleKey",
            description="Some Key",
            deletion_window_in_days=7,
            policy=example_policy_document.json)
        example_encryption_config = aws.xray.EncryptionConfig("exampleEncryptionConfig",
            type="KMS",
            key_id=example_key.arn)
        ```

        ## Import

        Using `pulumi import`, import XRay Encryption Config using the region name. For example:

        ```sh
         $ pulumi import aws:xray/encryptionConfig:EncryptionConfig example us-west-2
        ```

        :param str resource_name: The name of the resource.
        :param EncryptionConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EncryptionConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            EncryptionConfigArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EncryptionConfigArgs.__new__(EncryptionConfigArgs)

            __props__.__dict__["key_id"] = key_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(EncryptionConfig, __self__).__init__(
            'aws:xray/encryptionConfig:EncryptionConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'EncryptionConfig':
        """
        Get an existing EncryptionConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_id: An AWS KMS customer master key (CMK) ARN.
        :param pulumi.Input[str] type: The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _EncryptionConfigState.__new__(_EncryptionConfigState)

        __props__.__dict__["key_id"] = key_id
        __props__.__dict__["type"] = type
        return EncryptionConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[Optional[str]]:
        """
        An AWS KMS customer master key (CMK) ARN.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of encryption. Set to `KMS` to use your own key for encryption. Set to `NONE` for default encryption.
        """
        return pulumi.get(self, "type")


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

__all__ = ['BucketObjectLockConfigurationV2Args', 'BucketObjectLockConfigurationV2']

@pulumi.input_type
class BucketObjectLockConfigurationV2Args:
    def __init__(__self__, *,
                 bucket: pulumi.Input[str],
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 object_lock_enabled: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BucketObjectLockConfigurationV2 resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input[str] object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        :param pulumi.Input['BucketObjectLockConfigurationV2RuleArgs'] rule: Configuration block for specifying the Object Lock rule for the specified object. See below.
        :param pulumi.Input[str] token: Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
               The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        BucketObjectLockConfigurationV2Args._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket=bucket,
            expected_bucket_owner=expected_bucket_owner,
            object_lock_enabled=object_lock_enabled,
            rule=rule,
            token=token,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket: Optional[pulumi.Input[str]] = None,
             expected_bucket_owner: Optional[pulumi.Input[str]] = None,
             object_lock_enabled: Optional[pulumi.Input[str]] = None,
             rule: Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']] = None,
             token: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if bucket is None:
            raise TypeError("Missing 'bucket' argument")
        if expected_bucket_owner is None and 'expectedBucketOwner' in kwargs:
            expected_bucket_owner = kwargs['expectedBucketOwner']
        if object_lock_enabled is None and 'objectLockEnabled' in kwargs:
            object_lock_enabled = kwargs['objectLockEnabled']

        _setter("bucket", bucket)
        if expected_bucket_owner is not None:
            _setter("expected_bucket_owner", expected_bucket_owner)
        if object_lock_enabled is not None:
            _setter("object_lock_enabled", object_lock_enabled)
        if rule is not None:
            _setter("rule", rule)
        if token is not None:
            _setter("token", token)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[str]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)

    @property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        """
        return pulumi.get(self, "object_lock_enabled")

    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_lock_enabled", value)

    @property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']]:
        """
        Configuration block for specifying the Object Lock rule for the specified object. See below.
        """
        return pulumi.get(self, "rule")

    @rule.setter
    def rule(self, value: Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']]):
        pulumi.set(self, "rule", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
        The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


@pulumi.input_type
class _BucketObjectLockConfigurationV2State:
    def __init__(__self__, *,
                 bucket: Optional[pulumi.Input[str]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 object_lock_enabled: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']] = None,
                 token: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BucketObjectLockConfigurationV2 resources.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input[str] object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        :param pulumi.Input['BucketObjectLockConfigurationV2RuleArgs'] rule: Configuration block for specifying the Object Lock rule for the specified object. See below.
        :param pulumi.Input[str] token: Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
               The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        _BucketObjectLockConfigurationV2State._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket=bucket,
            expected_bucket_owner=expected_bucket_owner,
            object_lock_enabled=object_lock_enabled,
            rule=rule,
            token=token,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket: Optional[pulumi.Input[str]] = None,
             expected_bucket_owner: Optional[pulumi.Input[str]] = None,
             object_lock_enabled: Optional[pulumi.Input[str]] = None,
             rule: Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']] = None,
             token: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if expected_bucket_owner is None and 'expectedBucketOwner' in kwargs:
            expected_bucket_owner = kwargs['expectedBucketOwner']
        if object_lock_enabled is None and 'objectLockEnabled' in kwargs:
            object_lock_enabled = kwargs['objectLockEnabled']

        if bucket is not None:
            _setter("bucket", bucket)
        if expected_bucket_owner is not None:
            _setter("expected_bucket_owner", expected_bucket_owner)
        if object_lock_enabled is not None:
            _setter("object_lock_enabled", object_lock_enabled)
        if rule is not None:
            _setter("rule", rule)
        if token is not None:
            _setter("token", token)

    @property
    @pulumi.getter
    def bucket(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @bucket.setter
    def bucket(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        Account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)

    @property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        """
        return pulumi.get(self, "object_lock_enabled")

    @object_lock_enabled.setter
    def object_lock_enabled(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_lock_enabled", value)

    @property
    @pulumi.getter
    def rule(self) -> Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']]:
        """
        Configuration block for specifying the Object Lock rule for the specified object. See below.
        """
        return pulumi.get(self, "rule")

    @rule.setter
    def rule(self, value: Optional[pulumi.Input['BucketObjectLockConfigurationV2RuleArgs']]):
        pulumi.set(self, "rule", value)

    @property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[str]]:
        """
        Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
        The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        return pulumi.get(self, "token")

    @token.setter
    def token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token", value)


class BucketObjectLockConfigurationV2(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 object_lock_enabled: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationV2RuleArgs']]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an S3 bucket Object Lock configuration resource. For more information about Object Locking, go to [Using S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in the Amazon S3 User Guide.

        > **NOTE:** This resource **does not enable** Object Lock for **new** buckets. It configures a default retention period for objects placed in the specified bucket.
        Thus, to **enable** Object Lock for a **new** bucket, see the Using object lock configuration section in  the `s3.BucketV2` resource or the Object Lock configuration for a new bucket example below.
        If you want to **enable** Object Lock for an **existing** bucket, contact AWS Support and see the Object Lock configuration for an existing bucket example below.

        ## Example Usage
        ### Object Lock configuration for a new bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2", object_lock_enabled=True)
        example_bucket_object_lock_configuration_v2 = aws.s3.BucketObjectLockConfigurationV2("exampleBucketObjectLockConfigurationV2",
            bucket=example_bucket_v2.id,
            rule=aws.s3.BucketObjectLockConfigurationV2RuleArgs(
                default_retention=aws.s3.BucketObjectLockConfigurationV2RuleDefaultRetentionArgs(
                    mode="COMPLIANCE",
                    days=5,
                ),
            ))
        ```
        ### Object Lock configuration for an existing bucket

        This is a multistep process that requires AWS Support intervention.

        1. Enable versioning on your S3 bucket, if you have not already done so.
           Doing so will generate an "Object Lock token" in the back-end.

        <!-- markdownlint-disable MD029 -->
        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2")
        example_bucket_versioning_v2 = aws.s3.BucketVersioningV2("exampleBucketVersioningV2",
            bucket=example_bucket_v2.id,
            versioning_configuration=aws.s3.BucketVersioningV2VersioningConfigurationArgs(
                status="Enabled",
            ))
        ```
        <!-- markdownlint-disable MD029 -->

        2. Contact AWS Support to provide you with the "Object Lock token" for the specified bucket and use the token (or token ID) within your new `s3.BucketObjectLockConfigurationV2` resource.
           Notice the `object_lock_enabled` argument does not need to be specified as it defaults to `Enabled`.

        <!-- markdownlint-disable MD029 -->
        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketObjectLockConfigurationV2("example",
            bucket=aws_s3_bucket["example"]["id"],
            rule=aws.s3.BucketObjectLockConfigurationV2RuleArgs(
                default_retention=aws.s3.BucketObjectLockConfigurationV2RuleDefaultRetentionArgs(
                    mode="COMPLIANCE",
                    days=5,
                ),
            ),
            token="NG2MKsfoLqV3A+aquXneSG4LOu/ekrlXkRXwIPFVfERT7XOPos+/k444d7RIH0E3W3p5QU6ml2exS2F/eYCFmMWHJ3hFZGk6al1sIJkmNhUMYmsv0jYVQyTTZNLM+DnfooA6SATt39mM1VW1yJh4E+XljMlWzaBwHKbss3/EjlGDjOmVhaSs4Z6427mMCaFD0RLwsYY7zX49gEc31YfOMJGxbXCXSeyNwAhhM/A8UH7gQf38RmjHjjAFbbbLtl8arsxTPW8F1IYohqwmKIr9DnotLLj8Tg44U2SPwujVaqmlKKP9s41rfgb4UbIm7khSafDBng0LGfxC4pMlT9Ny2w==")
        ```
        <!-- markdownlint-disable MD029 -->

        ## Import

        If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        import {

         to = aws_s3_bucket_object_lock_configuration.example

         id = "bucket-name,123456789012" }

        __Using `pulumi import` to import__ S3 bucket Object Lock configuration using the `bucket` or using the `bucket` and `expected_bucket_owner` separated by a comma (`,`). For example:

        If the owner (account ID) of the source bucket is the same account used to configure the AWS Provider, import using the `bucket`:

        ```sh
         $ pulumi import aws:s3/bucketObjectLockConfigurationV2:BucketObjectLockConfigurationV2 example bucket-name
        ```
         If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        ```sh
         $ pulumi import aws:s3/bucketObjectLockConfigurationV2:BucketObjectLockConfigurationV2 example bucket-name,123456789012
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input[str] object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        :param pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationV2RuleArgs']] rule: Configuration block for specifying the Object Lock rule for the specified object. See below.
        :param pulumi.Input[str] token: Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
               The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BucketObjectLockConfigurationV2Args,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an S3 bucket Object Lock configuration resource. For more information about Object Locking, go to [Using S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) in the Amazon S3 User Guide.

        > **NOTE:** This resource **does not enable** Object Lock for **new** buckets. It configures a default retention period for objects placed in the specified bucket.
        Thus, to **enable** Object Lock for a **new** bucket, see the Using object lock configuration section in  the `s3.BucketV2` resource or the Object Lock configuration for a new bucket example below.
        If you want to **enable** Object Lock for an **existing** bucket, contact AWS Support and see the Object Lock configuration for an existing bucket example below.

        ## Example Usage
        ### Object Lock configuration for a new bucket

        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2", object_lock_enabled=True)
        example_bucket_object_lock_configuration_v2 = aws.s3.BucketObjectLockConfigurationV2("exampleBucketObjectLockConfigurationV2",
            bucket=example_bucket_v2.id,
            rule=aws.s3.BucketObjectLockConfigurationV2RuleArgs(
                default_retention=aws.s3.BucketObjectLockConfigurationV2RuleDefaultRetentionArgs(
                    mode="COMPLIANCE",
                    days=5,
                ),
            ))
        ```
        ### Object Lock configuration for an existing bucket

        This is a multistep process that requires AWS Support intervention.

        1. Enable versioning on your S3 bucket, if you have not already done so.
           Doing so will generate an "Object Lock token" in the back-end.

        <!-- markdownlint-disable MD029 -->
        ```python
        import pulumi
        import pulumi_aws as aws

        example_bucket_v2 = aws.s3.BucketV2("exampleBucketV2")
        example_bucket_versioning_v2 = aws.s3.BucketVersioningV2("exampleBucketVersioningV2",
            bucket=example_bucket_v2.id,
            versioning_configuration=aws.s3.BucketVersioningV2VersioningConfigurationArgs(
                status="Enabled",
            ))
        ```
        <!-- markdownlint-disable MD029 -->

        2. Contact AWS Support to provide you with the "Object Lock token" for the specified bucket and use the token (or token ID) within your new `s3.BucketObjectLockConfigurationV2` resource.
           Notice the `object_lock_enabled` argument does not need to be specified as it defaults to `Enabled`.

        <!-- markdownlint-disable MD029 -->
        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.s3.BucketObjectLockConfigurationV2("example",
            bucket=aws_s3_bucket["example"]["id"],
            rule=aws.s3.BucketObjectLockConfigurationV2RuleArgs(
                default_retention=aws.s3.BucketObjectLockConfigurationV2RuleDefaultRetentionArgs(
                    mode="COMPLIANCE",
                    days=5,
                ),
            ),
            token="NG2MKsfoLqV3A+aquXneSG4LOu/ekrlXkRXwIPFVfERT7XOPos+/k444d7RIH0E3W3p5QU6ml2exS2F/eYCFmMWHJ3hFZGk6al1sIJkmNhUMYmsv0jYVQyTTZNLM+DnfooA6SATt39mM1VW1yJh4E+XljMlWzaBwHKbss3/EjlGDjOmVhaSs4Z6427mMCaFD0RLwsYY7zX49gEc31YfOMJGxbXCXSeyNwAhhM/A8UH7gQf38RmjHjjAFbbbLtl8arsxTPW8F1IYohqwmKIr9DnotLLj8Tg44U2SPwujVaqmlKKP9s41rfgb4UbIm7khSafDBng0LGfxC4pMlT9Ny2w==")
        ```
        <!-- markdownlint-disable MD029 -->

        ## Import

        If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        import {

         to = aws_s3_bucket_object_lock_configuration.example

         id = "bucket-name,123456789012" }

        __Using `pulumi import` to import__ S3 bucket Object Lock configuration using the `bucket` or using the `bucket` and `expected_bucket_owner` separated by a comma (`,`). For example:

        If the owner (account ID) of the source bucket is the same account used to configure the AWS Provider, import using the `bucket`:

        ```sh
         $ pulumi import aws:s3/bucketObjectLockConfigurationV2:BucketObjectLockConfigurationV2 example bucket-name
        ```
         If the owner (account ID) of the source bucket differs from the account used to configure the AWS Provider, import using the `bucket` and `expected_bucket_owner` separated by a comma (`,`):

        ```sh
         $ pulumi import aws:s3/bucketObjectLockConfigurationV2:BucketObjectLockConfigurationV2 example bucket-name,123456789012
        ```

        :param str resource_name: The name of the resource.
        :param BucketObjectLockConfigurationV2Args args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BucketObjectLockConfigurationV2Args, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BucketObjectLockConfigurationV2Args._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 object_lock_enabled: Optional[pulumi.Input[str]] = None,
                 rule: Optional[pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationV2RuleArgs']]] = None,
                 token: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BucketObjectLockConfigurationV2Args.__new__(BucketObjectLockConfigurationV2Args)

            if bucket is None and not opts.urn:
                raise TypeError("Missing required property 'bucket'")
            __props__.__dict__["bucket"] = bucket
            __props__.__dict__["expected_bucket_owner"] = expected_bucket_owner
            __props__.__dict__["object_lock_enabled"] = object_lock_enabled
            rule = _utilities.configure(rule, BucketObjectLockConfigurationV2RuleArgs, True)
            __props__.__dict__["rule"] = rule
            __props__.__dict__["token"] = None if token is None else pulumi.Output.secret(token)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["token"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(BucketObjectLockConfigurationV2, __self__).__init__(
            'aws:s3/bucketObjectLockConfigurationV2:BucketObjectLockConfigurationV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            expected_bucket_owner: Optional[pulumi.Input[str]] = None,
            object_lock_enabled: Optional[pulumi.Input[str]] = None,
            rule: Optional[pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationV2RuleArgs']]] = None,
            token: Optional[pulumi.Input[str]] = None) -> 'BucketObjectLockConfigurationV2':
        """
        Get an existing BucketObjectLockConfigurationV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: Name of the bucket.
        :param pulumi.Input[str] expected_bucket_owner: Account ID of the expected bucket owner.
        :param pulumi.Input[str] object_lock_enabled: Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        :param pulumi.Input[pulumi.InputType['BucketObjectLockConfigurationV2RuleArgs']] rule: Configuration block for specifying the Object Lock rule for the specified object. See below.
        :param pulumi.Input[str] token: Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
               The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BucketObjectLockConfigurationV2State.__new__(_BucketObjectLockConfigurationV2State)

        __props__.__dict__["bucket"] = bucket
        __props__.__dict__["expected_bucket_owner"] = expected_bucket_owner
        __props__.__dict__["object_lock_enabled"] = object_lock_enabled
        __props__.__dict__["rule"] = rule
        __props__.__dict__["token"] = token
        return BucketObjectLockConfigurationV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> pulumi.Output[str]:
        """
        Name of the bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> pulumi.Output[Optional[str]]:
        """
        Account ID of the expected bucket owner.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @property
    @pulumi.getter(name="objectLockEnabled")
    def object_lock_enabled(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates whether this bucket has an Object Lock configuration enabled. Defaults to `Enabled`. Valid values: `Enabled`.
        """
        return pulumi.get(self, "object_lock_enabled")

    @property
    @pulumi.getter
    def rule(self) -> pulumi.Output[Optional['outputs.BucketObjectLockConfigurationV2Rule']]:
        """
        Configuration block for specifying the Object Lock rule for the specified object. See below.
        """
        return pulumi.get(self, "rule")

    @property
    @pulumi.getter
    def token(self) -> pulumi.Output[Optional[str]]:
        """
        Token to allow Object Lock to be enabled for an existing bucket. You must contact AWS support for the bucket's "Object Lock token".
        The token is generated in the back-end when [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/manage-versioning-examples.html) is enabled on a bucket. For more details on versioning, see the `s3.BucketVersioningV2` resource.
        """
        return pulumi.get(self, "token")


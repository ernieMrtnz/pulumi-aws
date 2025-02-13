# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DatabaseAclConfigurationArgs',
    'DatabaseEncryptionConfigurationArgs',
    'WorkgroupConfigurationArgs',
    'WorkgroupConfigurationEngineVersionArgs',
    'WorkgroupConfigurationResultConfigurationArgs',
    'WorkgroupConfigurationResultConfigurationAclConfigurationArgs',
    'WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs',
]

@pulumi.input_type
class DatabaseAclConfigurationArgs:
    def __init__(__self__, *,
                 s3_acl_option: pulumi.Input[str]):
        """
        :param pulumi.Input[str] s3_acl_option: Amazon S3 canned ACL that Athena should specify when storing query results. Valid value is `BUCKET_OWNER_FULL_CONTROL`.
               
               > **NOTE:** When Athena queries are executed, result files may be created in the specified bucket. Consider using `force_destroy` on the bucket too in order to avoid any problems when destroying the bucket.
        """
        DatabaseAclConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            s3_acl_option=s3_acl_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             s3_acl_option: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if s3_acl_option is None and 's3AclOption' in kwargs:
            s3_acl_option = kwargs['s3AclOption']
        if s3_acl_option is None:
            raise TypeError("Missing 's3_acl_option' argument")

        _setter("s3_acl_option", s3_acl_option)

    @property
    @pulumi.getter(name="s3AclOption")
    def s3_acl_option(self) -> pulumi.Input[str]:
        """
        Amazon S3 canned ACL that Athena should specify when storing query results. Valid value is `BUCKET_OWNER_FULL_CONTROL`.

        > **NOTE:** When Athena queries are executed, result files may be created in the specified bucket. Consider using `force_destroy` on the bucket too in order to avoid any problems when destroying the bucket.
        """
        return pulumi.get(self, "s3_acl_option")

    @s3_acl_option.setter
    def s3_acl_option(self, value: pulumi.Input[str]):
        pulumi.set(self, "s3_acl_option", value)


@pulumi.input_type
class DatabaseEncryptionConfigurationArgs:
    def __init__(__self__, *,
                 encryption_option: pulumi.Input[str],
                 kms_key: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] encryption_option: Type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`
        :param pulumi.Input[str] kms_key: KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.
        """
        DatabaseEncryptionConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encryption_option=encryption_option,
            kms_key=kms_key,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encryption_option: Optional[pulumi.Input[str]] = None,
             kms_key: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if encryption_option is None and 'encryptionOption' in kwargs:
            encryption_option = kwargs['encryptionOption']
        if encryption_option is None:
            raise TypeError("Missing 'encryption_option' argument")
        if kms_key is None and 'kmsKey' in kwargs:
            kms_key = kwargs['kmsKey']

        _setter("encryption_option", encryption_option)
        if kms_key is not None:
            _setter("kms_key", kms_key)

    @property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> pulumi.Input[str]:
        """
        Type of key; one of `SSE_S3`, `SSE_KMS`, `CSE_KMS`
        """
        return pulumi.get(self, "encryption_option")

    @encryption_option.setter
    def encryption_option(self, value: pulumi.Input[str]):
        pulumi.set(self, "encryption_option", value)

    @property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> Optional[pulumi.Input[str]]:
        """
        KMS key ARN or ID; required for key types `SSE_KMS` and `CSE_KMS`.
        """
        return pulumi.get(self, "kms_key")

    @kms_key.setter
    def kms_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key", value)


@pulumi.input_type
class WorkgroupConfigurationArgs:
    def __init__(__self__, *,
                 bytes_scanned_cutoff_per_query: Optional[pulumi.Input[int]] = None,
                 enforce_workgroup_configuration: Optional[pulumi.Input[bool]] = None,
                 engine_version: Optional[pulumi.Input['WorkgroupConfigurationEngineVersionArgs']] = None,
                 execution_role: Optional[pulumi.Input[str]] = None,
                 publish_cloudwatch_metrics_enabled: Optional[pulumi.Input[bool]] = None,
                 requester_pays_enabled: Optional[pulumi.Input[bool]] = None,
                 result_configuration: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationArgs']] = None):
        """
        :param pulumi.Input[int] bytes_scanned_cutoff_per_query: Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
        :param pulumi.Input[bool] enforce_workgroup_configuration: Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
        :param pulumi.Input['WorkgroupConfigurationEngineVersionArgs'] engine_version: Configuration block for the Athena Engine Versioning. For more information, see [Athena Engine Versioning](https://docs.aws.amazon.com/athena/latest/ug/engine-versions.html). See Engine Version below.
        :param pulumi.Input[str] execution_role: Role used in a notebook session for accessing the user's resources.
        :param pulumi.Input[bool] publish_cloudwatch_metrics_enabled: Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
        :param pulumi.Input[bool] requester_pays_enabled: If set to true , allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to false , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is false . For more information about Requester Pays buckets, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html) in the Amazon Simple Storage Service Developer Guide.
        :param pulumi.Input['WorkgroupConfigurationResultConfigurationArgs'] result_configuration: Configuration block with result settings. See Result Configuration below.
        """
        WorkgroupConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bytes_scanned_cutoff_per_query=bytes_scanned_cutoff_per_query,
            enforce_workgroup_configuration=enforce_workgroup_configuration,
            engine_version=engine_version,
            execution_role=execution_role,
            publish_cloudwatch_metrics_enabled=publish_cloudwatch_metrics_enabled,
            requester_pays_enabled=requester_pays_enabled,
            result_configuration=result_configuration,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bytes_scanned_cutoff_per_query: Optional[pulumi.Input[int]] = None,
             enforce_workgroup_configuration: Optional[pulumi.Input[bool]] = None,
             engine_version: Optional[pulumi.Input['WorkgroupConfigurationEngineVersionArgs']] = None,
             execution_role: Optional[pulumi.Input[str]] = None,
             publish_cloudwatch_metrics_enabled: Optional[pulumi.Input[bool]] = None,
             requester_pays_enabled: Optional[pulumi.Input[bool]] = None,
             result_configuration: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationArgs']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if bytes_scanned_cutoff_per_query is None and 'bytesScannedCutoffPerQuery' in kwargs:
            bytes_scanned_cutoff_per_query = kwargs['bytesScannedCutoffPerQuery']
        if enforce_workgroup_configuration is None and 'enforceWorkgroupConfiguration' in kwargs:
            enforce_workgroup_configuration = kwargs['enforceWorkgroupConfiguration']
        if engine_version is None and 'engineVersion' in kwargs:
            engine_version = kwargs['engineVersion']
        if execution_role is None and 'executionRole' in kwargs:
            execution_role = kwargs['executionRole']
        if publish_cloudwatch_metrics_enabled is None and 'publishCloudwatchMetricsEnabled' in kwargs:
            publish_cloudwatch_metrics_enabled = kwargs['publishCloudwatchMetricsEnabled']
        if requester_pays_enabled is None and 'requesterPaysEnabled' in kwargs:
            requester_pays_enabled = kwargs['requesterPaysEnabled']
        if result_configuration is None and 'resultConfiguration' in kwargs:
            result_configuration = kwargs['resultConfiguration']

        if bytes_scanned_cutoff_per_query is not None:
            _setter("bytes_scanned_cutoff_per_query", bytes_scanned_cutoff_per_query)
        if enforce_workgroup_configuration is not None:
            _setter("enforce_workgroup_configuration", enforce_workgroup_configuration)
        if engine_version is not None:
            _setter("engine_version", engine_version)
        if execution_role is not None:
            _setter("execution_role", execution_role)
        if publish_cloudwatch_metrics_enabled is not None:
            _setter("publish_cloudwatch_metrics_enabled", publish_cloudwatch_metrics_enabled)
        if requester_pays_enabled is not None:
            _setter("requester_pays_enabled", requester_pays_enabled)
        if result_configuration is not None:
            _setter("result_configuration", result_configuration)

    @property
    @pulumi.getter(name="bytesScannedCutoffPerQuery")
    def bytes_scanned_cutoff_per_query(self) -> Optional[pulumi.Input[int]]:
        """
        Integer for the upper data usage limit (cutoff) for the amount of bytes a single query in a workgroup is allowed to scan. Must be at least `10485760`.
        """
        return pulumi.get(self, "bytes_scanned_cutoff_per_query")

    @bytes_scanned_cutoff_per_query.setter
    def bytes_scanned_cutoff_per_query(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "bytes_scanned_cutoff_per_query", value)

    @property
    @pulumi.getter(name="enforceWorkgroupConfiguration")
    def enforce_workgroup_configuration(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether the settings for the workgroup override client-side settings. For more information, see [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html). Defaults to `true`.
        """
        return pulumi.get(self, "enforce_workgroup_configuration")

    @enforce_workgroup_configuration.setter
    def enforce_workgroup_configuration(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enforce_workgroup_configuration", value)

    @property
    @pulumi.getter(name="engineVersion")
    def engine_version(self) -> Optional[pulumi.Input['WorkgroupConfigurationEngineVersionArgs']]:
        """
        Configuration block for the Athena Engine Versioning. For more information, see [Athena Engine Versioning](https://docs.aws.amazon.com/athena/latest/ug/engine-versions.html). See Engine Version below.
        """
        return pulumi.get(self, "engine_version")

    @engine_version.setter
    def engine_version(self, value: Optional[pulumi.Input['WorkgroupConfigurationEngineVersionArgs']]):
        pulumi.set(self, "engine_version", value)

    @property
    @pulumi.getter(name="executionRole")
    def execution_role(self) -> Optional[pulumi.Input[str]]:
        """
        Role used in a notebook session for accessing the user's resources.
        """
        return pulumi.get(self, "execution_role")

    @execution_role.setter
    def execution_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "execution_role", value)

    @property
    @pulumi.getter(name="publishCloudwatchMetricsEnabled")
    def publish_cloudwatch_metrics_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether Amazon CloudWatch metrics are enabled for the workgroup. Defaults to `true`.
        """
        return pulumi.get(self, "publish_cloudwatch_metrics_enabled")

    @publish_cloudwatch_metrics_enabled.setter
    def publish_cloudwatch_metrics_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "publish_cloudwatch_metrics_enabled", value)

    @property
    @pulumi.getter(name="requesterPaysEnabled")
    def requester_pays_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to true , allows members assigned to a workgroup to reference Amazon S3 Requester Pays buckets in queries. If set to false , workgroup members cannot query data from Requester Pays buckets, and queries that retrieve data from Requester Pays buckets cause an error. The default is false . For more information about Requester Pays buckets, see [Requester Pays Buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html) in the Amazon Simple Storage Service Developer Guide.
        """
        return pulumi.get(self, "requester_pays_enabled")

    @requester_pays_enabled.setter
    def requester_pays_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "requester_pays_enabled", value)

    @property
    @pulumi.getter(name="resultConfiguration")
    def result_configuration(self) -> Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationArgs']]:
        """
        Configuration block with result settings. See Result Configuration below.
        """
        return pulumi.get(self, "result_configuration")

    @result_configuration.setter
    def result_configuration(self, value: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationArgs']]):
        pulumi.set(self, "result_configuration", value)


@pulumi.input_type
class WorkgroupConfigurationEngineVersionArgs:
    def __init__(__self__, *,
                 effective_engine_version: Optional[pulumi.Input[str]] = None,
                 selected_engine_version: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] effective_engine_version: The engine version on which the query runs. If `selected_engine_version` is set to `AUTO`, the effective engine version is chosen by Athena.
        :param pulumi.Input[str] selected_engine_version: Requested engine version. Defaults to `AUTO`.
        """
        WorkgroupConfigurationEngineVersionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            effective_engine_version=effective_engine_version,
            selected_engine_version=selected_engine_version,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             effective_engine_version: Optional[pulumi.Input[str]] = None,
             selected_engine_version: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if effective_engine_version is None and 'effectiveEngineVersion' in kwargs:
            effective_engine_version = kwargs['effectiveEngineVersion']
        if selected_engine_version is None and 'selectedEngineVersion' in kwargs:
            selected_engine_version = kwargs['selectedEngineVersion']

        if effective_engine_version is not None:
            _setter("effective_engine_version", effective_engine_version)
        if selected_engine_version is not None:
            _setter("selected_engine_version", selected_engine_version)

    @property
    @pulumi.getter(name="effectiveEngineVersion")
    def effective_engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        The engine version on which the query runs. If `selected_engine_version` is set to `AUTO`, the effective engine version is chosen by Athena.
        """
        return pulumi.get(self, "effective_engine_version")

    @effective_engine_version.setter
    def effective_engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "effective_engine_version", value)

    @property
    @pulumi.getter(name="selectedEngineVersion")
    def selected_engine_version(self) -> Optional[pulumi.Input[str]]:
        """
        Requested engine version. Defaults to `AUTO`.
        """
        return pulumi.get(self, "selected_engine_version")

    @selected_engine_version.setter
    def selected_engine_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "selected_engine_version", value)


@pulumi.input_type
class WorkgroupConfigurationResultConfigurationArgs:
    def __init__(__self__, *,
                 acl_configuration: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationAclConfigurationArgs']] = None,
                 encryption_configuration: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs']] = None,
                 expected_bucket_owner: Optional[pulumi.Input[str]] = None,
                 output_location: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input['WorkgroupConfigurationResultConfigurationAclConfigurationArgs'] acl_configuration: That an Amazon S3 canned ACL should be set to control ownership of stored query results. See ACL Configuration below.
        :param pulumi.Input['WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs'] encryption_configuration: Configuration block with encryption settings. See Encryption Configuration below.
        :param pulumi.Input[str] expected_bucket_owner: AWS account ID that you expect to be the owner of the Amazon S3 bucket.
        :param pulumi.Input[str] output_location: Location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
        """
        WorkgroupConfigurationResultConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            acl_configuration=acl_configuration,
            encryption_configuration=encryption_configuration,
            expected_bucket_owner=expected_bucket_owner,
            output_location=output_location,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             acl_configuration: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationAclConfigurationArgs']] = None,
             encryption_configuration: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs']] = None,
             expected_bucket_owner: Optional[pulumi.Input[str]] = None,
             output_location: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if acl_configuration is None and 'aclConfiguration' in kwargs:
            acl_configuration = kwargs['aclConfiguration']
        if encryption_configuration is None and 'encryptionConfiguration' in kwargs:
            encryption_configuration = kwargs['encryptionConfiguration']
        if expected_bucket_owner is None and 'expectedBucketOwner' in kwargs:
            expected_bucket_owner = kwargs['expectedBucketOwner']
        if output_location is None and 'outputLocation' in kwargs:
            output_location = kwargs['outputLocation']

        if acl_configuration is not None:
            _setter("acl_configuration", acl_configuration)
        if encryption_configuration is not None:
            _setter("encryption_configuration", encryption_configuration)
        if expected_bucket_owner is not None:
            _setter("expected_bucket_owner", expected_bucket_owner)
        if output_location is not None:
            _setter("output_location", output_location)

    @property
    @pulumi.getter(name="aclConfiguration")
    def acl_configuration(self) -> Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationAclConfigurationArgs']]:
        """
        That an Amazon S3 canned ACL should be set to control ownership of stored query results. See ACL Configuration below.
        """
        return pulumi.get(self, "acl_configuration")

    @acl_configuration.setter
    def acl_configuration(self, value: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationAclConfigurationArgs']]):
        pulumi.set(self, "acl_configuration", value)

    @property
    @pulumi.getter(name="encryptionConfiguration")
    def encryption_configuration(self) -> Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs']]:
        """
        Configuration block with encryption settings. See Encryption Configuration below.
        """
        return pulumi.get(self, "encryption_configuration")

    @encryption_configuration.setter
    def encryption_configuration(self, value: Optional[pulumi.Input['WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs']]):
        pulumi.set(self, "encryption_configuration", value)

    @property
    @pulumi.getter(name="expectedBucketOwner")
    def expected_bucket_owner(self) -> Optional[pulumi.Input[str]]:
        """
        AWS account ID that you expect to be the owner of the Amazon S3 bucket.
        """
        return pulumi.get(self, "expected_bucket_owner")

    @expected_bucket_owner.setter
    def expected_bucket_owner(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_bucket_owner", value)

    @property
    @pulumi.getter(name="outputLocation")
    def output_location(self) -> Optional[pulumi.Input[str]]:
        """
        Location in Amazon S3 where your query results are stored, such as `s3://path/to/query/bucket/`. For more information, see [Queries and Query Result Files](https://docs.aws.amazon.com/athena/latest/ug/querying.html).
        """
        return pulumi.get(self, "output_location")

    @output_location.setter
    def output_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "output_location", value)


@pulumi.input_type
class WorkgroupConfigurationResultConfigurationAclConfigurationArgs:
    def __init__(__self__, *,
                 s3_acl_option: pulumi.Input[str]):
        """
        :param pulumi.Input[str] s3_acl_option: Amazon S3 canned ACL that Athena should specify when storing query results. Valid value is `BUCKET_OWNER_FULL_CONTROL`.
        """
        WorkgroupConfigurationResultConfigurationAclConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            s3_acl_option=s3_acl_option,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             s3_acl_option: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if s3_acl_option is None and 's3AclOption' in kwargs:
            s3_acl_option = kwargs['s3AclOption']
        if s3_acl_option is None:
            raise TypeError("Missing 's3_acl_option' argument")

        _setter("s3_acl_option", s3_acl_option)

    @property
    @pulumi.getter(name="s3AclOption")
    def s3_acl_option(self) -> pulumi.Input[str]:
        """
        Amazon S3 canned ACL that Athena should specify when storing query results. Valid value is `BUCKET_OWNER_FULL_CONTROL`.
        """
        return pulumi.get(self, "s3_acl_option")

    @s3_acl_option.setter
    def s3_acl_option(self, value: pulumi.Input[str]):
        pulumi.set(self, "s3_acl_option", value)


@pulumi.input_type
class WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs:
    def __init__(__self__, *,
                 encryption_option: Optional[pulumi.Input[str]] = None,
                 kms_key_arn: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] encryption_option: Whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
        :param pulumi.Input[str] kms_key_arn: For `SSE_KMS` and `CSE_KMS`, this is the KMS key ARN.
        """
        WorkgroupConfigurationResultConfigurationEncryptionConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            encryption_option=encryption_option,
            kms_key_arn=kms_key_arn,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             encryption_option: Optional[pulumi.Input[str]] = None,
             kms_key_arn: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if encryption_option is None and 'encryptionOption' in kwargs:
            encryption_option = kwargs['encryptionOption']
        if kms_key_arn is None and 'kmsKeyArn' in kwargs:
            kms_key_arn = kwargs['kmsKeyArn']

        if encryption_option is not None:
            _setter("encryption_option", encryption_option)
        if kms_key_arn is not None:
            _setter("kms_key_arn", kms_key_arn)

    @property
    @pulumi.getter(name="encryptionOption")
    def encryption_option(self) -> Optional[pulumi.Input[str]]:
        """
        Whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3`), server-side encryption with KMS-managed keys (`SSE_KMS`), or client-side encryption with KMS-managed keys (`CSE_KMS`) is used. If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroup's setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.
        """
        return pulumi.get(self, "encryption_option")

    @encryption_option.setter
    def encryption_option(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encryption_option", value)

    @property
    @pulumi.getter(name="kmsKeyArn")
    def kms_key_arn(self) -> Optional[pulumi.Input[str]]:
        """
        For `SSE_KMS` and `CSE_KMS`, this is the KMS key ARN.
        """
        return pulumi.get(self, "kms_key_arn")

    @kms_key_arn.setter
    def kms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_arn", value)



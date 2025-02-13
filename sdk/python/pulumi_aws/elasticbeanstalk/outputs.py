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
    'ApplicationAppversionLifecycle',
    'ConfigurationTemplateSetting',
    'EnvironmentAllSetting',
    'EnvironmentSetting',
    'GetApplicationAppversionLifecycleResult',
]

@pulumi.output_type
class ApplicationAppversionLifecycle(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "serviceRole":
            suggest = "service_role"
        elif key == "deleteSourceFromS3":
            suggest = "delete_source_from_s3"
        elif key == "maxAgeInDays":
            suggest = "max_age_in_days"
        elif key == "maxCount":
            suggest = "max_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ApplicationAppversionLifecycle. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ApplicationAppversionLifecycle.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ApplicationAppversionLifecycle.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 service_role: str,
                 delete_source_from_s3: Optional[bool] = None,
                 max_age_in_days: Optional[int] = None,
                 max_count: Optional[int] = None):
        """
        :param str service_role: The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        :param bool delete_source_from_s3: Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        :param int max_age_in_days: The number of days to retain an application version ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        :param int max_count: The maximum number of application versions to retain ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        """
        ApplicationAppversionLifecycle._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            service_role=service_role,
            delete_source_from_s3=delete_source_from_s3,
            max_age_in_days=max_age_in_days,
            max_count=max_count,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             service_role: Optional[str] = None,
             delete_source_from_s3: Optional[bool] = None,
             max_age_in_days: Optional[int] = None,
             max_count: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if service_role is None and 'serviceRole' in kwargs:
            service_role = kwargs['serviceRole']
        if service_role is None:
            raise TypeError("Missing 'service_role' argument")
        if delete_source_from_s3 is None and 'deleteSourceFromS3' in kwargs:
            delete_source_from_s3 = kwargs['deleteSourceFromS3']
        if max_age_in_days is None and 'maxAgeInDays' in kwargs:
            max_age_in_days = kwargs['maxAgeInDays']
        if max_count is None and 'maxCount' in kwargs:
            max_count = kwargs['maxCount']

        _setter("service_role", service_role)
        if delete_source_from_s3 is not None:
            _setter("delete_source_from_s3", delete_source_from_s3)
        if max_age_in_days is not None:
            _setter("max_age_in_days", max_age_in_days)
        if max_count is not None:
            _setter("max_count", max_count)

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> str:
        """
        The ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        """
        return pulumi.get(self, "service_role")

    @property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> Optional[bool]:
        """
        Set to `true` to delete a version's source bundle from S3 when the application version is deleted.
        """
        return pulumi.get(self, "delete_source_from_s3")

    @property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> Optional[int]:
        """
        The number of days to retain an application version ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        """
        return pulumi.get(self, "max_age_in_days")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[int]:
        """
        The maximum number of application versions to retain ('max_age_in_days' and 'max_count' cannot be enabled simultaneously.).
        """
        return pulumi.get(self, "max_count")


@pulumi.output_type
class ConfigurationTemplateSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 namespace: str,
                 value: str,
                 resource: Optional[str] = None):
        """
        :param str name: A unique name for this Template.
        """
        ConfigurationTemplateSetting._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            namespace=namespace,
            value=value,
            resource=resource,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             namespace: Optional[str] = None,
             value: Optional[str] = None,
             resource: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if namespace is None:
            raise TypeError("Missing 'namespace' argument")
        if value is None:
            raise TypeError("Missing 'value' argument")

        _setter("name", name)
        _setter("namespace", namespace)
        _setter("value", value)
        if resource is not None:
            _setter("resource", resource)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for this Template.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")


@pulumi.output_type
class EnvironmentAllSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 namespace: str,
                 value: str,
                 resource: Optional[str] = None):
        """
        :param str name: A unique name for this Environment. This name is used
               in the application URL
        """
        EnvironmentAllSetting._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            namespace=namespace,
            value=value,
            resource=resource,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             namespace: Optional[str] = None,
             value: Optional[str] = None,
             resource: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if namespace is None:
            raise TypeError("Missing 'namespace' argument")
        if value is None:
            raise TypeError("Missing 'value' argument")

        _setter("name", name)
        _setter("namespace", namespace)
        _setter("value", value)
        if resource is not None:
            _setter("resource", resource)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for this Environment. This name is used
        in the application URL
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")


@pulumi.output_type
class EnvironmentSetting(dict):
    def __init__(__self__, *,
                 name: str,
                 namespace: str,
                 value: str,
                 resource: Optional[str] = None):
        """
        :param str name: A unique name for this Environment. This name is used
               in the application URL
        """
        EnvironmentSetting._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            namespace=namespace,
            value=value,
            resource=resource,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[str] = None,
             namespace: Optional[str] = None,
             value: Optional[str] = None,
             resource: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if namespace is None:
            raise TypeError("Missing 'namespace' argument")
        if value is None:
            raise TypeError("Missing 'value' argument")

        _setter("name", name)
        _setter("namespace", namespace)
        _setter("value", value)
        if resource is not None:
            _setter("resource", resource)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for this Environment. This name is used
        in the application URL
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def namespace(self) -> str:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")

    @property
    @pulumi.getter
    def resource(self) -> Optional[str]:
        return pulumi.get(self, "resource")


@pulumi.output_type
class GetApplicationAppversionLifecycleResult(dict):
    def __init__(__self__, *,
                 delete_source_from_s3: bool,
                 max_age_in_days: int,
                 max_count: int,
                 service_role: str):
        """
        :param bool delete_source_from_s3: Specifies whether delete a version's source bundle from S3 when the application version is deleted.
        :param int max_age_in_days: Number of days to retain an application version.
        :param int max_count: Maximum number of application versions to retain.
        :param str service_role: ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        """
        GetApplicationAppversionLifecycleResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            delete_source_from_s3=delete_source_from_s3,
            max_age_in_days=max_age_in_days,
            max_count=max_count,
            service_role=service_role,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             delete_source_from_s3: Optional[bool] = None,
             max_age_in_days: Optional[int] = None,
             max_count: Optional[int] = None,
             service_role: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if delete_source_from_s3 is None and 'deleteSourceFromS3' in kwargs:
            delete_source_from_s3 = kwargs['deleteSourceFromS3']
        if delete_source_from_s3 is None:
            raise TypeError("Missing 'delete_source_from_s3' argument")
        if max_age_in_days is None and 'maxAgeInDays' in kwargs:
            max_age_in_days = kwargs['maxAgeInDays']
        if max_age_in_days is None:
            raise TypeError("Missing 'max_age_in_days' argument")
        if max_count is None and 'maxCount' in kwargs:
            max_count = kwargs['maxCount']
        if max_count is None:
            raise TypeError("Missing 'max_count' argument")
        if service_role is None and 'serviceRole' in kwargs:
            service_role = kwargs['serviceRole']
        if service_role is None:
            raise TypeError("Missing 'service_role' argument")

        _setter("delete_source_from_s3", delete_source_from_s3)
        _setter("max_age_in_days", max_age_in_days)
        _setter("max_count", max_count)
        _setter("service_role", service_role)

    @property
    @pulumi.getter(name="deleteSourceFromS3")
    def delete_source_from_s3(self) -> bool:
        """
        Specifies whether delete a version's source bundle from S3 when the application version is deleted.
        """
        return pulumi.get(self, "delete_source_from_s3")

    @property
    @pulumi.getter(name="maxAgeInDays")
    def max_age_in_days(self) -> int:
        """
        Number of days to retain an application version.
        """
        return pulumi.get(self, "max_age_in_days")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> int:
        """
        Maximum number of application versions to retain.
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="serviceRole")
    def service_role(self) -> str:
        """
        ARN of an IAM service role under which the application version is deleted.  Elastic Beanstalk must have permission to assume this role.
        """
        return pulumi.get(self, "service_role")



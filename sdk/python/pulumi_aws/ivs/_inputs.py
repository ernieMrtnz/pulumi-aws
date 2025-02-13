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
    'RecordingConfigurationDestinationConfigurationArgs',
    'RecordingConfigurationDestinationConfigurationS3Args',
    'RecordingConfigurationThumbnailConfigurationArgs',
]

@pulumi.input_type
class RecordingConfigurationDestinationConfigurationArgs:
    def __init__(__self__, *,
                 s3: pulumi.Input['RecordingConfigurationDestinationConfigurationS3Args']):
        """
        :param pulumi.Input['RecordingConfigurationDestinationConfigurationS3Args'] s3: S3 destination configuration where recorded videos will be stored.
        """
        RecordingConfigurationDestinationConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            s3=s3,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             s3: Optional[pulumi.Input['RecordingConfigurationDestinationConfigurationS3Args']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if s3 is None:
            raise TypeError("Missing 's3' argument")

        _setter("s3", s3)

    @property
    @pulumi.getter
    def s3(self) -> pulumi.Input['RecordingConfigurationDestinationConfigurationS3Args']:
        """
        S3 destination configuration where recorded videos will be stored.
        """
        return pulumi.get(self, "s3")

    @s3.setter
    def s3(self, value: pulumi.Input['RecordingConfigurationDestinationConfigurationS3Args']):
        pulumi.set(self, "s3", value)


@pulumi.input_type
class RecordingConfigurationDestinationConfigurationS3Args:
    def __init__(__self__, *,
                 bucket_name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] bucket_name: S3 bucket name where recorded videos will be stored.
               
               The following arguments are optional:
        """
        RecordingConfigurationDestinationConfigurationS3Args._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            bucket_name=bucket_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             bucket_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if bucket_name is None and 'bucketName' in kwargs:
            bucket_name = kwargs['bucketName']
        if bucket_name is None:
            raise TypeError("Missing 'bucket_name' argument")

        _setter("bucket_name", bucket_name)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Input[str]:
        """
        S3 bucket name where recorded videos will be stored.

        The following arguments are optional:
        """
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "bucket_name", value)


@pulumi.input_type
class RecordingConfigurationThumbnailConfigurationArgs:
    def __init__(__self__, *,
                 recording_mode: Optional[pulumi.Input[str]] = None,
                 target_interval_seconds: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] recording_mode: Thumbnail recording mode. Valid values: `DISABLED`, `INTERVAL`.
        :param pulumi.Input[int] target_interval_seconds: The targeted thumbnail-generation interval in seconds.
        """
        RecordingConfigurationThumbnailConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            recording_mode=recording_mode,
            target_interval_seconds=target_interval_seconds,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             recording_mode: Optional[pulumi.Input[str]] = None,
             target_interval_seconds: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if recording_mode is None and 'recordingMode' in kwargs:
            recording_mode = kwargs['recordingMode']
        if target_interval_seconds is None and 'targetIntervalSeconds' in kwargs:
            target_interval_seconds = kwargs['targetIntervalSeconds']

        if recording_mode is not None:
            _setter("recording_mode", recording_mode)
        if target_interval_seconds is not None:
            _setter("target_interval_seconds", target_interval_seconds)

    @property
    @pulumi.getter(name="recordingMode")
    def recording_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Thumbnail recording mode. Valid values: `DISABLED`, `INTERVAL`.
        """
        return pulumi.get(self, "recording_mode")

    @recording_mode.setter
    def recording_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recording_mode", value)

    @property
    @pulumi.getter(name="targetIntervalSeconds")
    def target_interval_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        The targeted thumbnail-generation interval in seconds.
        """
        return pulumi.get(self, "target_interval_seconds")

    @target_interval_seconds.setter
    def target_interval_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "target_interval_seconds", value)



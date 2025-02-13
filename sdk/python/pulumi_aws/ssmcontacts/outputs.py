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

__all__ = [
    'ContactChannelDeliveryAddress',
    'PlanStage',
    'PlanStageTarget',
    'PlanStageTargetChannelTargetInfo',
    'PlanStageTargetContactTargetInfo',
    'GetContactChannelDeliveryAddressResult',
    'GetPlanStageResult',
    'GetPlanStageTargetResult',
    'GetPlanStageTargetChannelTargetInfoResult',
    'GetPlanStageTargetContactTargetInfoResult',
]

@pulumi.output_type
class ContactChannelDeliveryAddress(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "simpleAddress":
            suggest = "simple_address"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContactChannelDeliveryAddress. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContactChannelDeliveryAddress.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContactChannelDeliveryAddress.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 simple_address: str):
        """
        :param str simple_address: Details to engage this contact channel. The expected format depends on the contact channel type and is described in the [`ContactChannelAddress` section of the SSM Contacts API Reference](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ContactChannelAddress.html).
        """
        ContactChannelDeliveryAddress._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            simple_address=simple_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             simple_address: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if simple_address is None and 'simpleAddress' in kwargs:
            simple_address = kwargs['simpleAddress']
        if simple_address is None:
            raise TypeError("Missing 'simple_address' argument")

        _setter("simple_address", simple_address)

    @property
    @pulumi.getter(name="simpleAddress")
    def simple_address(self) -> str:
        """
        Details to engage this contact channel. The expected format depends on the contact channel type and is described in the [`ContactChannelAddress` section of the SSM Contacts API Reference](https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_SSMContacts_ContactChannelAddress.html).
        """
        return pulumi.get(self, "simple_address")


@pulumi.output_type
class PlanStage(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "durationInMinutes":
            suggest = "duration_in_minutes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PlanStage. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PlanStage.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PlanStage.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 duration_in_minutes: int,
                 targets: Optional[Sequence['outputs.PlanStageTarget']] = None):
        PlanStage._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            duration_in_minutes=duration_in_minutes,
            targets=targets,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             duration_in_minutes: Optional[int] = None,
             targets: Optional[Sequence['outputs.PlanStageTarget']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if duration_in_minutes is None and 'durationInMinutes' in kwargs:
            duration_in_minutes = kwargs['durationInMinutes']
        if duration_in_minutes is None:
            raise TypeError("Missing 'duration_in_minutes' argument")

        _setter("duration_in_minutes", duration_in_minutes)
        if targets is not None:
            _setter("targets", targets)

    @property
    @pulumi.getter(name="durationInMinutes")
    def duration_in_minutes(self) -> int:
        return pulumi.get(self, "duration_in_minutes")

    @property
    @pulumi.getter
    def targets(self) -> Optional[Sequence['outputs.PlanStageTarget']]:
        return pulumi.get(self, "targets")


@pulumi.output_type
class PlanStageTarget(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "channelTargetInfo":
            suggest = "channel_target_info"
        elif key == "contactTargetInfo":
            suggest = "contact_target_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PlanStageTarget. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PlanStageTarget.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PlanStageTarget.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 channel_target_info: Optional['outputs.PlanStageTargetChannelTargetInfo'] = None,
                 contact_target_info: Optional['outputs.PlanStageTargetContactTargetInfo'] = None):
        PlanStageTarget._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            channel_target_info=channel_target_info,
            contact_target_info=contact_target_info,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             channel_target_info: Optional['outputs.PlanStageTargetChannelTargetInfo'] = None,
             contact_target_info: Optional['outputs.PlanStageTargetContactTargetInfo'] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if channel_target_info is None and 'channelTargetInfo' in kwargs:
            channel_target_info = kwargs['channelTargetInfo']
        if contact_target_info is None and 'contactTargetInfo' in kwargs:
            contact_target_info = kwargs['contactTargetInfo']

        if channel_target_info is not None:
            _setter("channel_target_info", channel_target_info)
        if contact_target_info is not None:
            _setter("contact_target_info", contact_target_info)

    @property
    @pulumi.getter(name="channelTargetInfo")
    def channel_target_info(self) -> Optional['outputs.PlanStageTargetChannelTargetInfo']:
        return pulumi.get(self, "channel_target_info")

    @property
    @pulumi.getter(name="contactTargetInfo")
    def contact_target_info(self) -> Optional['outputs.PlanStageTargetContactTargetInfo']:
        return pulumi.get(self, "contact_target_info")


@pulumi.output_type
class PlanStageTargetChannelTargetInfo(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contactChannelId":
            suggest = "contact_channel_id"
        elif key == "retryIntervalInMinutes":
            suggest = "retry_interval_in_minutes"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PlanStageTargetChannelTargetInfo. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PlanStageTargetChannelTargetInfo.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PlanStageTargetChannelTargetInfo.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 contact_channel_id: str,
                 retry_interval_in_minutes: Optional[int] = None):
        PlanStageTargetChannelTargetInfo._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            contact_channel_id=contact_channel_id,
            retry_interval_in_minutes=retry_interval_in_minutes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             contact_channel_id: Optional[str] = None,
             retry_interval_in_minutes: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if contact_channel_id is None and 'contactChannelId' in kwargs:
            contact_channel_id = kwargs['contactChannelId']
        if contact_channel_id is None:
            raise TypeError("Missing 'contact_channel_id' argument")
        if retry_interval_in_minutes is None and 'retryIntervalInMinutes' in kwargs:
            retry_interval_in_minutes = kwargs['retryIntervalInMinutes']

        _setter("contact_channel_id", contact_channel_id)
        if retry_interval_in_minutes is not None:
            _setter("retry_interval_in_minutes", retry_interval_in_minutes)

    @property
    @pulumi.getter(name="contactChannelId")
    def contact_channel_id(self) -> str:
        return pulumi.get(self, "contact_channel_id")

    @property
    @pulumi.getter(name="retryIntervalInMinutes")
    def retry_interval_in_minutes(self) -> Optional[int]:
        return pulumi.get(self, "retry_interval_in_minutes")


@pulumi.output_type
class PlanStageTargetContactTargetInfo(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "isEssential":
            suggest = "is_essential"
        elif key == "contactId":
            suggest = "contact_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PlanStageTargetContactTargetInfo. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PlanStageTargetContactTargetInfo.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PlanStageTargetContactTargetInfo.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 is_essential: bool,
                 contact_id: Optional[str] = None):
        """
        :param str contact_id: The Amazon Resource Name (ARN) of the contact or escalation plan.
        """
        PlanStageTargetContactTargetInfo._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            is_essential=is_essential,
            contact_id=contact_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             is_essential: Optional[bool] = None,
             contact_id: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if is_essential is None and 'isEssential' in kwargs:
            is_essential = kwargs['isEssential']
        if is_essential is None:
            raise TypeError("Missing 'is_essential' argument")
        if contact_id is None and 'contactId' in kwargs:
            contact_id = kwargs['contactId']

        _setter("is_essential", is_essential)
        if contact_id is not None:
            _setter("contact_id", contact_id)

    @property
    @pulumi.getter(name="isEssential")
    def is_essential(self) -> bool:
        return pulumi.get(self, "is_essential")

    @property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of the contact or escalation plan.
        """
        return pulumi.get(self, "contact_id")


@pulumi.output_type
class GetContactChannelDeliveryAddressResult(dict):
    def __init__(__self__, *,
                 simple_address: str):
        GetContactChannelDeliveryAddressResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            simple_address=simple_address,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             simple_address: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if simple_address is None and 'simpleAddress' in kwargs:
            simple_address = kwargs['simpleAddress']
        if simple_address is None:
            raise TypeError("Missing 'simple_address' argument")

        _setter("simple_address", simple_address)

    @property
    @pulumi.getter(name="simpleAddress")
    def simple_address(self) -> str:
        return pulumi.get(self, "simple_address")


@pulumi.output_type
class GetPlanStageResult(dict):
    def __init__(__self__, *,
                 duration_in_minutes: int,
                 targets: Sequence['outputs.GetPlanStageTargetResult']):
        GetPlanStageResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            duration_in_minutes=duration_in_minutes,
            targets=targets,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             duration_in_minutes: Optional[int] = None,
             targets: Optional[Sequence['outputs.GetPlanStageTargetResult']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if duration_in_minutes is None and 'durationInMinutes' in kwargs:
            duration_in_minutes = kwargs['durationInMinutes']
        if duration_in_minutes is None:
            raise TypeError("Missing 'duration_in_minutes' argument")
        if targets is None:
            raise TypeError("Missing 'targets' argument")

        _setter("duration_in_minutes", duration_in_minutes)
        _setter("targets", targets)

    @property
    @pulumi.getter(name="durationInMinutes")
    def duration_in_minutes(self) -> int:
        return pulumi.get(self, "duration_in_minutes")

    @property
    @pulumi.getter
    def targets(self) -> Sequence['outputs.GetPlanStageTargetResult']:
        return pulumi.get(self, "targets")


@pulumi.output_type
class GetPlanStageTargetResult(dict):
    def __init__(__self__, *,
                 channel_target_infos: Sequence['outputs.GetPlanStageTargetChannelTargetInfoResult'],
                 contact_target_infos: Sequence['outputs.GetPlanStageTargetContactTargetInfoResult']):
        GetPlanStageTargetResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            channel_target_infos=channel_target_infos,
            contact_target_infos=contact_target_infos,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             channel_target_infos: Optional[Sequence['outputs.GetPlanStageTargetChannelTargetInfoResult']] = None,
             contact_target_infos: Optional[Sequence['outputs.GetPlanStageTargetContactTargetInfoResult']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if channel_target_infos is None and 'channelTargetInfos' in kwargs:
            channel_target_infos = kwargs['channelTargetInfos']
        if channel_target_infos is None:
            raise TypeError("Missing 'channel_target_infos' argument")
        if contact_target_infos is None and 'contactTargetInfos' in kwargs:
            contact_target_infos = kwargs['contactTargetInfos']
        if contact_target_infos is None:
            raise TypeError("Missing 'contact_target_infos' argument")

        _setter("channel_target_infos", channel_target_infos)
        _setter("contact_target_infos", contact_target_infos)

    @property
    @pulumi.getter(name="channelTargetInfos")
    def channel_target_infos(self) -> Sequence['outputs.GetPlanStageTargetChannelTargetInfoResult']:
        return pulumi.get(self, "channel_target_infos")

    @property
    @pulumi.getter(name="contactTargetInfos")
    def contact_target_infos(self) -> Sequence['outputs.GetPlanStageTargetContactTargetInfoResult']:
        return pulumi.get(self, "contact_target_infos")


@pulumi.output_type
class GetPlanStageTargetChannelTargetInfoResult(dict):
    def __init__(__self__, *,
                 contact_channel_id: str,
                 retry_interval_in_minutes: int):
        GetPlanStageTargetChannelTargetInfoResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            contact_channel_id=contact_channel_id,
            retry_interval_in_minutes=retry_interval_in_minutes,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             contact_channel_id: Optional[str] = None,
             retry_interval_in_minutes: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if contact_channel_id is None and 'contactChannelId' in kwargs:
            contact_channel_id = kwargs['contactChannelId']
        if contact_channel_id is None:
            raise TypeError("Missing 'contact_channel_id' argument")
        if retry_interval_in_minutes is None and 'retryIntervalInMinutes' in kwargs:
            retry_interval_in_minutes = kwargs['retryIntervalInMinutes']
        if retry_interval_in_minutes is None:
            raise TypeError("Missing 'retry_interval_in_minutes' argument")

        _setter("contact_channel_id", contact_channel_id)
        _setter("retry_interval_in_minutes", retry_interval_in_minutes)

    @property
    @pulumi.getter(name="contactChannelId")
    def contact_channel_id(self) -> str:
        return pulumi.get(self, "contact_channel_id")

    @property
    @pulumi.getter(name="retryIntervalInMinutes")
    def retry_interval_in_minutes(self) -> int:
        return pulumi.get(self, "retry_interval_in_minutes")


@pulumi.output_type
class GetPlanStageTargetContactTargetInfoResult(dict):
    def __init__(__self__, *,
                 contact_id: str,
                 is_essential: bool):
        """
        :param str contact_id: The Amazon Resource Name (ARN) of the contact or escalation plan.
        """
        GetPlanStageTargetContactTargetInfoResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            contact_id=contact_id,
            is_essential=is_essential,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             contact_id: Optional[str] = None,
             is_essential: Optional[bool] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if contact_id is None and 'contactId' in kwargs:
            contact_id = kwargs['contactId']
        if contact_id is None:
            raise TypeError("Missing 'contact_id' argument")
        if is_essential is None and 'isEssential' in kwargs:
            is_essential = kwargs['isEssential']
        if is_essential is None:
            raise TypeError("Missing 'is_essential' argument")

        _setter("contact_id", contact_id)
        _setter("is_essential", is_essential)

    @property
    @pulumi.getter(name="contactId")
    def contact_id(self) -> str:
        """
        The Amazon Resource Name (ARN) of the contact or escalation plan.
        """
        return pulumi.get(self, "contact_id")

    @property
    @pulumi.getter(name="isEssential")
    def is_essential(self) -> bool:
        return pulumi.get(self, "is_essential")



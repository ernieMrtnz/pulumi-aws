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
    'AliasRoutingConfigurationArgs',
    'StateMachineLoggingConfigurationArgs',
    'StateMachineTracingConfigurationArgs',
]

@pulumi.input_type
class AliasRoutingConfigurationArgs:
    def __init__(__self__, *,
                 state_machine_version_arn: pulumi.Input[str],
                 weight: pulumi.Input[int]):
        """
        :param pulumi.Input[str] state_machine_version_arn: The Amazon Resource Name (ARN) of the state machine version.
        :param pulumi.Input[int] weight: Percentage of traffic routed to the state machine version.
        """
        AliasRoutingConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            state_machine_version_arn=state_machine_version_arn,
            weight=weight,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             state_machine_version_arn: Optional[pulumi.Input[str]] = None,
             weight: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if state_machine_version_arn is None and 'stateMachineVersionArn' in kwargs:
            state_machine_version_arn = kwargs['stateMachineVersionArn']
        if state_machine_version_arn is None:
            raise TypeError("Missing 'state_machine_version_arn' argument")
        if weight is None:
            raise TypeError("Missing 'weight' argument")

        _setter("state_machine_version_arn", state_machine_version_arn)
        _setter("weight", weight)

    @property
    @pulumi.getter(name="stateMachineVersionArn")
    def state_machine_version_arn(self) -> pulumi.Input[str]:
        """
        The Amazon Resource Name (ARN) of the state machine version.
        """
        return pulumi.get(self, "state_machine_version_arn")

    @state_machine_version_arn.setter
    def state_machine_version_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "state_machine_version_arn", value)

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Input[int]:
        """
        Percentage of traffic routed to the state machine version.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: pulumi.Input[int]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class StateMachineLoggingConfigurationArgs:
    def __init__(__self__, *,
                 include_execution_data: Optional[pulumi.Input[bool]] = None,
                 level: Optional[pulumi.Input[str]] = None,
                 log_destination: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[bool] include_execution_data: Determines whether execution data is included in your log. When set to `false`, data is excluded.
        :param pulumi.Input[str] level: Defines which category of execution history events are logged. Valid values: `ALL`, `ERROR`, `FATAL`, `OFF`
        :param pulumi.Input[str] log_destination: Amazon Resource Name (ARN) of a CloudWatch log group. Make sure the State Machine has the correct IAM policies for logging. The ARN must end with `:*`
        """
        StateMachineLoggingConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            include_execution_data=include_execution_data,
            level=level,
            log_destination=log_destination,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             include_execution_data: Optional[pulumi.Input[bool]] = None,
             level: Optional[pulumi.Input[str]] = None,
             log_destination: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if include_execution_data is None and 'includeExecutionData' in kwargs:
            include_execution_data = kwargs['includeExecutionData']
        if log_destination is None and 'logDestination' in kwargs:
            log_destination = kwargs['logDestination']

        if include_execution_data is not None:
            _setter("include_execution_data", include_execution_data)
        if level is not None:
            _setter("level", level)
        if log_destination is not None:
            _setter("log_destination", log_destination)

    @property
    @pulumi.getter(name="includeExecutionData")
    def include_execution_data(self) -> Optional[pulumi.Input[bool]]:
        """
        Determines whether execution data is included in your log. When set to `false`, data is excluded.
        """
        return pulumi.get(self, "include_execution_data")

    @include_execution_data.setter
    def include_execution_data(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "include_execution_data", value)

    @property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[str]]:
        """
        Defines which category of execution history events are logged. Valid values: `ALL`, `ERROR`, `FATAL`, `OFF`
        """
        return pulumi.get(self, "level")

    @level.setter
    def level(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "level", value)

    @property
    @pulumi.getter(name="logDestination")
    def log_destination(self) -> Optional[pulumi.Input[str]]:
        """
        Amazon Resource Name (ARN) of a CloudWatch log group. Make sure the State Machine has the correct IAM policies for logging. The ARN must end with `:*`
        """
        return pulumi.get(self, "log_destination")

    @log_destination.setter
    def log_destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "log_destination", value)


@pulumi.input_type
class StateMachineTracingConfigurationArgs:
    def __init__(__self__, *,
                 enabled: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] enabled: When set to `true`, AWS X-Ray tracing is enabled. Make sure the State Machine has the correct IAM policies for logging. See the [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/xray-iam.html) for details.
        """
        StateMachineTracingConfigurationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if enabled is not None:
            _setter("enabled", enabled)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        When set to `true`, AWS X-Ray tracing is enabled. Make sure the State Machine has the correct IAM policies for logging. See the [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/xray-iam.html) for details.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)



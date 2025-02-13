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
    'GetStateMachineVersionsResult',
    'AwaitableGetStateMachineVersionsResult',
    'get_state_machine_versions',
    'get_state_machine_versions_output',
]

@pulumi.output_type
class GetStateMachineVersionsResult:
    """
    A collection of values returned by getStateMachineVersions.
    """
    def __init__(__self__, id=None, statemachine_arn=None, statemachine_versions=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if statemachine_arn and not isinstance(statemachine_arn, str):
            raise TypeError("Expected argument 'statemachine_arn' to be a str")
        pulumi.set(__self__, "statemachine_arn", statemachine_arn)
        if statemachine_versions and not isinstance(statemachine_versions, list):
            raise TypeError("Expected argument 'statemachine_versions' to be a list")
        pulumi.set(__self__, "statemachine_versions", statemachine_versions)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="statemachineArn")
    def statemachine_arn(self) -> str:
        return pulumi.get(self, "statemachine_arn")

    @property
    @pulumi.getter(name="statemachineVersions")
    def statemachine_versions(self) -> Sequence[str]:
        """
        ARN List identifying the statemachine versions.
        """
        return pulumi.get(self, "statemachine_versions")


class AwaitableGetStateMachineVersionsResult(GetStateMachineVersionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStateMachineVersionsResult(
            id=self.id,
            statemachine_arn=self.statemachine_arn,
            statemachine_versions=self.statemachine_versions)


def get_state_machine_versions(statemachine_arn: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStateMachineVersionsResult:
    """
    Data source for managing an AWS SFN (Step Functions) State Machine Versions.

    ## Example Usage
    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.sfn.get_state_machine_versions(statemachine_arn=aws_sfn_state_machine["test"]["arn"])
    ```


    :param str statemachine_arn: ARN of the State Machine.
    """
    __args__ = dict()
    __args__['statemachineArn'] = statemachine_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:sfn/getStateMachineVersions:getStateMachineVersions', __args__, opts=opts, typ=GetStateMachineVersionsResult).value

    return AwaitableGetStateMachineVersionsResult(
        id=pulumi.get(__ret__, 'id'),
        statemachine_arn=pulumi.get(__ret__, 'statemachine_arn'),
        statemachine_versions=pulumi.get(__ret__, 'statemachine_versions'))


@_utilities.lift_output_func(get_state_machine_versions)
def get_state_machine_versions_output(statemachine_arn: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStateMachineVersionsResult]:
    """
    Data source for managing an AWS SFN (Step Functions) State Machine Versions.

    ## Example Usage
    ### Basic Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    test = aws.sfn.get_state_machine_versions(statemachine_arn=aws_sfn_state_machine["test"]["arn"])
    ```


    :param str statemachine_arn: ARN of the State Machine.
    """
    ...

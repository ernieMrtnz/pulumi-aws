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
    'GetRulesPackagesResult',
    'AwaitableGetRulesPackagesResult',
    'get_rules_packages',
    'get_rules_packages_output',
]

@pulumi.output_type
class GetRulesPackagesResult:
    """
    A collection of values returned by getRulesPackages.
    """
    def __init__(__self__, arns=None, id=None):
        if arns and not isinstance(arns, list):
            raise TypeError("Expected argument 'arns' to be a list")
        pulumi.set(__self__, "arns", arns)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def arns(self) -> Sequence[str]:
        """
        List of the Amazon Inspector Classic Rules Packages arns available in the AWS region.
        """
        return pulumi.get(self, "arns")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")


class AwaitableGetRulesPackagesResult(GetRulesPackagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRulesPackagesResult(
            arns=self.arns,
            id=self.id)


def get_rules_packages(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRulesPackagesResult:
    """
    The Amazon Inspector Classic Rules Packages data source allows access to the list of AWS
    Inspector Rules Packages which can be used by Amazon Inspector Classic within the region
    configured in the provider.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    rules = aws.inspector.get_rules_packages()
    # e.g., Use in aws_inspector_assessment_template
    group = aws.inspector.ResourceGroup("group", tags={
        "test": "test",
    })
    assessment_assessment_target = aws.inspector.AssessmentTarget("assessmentAssessmentTarget", resource_group_arn=group.arn)
    assessment_assessment_template = aws.inspector.AssessmentTemplate("assessmentAssessmentTemplate",
        target_arn=assessment_assessment_target.arn,
        duration=60,
        rules_package_arns=rules.arns)
    ```
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:inspector/getRulesPackages:getRulesPackages', __args__, opts=opts, typ=GetRulesPackagesResult).value

    return AwaitableGetRulesPackagesResult(
        arns=pulumi.get(__ret__, 'arns'),
        id=pulumi.get(__ret__, 'id'))


@_utilities.lift_output_func(get_rules_packages)
def get_rules_packages_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRulesPackagesResult]:
    """
    The Amazon Inspector Classic Rules Packages data source allows access to the list of AWS
    Inspector Rules Packages which can be used by Amazon Inspector Classic within the region
    configured in the provider.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    rules = aws.inspector.get_rules_packages()
    # e.g., Use in aws_inspector_assessment_template
    group = aws.inspector.ResourceGroup("group", tags={
        "test": "test",
    })
    assessment_assessment_target = aws.inspector.AssessmentTarget("assessmentAssessmentTarget", resource_group_arn=group.arn)
    assessment_assessment_template = aws.inspector.AssessmentTemplate("assessmentAssessmentTemplate",
        target_arn=assessment_assessment_target.arn,
        duration=60,
        rules_package_arns=rules.arns)
    ```
    """
    ...

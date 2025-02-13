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
    'OrganizationConfigurationAutoEnableArgs',
]

@pulumi.input_type
class OrganizationConfigurationAutoEnableArgs:
    def __init__(__self__, *,
                 ec2: pulumi.Input[bool],
                 ecr: pulumi.Input[bool],
                 lambda_: Optional[pulumi.Input[bool]] = None):
        """
        :param pulumi.Input[bool] ec2: Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        :param pulumi.Input[bool] ecr: Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        :param pulumi.Input[bool] lambda_: Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        OrganizationConfigurationAutoEnableArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            ec2=ec2,
            ecr=ecr,
            lambda_=lambda_,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             ec2: Optional[pulumi.Input[bool]] = None,
             ecr: Optional[pulumi.Input[bool]] = None,
             lambda_: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if ec2 is None:
            raise TypeError("Missing 'ec2' argument")
        if ecr is None:
            raise TypeError("Missing 'ecr' argument")
        if lambda_ is None and 'lambda' in kwargs:
            lambda_ = kwargs['lambda']

        _setter("ec2", ec2)
        _setter("ecr", ecr)
        if lambda_ is not None:
            _setter("lambda_", lambda_)

    @property
    @pulumi.getter
    def ec2(self) -> pulumi.Input[bool]:
        """
        Whether Amazon EC2 scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "ec2")

    @ec2.setter
    def ec2(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ec2", value)

    @property
    @pulumi.getter
    def ecr(self) -> pulumi.Input[bool]:
        """
        Whether Amazon ECR scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "ecr")

    @ecr.setter
    def ecr(self, value: pulumi.Input[bool]):
        pulumi.set(self, "ecr", value)

    @property
    @pulumi.getter(name="lambda")
    def lambda_(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether Lambda Function scans are automatically enabled for new members of your Amazon Inspector organization.
        """
        return pulumi.get(self, "lambda_")

    @lambda_.setter
    def lambda_(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "lambda_", value)



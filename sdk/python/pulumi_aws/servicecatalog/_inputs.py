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
    'ProductProvisioningArtifactParametersArgs',
    'ProvisionedProductOutputArgs',
    'ProvisionedProductProvisioningParameterArgs',
    'ProvisionedProductStackSetProvisioningPreferencesArgs',
    'ServiceActionDefinitionArgs',
]

@pulumi.input_type
class ProductProvisioningArtifactParametersArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 disable_template_validation: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 template_physical_id: Optional[pulumi.Input[str]] = None,
                 template_url: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] description: Description of the provisioning artifact (i.e., version), including how it differs from the previous provisioning artifact.
        :param pulumi.Input[bool] disable_template_validation: Whether AWS Service Catalog stops validating the specified provisioning artifact template even if it is invalid.
        :param pulumi.Input[str] name: Name of the provisioning artifact (for example, `v1`, `v2beta`). No spaces are allowed.
        :param pulumi.Input[str] template_physical_id: Template source as the physical ID of the resource that contains the template. Currently only supports CloudFormation stack ARN. Specify the physical ID as `arn:[partition]:cloudformation:[region]:[account ID]:stack/[stack name]/[resource ID]`.
        :param pulumi.Input[str] template_url: Template source as URL of the CloudFormation template in Amazon S3.
        :param pulumi.Input[str] type: Type of provisioning artifact. See [AWS Docs](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactProperties.html) for valid list of values.
        """
        ProductProvisioningArtifactParametersArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            disable_template_validation=disable_template_validation,
            name=name,
            template_physical_id=template_physical_id,
            template_url=template_url,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             disable_template_validation: Optional[pulumi.Input[bool]] = None,
             name: Optional[pulumi.Input[str]] = None,
             template_physical_id: Optional[pulumi.Input[str]] = None,
             template_url: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if disable_template_validation is None and 'disableTemplateValidation' in kwargs:
            disable_template_validation = kwargs['disableTemplateValidation']
        if template_physical_id is None and 'templatePhysicalId' in kwargs:
            template_physical_id = kwargs['templatePhysicalId']
        if template_url is None and 'templateUrl' in kwargs:
            template_url = kwargs['templateUrl']

        if description is not None:
            _setter("description", description)
        if disable_template_validation is not None:
            _setter("disable_template_validation", disable_template_validation)
        if name is not None:
            _setter("name", name)
        if template_physical_id is not None:
            _setter("template_physical_id", template_physical_id)
        if template_url is not None:
            _setter("template_url", template_url)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the provisioning artifact (i.e., version), including how it differs from the previous provisioning artifact.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="disableTemplateValidation")
    def disable_template_validation(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether AWS Service Catalog stops validating the specified provisioning artifact template even if it is invalid.
        """
        return pulumi.get(self, "disable_template_validation")

    @disable_template_validation.setter
    def disable_template_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disable_template_validation", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the provisioning artifact (for example, `v1`, `v2beta`). No spaces are allowed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="templatePhysicalId")
    def template_physical_id(self) -> Optional[pulumi.Input[str]]:
        """
        Template source as the physical ID of the resource that contains the template. Currently only supports CloudFormation stack ARN. Specify the physical ID as `arn:[partition]:cloudformation:[region]:[account ID]:stack/[stack name]/[resource ID]`.
        """
        return pulumi.get(self, "template_physical_id")

    @template_physical_id.setter
    def template_physical_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_physical_id", value)

    @property
    @pulumi.getter(name="templateUrl")
    def template_url(self) -> Optional[pulumi.Input[str]]:
        """
        Template source as URL of the CloudFormation template in Amazon S3.
        """
        return pulumi.get(self, "template_url")

    @template_url.setter
    def template_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "template_url", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of provisioning artifact. See [AWS Docs](https://docs.aws.amazon.com/servicecatalog/latest/dg/API_ProvisioningArtifactProperties.html) for valid list of values.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class ProvisionedProductOutputArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] description: The description of the output.
        :param pulumi.Input[str] key: Parameter key.
        :param pulumi.Input[str] value: Parameter value.
        """
        ProvisionedProductOutputArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            description=description,
            key=key,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             description: Optional[pulumi.Input[str]] = None,
             key: Optional[pulumi.Input[str]] = None,
             value: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if description is not None:
            _setter("description", description)
        if key is not None:
            _setter("key", key)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the output.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ProvisionedProductProvisioningParameterArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 use_previous_value: Optional[pulumi.Input[bool]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] key: Parameter key.
        :param pulumi.Input[bool] use_previous_value: Whether to ignore `value` and keep the previous parameter value. Ignored when initially provisioning a product.
        :param pulumi.Input[str] value: Parameter value.
        """
        ProvisionedProductProvisioningParameterArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            use_previous_value=use_previous_value,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: Optional[pulumi.Input[str]] = None,
             use_previous_value: Optional[pulumi.Input[bool]] = None,
             value: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if key is None:
            raise TypeError("Missing 'key' argument")
        if use_previous_value is None and 'usePreviousValue' in kwargs:
            use_previous_value = kwargs['usePreviousValue']

        _setter("key", key)
        if use_previous_value is not None:
            _setter("use_previous_value", use_previous_value)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        Parameter key.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="usePreviousValue")
    def use_previous_value(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to ignore `value` and keep the previous parameter value. Ignored when initially provisioning a product.
        """
        return pulumi.get(self, "use_previous_value")

    @use_previous_value.setter
    def use_previous_value(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_previous_value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ProvisionedProductStackSetProvisioningPreferencesArgs:
    def __init__(__self__, *,
                 accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 failure_tolerance_count: Optional[pulumi.Input[int]] = None,
                 failure_tolerance_percentage: Optional[pulumi.Input[int]] = None,
                 max_concurrency_count: Optional[pulumi.Input[int]] = None,
                 max_concurrency_percentage: Optional[pulumi.Input[int]] = None,
                 regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input[str]]] accounts: One or more AWS accounts that will have access to the provisioned product. The AWS accounts specified should be within the list of accounts in the STACKSET constraint. To get the list of accounts in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all accounts from the STACKSET constraint.
        :param pulumi.Input[int] failure_tolerance_count: Number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both. The default value is 0 if no value is specified.
        :param pulumi.Input[int] failure_tolerance_percentage: Percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both.
        :param pulumi.Input[int] max_concurrency_count: Maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `failure_tolerance_count`. `max_concurrency_count` is at most one more than the `failure_tolerance_count`. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        :param pulumi.Input[int] max_concurrency_percentage: Maximum percentage of accounts in which to perform this operation at one time. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as 1 instead. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] regions: One or more AWS Regions where the provisioned product will be available. The specified regions should be within the list of regions from the STACKSET constraint. To get the list of regions in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all regions from the STACKSET constraint.
        """
        ProvisionedProductStackSetProvisioningPreferencesArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            accounts=accounts,
            failure_tolerance_count=failure_tolerance_count,
            failure_tolerance_percentage=failure_tolerance_percentage,
            max_concurrency_count=max_concurrency_count,
            max_concurrency_percentage=max_concurrency_percentage,
            regions=regions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             accounts: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             failure_tolerance_count: Optional[pulumi.Input[int]] = None,
             failure_tolerance_percentage: Optional[pulumi.Input[int]] = None,
             max_concurrency_count: Optional[pulumi.Input[int]] = None,
             max_concurrency_percentage: Optional[pulumi.Input[int]] = None,
             regions: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if failure_tolerance_count is None and 'failureToleranceCount' in kwargs:
            failure_tolerance_count = kwargs['failureToleranceCount']
        if failure_tolerance_percentage is None and 'failureTolerancePercentage' in kwargs:
            failure_tolerance_percentage = kwargs['failureTolerancePercentage']
        if max_concurrency_count is None and 'maxConcurrencyCount' in kwargs:
            max_concurrency_count = kwargs['maxConcurrencyCount']
        if max_concurrency_percentage is None and 'maxConcurrencyPercentage' in kwargs:
            max_concurrency_percentage = kwargs['maxConcurrencyPercentage']

        if accounts is not None:
            _setter("accounts", accounts)
        if failure_tolerance_count is not None:
            _setter("failure_tolerance_count", failure_tolerance_count)
        if failure_tolerance_percentage is not None:
            _setter("failure_tolerance_percentage", failure_tolerance_percentage)
        if max_concurrency_count is not None:
            _setter("max_concurrency_count", max_concurrency_count)
        if max_concurrency_percentage is not None:
            _setter("max_concurrency_percentage", max_concurrency_percentage)
        if regions is not None:
            _setter("regions", regions)

    @property
    @pulumi.getter
    def accounts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        One or more AWS accounts that will have access to the provisioned product. The AWS accounts specified should be within the list of accounts in the STACKSET constraint. To get the list of accounts in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all accounts from the STACKSET constraint.
        """
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter(name="failureToleranceCount")
    def failure_tolerance_count(self) -> Optional[pulumi.Input[int]]:
        """
        Number of accounts, per region, for which this operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both. The default value is 0 if no value is specified.
        """
        return pulumi.get(self, "failure_tolerance_count")

    @failure_tolerance_count.setter
    def failure_tolerance_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "failure_tolerance_count", value)

    @property
    @pulumi.getter(name="failureTolerancePercentage")
    def failure_tolerance_percentage(self) -> Optional[pulumi.Input[int]]:
        """
        Percentage of accounts, per region, for which this stack operation can fail before AWS Service Catalog stops the operation in that region. If the operation is stopped in a region, AWS Service Catalog doesn't attempt the operation in any subsequent regions. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. You must specify either `failure_tolerance_count` or `failure_tolerance_percentage`, but not both.
        """
        return pulumi.get(self, "failure_tolerance_percentage")

    @failure_tolerance_percentage.setter
    def failure_tolerance_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "failure_tolerance_percentage", value)

    @property
    @pulumi.getter(name="maxConcurrencyCount")
    def max_concurrency_count(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum number of accounts in which to perform this operation at one time. This is dependent on the value of `failure_tolerance_count`. `max_concurrency_count` is at most one more than the `failure_tolerance_count`. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        """
        return pulumi.get(self, "max_concurrency_count")

    @max_concurrency_count.setter
    def max_concurrency_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_concurrency_count", value)

    @property
    @pulumi.getter(name="maxConcurrencyPercentage")
    def max_concurrency_percentage(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum percentage of accounts in which to perform this operation at one time. When calculating the number of accounts based on the specified percentage, AWS Service Catalog rounds down to the next whole number. This is true except in cases where rounding down would result is zero. In this case, AWS Service Catalog sets the number as 1 instead. Note that this setting lets you specify the maximum for operations. For large deployments, under certain circumstances the actual number of accounts acted upon concurrently may be lower due to service throttling. You must specify either `max_concurrency_count` or `max_concurrency_percentage`, but not both.
        """
        return pulumi.get(self, "max_concurrency_percentage")

    @max_concurrency_percentage.setter
    def max_concurrency_percentage(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_concurrency_percentage", value)

    @property
    @pulumi.getter
    def regions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        One or more AWS Regions where the provisioned product will be available. The specified regions should be within the list of regions from the STACKSET constraint. To get the list of regions in the STACKSET constraint, use the `aws_servicecatalog_provisioning_parameters` data source. If no values are specified, the default value is all regions from the STACKSET constraint.
        """
        return pulumi.get(self, "regions")

    @regions.setter
    def regions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "regions", value)


@pulumi.input_type
class ServiceActionDefinitionArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 version: pulumi.Input[str],
                 assume_role: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] name: Name of the SSM document. For example, `AWS-RestartEC2Instance`. If you are using a shared SSM document, you must provide the ARN instead of the name.
        :param pulumi.Input[str] version: SSM document version. For example, `1`.
        :param pulumi.Input[str] assume_role: ARN of the role that performs the self-service actions on your behalf. For example, `arn:aws:iam::12345678910:role/ActionRole`. To reuse the provisioned product launch role, set to `LAUNCH_ROLE`.
        :param pulumi.Input[str] parameters: List of parameters in JSON format. For example: `[{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TARGET\\"}]` or `[{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TEXT_VALUE\\"}]`.
        :param pulumi.Input[str] type: Service action definition type. Valid value is `SSM_AUTOMATION`. Default is `SSM_AUTOMATION`.
        """
        ServiceActionDefinitionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            version=version,
            assume_role=assume_role,
            parameters=parameters,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             version: Optional[pulumi.Input[str]] = None,
             assume_role: Optional[pulumi.Input[str]] = None,
             parameters: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if version is None:
            raise TypeError("Missing 'version' argument")
        if assume_role is None and 'assumeRole' in kwargs:
            assume_role = kwargs['assumeRole']

        _setter("name", name)
        _setter("version", version)
        if assume_role is not None:
            _setter("assume_role", assume_role)
        if parameters is not None:
            _setter("parameters", parameters)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Name of the SSM document. For example, `AWS-RestartEC2Instance`. If you are using a shared SSM document, you must provide the ARN instead of the name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def version(self) -> pulumi.Input[str]:
        """
        SSM document version. For example, `1`.
        """
        return pulumi.get(self, "version")

    @version.setter
    def version(self, value: pulumi.Input[str]):
        pulumi.set(self, "version", value)

    @property
    @pulumi.getter(name="assumeRole")
    def assume_role(self) -> Optional[pulumi.Input[str]]:
        """
        ARN of the role that performs the self-service actions on your behalf. For example, `arn:aws:iam::12345678910:role/ActionRole`. To reuse the provisioned product launch role, set to `LAUNCH_ROLE`.
        """
        return pulumi.get(self, "assume_role")

    @assume_role.setter
    def assume_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assume_role", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[str]]:
        """
        List of parameters in JSON format. For example: `[{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TARGET\\"}]` or `[{\\"Name\\":\\"InstanceId\\",\\"Type\\":\\"TEXT_VALUE\\"}]`.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Service action definition type. Valid value is `SSM_AUTOMATION`. Default is `SSM_AUTOMATION`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)



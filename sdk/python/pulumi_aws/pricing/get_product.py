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

__all__ = [
    'GetProductResult',
    'AwaitableGetProductResult',
    'get_product',
    'get_product_output',
]

@pulumi.output_type
class GetProductResult:
    """
    A collection of values returned by getProduct.
    """
    def __init__(__self__, filters=None, id=None, result=None, service_code=None):
        if filters and not isinstance(filters, list):
            raise TypeError("Expected argument 'filters' to be a list")
        pulumi.set(__self__, "filters", filters)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if result and not isinstance(result, str):
            raise TypeError("Expected argument 'result' to be a str")
        pulumi.set(__self__, "result", result)
        if service_code and not isinstance(service_code, str):
            raise TypeError("Expected argument 'service_code' to be a str")
        pulumi.set(__self__, "service_code", service_code)

    @property
    @pulumi.getter
    def filters(self) -> Sequence['outputs.GetProductFilterResult']:
        return pulumi.get(self, "filters")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def result(self) -> str:
        """
        Set to the product returned from the API.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter(name="serviceCode")
    def service_code(self) -> str:
        return pulumi.get(self, "service_code")


class AwaitableGetProductResult(GetProductResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductResult(
            filters=self.filters,
            id=self.id,
            result=self.result,
            service_code=self.service_code)


def get_product(filters: Optional[Sequence[pulumi.InputType['GetProductFilterArgs']]] = None,
                service_code: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductResult:
    """
    Use this data source to get the pricing information of all products in AWS.
    This data source is only available in a us-east-1 or ap-south-1 provider.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.pricing.get_product(filters=[
            aws.pricing.GetProductFilterArgs(
                field="instanceType",
                value="c5.xlarge",
            ),
            aws.pricing.GetProductFilterArgs(
                field="operatingSystem",
                value="Linux",
            ),
            aws.pricing.GetProductFilterArgs(
                field="location",
                value="US East (N. Virginia)",
            ),
            aws.pricing.GetProductFilterArgs(
                field="preInstalledSw",
                value="NA",
            ),
            aws.pricing.GetProductFilterArgs(
                field="licenseModel",
                value="No License required",
            ),
            aws.pricing.GetProductFilterArgs(
                field="tenancy",
                value="Shared",
            ),
            aws.pricing.GetProductFilterArgs(
                field="capacitystatus",
                value="Used",
            ),
        ],
        service_code="AmazonEC2")
    ```

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.pricing.get_product(filters=[
            aws.pricing.GetProductFilterArgs(
                field="instanceType",
                value="ds1.xlarge",
            ),
            aws.pricing.GetProductFilterArgs(
                field="location",
                value="US East (N. Virginia)",
            ),
        ],
        service_code="AmazonRedshift")
    ```


    :param Sequence[pulumi.InputType['GetProductFilterArgs']] filters: List of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.
    :param str service_code: Code of the service. Available service codes can be fetched using the DescribeServices pricing API call.
    """
    __args__ = dict()
    __args__['filters'] = filters
    __args__['serviceCode'] = service_code
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws:pricing/getProduct:getProduct', __args__, opts=opts, typ=GetProductResult).value

    return AwaitableGetProductResult(
        filters=pulumi.get(__ret__, 'filters'),
        id=pulumi.get(__ret__, 'id'),
        result=pulumi.get(__ret__, 'result'),
        service_code=pulumi.get(__ret__, 'service_code'))


@_utilities.lift_output_func(get_product)
def get_product_output(filters: Optional[pulumi.Input[Sequence[pulumi.InputType['GetProductFilterArgs']]]] = None,
                       service_code: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProductResult]:
    """
    Use this data source to get the pricing information of all products in AWS.
    This data source is only available in a us-east-1 or ap-south-1 provider.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.pricing.get_product(filters=[
            aws.pricing.GetProductFilterArgs(
                field="instanceType",
                value="c5.xlarge",
            ),
            aws.pricing.GetProductFilterArgs(
                field="operatingSystem",
                value="Linux",
            ),
            aws.pricing.GetProductFilterArgs(
                field="location",
                value="US East (N. Virginia)",
            ),
            aws.pricing.GetProductFilterArgs(
                field="preInstalledSw",
                value="NA",
            ),
            aws.pricing.GetProductFilterArgs(
                field="licenseModel",
                value="No License required",
            ),
            aws.pricing.GetProductFilterArgs(
                field="tenancy",
                value="Shared",
            ),
            aws.pricing.GetProductFilterArgs(
                field="capacitystatus",
                value="Used",
            ),
        ],
        service_code="AmazonEC2")
    ```

    ```python
    import pulumi
    import pulumi_aws as aws

    example = aws.pricing.get_product(filters=[
            aws.pricing.GetProductFilterArgs(
                field="instanceType",
                value="ds1.xlarge",
            ),
            aws.pricing.GetProductFilterArgs(
                field="location",
                value="US East (N. Virginia)",
            ),
        ],
        service_code="AmazonRedshift")
    ```


    :param Sequence[pulumi.InputType['GetProductFilterArgs']] filters: List of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.
    :param str service_code: Code of the service. Available service codes can be fetched using the DescribeServices pricing API call.
    """
    ...

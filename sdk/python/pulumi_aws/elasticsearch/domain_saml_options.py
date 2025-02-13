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

__all__ = ['DomainSamlOptionsArgs', 'DomainSamlOptions']

@pulumi.input_type
class DomainSamlOptionsArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 saml_options: Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']] = None):
        """
        The set of arguments for constructing a DomainSamlOptions resource.
        :param pulumi.Input[str] domain_name: Name of the domain.
               
               The following arguments are optional:
        :param pulumi.Input['DomainSamlOptionsSamlOptionsArgs'] saml_options: The SAML authentication options for an AWS Elasticsearch Domain.
        """
        DomainSamlOptionsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_name=domain_name,
            saml_options=saml_options,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_name: Optional[pulumi.Input[str]] = None,
             saml_options: Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if domain_name is None and 'domainName' in kwargs:
            domain_name = kwargs['domainName']
        if domain_name is None:
            raise TypeError("Missing 'domain_name' argument")
        if saml_options is None and 'samlOptions' in kwargs:
            saml_options = kwargs['samlOptions']

        _setter("domain_name", domain_name)
        if saml_options is not None:
            _setter("saml_options", saml_options)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        Name of the domain.

        The following arguments are optional:
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="samlOptions")
    def saml_options(self) -> Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']]:
        """
        The SAML authentication options for an AWS Elasticsearch Domain.
        """
        return pulumi.get(self, "saml_options")

    @saml_options.setter
    def saml_options(self, value: Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']]):
        pulumi.set(self, "saml_options", value)


@pulumi.input_type
class _DomainSamlOptionsState:
    def __init__(__self__, *,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 saml_options: Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']] = None):
        """
        Input properties used for looking up and filtering DomainSamlOptions resources.
        :param pulumi.Input[str] domain_name: Name of the domain.
               
               The following arguments are optional:
        :param pulumi.Input['DomainSamlOptionsSamlOptionsArgs'] saml_options: The SAML authentication options for an AWS Elasticsearch Domain.
        """
        _DomainSamlOptionsState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            domain_name=domain_name,
            saml_options=saml_options,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             domain_name: Optional[pulumi.Input[str]] = None,
             saml_options: Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if domain_name is None and 'domainName' in kwargs:
            domain_name = kwargs['domainName']
        if saml_options is None and 'samlOptions' in kwargs:
            saml_options = kwargs['samlOptions']

        if domain_name is not None:
            _setter("domain_name", domain_name)
        if saml_options is not None:
            _setter("saml_options", saml_options)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the domain.

        The following arguments are optional:
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="samlOptions")
    def saml_options(self) -> Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']]:
        """
        The SAML authentication options for an AWS Elasticsearch Domain.
        """
        return pulumi.get(self, "saml_options")

    @saml_options.setter
    def saml_options(self, value: Optional[pulumi.Input['DomainSamlOptionsSamlOptionsArgs']]):
        pulumi.set(self, "saml_options", value)


class DomainSamlOptions(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 saml_options: Optional[pulumi.Input[pulumi.InputType['DomainSamlOptionsSamlOptionsArgs']]] = None,
                 __props__=None):
        """
        Manages SAML authentication options for an AWS Elasticsearch Domain.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain = aws.elasticsearch.Domain("exampleDomain",
            elasticsearch_version="1.5",
            cluster_config=aws.elasticsearch.DomainClusterConfigArgs(
                instance_type="r4.large.elasticsearch",
            ),
            snapshot_options=aws.elasticsearch.DomainSnapshotOptionsArgs(
                automated_snapshot_start_hour=23,
            ),
            tags={
                "Domain": "TestDomain",
            })
        example_domain_saml_options = aws.elasticsearch.DomainSamlOptions("exampleDomainSamlOptions",
            domain_name=example_domain.domain_name,
            saml_options=aws.elasticsearch.DomainSamlOptionsSamlOptionsArgs(
                enabled=True,
                idp=aws.elasticsearch.DomainSamlOptionsSamlOptionsIdpArgs(
                    entity_id="https://example.com",
                    metadata_content=(lambda path: open(path).read())("./saml-metadata.xml"),
                ),
            ))
        ```

        ## Import

        Using `pulumi import`, import Elasticsearch domains using the `domain_name`. For example:

        ```sh
         $ pulumi import aws:elasticsearch/domainSamlOptions:DomainSamlOptions example domain_name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Name of the domain.
               
               The following arguments are optional:
        :param pulumi.Input[pulumi.InputType['DomainSamlOptionsSamlOptionsArgs']] saml_options: The SAML authentication options for an AWS Elasticsearch Domain.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainSamlOptionsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages SAML authentication options for an AWS Elasticsearch Domain.

        ## Example Usage
        ### Basic Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_domain = aws.elasticsearch.Domain("exampleDomain",
            elasticsearch_version="1.5",
            cluster_config=aws.elasticsearch.DomainClusterConfigArgs(
                instance_type="r4.large.elasticsearch",
            ),
            snapshot_options=aws.elasticsearch.DomainSnapshotOptionsArgs(
                automated_snapshot_start_hour=23,
            ),
            tags={
                "Domain": "TestDomain",
            })
        example_domain_saml_options = aws.elasticsearch.DomainSamlOptions("exampleDomainSamlOptions",
            domain_name=example_domain.domain_name,
            saml_options=aws.elasticsearch.DomainSamlOptionsSamlOptionsArgs(
                enabled=True,
                idp=aws.elasticsearch.DomainSamlOptionsSamlOptionsIdpArgs(
                    entity_id="https://example.com",
                    metadata_content=(lambda path: open(path).read())("./saml-metadata.xml"),
                ),
            ))
        ```

        ## Import

        Using `pulumi import`, import Elasticsearch domains using the `domain_name`. For example:

        ```sh
         $ pulumi import aws:elasticsearch/domainSamlOptions:DomainSamlOptions example domain_name
        ```

        :param str resource_name: The name of the resource.
        :param DomainSamlOptionsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainSamlOptionsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            DomainSamlOptionsArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 saml_options: Optional[pulumi.Input[pulumi.InputType['DomainSamlOptionsSamlOptionsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainSamlOptionsArgs.__new__(DomainSamlOptionsArgs)

            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            saml_options = _utilities.configure(saml_options, DomainSamlOptionsSamlOptionsArgs, True)
            __props__.__dict__["saml_options"] = saml_options
        super(DomainSamlOptions, __self__).__init__(
            'aws:elasticsearch/domainSamlOptions:DomainSamlOptions',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            saml_options: Optional[pulumi.Input[pulumi.InputType['DomainSamlOptionsSamlOptionsArgs']]] = None) -> 'DomainSamlOptions':
        """
        Get an existing DomainSamlOptions resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_name: Name of the domain.
               
               The following arguments are optional:
        :param pulumi.Input[pulumi.InputType['DomainSamlOptionsSamlOptionsArgs']] saml_options: The SAML authentication options for an AWS Elasticsearch Domain.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainSamlOptionsState.__new__(_DomainSamlOptionsState)

        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["saml_options"] = saml_options
        return DomainSamlOptions(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        Name of the domain.

        The following arguments are optional:
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="samlOptions")
    def saml_options(self) -> pulumi.Output[Optional['outputs.DomainSamlOptionsSamlOptions']]:
        """
        The SAML authentication options for an AWS Elasticsearch Domain.
        """
        return pulumi.get(self, "saml_options")


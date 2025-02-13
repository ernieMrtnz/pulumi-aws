# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RequestValidatorArgs', 'RequestValidator']

@pulumi.input_type
class RequestValidatorArgs:
    def __init__(__self__, *,
                 rest_api: pulumi.Input[str],
                 name: Optional[pulumi.Input[str]] = None,
                 validate_request_body: Optional[pulumi.Input[bool]] = None,
                 validate_request_parameters: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a RequestValidator resource.
        :param pulumi.Input[str] rest_api: ID of the associated Rest API
        :param pulumi.Input[str] name: Name of the request validator
        :param pulumi.Input[bool] validate_request_body: Boolean whether to validate request body. Defaults to `false`.
        :param pulumi.Input[bool] validate_request_parameters: Boolean whether to validate request parameters. Defaults to `false`.
        """
        RequestValidatorArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            rest_api=rest_api,
            name=name,
            validate_request_body=validate_request_body,
            validate_request_parameters=validate_request_parameters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             rest_api: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             validate_request_body: Optional[pulumi.Input[bool]] = None,
             validate_request_parameters: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if rest_api is None and 'restApi' in kwargs:
            rest_api = kwargs['restApi']
        if rest_api is None:
            raise TypeError("Missing 'rest_api' argument")
        if validate_request_body is None and 'validateRequestBody' in kwargs:
            validate_request_body = kwargs['validateRequestBody']
        if validate_request_parameters is None and 'validateRequestParameters' in kwargs:
            validate_request_parameters = kwargs['validateRequestParameters']

        _setter("rest_api", rest_api)
        if name is not None:
            _setter("name", name)
        if validate_request_body is not None:
            _setter("validate_request_body", validate_request_body)
        if validate_request_parameters is not None:
            _setter("validate_request_parameters", validate_request_parameters)

    @property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Input[str]:
        """
        ID of the associated Rest API
        """
        return pulumi.get(self, "rest_api")

    @rest_api.setter
    def rest_api(self, value: pulumi.Input[str]):
        pulumi.set(self, "rest_api", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the request validator
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether to validate request body. Defaults to `false`.
        """
        return pulumi.get(self, "validate_request_body")

    @validate_request_body.setter
    def validate_request_body(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validate_request_body", value)

    @property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether to validate request parameters. Defaults to `false`.
        """
        return pulumi.get(self, "validate_request_parameters")

    @validate_request_parameters.setter
    def validate_request_parameters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validate_request_parameters", value)


@pulumi.input_type
class _RequestValidatorState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 rest_api: Optional[pulumi.Input[str]] = None,
                 validate_request_body: Optional[pulumi.Input[bool]] = None,
                 validate_request_parameters: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering RequestValidator resources.
        :param pulumi.Input[str] name: Name of the request validator
        :param pulumi.Input[str] rest_api: ID of the associated Rest API
        :param pulumi.Input[bool] validate_request_body: Boolean whether to validate request body. Defaults to `false`.
        :param pulumi.Input[bool] validate_request_parameters: Boolean whether to validate request parameters. Defaults to `false`.
        """
        _RequestValidatorState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            rest_api=rest_api,
            validate_request_body=validate_request_body,
            validate_request_parameters=validate_request_parameters,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             rest_api: Optional[pulumi.Input[str]] = None,
             validate_request_body: Optional[pulumi.Input[bool]] = None,
             validate_request_parameters: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if rest_api is None and 'restApi' in kwargs:
            rest_api = kwargs['restApi']
        if validate_request_body is None and 'validateRequestBody' in kwargs:
            validate_request_body = kwargs['validateRequestBody']
        if validate_request_parameters is None and 'validateRequestParameters' in kwargs:
            validate_request_parameters = kwargs['validateRequestParameters']

        if name is not None:
            _setter("name", name)
        if rest_api is not None:
            _setter("rest_api", rest_api)
        if validate_request_body is not None:
            _setter("validate_request_body", validate_request_body)
        if validate_request_parameters is not None:
            _setter("validate_request_parameters", validate_request_parameters)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the request validator
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the associated Rest API
        """
        return pulumi.get(self, "rest_api")

    @rest_api.setter
    def rest_api(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rest_api", value)

    @property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether to validate request body. Defaults to `false`.
        """
        return pulumi.get(self, "validate_request_body")

    @validate_request_body.setter
    def validate_request_body(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validate_request_body", value)

    @property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> Optional[pulumi.Input[bool]]:
        """
        Boolean whether to validate request parameters. Defaults to `false`.
        """
        return pulumi.get(self, "validate_request_parameters")

    @validate_request_parameters.setter
    def validate_request_parameters(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "validate_request_parameters", value)


class RequestValidator(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rest_api: Optional[pulumi.Input[str]] = None,
                 validate_request_body: Optional[pulumi.Input[bool]] = None,
                 validate_request_parameters: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        Manages an API Gateway Request Validator.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigateway.RequestValidator("example",
            rest_api=aws_api_gateway_rest_api["example"]["id"],
            validate_request_body=True,
            validate_request_parameters=True)
        ```

        ## Import

        Using `pulumi import`, import `aws_api_gateway_request_validator` using `REST-API-ID/REQUEST-VALIDATOR-ID`. For example:

        ```sh
         $ pulumi import aws:apigateway/requestValidator:RequestValidator example 12345abcde/67890fghij
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the request validator
        :param pulumi.Input[str] rest_api: ID of the associated Rest API
        :param pulumi.Input[bool] validate_request_body: Boolean whether to validate request body. Defaults to `false`.
        :param pulumi.Input[bool] validate_request_parameters: Boolean whether to validate request parameters. Defaults to `false`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RequestValidatorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an API Gateway Request Validator.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example = aws.apigateway.RequestValidator("example",
            rest_api=aws_api_gateway_rest_api["example"]["id"],
            validate_request_body=True,
            validate_request_parameters=True)
        ```

        ## Import

        Using `pulumi import`, import `aws_api_gateway_request_validator` using `REST-API-ID/REQUEST-VALIDATOR-ID`. For example:

        ```sh
         $ pulumi import aws:apigateway/requestValidator:RequestValidator example 12345abcde/67890fghij
        ```

        :param str resource_name: The name of the resource.
        :param RequestValidatorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RequestValidatorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RequestValidatorArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rest_api: Optional[pulumi.Input[str]] = None,
                 validate_request_body: Optional[pulumi.Input[bool]] = None,
                 validate_request_parameters: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RequestValidatorArgs.__new__(RequestValidatorArgs)

            __props__.__dict__["name"] = name
            if rest_api is None and not opts.urn:
                raise TypeError("Missing required property 'rest_api'")
            __props__.__dict__["rest_api"] = rest_api
            __props__.__dict__["validate_request_body"] = validate_request_body
            __props__.__dict__["validate_request_parameters"] = validate_request_parameters
        super(RequestValidator, __self__).__init__(
            'aws:apigateway/requestValidator:RequestValidator',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            rest_api: Optional[pulumi.Input[str]] = None,
            validate_request_body: Optional[pulumi.Input[bool]] = None,
            validate_request_parameters: Optional[pulumi.Input[bool]] = None) -> 'RequestValidator':
        """
        Get an existing RequestValidator resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: Name of the request validator
        :param pulumi.Input[str] rest_api: ID of the associated Rest API
        :param pulumi.Input[bool] validate_request_body: Boolean whether to validate request body. Defaults to `false`.
        :param pulumi.Input[bool] validate_request_parameters: Boolean whether to validate request parameters. Defaults to `false`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RequestValidatorState.__new__(_RequestValidatorState)

        __props__.__dict__["name"] = name
        __props__.__dict__["rest_api"] = rest_api
        __props__.__dict__["validate_request_body"] = validate_request_body
        __props__.__dict__["validate_request_parameters"] = validate_request_parameters
        return RequestValidator(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the request validator
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="restApi")
    def rest_api(self) -> pulumi.Output[str]:
        """
        ID of the associated Rest API
        """
        return pulumi.get(self, "rest_api")

    @property
    @pulumi.getter(name="validateRequestBody")
    def validate_request_body(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean whether to validate request body. Defaults to `false`.
        """
        return pulumi.get(self, "validate_request_body")

    @property
    @pulumi.getter(name="validateRequestParameters")
    def validate_request_parameters(self) -> pulumi.Output[Optional[bool]]:
        """
        Boolean whether to validate request parameters. Defaults to `false`.
        """
        return pulumi.get(self, "validate_request_parameters")


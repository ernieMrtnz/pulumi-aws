# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['BackendEnvironmentArgs', 'BackendEnvironment']

@pulumi.input_type
class BackendEnvironmentArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 environment_name: pulumi.Input[str],
                 deployment_artifacts: Optional[pulumi.Input[str]] = None,
                 stack_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a BackendEnvironment resource.
        :param pulumi.Input[str] app_id: Unique ID for an Amplify app.
        :param pulumi.Input[str] environment_name: Name for the backend environment.
        :param pulumi.Input[str] deployment_artifacts: Name of deployment artifacts.
        :param pulumi.Input[str] stack_name: AWS CloudFormation stack name of a backend environment.
        """
        BackendEnvironmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            app_id=app_id,
            environment_name=environment_name,
            deployment_artifacts=deployment_artifacts,
            stack_name=stack_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             app_id: Optional[pulumi.Input[str]] = None,
             environment_name: Optional[pulumi.Input[str]] = None,
             deployment_artifacts: Optional[pulumi.Input[str]] = None,
             stack_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if app_id is None and 'appId' in kwargs:
            app_id = kwargs['appId']
        if app_id is None:
            raise TypeError("Missing 'app_id' argument")
        if environment_name is None and 'environmentName' in kwargs:
            environment_name = kwargs['environmentName']
        if environment_name is None:
            raise TypeError("Missing 'environment_name' argument")
        if deployment_artifacts is None and 'deploymentArtifacts' in kwargs:
            deployment_artifacts = kwargs['deploymentArtifacts']
        if stack_name is None and 'stackName' in kwargs:
            stack_name = kwargs['stackName']

        _setter("app_id", app_id)
        _setter("environment_name", environment_name)
        if deployment_artifacts is not None:
            _setter("deployment_artifacts", deployment_artifacts)
        if stack_name is not None:
            _setter("stack_name", stack_name)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        """
        Unique ID for an Amplify app.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Input[str]:
        """
        Name for the backend environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter(name="deploymentArtifacts")
    def deployment_artifacts(self) -> Optional[pulumi.Input[str]]:
        """
        Name of deployment artifacts.
        """
        return pulumi.get(self, "deployment_artifacts")

    @deployment_artifacts.setter
    def deployment_artifacts(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_artifacts", value)

    @property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> Optional[pulumi.Input[str]]:
        """
        AWS CloudFormation stack name of a backend environment.
        """
        return pulumi.get(self, "stack_name")

    @stack_name.setter
    def stack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_name", value)


@pulumi.input_type
class _BackendEnvironmentState:
    def __init__(__self__, *,
                 app_id: Optional[pulumi.Input[str]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 deployment_artifacts: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 stack_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering BackendEnvironment resources.
        :param pulumi.Input[str] app_id: Unique ID for an Amplify app.
        :param pulumi.Input[str] arn: ARN for a backend environment that is part of an Amplify app.
        :param pulumi.Input[str] deployment_artifacts: Name of deployment artifacts.
        :param pulumi.Input[str] environment_name: Name for the backend environment.
        :param pulumi.Input[str] stack_name: AWS CloudFormation stack name of a backend environment.
        """
        _BackendEnvironmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            app_id=app_id,
            arn=arn,
            deployment_artifacts=deployment_artifacts,
            environment_name=environment_name,
            stack_name=stack_name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             app_id: Optional[pulumi.Input[str]] = None,
             arn: Optional[pulumi.Input[str]] = None,
             deployment_artifacts: Optional[pulumi.Input[str]] = None,
             environment_name: Optional[pulumi.Input[str]] = None,
             stack_name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if app_id is None and 'appId' in kwargs:
            app_id = kwargs['appId']
        if deployment_artifacts is None and 'deploymentArtifacts' in kwargs:
            deployment_artifacts = kwargs['deploymentArtifacts']
        if environment_name is None and 'environmentName' in kwargs:
            environment_name = kwargs['environmentName']
        if stack_name is None and 'stackName' in kwargs:
            stack_name = kwargs['stackName']

        if app_id is not None:
            _setter("app_id", app_id)
        if arn is not None:
            _setter("arn", arn)
        if deployment_artifacts is not None:
            _setter("deployment_artifacts", deployment_artifacts)
        if environment_name is not None:
            _setter("environment_name", environment_name)
        if stack_name is not None:
            _setter("stack_name", stack_name)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[str]]:
        """
        Unique ID for an Amplify app.
        """
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        ARN for a backend environment that is part of an Amplify app.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="deploymentArtifacts")
    def deployment_artifacts(self) -> Optional[pulumi.Input[str]]:
        """
        Name of deployment artifacts.
        """
        return pulumi.get(self, "deployment_artifacts")

    @deployment_artifacts.setter
    def deployment_artifacts(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_artifacts", value)

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name for the backend environment.
        """
        return pulumi.get(self, "environment_name")

    @environment_name.setter
    def environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_name", value)

    @property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> Optional[pulumi.Input[str]]:
        """
        AWS CloudFormation stack name of a backend environment.
        """
        return pulumi.get(self, "stack_name")

    @stack_name.setter
    def stack_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "stack_name", value)


class BackendEnvironment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 deployment_artifacts: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 stack_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Amplify Backend Environment resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_app = aws.amplify.App("exampleApp")
        example_backend_environment = aws.amplify.BackendEnvironment("exampleBackendEnvironment",
            app_id=example_app.id,
            environment_name="example",
            deployment_artifacts="app-example-deployment",
            stack_name="amplify-app-example")
        ```

        ## Import

        Using `pulumi import`, import Amplify backend environment using `app_id` and `environment_name`. For example:

        ```sh
         $ pulumi import aws:amplify/backendEnvironment:BackendEnvironment example d2ypk4k47z8u6/example
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: Unique ID for an Amplify app.
        :param pulumi.Input[str] deployment_artifacts: Name of deployment artifacts.
        :param pulumi.Input[str] environment_name: Name for the backend environment.
        :param pulumi.Input[str] stack_name: AWS CloudFormation stack name of a backend environment.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BackendEnvironmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Amplify Backend Environment resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        example_app = aws.amplify.App("exampleApp")
        example_backend_environment = aws.amplify.BackendEnvironment("exampleBackendEnvironment",
            app_id=example_app.id,
            environment_name="example",
            deployment_artifacts="app-example-deployment",
            stack_name="amplify-app-example")
        ```

        ## Import

        Using `pulumi import`, import Amplify backend environment using `app_id` and `environment_name`. For example:

        ```sh
         $ pulumi import aws:amplify/backendEnvironment:BackendEnvironment example d2ypk4k47z8u6/example
        ```

        :param str resource_name: The name of the resource.
        :param BackendEnvironmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BackendEnvironmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BackendEnvironmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 deployment_artifacts: Optional[pulumi.Input[str]] = None,
                 environment_name: Optional[pulumi.Input[str]] = None,
                 stack_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BackendEnvironmentArgs.__new__(BackendEnvironmentArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["deployment_artifacts"] = deployment_artifacts
            if environment_name is None and not opts.urn:
                raise TypeError("Missing required property 'environment_name'")
            __props__.__dict__["environment_name"] = environment_name
            __props__.__dict__["stack_name"] = stack_name
            __props__.__dict__["arn"] = None
        super(BackendEnvironment, __self__).__init__(
            'aws:amplify/backendEnvironment:BackendEnvironment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            app_id: Optional[pulumi.Input[str]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            deployment_artifacts: Optional[pulumi.Input[str]] = None,
            environment_name: Optional[pulumi.Input[str]] = None,
            stack_name: Optional[pulumi.Input[str]] = None) -> 'BackendEnvironment':
        """
        Get an existing BackendEnvironment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] app_id: Unique ID for an Amplify app.
        :param pulumi.Input[str] arn: ARN for a backend environment that is part of an Amplify app.
        :param pulumi.Input[str] deployment_artifacts: Name of deployment artifacts.
        :param pulumi.Input[str] environment_name: Name for the backend environment.
        :param pulumi.Input[str] stack_name: AWS CloudFormation stack name of a backend environment.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BackendEnvironmentState.__new__(_BackendEnvironmentState)

        __props__.__dict__["app_id"] = app_id
        __props__.__dict__["arn"] = arn
        __props__.__dict__["deployment_artifacts"] = deployment_artifacts
        __props__.__dict__["environment_name"] = environment_name
        __props__.__dict__["stack_name"] = stack_name
        return BackendEnvironment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        """
        Unique ID for an Amplify app.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN for a backend environment that is part of an Amplify app.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="deploymentArtifacts")
    def deployment_artifacts(self) -> pulumi.Output[str]:
        """
        Name of deployment artifacts.
        """
        return pulumi.get(self, "deployment_artifacts")

    @property
    @pulumi.getter(name="environmentName")
    def environment_name(self) -> pulumi.Output[str]:
        """
        Name for the backend environment.
        """
        return pulumi.get(self, "environment_name")

    @property
    @pulumi.getter(name="stackName")
    def stack_name(self) -> pulumi.Output[str]:
        """
        AWS CloudFormation stack name of a backend environment.
        """
        return pulumi.get(self, "stack_name")


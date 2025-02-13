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

__all__ = ['TriggerArgs', 'Trigger']

@pulumi.input_type
class TriggerArgs:
    def __init__(__self__, *,
                 repository_name: pulumi.Input[str],
                 triggers: pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]):
        """
        The set of arguments for constructing a Trigger resource.
        :param pulumi.Input[str] repository_name: The name for the repository. This needs to be less than 100 characters.
        """
        TriggerArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            repository_name=repository_name,
            triggers=triggers,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             repository_name: Optional[pulumi.Input[str]] = None,
             triggers: Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if repository_name is None and 'repositoryName' in kwargs:
            repository_name = kwargs['repositoryName']
        if repository_name is None:
            raise TypeError("Missing 'repository_name' argument")
        if triggers is None:
            raise TypeError("Missing 'triggers' argument")

        _setter("repository_name", repository_name)
        _setter("triggers", triggers)

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Input[str]:
        """
        The name for the repository. This needs to be less than 100 characters.
        """
        return pulumi.get(self, "repository_name")

    @repository_name.setter
    def repository_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "repository_name", value)

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]:
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]):
        pulumi.set(self, "triggers", value)


@pulumi.input_type
class _TriggerState:
    def __init__(__self__, *,
                 configuration_id: Optional[pulumi.Input[str]] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]] = None):
        """
        Input properties used for looking up and filtering Trigger resources.
        :param pulumi.Input[str] configuration_id: System-generated unique identifier.
        :param pulumi.Input[str] repository_name: The name for the repository. This needs to be less than 100 characters.
        """
        _TriggerState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            configuration_id=configuration_id,
            repository_name=repository_name,
            triggers=triggers,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             configuration_id: Optional[pulumi.Input[str]] = None,
             repository_name: Optional[pulumi.Input[str]] = None,
             triggers: Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if configuration_id is None and 'configurationId' in kwargs:
            configuration_id = kwargs['configurationId']
        if repository_name is None and 'repositoryName' in kwargs:
            repository_name = kwargs['repositoryName']

        if configuration_id is not None:
            _setter("configuration_id", configuration_id)
        if repository_name is not None:
            _setter("repository_name", repository_name)
        if triggers is not None:
            _setter("triggers", triggers)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> Optional[pulumi.Input[str]]:
        """
        System-generated unique identifier.
        """
        return pulumi.get(self, "configuration_id")

    @configuration_id.setter
    def configuration_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_id", value)

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name for the repository. This needs to be less than 100 characters.
        """
        return pulumi.get(self, "repository_name")

    @repository_name.setter
    def repository_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "repository_name", value)

    @property
    @pulumi.getter
    def triggers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]]:
        return pulumi.get(self, "triggers")

    @triggers.setter
    def triggers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TriggerTriggerArgs']]]]):
        pulumi.set(self, "triggers", value)


class Trigger(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerTriggerArgs']]]]] = None,
                 __props__=None):
        """
        Provides a CodeCommit Trigger Resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_repository = aws.codecommit.Repository("testRepository", repository_name="test")
        test_trigger = aws.codecommit.Trigger("testTrigger",
            repository_name=test_repository.repository_name,
            triggers=[aws.codecommit.TriggerTriggerArgs(
                name="all",
                events=["all"],
                destination_arn=aws_sns_topic["test"]["arn"],
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] repository_name: The name for the repository. This needs to be less than 100 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TriggerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a CodeCommit Trigger Resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        test_repository = aws.codecommit.Repository("testRepository", repository_name="test")
        test_trigger = aws.codecommit.Trigger("testTrigger",
            repository_name=test_repository.repository_name,
            triggers=[aws.codecommit.TriggerTriggerArgs(
                name="all",
                events=["all"],
                destination_arn=aws_sns_topic["test"]["arn"],
            )])
        ```

        :param str resource_name: The name of the resource.
        :param TriggerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TriggerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TriggerArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 repository_name: Optional[pulumi.Input[str]] = None,
                 triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerTriggerArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TriggerArgs.__new__(TriggerArgs)

            if repository_name is None and not opts.urn:
                raise TypeError("Missing required property 'repository_name'")
            __props__.__dict__["repository_name"] = repository_name
            if triggers is None and not opts.urn:
                raise TypeError("Missing required property 'triggers'")
            __props__.__dict__["triggers"] = triggers
            __props__.__dict__["configuration_id"] = None
        super(Trigger, __self__).__init__(
            'aws:codecommit/trigger:Trigger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            configuration_id: Optional[pulumi.Input[str]] = None,
            repository_name: Optional[pulumi.Input[str]] = None,
            triggers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TriggerTriggerArgs']]]]] = None) -> 'Trigger':
        """
        Get an existing Trigger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] configuration_id: System-generated unique identifier.
        :param pulumi.Input[str] repository_name: The name for the repository. This needs to be less than 100 characters.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TriggerState.__new__(_TriggerState)

        __props__.__dict__["configuration_id"] = configuration_id
        __props__.__dict__["repository_name"] = repository_name
        __props__.__dict__["triggers"] = triggers
        return Trigger(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="configurationId")
    def configuration_id(self) -> pulumi.Output[str]:
        """
        System-generated unique identifier.
        """
        return pulumi.get(self, "configuration_id")

    @property
    @pulumi.getter(name="repositoryName")
    def repository_name(self) -> pulumi.Output[str]:
        """
        The name for the repository. This needs to be less than 100 characters.
        """
        return pulumi.get(self, "repository_name")

    @property
    @pulumi.getter
    def triggers(self) -> pulumi.Output[Sequence['outputs.TriggerTrigger']]:
        return pulumi.get(self, "triggers")


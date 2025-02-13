# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['WorkspaceApiKeyArgs', 'WorkspaceApiKey']

@pulumi.input_type
class WorkspaceApiKeyArgs:
    def __init__(__self__, *,
                 key_name: pulumi.Input[str],
                 key_role: pulumi.Input[str],
                 seconds_to_live: pulumi.Input[int],
                 workspace_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a WorkspaceApiKey resource.
        :param pulumi.Input[str] key_name: Specifies the name of the API key. Key names must be unique to the workspace.
        :param pulumi.Input[str] key_role: Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        :param pulumi.Input[int] seconds_to_live: Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        :param pulumi.Input[str] workspace_id: The ID of the workspace that the API key is valid for.
        """
        WorkspaceApiKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key_name=key_name,
            key_role=key_role,
            seconds_to_live=seconds_to_live,
            workspace_id=workspace_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key_name: Optional[pulumi.Input[str]] = None,
             key_role: Optional[pulumi.Input[str]] = None,
             seconds_to_live: Optional[pulumi.Input[int]] = None,
             workspace_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if key_name is None and 'keyName' in kwargs:
            key_name = kwargs['keyName']
        if key_name is None:
            raise TypeError("Missing 'key_name' argument")
        if key_role is None and 'keyRole' in kwargs:
            key_role = kwargs['keyRole']
        if key_role is None:
            raise TypeError("Missing 'key_role' argument")
        if seconds_to_live is None and 'secondsToLive' in kwargs:
            seconds_to_live = kwargs['secondsToLive']
        if seconds_to_live is None:
            raise TypeError("Missing 'seconds_to_live' argument")
        if workspace_id is None and 'workspaceId' in kwargs:
            workspace_id = kwargs['workspaceId']
        if workspace_id is None:
            raise TypeError("Missing 'workspace_id' argument")

        _setter("key_name", key_name)
        _setter("key_role", key_role)
        _setter("seconds_to_live", seconds_to_live)
        _setter("workspace_id", workspace_id)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[str]:
        """
        Specifies the name of the API key. Key names must be unique to the workspace.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyRole")
    def key_role(self) -> pulumi.Input[str]:
        """
        Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        """
        return pulumi.get(self, "key_role")

    @key_role.setter
    def key_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_role", value)

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> pulumi.Input[int]:
        """
        Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        """
        return pulumi.get(self, "seconds_to_live")

    @seconds_to_live.setter
    def seconds_to_live(self, value: pulumi.Input[int]):
        pulumi.set(self, "seconds_to_live", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Input[str]:
        """
        The ID of the workspace that the API key is valid for.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_id", value)


@pulumi.input_type
class _WorkspaceApiKeyState:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_role: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering WorkspaceApiKey resources.
        :param pulumi.Input[str] key: The key token in JSON format. Use this value as a bearer token to authenticate HTTP requests to the workspace.
        :param pulumi.Input[str] key_name: Specifies the name of the API key. Key names must be unique to the workspace.
        :param pulumi.Input[str] key_role: Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        :param pulumi.Input[int] seconds_to_live: Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        :param pulumi.Input[str] workspace_id: The ID of the workspace that the API key is valid for.
        """
        _WorkspaceApiKeyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            key_name=key_name,
            key_role=key_role,
            seconds_to_live=seconds_to_live,
            workspace_id=workspace_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: Optional[pulumi.Input[str]] = None,
             key_name: Optional[pulumi.Input[str]] = None,
             key_role: Optional[pulumi.Input[str]] = None,
             seconds_to_live: Optional[pulumi.Input[int]] = None,
             workspace_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if key_name is None and 'keyName' in kwargs:
            key_name = kwargs['keyName']
        if key_role is None and 'keyRole' in kwargs:
            key_role = kwargs['keyRole']
        if seconds_to_live is None and 'secondsToLive' in kwargs:
            seconds_to_live = kwargs['secondsToLive']
        if workspace_id is None and 'workspaceId' in kwargs:
            workspace_id = kwargs['workspaceId']

        if key is not None:
            _setter("key", key)
        if key_name is not None:
            _setter("key_name", key_name)
        if key_role is not None:
            _setter("key_role", key_role)
        if seconds_to_live is not None:
            _setter("seconds_to_live", seconds_to_live)
        if workspace_id is not None:
            _setter("workspace_id", workspace_id)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The key token in JSON format. Use this value as a bearer token to authenticate HTTP requests to the workspace.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the name of the API key. Key names must be unique to the workspace.
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyRole")
    def key_role(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        """
        return pulumi.get(self, "key_role")

    @key_role.setter
    def key_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_role", value)

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> Optional[pulumi.Input[int]]:
        """
        Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        """
        return pulumi.get(self, "seconds_to_live")

    @seconds_to_live.setter
    def seconds_to_live(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "seconds_to_live", value)

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the workspace that the API key is valid for.
        """
        return pulumi.get(self, "workspace_id")

    @workspace_id.setter
    def workspace_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "workspace_id", value)


class WorkspaceApiKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_role: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides an Amazon Managed Grafana workspace API Key resource.

        ## Example Usage
        ### Basic configuration

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.grafana.WorkspaceApiKey("key",
            key_name="test-key",
            key_role="VIEWER",
            seconds_to_live=3600,
            workspace_id=aws_grafana_workspace["test"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key_name: Specifies the name of the API key. Key names must be unique to the workspace.
        :param pulumi.Input[str] key_role: Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        :param pulumi.Input[int] seconds_to_live: Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        :param pulumi.Input[str] workspace_id: The ID of the workspace that the API key is valid for.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkspaceApiKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an Amazon Managed Grafana workspace API Key resource.

        ## Example Usage
        ### Basic configuration

        ```python
        import pulumi
        import pulumi_aws as aws

        key = aws.grafana.WorkspaceApiKey("key",
            key_name="test-key",
            key_role="VIEWER",
            seconds_to_live=3600,
            workspace_id=aws_grafana_workspace["test"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param WorkspaceApiKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkspaceApiKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            WorkspaceApiKeyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key_name: Optional[pulumi.Input[str]] = None,
                 key_role: Optional[pulumi.Input[str]] = None,
                 seconds_to_live: Optional[pulumi.Input[int]] = None,
                 workspace_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkspaceApiKeyArgs.__new__(WorkspaceApiKeyArgs)

            if key_name is None and not opts.urn:
                raise TypeError("Missing required property 'key_name'")
            __props__.__dict__["key_name"] = key_name
            if key_role is None and not opts.urn:
                raise TypeError("Missing required property 'key_role'")
            __props__.__dict__["key_role"] = key_role
            if seconds_to_live is None and not opts.urn:
                raise TypeError("Missing required property 'seconds_to_live'")
            __props__.__dict__["seconds_to_live"] = seconds_to_live
            if workspace_id is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_id'")
            __props__.__dict__["workspace_id"] = workspace_id
            __props__.__dict__["key"] = None
        super(WorkspaceApiKey, __self__).__init__(
            'aws:grafana/workspaceApiKey:WorkspaceApiKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key: Optional[pulumi.Input[str]] = None,
            key_name: Optional[pulumi.Input[str]] = None,
            key_role: Optional[pulumi.Input[str]] = None,
            seconds_to_live: Optional[pulumi.Input[int]] = None,
            workspace_id: Optional[pulumi.Input[str]] = None) -> 'WorkspaceApiKey':
        """
        Get an existing WorkspaceApiKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The key token in JSON format. Use this value as a bearer token to authenticate HTTP requests to the workspace.
        :param pulumi.Input[str] key_name: Specifies the name of the API key. Key names must be unique to the workspace.
        :param pulumi.Input[str] key_role: Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        :param pulumi.Input[int] seconds_to_live: Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        :param pulumi.Input[str] workspace_id: The ID of the workspace that the API key is valid for.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _WorkspaceApiKeyState.__new__(_WorkspaceApiKeyState)

        __props__.__dict__["key"] = key
        __props__.__dict__["key_name"] = key_name
        __props__.__dict__["key_role"] = key_role
        __props__.__dict__["seconds_to_live"] = seconds_to_live
        __props__.__dict__["workspace_id"] = workspace_id
        return WorkspaceApiKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The key token in JSON format. Use this value as a bearer token to authenticate HTTP requests to the workspace.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Output[str]:
        """
        Specifies the name of the API key. Key names must be unique to the workspace.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter(name="keyRole")
    def key_role(self) -> pulumi.Output[str]:
        """
        Specifies the permission level of the API key. Valid values are `VIEWER`, `EDITOR`, or `ADMIN`.
        """
        return pulumi.get(self, "key_role")

    @property
    @pulumi.getter(name="secondsToLive")
    def seconds_to_live(self) -> pulumi.Output[int]:
        """
        Specifies the time in seconds until the API key expires. Keys can be valid for up to 30 days.
        """
        return pulumi.get(self, "seconds_to_live")

    @property
    @pulumi.getter(name="workspaceId")
    def workspace_id(self) -> pulumi.Output[str]:
        """
        The ID of the workspace that the API key is valid for.
        """
        return pulumi.get(self, "workspace_id")


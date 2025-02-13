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

__all__ = ['ListenerRuleArgs', 'ListenerRule']

@pulumi.input_type
class ListenerRuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]],
                 conditions: pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]],
                 listener_arn: pulumi.Input[str],
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ListenerRule resource.
        :param pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]] actions: An Action block. Action blocks are documented below.
        :param pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]] conditions: A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        :param pulumi.Input[str] listener_arn: The ARN of the listener to which to attach the rule.
        :param pulumi.Input[int] priority: The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ListenerRuleArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            conditions=conditions,
            listener_arn=listener_arn,
            priority=priority,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]] = None,
             conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]] = None,
             listener_arn: Optional[pulumi.Input[str]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if actions is None:
            raise TypeError("Missing 'actions' argument")
        if conditions is None:
            raise TypeError("Missing 'conditions' argument")
        if listener_arn is None and 'listenerArn' in kwargs:
            listener_arn = kwargs['listenerArn']
        if listener_arn is None:
            raise TypeError("Missing 'listener_arn' argument")

        _setter("actions", actions)
        _setter("conditions", conditions)
        _setter("listener_arn", listener_arn)
        if priority is not None:
            _setter("priority", priority)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]:
        """
        An Action block. Action blocks are documented below.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]:
        """
        A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the listener to which to attach the rule.
        """
        return pulumi.get(self, "listener_arn")

    @listener_arn.setter
    def listener_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_arn", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _ListenerRuleState:
    def __init__(__self__, *,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]] = None,
                 arn: Optional[pulumi.Input[str]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering ListenerRule resources.
        :param pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]] actions: An Action block. Action blocks are documented below.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the target group.
        :param pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]] conditions: A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        :param pulumi.Input[str] listener_arn: The ARN of the listener to which to attach the rule.
        :param pulumi.Input[int] priority: The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        _ListenerRuleState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            arn=arn,
            conditions=conditions,
            listener_arn=listener_arn,
            priority=priority,
            tags=tags,
            tags_all=tags_all,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]] = None,
             arn: Optional[pulumi.Input[str]] = None,
             conditions: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]] = None,
             listener_arn: Optional[pulumi.Input[str]] = None,
             priority: Optional[pulumi.Input[int]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if listener_arn is None and 'listenerArn' in kwargs:
            listener_arn = kwargs['listenerArn']
        if tags_all is None and 'tagsAll' in kwargs:
            tags_all = kwargs['tagsAll']

        if actions is not None:
            _setter("actions", actions)
        if arn is not None:
            _setter("arn", arn)
        if conditions is not None:
            _setter("conditions", conditions)
        if listener_arn is not None:
            _setter("listener_arn", listener_arn)
        if priority is not None:
            _setter("priority", priority)
        if tags is not None:
            _setter("tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            _setter("tags_all", tags_all)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]]:
        """
        An Action block. Action blocks are documented below.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the target group.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]]:
        """
        A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ListenerRuleConditionArgs']]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the listener to which to attach the rule.
        """
        return pulumi.get(self, "listener_arn")

    @listener_arn.setter
    def listener_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_arn", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
        pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")

        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class ListenerRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleConditionArgs']]]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Load Balancer Listener Rule resource.

        > **Note:** `alb.ListenerRule` is known as `lb.ListenerRule`. The functionality is identical.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        # ...
        front_end_listener = aws.lb.Listener("frontEndListener")
        # Other parameters
        static = aws.lb.ListenerRule("static",
            listener_arn=front_end_listener.arn,
            priority=100,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="forward",
                target_group_arn=aws_lb_target_group["static"]["arn"],
            )],
            conditions=[
                aws.lb.ListenerRuleConditionArgs(
                    path_pattern=aws.lb.ListenerRuleConditionPathPatternArgs(
                        values=["/static/*"],
                    ),
                ),
                aws.lb.ListenerRuleConditionArgs(
                    host_header=aws.lb.ListenerRuleConditionHostHeaderArgs(
                        values=["example.com"],
                    ),
                ),
            ])
        # Forward action
        host_based_weighted_routing = aws.lb.ListenerRule("hostBasedWeightedRouting",
            listener_arn=front_end_listener.arn,
            priority=99,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="forward",
                target_group_arn=aws_lb_target_group["static"]["arn"],
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                host_header=aws.lb.ListenerRuleConditionHostHeaderArgs(
                    values=["my-service.*.mycompany.io"],
                ),
            )])
        # Weighted Forward action
        host_based_routing = aws.lb.ListenerRule("hostBasedRouting",
            listener_arn=front_end_listener.arn,
            priority=99,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="forward",
                forward=aws.lb.ListenerRuleActionForwardArgs(
                    target_groups=[
                        aws.lb.ListenerRuleActionForwardTargetGroupArgs(
                            arn=aws_lb_target_group["main"]["arn"],
                            weight=80,
                        ),
                        aws.lb.ListenerRuleActionForwardTargetGroupArgs(
                            arn=aws_lb_target_group["canary"]["arn"],
                            weight=20,
                        ),
                    ],
                    stickiness=aws.lb.ListenerRuleActionForwardStickinessArgs(
                        enabled=True,
                        duration=600,
                    ),
                ),
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                host_header=aws.lb.ListenerRuleConditionHostHeaderArgs(
                    values=["my-service.*.mycompany.io"],
                ),
            )])
        # Redirect action
        redirect_http_to_https = aws.lb.ListenerRule("redirectHttpToHttps",
            listener_arn=front_end_listener.arn,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="redirect",
                redirect=aws.lb.ListenerRuleActionRedirectArgs(
                    port="443",
                    protocol="HTTPS",
                    status_code="HTTP_301",
                ),
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                http_header=aws.lb.ListenerRuleConditionHttpHeaderArgs(
                    http_header_name="X-Forwarded-For",
                    values=["192.168.1.*"],
                ),
            )])
        # Fixed-response action
        health_check = aws.lb.ListenerRule("healthCheck",
            listener_arn=front_end_listener.arn,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="fixed-response",
                fixed_response=aws.lb.ListenerRuleActionFixedResponseArgs(
                    content_type="text/plain",
                    message_body="HEALTHY",
                    status_code="200",
                ),
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                query_strings=[
                    aws.lb.ListenerRuleConditionQueryStringArgs(
                        key="health",
                        value="check",
                    ),
                    aws.lb.ListenerRuleConditionQueryStringArgs(
                        value="bar",
                    ),
                ],
            )])
        # Authenticate-cognito Action
        pool = aws.cognito.UserPool("pool")
        # ...
        client = aws.cognito.UserPoolClient("client")
        # ...
        domain = aws.cognito.UserPoolDomain("domain")
        # ...
        admin = aws.lb.ListenerRule("admin",
            listener_arn=front_end_listener.arn,
            actions=[
                aws.lb.ListenerRuleActionArgs(
                    type="authenticate-cognito",
                    authenticate_cognito=aws.lb.ListenerRuleActionAuthenticateCognitoArgs(
                        user_pool_arn=pool.arn,
                        user_pool_client_id=client.id,
                        user_pool_domain=domain.domain,
                    ),
                ),
                aws.lb.ListenerRuleActionArgs(
                    type="forward",
                    target_group_arn=aws_lb_target_group["static"]["arn"],
                ),
            ])
        # Authenticate-oidc Action
        oidc = aws.lb.ListenerRule("oidc",
            listener_arn=front_end_listener.arn,
            actions=[
                aws.lb.ListenerRuleActionArgs(
                    type="authenticate-oidc",
                    authenticate_oidc=aws.lb.ListenerRuleActionAuthenticateOidcArgs(
                        authorization_endpoint="https://example.com/authorization_endpoint",
                        client_id="client_id",
                        client_secret="client_secret",
                        issuer="https://example.com",
                        token_endpoint="https://example.com/token_endpoint",
                        user_info_endpoint="https://example.com/user_info_endpoint",
                    ),
                ),
                aws.lb.ListenerRuleActionArgs(
                    type="forward",
                    target_group_arn=aws_lb_target_group["static"]["arn"],
                ),
            ])
        ```

        ## Import

        Using `pulumi import`, import rules using their ARN. For example:

        ```sh
         $ pulumi import aws:lb/listenerRule:ListenerRule front_end arn:aws:elasticloadbalancing:us-west-2:187416307283:listener-rule/app/test/8e4497da625e2d8a/9ab28ade35828f96/67b3d2d36dd7c26b
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]] actions: An Action block. Action blocks are documented below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleConditionArgs']]]] conditions: A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        :param pulumi.Input[str] listener_arn: The ARN of the listener to which to attach the rule.
        :param pulumi.Input[int] priority: The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ListenerRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Load Balancer Listener Rule resource.

        > **Note:** `alb.ListenerRule` is known as `lb.ListenerRule`. The functionality is identical.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws

        front_end_load_balancer = aws.lb.LoadBalancer("frontEndLoadBalancer")
        # ...
        front_end_listener = aws.lb.Listener("frontEndListener")
        # Other parameters
        static = aws.lb.ListenerRule("static",
            listener_arn=front_end_listener.arn,
            priority=100,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="forward",
                target_group_arn=aws_lb_target_group["static"]["arn"],
            )],
            conditions=[
                aws.lb.ListenerRuleConditionArgs(
                    path_pattern=aws.lb.ListenerRuleConditionPathPatternArgs(
                        values=["/static/*"],
                    ),
                ),
                aws.lb.ListenerRuleConditionArgs(
                    host_header=aws.lb.ListenerRuleConditionHostHeaderArgs(
                        values=["example.com"],
                    ),
                ),
            ])
        # Forward action
        host_based_weighted_routing = aws.lb.ListenerRule("hostBasedWeightedRouting",
            listener_arn=front_end_listener.arn,
            priority=99,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="forward",
                target_group_arn=aws_lb_target_group["static"]["arn"],
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                host_header=aws.lb.ListenerRuleConditionHostHeaderArgs(
                    values=["my-service.*.mycompany.io"],
                ),
            )])
        # Weighted Forward action
        host_based_routing = aws.lb.ListenerRule("hostBasedRouting",
            listener_arn=front_end_listener.arn,
            priority=99,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="forward",
                forward=aws.lb.ListenerRuleActionForwardArgs(
                    target_groups=[
                        aws.lb.ListenerRuleActionForwardTargetGroupArgs(
                            arn=aws_lb_target_group["main"]["arn"],
                            weight=80,
                        ),
                        aws.lb.ListenerRuleActionForwardTargetGroupArgs(
                            arn=aws_lb_target_group["canary"]["arn"],
                            weight=20,
                        ),
                    ],
                    stickiness=aws.lb.ListenerRuleActionForwardStickinessArgs(
                        enabled=True,
                        duration=600,
                    ),
                ),
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                host_header=aws.lb.ListenerRuleConditionHostHeaderArgs(
                    values=["my-service.*.mycompany.io"],
                ),
            )])
        # Redirect action
        redirect_http_to_https = aws.lb.ListenerRule("redirectHttpToHttps",
            listener_arn=front_end_listener.arn,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="redirect",
                redirect=aws.lb.ListenerRuleActionRedirectArgs(
                    port="443",
                    protocol="HTTPS",
                    status_code="HTTP_301",
                ),
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                http_header=aws.lb.ListenerRuleConditionHttpHeaderArgs(
                    http_header_name="X-Forwarded-For",
                    values=["192.168.1.*"],
                ),
            )])
        # Fixed-response action
        health_check = aws.lb.ListenerRule("healthCheck",
            listener_arn=front_end_listener.arn,
            actions=[aws.lb.ListenerRuleActionArgs(
                type="fixed-response",
                fixed_response=aws.lb.ListenerRuleActionFixedResponseArgs(
                    content_type="text/plain",
                    message_body="HEALTHY",
                    status_code="200",
                ),
            )],
            conditions=[aws.lb.ListenerRuleConditionArgs(
                query_strings=[
                    aws.lb.ListenerRuleConditionQueryStringArgs(
                        key="health",
                        value="check",
                    ),
                    aws.lb.ListenerRuleConditionQueryStringArgs(
                        value="bar",
                    ),
                ],
            )])
        # Authenticate-cognito Action
        pool = aws.cognito.UserPool("pool")
        # ...
        client = aws.cognito.UserPoolClient("client")
        # ...
        domain = aws.cognito.UserPoolDomain("domain")
        # ...
        admin = aws.lb.ListenerRule("admin",
            listener_arn=front_end_listener.arn,
            actions=[
                aws.lb.ListenerRuleActionArgs(
                    type="authenticate-cognito",
                    authenticate_cognito=aws.lb.ListenerRuleActionAuthenticateCognitoArgs(
                        user_pool_arn=pool.arn,
                        user_pool_client_id=client.id,
                        user_pool_domain=domain.domain,
                    ),
                ),
                aws.lb.ListenerRuleActionArgs(
                    type="forward",
                    target_group_arn=aws_lb_target_group["static"]["arn"],
                ),
            ])
        # Authenticate-oidc Action
        oidc = aws.lb.ListenerRule("oidc",
            listener_arn=front_end_listener.arn,
            actions=[
                aws.lb.ListenerRuleActionArgs(
                    type="authenticate-oidc",
                    authenticate_oidc=aws.lb.ListenerRuleActionAuthenticateOidcArgs(
                        authorization_endpoint="https://example.com/authorization_endpoint",
                        client_id="client_id",
                        client_secret="client_secret",
                        issuer="https://example.com",
                        token_endpoint="https://example.com/token_endpoint",
                        user_info_endpoint="https://example.com/user_info_endpoint",
                    ),
                ),
                aws.lb.ListenerRuleActionArgs(
                    type="forward",
                    target_group_arn=aws_lb_target_group["static"]["arn"],
                ),
            ])
        ```

        ## Import

        Using `pulumi import`, import rules using their ARN. For example:

        ```sh
         $ pulumi import aws:lb/listenerRule:ListenerRule front_end arn:aws:elasticloadbalancing:us-west-2:187416307283:listener-rule/app/test/8e4497da625e2d8a/9ab28ade35828f96/67b3d2d36dd7c26b
        ```

        :param str resource_name: The name of the resource.
        :param ListenerRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ListenerRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ListenerRuleArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleConditionArgs']]]]] = None,
                 listener_arn: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ListenerRuleArgs.__new__(ListenerRuleArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            if conditions is None and not opts.urn:
                raise TypeError("Missing required property 'conditions'")
            __props__.__dict__["conditions"] = conditions
            if listener_arn is None and not opts.urn:
                raise TypeError("Missing required property 'listener_arn'")
            __props__.__dict__["listener_arn"] = listener_arn
            __props__.__dict__["priority"] = priority
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["tags_all"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="aws:elasticloadbalancingv2/listenerRule:ListenerRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["tagsAll"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(ListenerRule, __self__).__init__(
            'aws:lb/listenerRule:ListenerRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            actions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]]] = None,
            arn: Optional[pulumi.Input[str]] = None,
            conditions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleConditionArgs']]]]] = None,
            listener_arn: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'ListenerRule':
        """
        Get an existing ListenerRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleActionArgs']]]] actions: An Action block. Action blocks are documented below.
        :param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the target group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ListenerRuleConditionArgs']]]] conditions: A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        :param pulumi.Input[str] listener_arn: The ARN of the listener to which to attach the rule.
        :param pulumi.Input[int] priority: The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags_all: A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ListenerRuleState.__new__(_ListenerRuleState)

        __props__.__dict__["actions"] = actions
        __props__.__dict__["arn"] = arn
        __props__.__dict__["conditions"] = conditions
        __props__.__dict__["listener_arn"] = listener_arn
        __props__.__dict__["priority"] = priority
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return ListenerRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence['outputs.ListenerRuleAction']]:
        """
        An Action block. Action blocks are documented below.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the target group.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Sequence['outputs.ListenerRuleCondition']]:
        """
        A Condition block. Multiple condition blocks of different types can be set and all must be satisfied for the rule to match. Condition blocks are documented below.
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="listenerArn")
    def listener_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the listener to which to attach the rule.
        """
        return pulumi.get(self, "listener_arn")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[int]:
        """
        The priority for the rule between `1` and `50000`. Leaving it unset will automatically set the rule with next available priority after currently existing highest rule. A listener can't have multiple rules with the same priority.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the resource. .If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        """
        A map of tags assigned to the resource, including those inherited from the provider `default_tags` configuration block.
        """
        warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
        pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")

        return pulumi.get(self, "tags_all")


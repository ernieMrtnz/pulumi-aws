# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RedriveAllowPolicyArgs', 'RedriveAllowPolicy']

@pulumi.input_type
class RedriveAllowPolicyArgs:
    def __init__(__self__, *,
                 queue_url: pulumi.Input[str],
                 redrive_allow_policy: pulumi.Input[str]):
        """
        The set of arguments for constructing a RedriveAllowPolicy resource.
        :param pulumi.Input[str] queue_url: The URL of the SQS Queue to which to attach the policy
        :param pulumi.Input[str] redrive_allow_policy: The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        RedriveAllowPolicyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            queue_url=queue_url,
            redrive_allow_policy=redrive_allow_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             queue_url: Optional[pulumi.Input[str]] = None,
             redrive_allow_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if queue_url is None and 'queueUrl' in kwargs:
            queue_url = kwargs['queueUrl']
        if queue_url is None:
            raise TypeError("Missing 'queue_url' argument")
        if redrive_allow_policy is None and 'redriveAllowPolicy' in kwargs:
            redrive_allow_policy = kwargs['redriveAllowPolicy']
        if redrive_allow_policy is None:
            raise TypeError("Missing 'redrive_allow_policy' argument")

        _setter("queue_url", queue_url)
        _setter("redrive_allow_policy", redrive_allow_policy)

    @property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Input[str]:
        """
        The URL of the SQS Queue to which to attach the policy
        """
        return pulumi.get(self, "queue_url")

    @queue_url.setter
    def queue_url(self, value: pulumi.Input[str]):
        pulumi.set(self, "queue_url", value)

    @property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> pulumi.Input[str]:
        """
        The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        return pulumi.get(self, "redrive_allow_policy")

    @redrive_allow_policy.setter
    def redrive_allow_policy(self, value: pulumi.Input[str]):
        pulumi.set(self, "redrive_allow_policy", value)


@pulumi.input_type
class _RedriveAllowPolicyState:
    def __init__(__self__, *,
                 queue_url: Optional[pulumi.Input[str]] = None,
                 redrive_allow_policy: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering RedriveAllowPolicy resources.
        :param pulumi.Input[str] queue_url: The URL of the SQS Queue to which to attach the policy
        :param pulumi.Input[str] redrive_allow_policy: The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        _RedriveAllowPolicyState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            queue_url=queue_url,
            redrive_allow_policy=redrive_allow_policy,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             queue_url: Optional[pulumi.Input[str]] = None,
             redrive_allow_policy: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if queue_url is None and 'queueUrl' in kwargs:
            queue_url = kwargs['queueUrl']
        if redrive_allow_policy is None and 'redriveAllowPolicy' in kwargs:
            redrive_allow_policy = kwargs['redriveAllowPolicy']

        if queue_url is not None:
            _setter("queue_url", queue_url)
        if redrive_allow_policy is not None:
            _setter("redrive_allow_policy", redrive_allow_policy)

    @property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL of the SQS Queue to which to attach the policy
        """
        return pulumi.get(self, "queue_url")

    @queue_url.setter
    def queue_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "queue_url", value)

    @property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> Optional[pulumi.Input[str]]:
        """
        The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        return pulumi.get(self, "redrive_allow_policy")

    @redrive_allow_policy.setter
    def redrive_allow_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "redrive_allow_policy", value)


class RedriveAllowPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 queue_url: Optional[pulumi.Input[str]] = None,
                 redrive_allow_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a SQS Queue Redrive Allow Policy resource.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example_queue = aws.sqs.Queue("exampleQueue")
        src = aws.sqs.Queue("src", redrive_policy=example_queue.arn.apply(lambda arn: json.dumps({
            "deadLetterTargetArn": arn,
            "maxReceiveCount": 4,
        })))
        example_redrive_allow_policy = aws.sqs.RedriveAllowPolicy("exampleRedriveAllowPolicy",
            queue_url=example_queue.id,
            redrive_allow_policy=src.arn.apply(lambda arn: json.dumps({
                "redrivePermission": "byQueue",
                "sourceQueueArns": [arn],
            })))
        ```

        ## Import

        Using `pulumi import`, import SQS Queue Redrive Allow Policies using the queue URL. For example:

        ```sh
         $ pulumi import aws:sqs/redriveAllowPolicy:RedriveAllowPolicy test https://queue.amazonaws.com/0123456789012/myqueue
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] queue_url: The URL of the SQS Queue to which to attach the policy
        :param pulumi.Input[str] redrive_allow_policy: The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RedriveAllowPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a SQS Queue Redrive Allow Policy resource.

        ## Example Usage

        ```python
        import pulumi
        import json
        import pulumi_aws as aws

        example_queue = aws.sqs.Queue("exampleQueue")
        src = aws.sqs.Queue("src", redrive_policy=example_queue.arn.apply(lambda arn: json.dumps({
            "deadLetterTargetArn": arn,
            "maxReceiveCount": 4,
        })))
        example_redrive_allow_policy = aws.sqs.RedriveAllowPolicy("exampleRedriveAllowPolicy",
            queue_url=example_queue.id,
            redrive_allow_policy=src.arn.apply(lambda arn: json.dumps({
                "redrivePermission": "byQueue",
                "sourceQueueArns": [arn],
            })))
        ```

        ## Import

        Using `pulumi import`, import SQS Queue Redrive Allow Policies using the queue URL. For example:

        ```sh
         $ pulumi import aws:sqs/redriveAllowPolicy:RedriveAllowPolicy test https://queue.amazonaws.com/0123456789012/myqueue
        ```

        :param str resource_name: The name of the resource.
        :param RedriveAllowPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RedriveAllowPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            RedriveAllowPolicyArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 queue_url: Optional[pulumi.Input[str]] = None,
                 redrive_allow_policy: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RedriveAllowPolicyArgs.__new__(RedriveAllowPolicyArgs)

            if queue_url is None and not opts.urn:
                raise TypeError("Missing required property 'queue_url'")
            __props__.__dict__["queue_url"] = queue_url
            if redrive_allow_policy is None and not opts.urn:
                raise TypeError("Missing required property 'redrive_allow_policy'")
            __props__.__dict__["redrive_allow_policy"] = redrive_allow_policy
        super(RedriveAllowPolicy, __self__).__init__(
            'aws:sqs/redriveAllowPolicy:RedriveAllowPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            queue_url: Optional[pulumi.Input[str]] = None,
            redrive_allow_policy: Optional[pulumi.Input[str]] = None) -> 'RedriveAllowPolicy':
        """
        Get an existing RedriveAllowPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] queue_url: The URL of the SQS Queue to which to attach the policy
        :param pulumi.Input[str] redrive_allow_policy: The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _RedriveAllowPolicyState.__new__(_RedriveAllowPolicyState)

        __props__.__dict__["queue_url"] = queue_url
        __props__.__dict__["redrive_allow_policy"] = redrive_allow_policy
        return RedriveAllowPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="queueUrl")
    def queue_url(self) -> pulumi.Output[str]:
        """
        The URL of the SQS Queue to which to attach the policy
        """
        return pulumi.get(self, "queue_url")

    @property
    @pulumi.getter(name="redriveAllowPolicy")
    def redrive_allow_policy(self) -> pulumi.Output[str]:
        """
        The JSON redrive allow policy for the SQS queue. Learn more in the [Amazon SQS dead-letter queues documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html).
        """
        return pulumi.get(self, "redrive_allow_policy")


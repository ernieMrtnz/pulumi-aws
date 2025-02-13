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

__all__ = [
    'CustomActionTypeConfigurationProperty',
    'CustomActionTypeInputArtifactDetails',
    'CustomActionTypeOutputArtifactDetails',
    'CustomActionTypeSettings',
    'PipelineArtifactStore',
    'PipelineArtifactStoreEncryptionKey',
    'PipelineStage',
    'PipelineStageAction',
    'WebhookAuthenticationConfiguration',
    'WebhookFilter',
]

@pulumi.output_type
class CustomActionTypeConfigurationProperty(dict):
    def __init__(__self__, *,
                 key: bool,
                 name: str,
                 required: bool,
                 secret: bool,
                 description: Optional[str] = None,
                 queryable: Optional[bool] = None,
                 type: Optional[str] = None):
        """
        :param bool key: Whether the configuration property is a key.
        :param str name: The name of the action configuration property.
        :param bool required: Whether the configuration property is a required value.
        :param bool secret: Whether the configuration property is secret.
        :param str description: The description of the action configuration property.
        :param bool queryable: Indicates that the property will be used in conjunction with PollForJobs.
        :param str type: The type of the configuration property. Valid values: `String`, `Number`, `Boolean`
        """
        CustomActionTypeConfigurationProperty._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            name=name,
            required=required,
            secret=secret,
            description=description,
            queryable=queryable,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: Optional[bool] = None,
             name: Optional[str] = None,
             required: Optional[bool] = None,
             secret: Optional[bool] = None,
             description: Optional[str] = None,
             queryable: Optional[bool] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if key is None:
            raise TypeError("Missing 'key' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if required is None:
            raise TypeError("Missing 'required' argument")
        if secret is None:
            raise TypeError("Missing 'secret' argument")

        _setter("key", key)
        _setter("name", name)
        _setter("required", required)
        _setter("secret", secret)
        if description is not None:
            _setter("description", description)
        if queryable is not None:
            _setter("queryable", queryable)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def key(self) -> bool:
        """
        Whether the configuration property is a key.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the action configuration property.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def required(self) -> bool:
        """
        Whether the configuration property is a required value.
        """
        return pulumi.get(self, "required")

    @property
    @pulumi.getter
    def secret(self) -> bool:
        """
        Whether the configuration property is secret.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the action configuration property.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def queryable(self) -> Optional[bool]:
        """
        Indicates that the property will be used in conjunction with PollForJobs.
        """
        return pulumi.get(self, "queryable")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of the configuration property. Valid values: `String`, `Number`, `Boolean`
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class CustomActionTypeInputArtifactDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maximumCount":
            suggest = "maximum_count"
        elif key == "minimumCount":
            suggest = "minimum_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomActionTypeInputArtifactDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomActionTypeInputArtifactDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomActionTypeInputArtifactDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 maximum_count: int,
                 minimum_count: int):
        """
        :param int maximum_count: The maximum number of artifacts allowed for the action type. Min: 0, Max: 5
        :param int minimum_count: The minimum number of artifacts allowed for the action type. Min: 0, Max: 5
        """
        CustomActionTypeInputArtifactDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            maximum_count=maximum_count,
            minimum_count=minimum_count,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             maximum_count: Optional[int] = None,
             minimum_count: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if maximum_count is None and 'maximumCount' in kwargs:
            maximum_count = kwargs['maximumCount']
        if maximum_count is None:
            raise TypeError("Missing 'maximum_count' argument")
        if minimum_count is None and 'minimumCount' in kwargs:
            minimum_count = kwargs['minimumCount']
        if minimum_count is None:
            raise TypeError("Missing 'minimum_count' argument")

        _setter("maximum_count", maximum_count)
        _setter("minimum_count", minimum_count)

    @property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> int:
        """
        The maximum number of artifacts allowed for the action type. Min: 0, Max: 5
        """
        return pulumi.get(self, "maximum_count")

    @property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> int:
        """
        The minimum number of artifacts allowed for the action type. Min: 0, Max: 5
        """
        return pulumi.get(self, "minimum_count")


@pulumi.output_type
class CustomActionTypeOutputArtifactDetails(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "maximumCount":
            suggest = "maximum_count"
        elif key == "minimumCount":
            suggest = "minimum_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomActionTypeOutputArtifactDetails. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomActionTypeOutputArtifactDetails.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomActionTypeOutputArtifactDetails.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 maximum_count: int,
                 minimum_count: int):
        """
        :param int maximum_count: The maximum number of artifacts allowed for the action type. Min: 0, Max: 5
        :param int minimum_count: The minimum number of artifacts allowed for the action type. Min: 0, Max: 5
        """
        CustomActionTypeOutputArtifactDetails._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            maximum_count=maximum_count,
            minimum_count=minimum_count,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             maximum_count: Optional[int] = None,
             minimum_count: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if maximum_count is None and 'maximumCount' in kwargs:
            maximum_count = kwargs['maximumCount']
        if maximum_count is None:
            raise TypeError("Missing 'maximum_count' argument")
        if minimum_count is None and 'minimumCount' in kwargs:
            minimum_count = kwargs['minimumCount']
        if minimum_count is None:
            raise TypeError("Missing 'minimum_count' argument")

        _setter("maximum_count", maximum_count)
        _setter("minimum_count", minimum_count)

    @property
    @pulumi.getter(name="maximumCount")
    def maximum_count(self) -> int:
        """
        The maximum number of artifacts allowed for the action type. Min: 0, Max: 5
        """
        return pulumi.get(self, "maximum_count")

    @property
    @pulumi.getter(name="minimumCount")
    def minimum_count(self) -> int:
        """
        The minimum number of artifacts allowed for the action type. Min: 0, Max: 5
        """
        return pulumi.get(self, "minimum_count")


@pulumi.output_type
class CustomActionTypeSettings(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "entityUrlTemplate":
            suggest = "entity_url_template"
        elif key == "executionUrlTemplate":
            suggest = "execution_url_template"
        elif key == "revisionUrlTemplate":
            suggest = "revision_url_template"
        elif key == "thirdPartyConfigurationUrl":
            suggest = "third_party_configuration_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CustomActionTypeSettings. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CustomActionTypeSettings.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CustomActionTypeSettings.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 entity_url_template: Optional[str] = None,
                 execution_url_template: Optional[str] = None,
                 revision_url_template: Optional[str] = None,
                 third_party_configuration_url: Optional[str] = None):
        """
        :param str entity_url_template: The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system.
        :param str execution_url_template: The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system.
        :param str revision_url_template: The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
        :param str third_party_configuration_url: The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
        """
        CustomActionTypeSettings._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            entity_url_template=entity_url_template,
            execution_url_template=execution_url_template,
            revision_url_template=revision_url_template,
            third_party_configuration_url=third_party_configuration_url,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             entity_url_template: Optional[str] = None,
             execution_url_template: Optional[str] = None,
             revision_url_template: Optional[str] = None,
             third_party_configuration_url: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if entity_url_template is None and 'entityUrlTemplate' in kwargs:
            entity_url_template = kwargs['entityUrlTemplate']
        if execution_url_template is None and 'executionUrlTemplate' in kwargs:
            execution_url_template = kwargs['executionUrlTemplate']
        if revision_url_template is None and 'revisionUrlTemplate' in kwargs:
            revision_url_template = kwargs['revisionUrlTemplate']
        if third_party_configuration_url is None and 'thirdPartyConfigurationUrl' in kwargs:
            third_party_configuration_url = kwargs['thirdPartyConfigurationUrl']

        if entity_url_template is not None:
            _setter("entity_url_template", entity_url_template)
        if execution_url_template is not None:
            _setter("execution_url_template", execution_url_template)
        if revision_url_template is not None:
            _setter("revision_url_template", revision_url_template)
        if third_party_configuration_url is not None:
            _setter("third_party_configuration_url", third_party_configuration_url)

    @property
    @pulumi.getter(name="entityUrlTemplate")
    def entity_url_template(self) -> Optional[str]:
        """
        The URL returned to the AWS CodePipeline console that provides a deep link to the resources of the external system.
        """
        return pulumi.get(self, "entity_url_template")

    @property
    @pulumi.getter(name="executionUrlTemplate")
    def execution_url_template(self) -> Optional[str]:
        """
        The URL returned to the AWS CodePipeline console that contains a link to the top-level landing page for the external system.
        """
        return pulumi.get(self, "execution_url_template")

    @property
    @pulumi.getter(name="revisionUrlTemplate")
    def revision_url_template(self) -> Optional[str]:
        """
        The URL returned to the AWS CodePipeline console that contains a link to the page where customers can update or change the configuration of the external action.
        """
        return pulumi.get(self, "revision_url_template")

    @property
    @pulumi.getter(name="thirdPartyConfigurationUrl")
    def third_party_configuration_url(self) -> Optional[str]:
        """
        The URL of a sign-up page where users can sign up for an external service and perform initial configuration of the action provided by that service.
        """
        return pulumi.get(self, "third_party_configuration_url")


@pulumi.output_type
class PipelineArtifactStore(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "encryptionKey":
            suggest = "encryption_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineArtifactStore. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineArtifactStore.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineArtifactStore.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 location: str,
                 type: str,
                 encryption_key: Optional['outputs.PipelineArtifactStoreEncryptionKey'] = None,
                 region: Optional[str] = None):
        """
        :param str location: The location where AWS CodePipeline stores artifacts for a pipeline; currently only `S3` is supported.
        :param str type: The type of the artifact store, such as Amazon S3
        :param 'PipelineArtifactStoreEncryptionKeyArgs' encryption_key: The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don't specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An `encryption_key` block is documented below.
        :param str region: The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.
        """
        PipelineArtifactStore._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            location=location,
            type=type,
            encryption_key=encryption_key,
            region=region,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             location: Optional[str] = None,
             type: Optional[str] = None,
             encryption_key: Optional['outputs.PipelineArtifactStoreEncryptionKey'] = None,
             region: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if location is None:
            raise TypeError("Missing 'location' argument")
        if type is None:
            raise TypeError("Missing 'type' argument")
        if encryption_key is None and 'encryptionKey' in kwargs:
            encryption_key = kwargs['encryptionKey']

        _setter("location", location)
        _setter("type", type)
        if encryption_key is not None:
            _setter("encryption_key", encryption_key)
        if region is not None:
            _setter("region", region)

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location where AWS CodePipeline stores artifacts for a pipeline; currently only `S3` is supported.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the artifact store, such as Amazon S3
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional['outputs.PipelineArtifactStoreEncryptionKey']:
        """
        The encryption key block AWS CodePipeline uses to encrypt the data in the artifact store, such as an AWS Key Management Service (AWS KMS) key. If you don't specify a key, AWS CodePipeline uses the default key for Amazon Simple Storage Service (Amazon S3). An `encryption_key` block is documented below.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region where the artifact store is located. Required for a cross-region CodePipeline, do not provide for a single-region CodePipeline.
        """
        return pulumi.get(self, "region")


@pulumi.output_type
class PipelineArtifactStoreEncryptionKey(dict):
    def __init__(__self__, *,
                 id: str,
                 type: str):
        """
        :param str id: The KMS key ARN or ID
        :param str type: The type of key; currently only `KMS` is supported
        """
        PipelineArtifactStoreEncryptionKey._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            id=id,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             id: Optional[str] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if id is None:
            raise TypeError("Missing 'id' argument")
        if type is None:
            raise TypeError("Missing 'type' argument")

        _setter("id", id)
        _setter("type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The KMS key ARN or ID
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of key; currently only `KMS` is supported
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class PipelineStage(dict):
    def __init__(__self__, *,
                 actions: Sequence['outputs.PipelineStageAction'],
                 name: str):
        """
        :param Sequence['PipelineStageActionArgs'] actions: The action(s) to include in the stage. Defined as an `action` block below
        :param str name: The name of the stage.
        """
        PipelineStage._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            actions=actions,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             actions: Optional[Sequence['outputs.PipelineStageAction']] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if actions is None:
            raise TypeError("Missing 'actions' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")

        _setter("actions", actions)
        _setter("name", name)

    @property
    @pulumi.getter
    def actions(self) -> Sequence['outputs.PipelineStageAction']:
        """
        The action(s) to include in the stage. Defined as an `action` block below
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the stage.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class PipelineStageAction(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "inputArtifacts":
            suggest = "input_artifacts"
        elif key == "outputArtifacts":
            suggest = "output_artifacts"
        elif key == "roleArn":
            suggest = "role_arn"
        elif key == "runOrder":
            suggest = "run_order"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PipelineStageAction. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PipelineStageAction.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PipelineStageAction.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 category: str,
                 name: str,
                 owner: str,
                 provider: str,
                 version: str,
                 configuration: Optional[Mapping[str, str]] = None,
                 input_artifacts: Optional[Sequence[str]] = None,
                 namespace: Optional[str] = None,
                 output_artifacts: Optional[Sequence[str]] = None,
                 region: Optional[str] = None,
                 role_arn: Optional[str] = None,
                 run_order: Optional[int] = None):
        """
        :param str category: A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are `Approval`, `Build`, `Deploy`, `Invoke`, `Source` and `Test`.
        :param str name: The action declaration's name.
        :param str owner: The creator of the action being called. Possible values are `AWS`, `Custom` and `ThirdParty`.
        :param str provider: The provider of the service being called by the action. Valid providers are determined by the action category. Provider names are listed in the [Action Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) documentation.
        :param str version: A string that identifies the action type.
        :param Mapping[str, str] configuration: A map of the action declaration's configuration. Configurations options for action types and providers can be found in the [Pipeline Structure Reference](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements) and [Action Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) documentation.
        :param Sequence[str] input_artifacts: A list of artifact names to be worked on.
        :param str namespace: The namespace all output variables will be accessed from.
               
               > **Note:** The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        :param Sequence[str] output_artifacts: A list of artifact names to output. Output artifact names must be unique within a pipeline.
        :param str region: The region in which to run the action.
        :param str role_arn: The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        :param int run_order: The order in which actions are run.
        """
        PipelineStageAction._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            category=category,
            name=name,
            owner=owner,
            provider=provider,
            version=version,
            configuration=configuration,
            input_artifacts=input_artifacts,
            namespace=namespace,
            output_artifacts=output_artifacts,
            region=region,
            role_arn=role_arn,
            run_order=run_order,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             category: Optional[str] = None,
             name: Optional[str] = None,
             owner: Optional[str] = None,
             provider: Optional[str] = None,
             version: Optional[str] = None,
             configuration: Optional[Mapping[str, str]] = None,
             input_artifacts: Optional[Sequence[str]] = None,
             namespace: Optional[str] = None,
             output_artifacts: Optional[Sequence[str]] = None,
             region: Optional[str] = None,
             role_arn: Optional[str] = None,
             run_order: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if category is None:
            raise TypeError("Missing 'category' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if owner is None:
            raise TypeError("Missing 'owner' argument")
        if provider is None:
            raise TypeError("Missing 'provider' argument")
        if version is None:
            raise TypeError("Missing 'version' argument")
        if input_artifacts is None and 'inputArtifacts' in kwargs:
            input_artifacts = kwargs['inputArtifacts']
        if output_artifacts is None and 'outputArtifacts' in kwargs:
            output_artifacts = kwargs['outputArtifacts']
        if role_arn is None and 'roleArn' in kwargs:
            role_arn = kwargs['roleArn']
        if run_order is None and 'runOrder' in kwargs:
            run_order = kwargs['runOrder']

        _setter("category", category)
        _setter("name", name)
        _setter("owner", owner)
        _setter("provider", provider)
        _setter("version", version)
        if configuration is not None:
            _setter("configuration", configuration)
        if input_artifacts is not None:
            _setter("input_artifacts", input_artifacts)
        if namespace is not None:
            _setter("namespace", namespace)
        if output_artifacts is not None:
            _setter("output_artifacts", output_artifacts)
        if region is not None:
            _setter("region", region)
        if role_arn is not None:
            _setter("role_arn", role_arn)
        if run_order is not None:
            _setter("run_order", run_order)

    @property
    @pulumi.getter
    def category(self) -> str:
        """
        A category defines what kind of action can be taken in the stage, and constrains the provider type for the action. Possible values are `Approval`, `Build`, `Deploy`, `Invoke`, `Source` and `Test`.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The action declaration's name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def owner(self) -> str:
        """
        The creator of the action being called. Possible values are `AWS`, `Custom` and `ThirdParty`.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def provider(self) -> str:
        """
        The provider of the service being called by the action. Valid providers are determined by the action category. Provider names are listed in the [Action Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) documentation.
        """
        return pulumi.get(self, "provider")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        A string that identifies the action type.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter
    def configuration(self) -> Optional[Mapping[str, str]]:
        """
        A map of the action declaration's configuration. Configurations options for action types and providers can be found in the [Pipeline Structure Reference](http://docs.aws.amazon.com/codepipeline/latest/userguide/reference-pipeline-structure.html#action-requirements) and [Action Structure Reference](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference.html) documentation.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter(name="inputArtifacts")
    def input_artifacts(self) -> Optional[Sequence[str]]:
        """
        A list of artifact names to be worked on.
        """
        return pulumi.get(self, "input_artifacts")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        """
        The namespace all output variables will be accessed from.

        > **Note:** The input artifact of an action must exactly match the output artifact declared in a preceding action, but the input artifact does not have to be the next action in strict sequence from the action that provided the output artifact. Actions in parallel can declare different output artifacts, which are in turn consumed by different following actions.
        """
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter(name="outputArtifacts")
    def output_artifacts(self) -> Optional[Sequence[str]]:
        """
        A list of artifact names to output. Output artifact names must be unique within a pipeline.
        """
        return pulumi.get(self, "output_artifacts")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region in which to run the action.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> Optional[str]:
        """
        The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter(name="runOrder")
    def run_order(self) -> Optional[int]:
        """
        The order in which actions are run.
        """
        return pulumi.get(self, "run_order")


@pulumi.output_type
class WebhookAuthenticationConfiguration(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedIpRange":
            suggest = "allowed_ip_range"
        elif key == "secretToken":
            suggest = "secret_token"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WebhookAuthenticationConfiguration. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WebhookAuthenticationConfiguration.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WebhookAuthenticationConfiguration.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_ip_range: Optional[str] = None,
                 secret_token: Optional[str] = None):
        """
        :param str allowed_ip_range: A valid CIDR block for `IP` filtering. Required for `IP`.
        :param str secret_token: The shared secret for the GitHub repository webhook. Set this as `secret` in your `github_repository_webhook`'s `configuration` block. Required for `GITHUB_HMAC`.
        """
        WebhookAuthenticationConfiguration._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            allowed_ip_range=allowed_ip_range,
            secret_token=secret_token,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             allowed_ip_range: Optional[str] = None,
             secret_token: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if allowed_ip_range is None and 'allowedIpRange' in kwargs:
            allowed_ip_range = kwargs['allowedIpRange']
        if secret_token is None and 'secretToken' in kwargs:
            secret_token = kwargs['secretToken']

        if allowed_ip_range is not None:
            _setter("allowed_ip_range", allowed_ip_range)
        if secret_token is not None:
            _setter("secret_token", secret_token)

    @property
    @pulumi.getter(name="allowedIpRange")
    def allowed_ip_range(self) -> Optional[str]:
        """
        A valid CIDR block for `IP` filtering. Required for `IP`.
        """
        return pulumi.get(self, "allowed_ip_range")

    @property
    @pulumi.getter(name="secretToken")
    def secret_token(self) -> Optional[str]:
        """
        The shared secret for the GitHub repository webhook. Set this as `secret` in your `github_repository_webhook`'s `configuration` block. Required for `GITHUB_HMAC`.
        """
        return pulumi.get(self, "secret_token")


@pulumi.output_type
class WebhookFilter(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "jsonPath":
            suggest = "json_path"
        elif key == "matchEquals":
            suggest = "match_equals"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WebhookFilter. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WebhookFilter.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WebhookFilter.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 json_path: str,
                 match_equals: str):
        """
        :param str json_path: The [JSON path](https://github.com/json-path/JsonPath) to filter on.
        :param str match_equals: The value to match on (e.g., `refs/heads/{Branch}`). See [AWS docs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html) for details.
        """
        WebhookFilter._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            json_path=json_path,
            match_equals=match_equals,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             json_path: Optional[str] = None,
             match_equals: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if json_path is None and 'jsonPath' in kwargs:
            json_path = kwargs['jsonPath']
        if json_path is None:
            raise TypeError("Missing 'json_path' argument")
        if match_equals is None and 'matchEquals' in kwargs:
            match_equals = kwargs['matchEquals']
        if match_equals is None:
            raise TypeError("Missing 'match_equals' argument")

        _setter("json_path", json_path)
        _setter("match_equals", match_equals)

    @property
    @pulumi.getter(name="jsonPath")
    def json_path(self) -> str:
        """
        The [JSON path](https://github.com/json-path/JsonPath) to filter on.
        """
        return pulumi.get(self, "json_path")

    @property
    @pulumi.getter(name="matchEquals")
    def match_equals(self) -> str:
        """
        The value to match on (e.g., `refs/heads/{Branch}`). See [AWS docs](https://docs.aws.amazon.com/codepipeline/latest/APIReference/API_WebhookFilterRule.html) for details.
        """
        return pulumi.get(self, "match_equals")



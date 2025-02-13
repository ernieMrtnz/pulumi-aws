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

__all__ = ['GrantArgs', 'Grant']

@pulumi.input_type
class GrantArgs:
    def __init__(__self__, *,
                 grantee_principal: pulumi.Input[str],
                 key_id: pulumi.Input[str],
                 operations: pulumi.Input[Sequence[pulumi.Input[str]]],
                 constraints: Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]] = None,
                 grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 retire_on_delete: Optional[pulumi.Input[bool]] = None,
                 retiring_principal: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Grant resource.
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        :param pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[bool] retire_on_delete: If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        GrantArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            grantee_principal=grantee_principal,
            key_id=key_id,
            operations=operations,
            constraints=constraints,
            grant_creation_tokens=grant_creation_tokens,
            name=name,
            retire_on_delete=retire_on_delete,
            retiring_principal=retiring_principal,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             grantee_principal: Optional[pulumi.Input[str]] = None,
             key_id: Optional[pulumi.Input[str]] = None,
             operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             constraints: Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]] = None,
             grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             retire_on_delete: Optional[pulumi.Input[bool]] = None,
             retiring_principal: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if grantee_principal is None and 'granteePrincipal' in kwargs:
            grantee_principal = kwargs['granteePrincipal']
        if grantee_principal is None:
            raise TypeError("Missing 'grantee_principal' argument")
        if key_id is None and 'keyId' in kwargs:
            key_id = kwargs['keyId']
        if key_id is None:
            raise TypeError("Missing 'key_id' argument")
        if operations is None:
            raise TypeError("Missing 'operations' argument")
        if grant_creation_tokens is None and 'grantCreationTokens' in kwargs:
            grant_creation_tokens = kwargs['grantCreationTokens']
        if retire_on_delete is None and 'retireOnDelete' in kwargs:
            retire_on_delete = kwargs['retireOnDelete']
        if retiring_principal is None and 'retiringPrincipal' in kwargs:
            retiring_principal = kwargs['retiringPrincipal']

        _setter("grantee_principal", grantee_principal)
        _setter("key_id", key_id)
        _setter("operations", operations)
        if constraints is not None:
            _setter("constraints", constraints)
        if grant_creation_tokens is not None:
            _setter("grant_creation_tokens", grant_creation_tokens)
        if name is not None:
            _setter("name", name)
        if retire_on_delete is not None:
            _setter("retire_on_delete", retire_on_delete)
        if retiring_principal is not None:
            _setter("retiring_principal", retiring_principal)

    @property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> pulumi.Input[str]:
        """
        The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "grantee_principal")

    @grantee_principal.setter
    def grantee_principal(self, value: pulumi.Input[str]):
        pulumi.set(self, "grantee_principal", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Input[str]:
        """
        The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter
    def operations(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        """
        return pulumi.get(self, "operations")

    @operations.setter
    def operations(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "operations", value)

    @property
    @pulumi.getter
    def constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]]:
        """
        A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        """
        return pulumi.get(self, "constraints")

    @constraints.setter
    def constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]]):
        pulumi.set(self, "constraints", value)

    @property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        """
        return pulumi.get(self, "grant_creation_tokens")

    @grant_creation_tokens.setter
    def grant_creation_tokens(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "grant_creation_tokens", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly name for identifying the grant.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
        See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        """
        return pulumi.get(self, "retire_on_delete")

    @retire_on_delete.setter
    def retire_on_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "retire_on_delete", value)

    @property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> Optional[pulumi.Input[str]]:
        """
        The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "retiring_principal")

    @retiring_principal.setter
    def retiring_principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retiring_principal", value)


@pulumi.input_type
class _GrantState:
    def __init__(__self__, *,
                 constraints: Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]] = None,
                 grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 grant_id: Optional[pulumi.Input[str]] = None,
                 grant_token: Optional[pulumi.Input[str]] = None,
                 grantee_principal: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retire_on_delete: Optional[pulumi.Input[bool]] = None,
                 retiring_principal: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Grant resources.
        :param pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grant_id: The unique identifier for the grant.
        :param pulumi.Input[str] grant_token: The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        :param pulumi.Input[bool] retire_on_delete: If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        _GrantState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            constraints=constraints,
            grant_creation_tokens=grant_creation_tokens,
            grant_id=grant_id,
            grant_token=grant_token,
            grantee_principal=grantee_principal,
            key_id=key_id,
            name=name,
            operations=operations,
            retire_on_delete=retire_on_delete,
            retiring_principal=retiring_principal,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             constraints: Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]] = None,
             grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             grant_id: Optional[pulumi.Input[str]] = None,
             grant_token: Optional[pulumi.Input[str]] = None,
             grantee_principal: Optional[pulumi.Input[str]] = None,
             key_id: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             retire_on_delete: Optional[pulumi.Input[bool]] = None,
             retiring_principal: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if grant_creation_tokens is None and 'grantCreationTokens' in kwargs:
            grant_creation_tokens = kwargs['grantCreationTokens']
        if grant_id is None and 'grantId' in kwargs:
            grant_id = kwargs['grantId']
        if grant_token is None and 'grantToken' in kwargs:
            grant_token = kwargs['grantToken']
        if grantee_principal is None and 'granteePrincipal' in kwargs:
            grantee_principal = kwargs['granteePrincipal']
        if key_id is None and 'keyId' in kwargs:
            key_id = kwargs['keyId']
        if retire_on_delete is None and 'retireOnDelete' in kwargs:
            retire_on_delete = kwargs['retireOnDelete']
        if retiring_principal is None and 'retiringPrincipal' in kwargs:
            retiring_principal = kwargs['retiringPrincipal']

        if constraints is not None:
            _setter("constraints", constraints)
        if grant_creation_tokens is not None:
            _setter("grant_creation_tokens", grant_creation_tokens)
        if grant_id is not None:
            _setter("grant_id", grant_id)
        if grant_token is not None:
            _setter("grant_token", grant_token)
        if grantee_principal is not None:
            _setter("grantee_principal", grantee_principal)
        if key_id is not None:
            _setter("key_id", key_id)
        if name is not None:
            _setter("name", name)
        if operations is not None:
            _setter("operations", operations)
        if retire_on_delete is not None:
            _setter("retire_on_delete", retire_on_delete)
        if retiring_principal is not None:
            _setter("retiring_principal", retiring_principal)

    @property
    @pulumi.getter
    def constraints(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]]:
        """
        A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        """
        return pulumi.get(self, "constraints")

    @constraints.setter
    def constraints(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GrantConstraintArgs']]]]):
        pulumi.set(self, "constraints", value)

    @property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        """
        return pulumi.get(self, "grant_creation_tokens")

    @grant_creation_tokens.setter
    def grant_creation_tokens(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "grant_creation_tokens", value)

    @property
    @pulumi.getter(name="grantId")
    def grant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the grant.
        """
        return pulumi.get(self, "grant_id")

    @grant_id.setter
    def grant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "grant_id", value)

    @property
    @pulumi.getter(name="grantToken")
    def grant_token(self) -> Optional[pulumi.Input[str]]:
        """
        The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        """
        return pulumi.get(self, "grant_token")

    @grant_token.setter
    def grant_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "grant_token", value)

    @property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> Optional[pulumi.Input[str]]:
        """
        The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "grantee_principal")

    @grantee_principal.setter
    def grantee_principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "grantee_principal", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[str]]:
        """
        The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        A friendly name for identifying the grant.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def operations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        """
        return pulumi.get(self, "operations")

    @operations.setter
    def operations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "operations", value)

    @property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> Optional[pulumi.Input[bool]]:
        """
        If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
        See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        """
        return pulumi.get(self, "retire_on_delete")

    @retire_on_delete.setter
    def retire_on_delete(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "retire_on_delete", value)

    @property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> Optional[pulumi.Input[str]]:
        """
        The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "retiring_principal")

    @retiring_principal.setter
    def retiring_principal(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retiring_principal", value)


class Grant(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]]] = None,
                 grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 grantee_principal: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retire_on_delete: Optional[pulumi.Input[bool]] = None,
                 retiring_principal: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a resource-based access control mechanism for a KMS customer master key.

        ## Import

        Using `pulumi import`, import KMS Grants using the Key ID and Grant ID separated by a colon (`:`). For example:

        ```sh
         $ pulumi import aws:kms/grant:Grant test 1234abcd-12ab-34cd-56ef-1234567890ab:abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        :param pulumi.Input[bool] retire_on_delete: If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GrantArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a resource-based access control mechanism for a KMS customer master key.

        ## Import

        Using `pulumi import`, import KMS Grants using the Key ID and Grant ID separated by a colon (`:`). For example:

        ```sh
         $ pulumi import aws:kms/grant:Grant test 1234abcd-12ab-34cd-56ef-1234567890ab:abcde1237f76e4ba7987489ac329fbfba6ad343d6f7075dbd1ef191f0120514
        ```

        :param str resource_name: The name of the resource.
        :param GrantArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GrantArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            GrantArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]]] = None,
                 grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 grantee_principal: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 retire_on_delete: Optional[pulumi.Input[bool]] = None,
                 retiring_principal: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GrantArgs.__new__(GrantArgs)

            __props__.__dict__["constraints"] = constraints
            __props__.__dict__["grant_creation_tokens"] = grant_creation_tokens
            if grantee_principal is None and not opts.urn:
                raise TypeError("Missing required property 'grantee_principal'")
            __props__.__dict__["grantee_principal"] = grantee_principal
            if key_id is None and not opts.urn:
                raise TypeError("Missing required property 'key_id'")
            __props__.__dict__["key_id"] = key_id
            __props__.__dict__["name"] = name
            if operations is None and not opts.urn:
                raise TypeError("Missing required property 'operations'")
            __props__.__dict__["operations"] = operations
            __props__.__dict__["retire_on_delete"] = retire_on_delete
            __props__.__dict__["retiring_principal"] = retiring_principal
            __props__.__dict__["grant_id"] = None
            __props__.__dict__["grant_token"] = None
        super(Grant, __self__).__init__(
            'aws:kms/grant:Grant',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            constraints: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]]] = None,
            grant_creation_tokens: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            grant_id: Optional[pulumi.Input[str]] = None,
            grant_token: Optional[pulumi.Input[str]] = None,
            grantee_principal: Optional[pulumi.Input[str]] = None,
            key_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            operations: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            retire_on_delete: Optional[pulumi.Input[bool]] = None,
            retiring_principal: Optional[pulumi.Input[str]] = None) -> 'Grant':
        """
        Get an existing Grant resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GrantConstraintArgs']]]] constraints: A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] grant_creation_tokens: A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        :param pulumi.Input[str] grant_id: The unique identifier for the grant.
        :param pulumi.Input[str] grant_token: The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        :param pulumi.Input[str] grantee_principal: The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        :param pulumi.Input[str] key_id: The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        :param pulumi.Input[str] name: A friendly name for identifying the grant.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operations: A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        :param pulumi.Input[bool] retire_on_delete: If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
               See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        :param pulumi.Input[str] retiring_principal: The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _GrantState.__new__(_GrantState)

        __props__.__dict__["constraints"] = constraints
        __props__.__dict__["grant_creation_tokens"] = grant_creation_tokens
        __props__.__dict__["grant_id"] = grant_id
        __props__.__dict__["grant_token"] = grant_token
        __props__.__dict__["grantee_principal"] = grantee_principal
        __props__.__dict__["key_id"] = key_id
        __props__.__dict__["name"] = name
        __props__.__dict__["operations"] = operations
        __props__.__dict__["retire_on_delete"] = retire_on_delete
        __props__.__dict__["retiring_principal"] = retiring_principal
        return Grant(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def constraints(self) -> pulumi.Output[Optional[Sequence['outputs.GrantConstraint']]]:
        """
        A structure that you can use to allow certain operations in the grant only when the desired encryption context is present. For more information about encryption context, see [Encryption Context](http://docs.aws.amazon.com/kms/latest/developerguide/encryption-context.html).
        """
        return pulumi.get(self, "constraints")

    @property
    @pulumi.getter(name="grantCreationTokens")
    def grant_creation_tokens(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of grant tokens to be used when creating the grant. See [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token) for more information about grant tokens.
        """
        return pulumi.get(self, "grant_creation_tokens")

    @property
    @pulumi.getter(name="grantId")
    def grant_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the grant.
        """
        return pulumi.get(self, "grant_id")

    @property
    @pulumi.getter(name="grantToken")
    def grant_token(self) -> pulumi.Output[str]:
        """
        The grant token for the created grant. For more information, see [Grant Tokens](http://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token).
        """
        return pulumi.get(self, "grant_token")

    @property
    @pulumi.getter(name="granteePrincipal")
    def grantee_principal(self) -> pulumi.Output[str]:
        """
        The principal that is given permission to perform the operations that the grant permits in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "grantee_principal")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the customer master key (CMK) that the grant applies to. Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a different AWS account, you must use the key ARN.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A friendly name for identifying the grant.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operations(self) -> pulumi.Output[Sequence[str]]:
        """
        A list of operations that the grant permits. The permitted values are: `Decrypt`, `Encrypt`, `GenerateDataKey`, `GenerateDataKeyWithoutPlaintext`, `ReEncryptFrom`, `ReEncryptTo`, `Sign`, `Verify`, `GetPublicKey`, `CreateGrant`, `RetireGrant`, `DescribeKey`, `GenerateDataKeyPair`, or `GenerateDataKeyPairWithoutPlaintext`.
        """
        return pulumi.get(self, "operations")

    @property
    @pulumi.getter(name="retireOnDelete")
    def retire_on_delete(self) -> pulumi.Output[Optional[bool]]:
        """
        If set to false (the default) the grants will be revoked upon deletion, and if set to true the grants will try to be retired upon deletion. Note that retiring grants requires special permissions, hence why we default to revoking grants.
        See [RetireGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_RetireGrant.html) for more information.
        """
        return pulumi.get(self, "retire_on_delete")

    @property
    @pulumi.getter(name="retiringPrincipal")
    def retiring_principal(self) -> pulumi.Output[Optional[str]]:
        """
        The principal that is given permission to retire the grant by using RetireGrant operation in ARN format. Note that due to eventual consistency issues around IAM principals, the providers's state may not always be refreshed to reflect what is true in AWS.
        """
        return pulumi.get(self, "retiring_principal")


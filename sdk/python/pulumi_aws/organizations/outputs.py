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
    'OrganizationAccount',
    'OrganizationNonMasterAccount',
    'OrganizationRoot',
    'OrganizationRootPolicyType',
    'OrganizationalUnitAccount',
    'GetDelegatedAdministratorsDelegatedAdministratorResult',
    'GetDelegatedServicesDelegatedServiceResult',
    'GetOrganizationAccountResult',
    'GetOrganizationNonMasterAccountResult',
    'GetOrganizationRootResult',
    'GetOrganizationRootPolicyTypeResult',
    'GetOrganizationalUnitChildAccountsAccountResult',
    'GetOrganizationalUnitDescendantAccountsAccountResult',
    'GetOrganizationalUnitsChildResult',
]

@pulumi.output_type
class OrganizationAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        OrganizationAccount._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if arn is not None:
            _setter("arn", arn)
        if email is not None:
            _setter("email", email)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class OrganizationNonMasterAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        OrganizationNonMasterAccount._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if arn is not None:
            _setter("arn", arn)
        if email is not None:
            _setter("email", email)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class OrganizationRoot(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "policyTypes":
            suggest = "policy_types"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in OrganizationRoot. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        OrganizationRoot.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        OrganizationRoot.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None,
                 policy_types: Optional[Sequence['outputs.OrganizationRootPolicyType']] = None):
        """
        :param str arn: ARN of the root
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param Sequence['OrganizationRootPolicyTypeArgs'] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        OrganizationRoot._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            id=id,
            name=name,
            policy_types=policy_types,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             policy_types: Optional[Sequence['outputs.OrganizationRootPolicyType']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if policy_types is None and 'policyTypes' in kwargs:
            policy_types = kwargs['policyTypes']

        if arn is not None:
            _setter("arn", arn)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)
        if policy_types is not None:
            _setter("policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Optional[Sequence['outputs.OrganizationRootPolicyType']]:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")


@pulumi.output_type
class OrganizationRootPolicyType(dict):
    def __init__(__self__, *,
                 status: Optional[str] = None,
                 type: Optional[str] = None):
        """
        :param str status: The status of the policy type as it relates to the associated root
        """
        OrganizationRootPolicyType._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[str] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if status is not None:
            _setter("status", status)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        return pulumi.get(self, "type")


@pulumi.output_type
class OrganizationalUnitAccount(dict):
    def __init__(__self__, *,
                 arn: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[str] = None,
                 name: Optional[str] = None):
        """
        :param str arn: ARN of the organizational unit
        :param str email: Email of the account
        :param str id: Identifier of the organization unit
        :param str name: The name for the organizational unit
        """
        OrganizationalUnitAccount._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if arn is not None:
            _setter("arn", arn)
        if email is not None:
            _setter("email", email)
        if id is not None:
            _setter("id", id)
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Identifier of the organization unit
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The name for the organizational unit
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class GetDelegatedAdministratorsDelegatedAdministratorResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 delegation_enabled_date: str,
                 email: str,
                 id: str,
                 joined_method: str,
                 joined_timestamp: str,
                 name: str,
                 status: str):
        """
        :param str arn: The ARN of the delegated administrator's account.
        :param str delegation_enabled_date: The date when the account was made a delegated administrator.
        :param str email: The email address that is associated with the delegated administrator's AWS account.
        :param str id: The unique identifier (ID) of the delegated administrator's account.
        :param str joined_method: The method by which the delegated administrator's account joined the organization.
        :param str joined_timestamp: The date when the delegated administrator's account became a part of the organization.
        :param str name: The friendly name of the delegated administrator's account.
        :param str status: The status of the delegated administrator's account in the organization.
        """
        GetDelegatedAdministratorsDelegatedAdministratorResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            delegation_enabled_date=delegation_enabled_date,
            email=email,
            id=id,
            joined_method=joined_method,
            joined_timestamp=joined_timestamp,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             delegation_enabled_date: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             joined_method: Optional[str] = None,
             joined_timestamp: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if delegation_enabled_date is None and 'delegationEnabledDate' in kwargs:
            delegation_enabled_date = kwargs['delegationEnabledDate']
        if delegation_enabled_date is None:
            raise TypeError("Missing 'delegation_enabled_date' argument")
        if email is None:
            raise TypeError("Missing 'email' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if joined_method is None and 'joinedMethod' in kwargs:
            joined_method = kwargs['joinedMethod']
        if joined_method is None:
            raise TypeError("Missing 'joined_method' argument")
        if joined_timestamp is None and 'joinedTimestamp' in kwargs:
            joined_timestamp = kwargs['joinedTimestamp']
        if joined_timestamp is None:
            raise TypeError("Missing 'joined_timestamp' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("arn", arn)
        _setter("delegation_enabled_date", delegation_enabled_date)
        _setter("email", email)
        _setter("id", id)
        _setter("joined_method", joined_method)
        _setter("joined_timestamp", joined_timestamp)
        _setter("name", name)
        _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The ARN of the delegated administrator's account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="delegationEnabledDate")
    def delegation_enabled_date(self) -> str:
        """
        The date when the account was made a delegated administrator.
        """
        return pulumi.get(self, "delegation_enabled_date")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address that is associated with the delegated administrator's AWS account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The unique identifier (ID) of the delegated administrator's account.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="joinedMethod")
    def joined_method(self) -> str:
        """
        The method by which the delegated administrator's account joined the organization.
        """
        return pulumi.get(self, "joined_method")

    @property
    @pulumi.getter(name="joinedTimestamp")
    def joined_timestamp(self) -> str:
        """
        The date when the delegated administrator's account became a part of the organization.
        """
        return pulumi.get(self, "joined_timestamp")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The friendly name of the delegated administrator's account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the delegated administrator's account in the organization.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetDelegatedServicesDelegatedServiceResult(dict):
    def __init__(__self__, *,
                 delegation_enabled_date: str,
                 service_principal: str):
        """
        :param str delegation_enabled_date: The date that the account became a delegated administrator for this service.
        :param str service_principal: The name of an AWS service that can request an operation for the specified service.
        """
        GetDelegatedServicesDelegatedServiceResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            delegation_enabled_date=delegation_enabled_date,
            service_principal=service_principal,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             delegation_enabled_date: Optional[str] = None,
             service_principal: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if delegation_enabled_date is None and 'delegationEnabledDate' in kwargs:
            delegation_enabled_date = kwargs['delegationEnabledDate']
        if delegation_enabled_date is None:
            raise TypeError("Missing 'delegation_enabled_date' argument")
        if service_principal is None and 'servicePrincipal' in kwargs:
            service_principal = kwargs['servicePrincipal']
        if service_principal is None:
            raise TypeError("Missing 'service_principal' argument")

        _setter("delegation_enabled_date", delegation_enabled_date)
        _setter("service_principal", service_principal)

    @property
    @pulumi.getter(name="delegationEnabledDate")
    def delegation_enabled_date(self) -> str:
        """
        The date that the account became a delegated administrator for this service.
        """
        return pulumi.get(self, "delegation_enabled_date")

    @property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> str:
        """
        The name of an AWS service that can request an operation for the specified service.
        """
        return pulumi.get(self, "service_principal")


@pulumi.output_type
class GetOrganizationAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        GetOrganizationAccountResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if email is None:
            raise TypeError("Missing 'email' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("arn", arn)
        _setter("email", email)
        _setter("id", id)
        _setter("name", name)
        _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationNonMasterAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: ARN of the root
        :param str email: Email of the account
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param str status: The status of the policy type as it relates to the associated root
        """
        GetOrganizationNonMasterAccountResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if email is None:
            raise TypeError("Missing 'email' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("arn", arn)
        _setter("email", email)
        _setter("id", id)
        _setter("name", name)
        _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        Email of the account
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationRootResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str,
                 policy_types: Sequence['outputs.GetOrganizationRootPolicyTypeResult']):
        """
        :param str arn: ARN of the root
        :param str id: Identifier of the root
        :param str name: The name of the policy type
        :param Sequence['GetOrganizationRootPolicyTypeArgs'] policy_types: List of policy types enabled for this root. All elements have these attributes:
        """
        GetOrganizationRootResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            id=id,
            name=name,
            policy_types=policy_types,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             policy_types: Optional[Sequence['outputs.GetOrganizationRootPolicyTypeResult']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if policy_types is None and 'policyTypes' in kwargs:
            policy_types = kwargs['policyTypes']
        if policy_types is None:
            raise TypeError("Missing 'policy_types' argument")

        _setter("arn", arn)
        _setter("id", id)
        _setter("name", name)
        _setter("policy_types", policy_types)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the root
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Identifier of the root
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the policy type
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyTypes")
    def policy_types(self) -> Sequence['outputs.GetOrganizationRootPolicyTypeResult']:
        """
        List of policy types enabled for this root. All elements have these attributes:
        """
        return pulumi.get(self, "policy_types")


@pulumi.output_type
class GetOrganizationRootPolicyTypeResult(dict):
    def __init__(__self__, *,
                 status: str,
                 type: str):
        """
        :param str status: The status of the policy type as it relates to the associated root
        """
        GetOrganizationRootPolicyTypeResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[str] = None,
             type: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if status is None:
            raise TypeError("Missing 'status' argument")
        if type is None:
            raise TypeError("Missing 'type' argument")

        _setter("status", status)
        _setter("type", type)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the policy type as it relates to the associated root
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")


@pulumi.output_type
class GetOrganizationalUnitChildAccountsAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: The Amazon Resource Name (ARN) of the account.
        :param str email: The email address associated with the AWS account.
        :param str id: Parent identifier of the organizational units.
        :param str name: The friendly name of the account.
        :param str status: The status of the account in the organization.
        """
        GetOrganizationalUnitChildAccountsAccountResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if email is None:
            raise TypeError("Missing 'email' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("arn", arn)
        _setter("email", email)
        _setter("id", id)
        _setter("name", name)
        _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address associated with the AWS account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The friendly name of the account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the account in the organization.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationalUnitDescendantAccountsAccountResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 email: str,
                 id: str,
                 name: str,
                 status: str):
        """
        :param str arn: The Amazon Resource Name (ARN) of the account.
        :param str email: The email address associated with the AWS account.
        :param str id: Parent identifier of the organizational units.
        :param str name: The friendly name of the account.
        :param str status: The status of the account in the organization.
        """
        GetOrganizationalUnitDescendantAccountsAccountResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            email=email,
            id=id,
            name=name,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             email: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if email is None:
            raise TypeError("Missing 'email' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("arn", arn)
        _setter("email", email)
        _setter("id", id)
        _setter("name", name)
        _setter("status", status)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the account.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def email(self) -> str:
        """
        The email address associated with the AWS account.
        """
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The friendly name of the account.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The status of the account in the organization.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class GetOrganizationalUnitsChildResult(dict):
    def __init__(__self__, *,
                 arn: str,
                 id: str,
                 name: str):
        """
        :param str arn: ARN of the organizational unit
        :param str id: Parent identifier of the organizational units.
        :param str name: Name of the organizational unit
        """
        GetOrganizationalUnitsChildResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            id=id,
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[str] = None,
             id: Optional[str] = None,
             name: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if arn is None:
            raise TypeError("Missing 'arn' argument")
        if id is None:
            raise TypeError("Missing 'id' argument")
        if name is None:
            raise TypeError("Missing 'name' argument")

        _setter("arn", arn)
        _setter("id", id)
        _setter("name", name)

    @property
    @pulumi.getter
    def arn(self) -> str:
        """
        ARN of the organizational unit
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Parent identifier of the organizational units.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the organizational unit
        """
        return pulumi.get(self, "name")



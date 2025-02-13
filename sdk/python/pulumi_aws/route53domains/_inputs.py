# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'RegisteredDomainAdminContactArgs',
    'RegisteredDomainNameServerArgs',
    'RegisteredDomainRegistrantContactArgs',
    'RegisteredDomainTechContactArgs',
]

@pulumi.input_type
class RegisteredDomainAdminContactArgs:
    def __init__(__self__, *,
                 address_line1: Optional[pulumi.Input[str]] = None,
                 address_line2: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 contact_type: Optional[pulumi.Input[str]] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 zip_code: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address_line1: First line of the contact's address.
        :param pulumi.Input[str] address_line2: Second line of contact's address, if any.
        :param pulumi.Input[str] city: The city of the contact's address.
        :param pulumi.Input[str] contact_type: Indicates whether the contact is a person, company, association, or public organization. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-ContactType) for valid values.
        :param pulumi.Input[str] country_code: Code for the country of the contact's address. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-CountryCode) for valid values.
        :param pulumi.Input[str] email: Email address of the contact.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extra_params: A key-value map of parameters required by certain top-level domains.
        :param pulumi.Input[str] fax: Fax number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        :param pulumi.Input[str] first_name: First name of contact.
        :param pulumi.Input[str] last_name: Last name of contact.
        :param pulumi.Input[str] organization_name: Name of the organization for contact types other than `PERSON`.
        :param pulumi.Input[str] phone_number: The phone number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        :param pulumi.Input[str] state: The state or province of the contact's city.
        :param pulumi.Input[str] zip_code: The zip or postal code of the contact's address.
        """
        RegisteredDomainAdminContactArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            contact_type=contact_type,
            country_code=country_code,
            email=email,
            extra_params=extra_params,
            fax=fax,
            first_name=first_name,
            last_name=last_name,
            organization_name=organization_name,
            phone_number=phone_number,
            state=state,
            zip_code=zip_code,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_line1: Optional[pulumi.Input[str]] = None,
             address_line2: Optional[pulumi.Input[str]] = None,
             city: Optional[pulumi.Input[str]] = None,
             contact_type: Optional[pulumi.Input[str]] = None,
             country_code: Optional[pulumi.Input[str]] = None,
             email: Optional[pulumi.Input[str]] = None,
             extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             fax: Optional[pulumi.Input[str]] = None,
             first_name: Optional[pulumi.Input[str]] = None,
             last_name: Optional[pulumi.Input[str]] = None,
             organization_name: Optional[pulumi.Input[str]] = None,
             phone_number: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             zip_code: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if address_line1 is None and 'addressLine1' in kwargs:
            address_line1 = kwargs['addressLine1']
        if address_line2 is None and 'addressLine2' in kwargs:
            address_line2 = kwargs['addressLine2']
        if contact_type is None and 'contactType' in kwargs:
            contact_type = kwargs['contactType']
        if country_code is None and 'countryCode' in kwargs:
            country_code = kwargs['countryCode']
        if extra_params is None and 'extraParams' in kwargs:
            extra_params = kwargs['extraParams']
        if first_name is None and 'firstName' in kwargs:
            first_name = kwargs['firstName']
        if last_name is None and 'lastName' in kwargs:
            last_name = kwargs['lastName']
        if organization_name is None and 'organizationName' in kwargs:
            organization_name = kwargs['organizationName']
        if phone_number is None and 'phoneNumber' in kwargs:
            phone_number = kwargs['phoneNumber']
        if zip_code is None and 'zipCode' in kwargs:
            zip_code = kwargs['zipCode']

        if address_line1 is not None:
            _setter("address_line1", address_line1)
        if address_line2 is not None:
            _setter("address_line2", address_line2)
        if city is not None:
            _setter("city", city)
        if contact_type is not None:
            _setter("contact_type", contact_type)
        if country_code is not None:
            _setter("country_code", country_code)
        if email is not None:
            _setter("email", email)
        if extra_params is not None:
            _setter("extra_params", extra_params)
        if fax is not None:
            _setter("fax", fax)
        if first_name is not None:
            _setter("first_name", first_name)
        if last_name is not None:
            _setter("last_name", last_name)
        if organization_name is not None:
            _setter("organization_name", organization_name)
        if phone_number is not None:
            _setter("phone_number", phone_number)
        if state is not None:
            _setter("state", state)
        if zip_code is not None:
            _setter("zip_code", zip_code)

    @property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[str]]:
        """
        First line of the contact's address.
        """
        return pulumi.get(self, "address_line1")

    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line1", value)

    @property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[str]]:
        """
        Second line of contact's address, if any.
        """
        return pulumi.get(self, "address_line2")

    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line2", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        The city of the contact's address.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the contact is a person, company, association, or public organization. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-ContactType) for valid values.
        """
        return pulumi.get(self, "contact_type")

    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_type", value)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        """
        Code for the country of the contact's address. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-CountryCode) for valid values.
        """
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the contact.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value map of parameters required by certain top-level domains.
        """
        return pulumi.get(self, "extra_params")

    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "extra_params", value)

    @property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[str]]:
        """
        Fax number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        """
        return pulumi.get(self, "fax")

    @fax.setter
    def fax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fax", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name of contact.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name of contact.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the organization for contact types other than `PERSON`.
        """
        return pulumi.get(self, "organization_name")

    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_name", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state or province of the contact's city.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[str]]:
        """
        The zip or postal code of the contact's address.
        """
        return pulumi.get(self, "zip_code")

    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_code", value)


@pulumi.input_type
class RegisteredDomainNameServerArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 glue_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        :param pulumi.Input[str] name: The fully qualified host name of the name server.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] glue_ips: Glue IP addresses of a name server. The list can contain only one IPv4 and one IPv6 address.
        """
        RegisteredDomainNameServerArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            glue_ips=glue_ips,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             glue_ips: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if glue_ips is None and 'glueIps' in kwargs:
            glue_ips = kwargs['glueIps']

        _setter("name", name)
        if glue_ips is not None:
            _setter("glue_ips", glue_ips)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The fully qualified host name of the name server.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="glueIps")
    def glue_ips(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Glue IP addresses of a name server. The list can contain only one IPv4 and one IPv6 address.
        """
        return pulumi.get(self, "glue_ips")

    @glue_ips.setter
    def glue_ips(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "glue_ips", value)


@pulumi.input_type
class RegisteredDomainRegistrantContactArgs:
    def __init__(__self__, *,
                 address_line1: Optional[pulumi.Input[str]] = None,
                 address_line2: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 contact_type: Optional[pulumi.Input[str]] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 zip_code: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address_line1: First line of the contact's address.
        :param pulumi.Input[str] address_line2: Second line of contact's address, if any.
        :param pulumi.Input[str] city: The city of the contact's address.
        :param pulumi.Input[str] contact_type: Indicates whether the contact is a person, company, association, or public organization. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-ContactType) for valid values.
        :param pulumi.Input[str] country_code: Code for the country of the contact's address. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-CountryCode) for valid values.
        :param pulumi.Input[str] email: Email address of the contact.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extra_params: A key-value map of parameters required by certain top-level domains.
        :param pulumi.Input[str] fax: Fax number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        :param pulumi.Input[str] first_name: First name of contact.
        :param pulumi.Input[str] last_name: Last name of contact.
        :param pulumi.Input[str] organization_name: Name of the organization for contact types other than `PERSON`.
        :param pulumi.Input[str] phone_number: The phone number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        :param pulumi.Input[str] state: The state or province of the contact's city.
        :param pulumi.Input[str] zip_code: The zip or postal code of the contact's address.
        """
        RegisteredDomainRegistrantContactArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            contact_type=contact_type,
            country_code=country_code,
            email=email,
            extra_params=extra_params,
            fax=fax,
            first_name=first_name,
            last_name=last_name,
            organization_name=organization_name,
            phone_number=phone_number,
            state=state,
            zip_code=zip_code,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_line1: Optional[pulumi.Input[str]] = None,
             address_line2: Optional[pulumi.Input[str]] = None,
             city: Optional[pulumi.Input[str]] = None,
             contact_type: Optional[pulumi.Input[str]] = None,
             country_code: Optional[pulumi.Input[str]] = None,
             email: Optional[pulumi.Input[str]] = None,
             extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             fax: Optional[pulumi.Input[str]] = None,
             first_name: Optional[pulumi.Input[str]] = None,
             last_name: Optional[pulumi.Input[str]] = None,
             organization_name: Optional[pulumi.Input[str]] = None,
             phone_number: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             zip_code: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if address_line1 is None and 'addressLine1' in kwargs:
            address_line1 = kwargs['addressLine1']
        if address_line2 is None and 'addressLine2' in kwargs:
            address_line2 = kwargs['addressLine2']
        if contact_type is None and 'contactType' in kwargs:
            contact_type = kwargs['contactType']
        if country_code is None and 'countryCode' in kwargs:
            country_code = kwargs['countryCode']
        if extra_params is None and 'extraParams' in kwargs:
            extra_params = kwargs['extraParams']
        if first_name is None and 'firstName' in kwargs:
            first_name = kwargs['firstName']
        if last_name is None and 'lastName' in kwargs:
            last_name = kwargs['lastName']
        if organization_name is None and 'organizationName' in kwargs:
            organization_name = kwargs['organizationName']
        if phone_number is None and 'phoneNumber' in kwargs:
            phone_number = kwargs['phoneNumber']
        if zip_code is None and 'zipCode' in kwargs:
            zip_code = kwargs['zipCode']

        if address_line1 is not None:
            _setter("address_line1", address_line1)
        if address_line2 is not None:
            _setter("address_line2", address_line2)
        if city is not None:
            _setter("city", city)
        if contact_type is not None:
            _setter("contact_type", contact_type)
        if country_code is not None:
            _setter("country_code", country_code)
        if email is not None:
            _setter("email", email)
        if extra_params is not None:
            _setter("extra_params", extra_params)
        if fax is not None:
            _setter("fax", fax)
        if first_name is not None:
            _setter("first_name", first_name)
        if last_name is not None:
            _setter("last_name", last_name)
        if organization_name is not None:
            _setter("organization_name", organization_name)
        if phone_number is not None:
            _setter("phone_number", phone_number)
        if state is not None:
            _setter("state", state)
        if zip_code is not None:
            _setter("zip_code", zip_code)

    @property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[str]]:
        """
        First line of the contact's address.
        """
        return pulumi.get(self, "address_line1")

    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line1", value)

    @property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[str]]:
        """
        Second line of contact's address, if any.
        """
        return pulumi.get(self, "address_line2")

    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line2", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        The city of the contact's address.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the contact is a person, company, association, or public organization. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-ContactType) for valid values.
        """
        return pulumi.get(self, "contact_type")

    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_type", value)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        """
        Code for the country of the contact's address. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-CountryCode) for valid values.
        """
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the contact.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value map of parameters required by certain top-level domains.
        """
        return pulumi.get(self, "extra_params")

    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "extra_params", value)

    @property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[str]]:
        """
        Fax number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        """
        return pulumi.get(self, "fax")

    @fax.setter
    def fax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fax", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name of contact.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name of contact.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the organization for contact types other than `PERSON`.
        """
        return pulumi.get(self, "organization_name")

    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_name", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state or province of the contact's city.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[str]]:
        """
        The zip or postal code of the contact's address.
        """
        return pulumi.get(self, "zip_code")

    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_code", value)


@pulumi.input_type
class RegisteredDomainTechContactArgs:
    def __init__(__self__, *,
                 address_line1: Optional[pulumi.Input[str]] = None,
                 address_line2: Optional[pulumi.Input[str]] = None,
                 city: Optional[pulumi.Input[str]] = None,
                 contact_type: Optional[pulumi.Input[str]] = None,
                 country_code: Optional[pulumi.Input[str]] = None,
                 email: Optional[pulumi.Input[str]] = None,
                 extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 fax: Optional[pulumi.Input[str]] = None,
                 first_name: Optional[pulumi.Input[str]] = None,
                 last_name: Optional[pulumi.Input[str]] = None,
                 organization_name: Optional[pulumi.Input[str]] = None,
                 phone_number: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 zip_code: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] address_line1: First line of the contact's address.
        :param pulumi.Input[str] address_line2: Second line of contact's address, if any.
        :param pulumi.Input[str] city: The city of the contact's address.
        :param pulumi.Input[str] contact_type: Indicates whether the contact is a person, company, association, or public organization. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-ContactType) for valid values.
        :param pulumi.Input[str] country_code: Code for the country of the contact's address. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-CountryCode) for valid values.
        :param pulumi.Input[str] email: Email address of the contact.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] extra_params: A key-value map of parameters required by certain top-level domains.
        :param pulumi.Input[str] fax: Fax number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        :param pulumi.Input[str] first_name: First name of contact.
        :param pulumi.Input[str] last_name: Last name of contact.
        :param pulumi.Input[str] organization_name: Name of the organization for contact types other than `PERSON`.
        :param pulumi.Input[str] phone_number: The phone number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        :param pulumi.Input[str] state: The state or province of the contact's city.
        :param pulumi.Input[str] zip_code: The zip or postal code of the contact's address.
        """
        RegisteredDomainTechContactArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            address_line1=address_line1,
            address_line2=address_line2,
            city=city,
            contact_type=contact_type,
            country_code=country_code,
            email=email,
            extra_params=extra_params,
            fax=fax,
            first_name=first_name,
            last_name=last_name,
            organization_name=organization_name,
            phone_number=phone_number,
            state=state,
            zip_code=zip_code,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             address_line1: Optional[pulumi.Input[str]] = None,
             address_line2: Optional[pulumi.Input[str]] = None,
             city: Optional[pulumi.Input[str]] = None,
             contact_type: Optional[pulumi.Input[str]] = None,
             country_code: Optional[pulumi.Input[str]] = None,
             email: Optional[pulumi.Input[str]] = None,
             extra_params: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             fax: Optional[pulumi.Input[str]] = None,
             first_name: Optional[pulumi.Input[str]] = None,
             last_name: Optional[pulumi.Input[str]] = None,
             organization_name: Optional[pulumi.Input[str]] = None,
             phone_number: Optional[pulumi.Input[str]] = None,
             state: Optional[pulumi.Input[str]] = None,
             zip_code: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if address_line1 is None and 'addressLine1' in kwargs:
            address_line1 = kwargs['addressLine1']
        if address_line2 is None and 'addressLine2' in kwargs:
            address_line2 = kwargs['addressLine2']
        if contact_type is None and 'contactType' in kwargs:
            contact_type = kwargs['contactType']
        if country_code is None and 'countryCode' in kwargs:
            country_code = kwargs['countryCode']
        if extra_params is None and 'extraParams' in kwargs:
            extra_params = kwargs['extraParams']
        if first_name is None and 'firstName' in kwargs:
            first_name = kwargs['firstName']
        if last_name is None and 'lastName' in kwargs:
            last_name = kwargs['lastName']
        if organization_name is None and 'organizationName' in kwargs:
            organization_name = kwargs['organizationName']
        if phone_number is None and 'phoneNumber' in kwargs:
            phone_number = kwargs['phoneNumber']
        if zip_code is None and 'zipCode' in kwargs:
            zip_code = kwargs['zipCode']

        if address_line1 is not None:
            _setter("address_line1", address_line1)
        if address_line2 is not None:
            _setter("address_line2", address_line2)
        if city is not None:
            _setter("city", city)
        if contact_type is not None:
            _setter("contact_type", contact_type)
        if country_code is not None:
            _setter("country_code", country_code)
        if email is not None:
            _setter("email", email)
        if extra_params is not None:
            _setter("extra_params", extra_params)
        if fax is not None:
            _setter("fax", fax)
        if first_name is not None:
            _setter("first_name", first_name)
        if last_name is not None:
            _setter("last_name", last_name)
        if organization_name is not None:
            _setter("organization_name", organization_name)
        if phone_number is not None:
            _setter("phone_number", phone_number)
        if state is not None:
            _setter("state", state)
        if zip_code is not None:
            _setter("zip_code", zip_code)

    @property
    @pulumi.getter(name="addressLine1")
    def address_line1(self) -> Optional[pulumi.Input[str]]:
        """
        First line of the contact's address.
        """
        return pulumi.get(self, "address_line1")

    @address_line1.setter
    def address_line1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line1", value)

    @property
    @pulumi.getter(name="addressLine2")
    def address_line2(self) -> Optional[pulumi.Input[str]]:
        """
        Second line of contact's address, if any.
        """
        return pulumi.get(self, "address_line2")

    @address_line2.setter
    def address_line2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "address_line2", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        The city of the contact's address.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="contactType")
    def contact_type(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the contact is a person, company, association, or public organization. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-ContactType) for valid values.
        """
        return pulumi.get(self, "contact_type")

    @contact_type.setter
    def contact_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "contact_type", value)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        """
        Code for the country of the contact's address. See the [AWS API documentation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_domains_ContactDetail.html#Route53Domains-Type-domains_ContactDetail-CountryCode) for valid values.
        """
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter
    def email(self) -> Optional[pulumi.Input[str]]:
        """
        Email address of the contact.
        """
        return pulumi.get(self, "email")

    @email.setter
    def email(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "email", value)

    @property
    @pulumi.getter(name="extraParams")
    def extra_params(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A key-value map of parameters required by certain top-level domains.
        """
        return pulumi.get(self, "extra_params")

    @extra_params.setter
    def extra_params(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "extra_params", value)

    @property
    @pulumi.getter
    def fax(self) -> Optional[pulumi.Input[str]]:
        """
        Fax number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        """
        return pulumi.get(self, "fax")

    @fax.setter
    def fax(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fax", value)

    @property
    @pulumi.getter(name="firstName")
    def first_name(self) -> Optional[pulumi.Input[str]]:
        """
        First name of contact.
        """
        return pulumi.get(self, "first_name")

    @first_name.setter
    def first_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "first_name", value)

    @property
    @pulumi.getter(name="lastName")
    def last_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last name of contact.
        """
        return pulumi.get(self, "last_name")

    @last_name.setter
    def last_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_name", value)

    @property
    @pulumi.getter(name="organizationName")
    def organization_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the organization for contact types other than `PERSON`.
        """
        return pulumi.get(self, "organization_name")

    @organization_name.setter
    def organization_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_name", value)

    @property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[str]]:
        """
        The phone number of the contact. Phone number must be specified in the format "+[country dialing code].[number including any area code]".
        """
        return pulumi.get(self, "phone_number")

    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "phone_number", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state or province of the contact's city.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="zipCode")
    def zip_code(self) -> Optional[pulumi.Input[str]]:
        """
        The zip or postal code of the contact's address.
        """
        return pulumi.get(self, "zip_code")

    @zip_code.setter
    def zip_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zip_code", value)



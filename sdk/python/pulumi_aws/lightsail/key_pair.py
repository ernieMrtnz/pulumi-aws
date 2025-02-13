# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['KeyPairArgs', 'KeyPair']

@pulumi.input_type
class KeyPairArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a KeyPair resource.
        :param pulumi.Input[str] name: The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        :param pulumi.Input[str] public_key: The public key material. This public key will be imported into Lightsail
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
               
               > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        KeyPairArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            name_prefix=name_prefix,
            pgp_key=pgp_key,
            public_key=public_key,
            tags=tags,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             name_prefix: Optional[pulumi.Input[str]] = None,
             pgp_key: Optional[pulumi.Input[str]] = None,
             public_key: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name_prefix is None and 'namePrefix' in kwargs:
            name_prefix = kwargs['namePrefix']
        if pgp_key is None and 'pgpKey' in kwargs:
            pgp_key = kwargs['pgpKey']
        if public_key is None and 'publicKey' in kwargs:
            public_key = kwargs['publicKey']

        if name is not None:
            _setter("name", name)
        if name_prefix is not None:
            _setter("name_prefix", name_prefix)
        if pgp_key is not None:
            _setter("pgp_key", pgp_key)
        if public_key is not None:
            _setter("public_key", public_key)
        if tags is not None:
            _setter("tags", tags)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        """
        An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        """
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        The public key material. This public key will be imported into Lightsail
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.

        > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


@pulumi.input_type
class _KeyPairState:
    def __init__(__self__, *,
                 arn: Optional[pulumi.Input[str]] = None,
                 encrypted_fingerprint: Optional[pulumi.Input[str]] = None,
                 encrypted_private_key: Optional[pulumi.Input[str]] = None,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering KeyPair resources.
        :param pulumi.Input[str] arn: The ARN of the Lightsail key pair.
        :param pulumi.Input[str] encrypted_fingerprint: The MD5 public key fingerprint for the encrypted private key.
        :param pulumi.Input[str] encrypted_private_key: the private key material, base 64 encoded and encrypted with the given `pgp_key`. This is only populated when creating a new key and `pgp_key` is supplied.
        :param pulumi.Input[str] fingerprint: The MD5 public key fingerprint as specified in section 4 of RFC 4716.
        :param pulumi.Input[str] name: The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        :param pulumi.Input[str] private_key: the private key, base64 encoded. This is only populated when creating a new key, and when no `pgp_key` is provided.
        :param pulumi.Input[str] public_key: The public key material. This public key will be imported into Lightsail
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
               
               > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        _KeyPairState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arn=arn,
            encrypted_fingerprint=encrypted_fingerprint,
            encrypted_private_key=encrypted_private_key,
            fingerprint=fingerprint,
            name=name,
            name_prefix=name_prefix,
            pgp_key=pgp_key,
            private_key=private_key,
            public_key=public_key,
            tags=tags,
            tags_all=tags_all,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arn: Optional[pulumi.Input[str]] = None,
             encrypted_fingerprint: Optional[pulumi.Input[str]] = None,
             encrypted_private_key: Optional[pulumi.Input[str]] = None,
             fingerprint: Optional[pulumi.Input[str]] = None,
             name: Optional[pulumi.Input[str]] = None,
             name_prefix: Optional[pulumi.Input[str]] = None,
             pgp_key: Optional[pulumi.Input[str]] = None,
             private_key: Optional[pulumi.Input[str]] = None,
             public_key: Optional[pulumi.Input[str]] = None,
             tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if encrypted_fingerprint is None and 'encryptedFingerprint' in kwargs:
            encrypted_fingerprint = kwargs['encryptedFingerprint']
        if encrypted_private_key is None and 'encryptedPrivateKey' in kwargs:
            encrypted_private_key = kwargs['encryptedPrivateKey']
        if name_prefix is None and 'namePrefix' in kwargs:
            name_prefix = kwargs['namePrefix']
        if pgp_key is None and 'pgpKey' in kwargs:
            pgp_key = kwargs['pgpKey']
        if private_key is None and 'privateKey' in kwargs:
            private_key = kwargs['privateKey']
        if public_key is None and 'publicKey' in kwargs:
            public_key = kwargs['publicKey']
        if tags_all is None and 'tagsAll' in kwargs:
            tags_all = kwargs['tagsAll']

        if arn is not None:
            _setter("arn", arn)
        if encrypted_fingerprint is not None:
            _setter("encrypted_fingerprint", encrypted_fingerprint)
        if encrypted_private_key is not None:
            _setter("encrypted_private_key", encrypted_private_key)
        if fingerprint is not None:
            _setter("fingerprint", fingerprint)
        if name is not None:
            _setter("name", name)
        if name_prefix is not None:
            _setter("name_prefix", name_prefix)
        if pgp_key is not None:
            _setter("pgp_key", pgp_key)
        if private_key is not None:
            _setter("private_key", private_key)
        if public_key is not None:
            _setter("public_key", public_key)
        if tags is not None:
            _setter("tags", tags)
        if tags_all is not None:
            warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
            pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")
        if tags_all is not None:
            _setter("tags_all", tags_all)

    @property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[str]]:
        """
        The ARN of the Lightsail key pair.
        """
        return pulumi.get(self, "arn")

    @arn.setter
    def arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arn", value)

    @property
    @pulumi.getter(name="encryptedFingerprint")
    def encrypted_fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        The MD5 public key fingerprint for the encrypted private key.
        """
        return pulumi.get(self, "encrypted_fingerprint")

    @encrypted_fingerprint.setter
    def encrypted_fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_fingerprint", value)

    @property
    @pulumi.getter(name="encryptedPrivateKey")
    def encrypted_private_key(self) -> Optional[pulumi.Input[str]]:
        """
        the private key material, base 64 encoded and encrypted with the given `pgp_key`. This is only populated when creating a new key and `pgp_key` is supplied.
        """
        return pulumi.get(self, "encrypted_private_key")

    @encrypted_private_key.setter
    def encrypted_private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encrypted_private_key", value)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        The MD5 public key fingerprint as specified in section 4 of RFC 4716.
        """
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name_prefix")

    @name_prefix.setter
    def name_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name_prefix", value)

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[pulumi.Input[str]]:
        """
        An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        """
        return pulumi.get(self, "pgp_key")

    @pgp_key.setter
    def pgp_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pgp_key", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        the private key, base64 encoded. This is only populated when creating a new key, and when no `pgp_key` is provided.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        The public key material. This public key will be imported into Lightsail
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.

        > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
        pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")

        return pulumi.get(self, "tags_all")

    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags_all", value)


class KeyPair(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Provides a Lightsail Key Pair, for use with Lightsail Instances. These key pairs
        are separate from EC2 Key Pairs, and must be created or imported for use with
        Lightsail.

        > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

        ## Example Usage
        ### Create New Key Pair

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new Lightsail Key Pair
        lg_key_pair = aws.lightsail.KeyPair("lgKeyPair")
        ```
        ### Create New Key Pair with PGP Encrypted Private Key

        ```python
        import pulumi
        import pulumi_aws as aws

        lg_key_pair = aws.lightsail.KeyPair("lgKeyPair", pgp_key="keybase:keybaseusername")
        ```
        ### Existing Public Key Import

        ```python
        import pulumi
        import pulumi_aws as aws

        lg_key_pair = aws.lightsail.KeyPair("lgKeyPair", public_key=(lambda path: open(path).read())("~/.ssh/id_rsa.pub"))
        ```

        ## Import

        You cannot import Lightsail Key Pairs because the private and public key are only available on initial creation.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        :param pulumi.Input[str] public_key: The public key material. This public key will be imported into Lightsail
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
               
               > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[KeyPairArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Lightsail Key Pair, for use with Lightsail Instances. These key pairs
        are separate from EC2 Key Pairs, and must be created or imported for use with
        Lightsail.

        > **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

        ## Example Usage
        ### Create New Key Pair

        ```python
        import pulumi
        import pulumi_aws as aws

        # Create a new Lightsail Key Pair
        lg_key_pair = aws.lightsail.KeyPair("lgKeyPair")
        ```
        ### Create New Key Pair with PGP Encrypted Private Key

        ```python
        import pulumi
        import pulumi_aws as aws

        lg_key_pair = aws.lightsail.KeyPair("lgKeyPair", pgp_key="keybase:keybaseusername")
        ```
        ### Existing Public Key Import

        ```python
        import pulumi
        import pulumi_aws as aws

        lg_key_pair = aws.lightsail.KeyPair("lgKeyPair", public_key=(lambda path: open(path).read())("~/.ssh/id_rsa.pub"))
        ```

        ## Import

        You cannot import Lightsail Key Pairs because the private and public key are only available on initial creation.

        :param str resource_name: The name of the resource.
        :param KeyPairArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyPairArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            KeyPairArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 name_prefix: Optional[pulumi.Input[str]] = None,
                 pgp_key: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyPairArgs.__new__(KeyPairArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["name_prefix"] = name_prefix
            __props__.__dict__["pgp_key"] = pgp_key
            __props__.__dict__["public_key"] = public_key
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["encrypted_fingerprint"] = None
            __props__.__dict__["encrypted_private_key"] = None
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["private_key"] = None
            __props__.__dict__["tags_all"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["tagsAll"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(KeyPair, __self__).__init__(
            'aws:lightsail/keyPair:KeyPair',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arn: Optional[pulumi.Input[str]] = None,
            encrypted_fingerprint: Optional[pulumi.Input[str]] = None,
            encrypted_private_key: Optional[pulumi.Input[str]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            name_prefix: Optional[pulumi.Input[str]] = None,
            pgp_key: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'KeyPair':
        """
        Get an existing KeyPair resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] arn: The ARN of the Lightsail key pair.
        :param pulumi.Input[str] encrypted_fingerprint: The MD5 public key fingerprint for the encrypted private key.
        :param pulumi.Input[str] encrypted_private_key: the private key material, base 64 encoded and encrypted with the given `pgp_key`. This is only populated when creating a new key and `pgp_key` is supplied.
        :param pulumi.Input[str] fingerprint: The MD5 public key fingerprint as specified in section 4 of RFC 4716.
        :param pulumi.Input[str] name: The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        :param pulumi.Input[str] pgp_key: An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        :param pulumi.Input[str] private_key: the private key, base64 encoded. This is only populated when creating a new key, and when no `pgp_key` is provided.
        :param pulumi.Input[str] public_key: The public key material. This public key will be imported into Lightsail
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.
               
               > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _KeyPairState.__new__(_KeyPairState)

        __props__.__dict__["arn"] = arn
        __props__.__dict__["encrypted_fingerprint"] = encrypted_fingerprint
        __props__.__dict__["encrypted_private_key"] = encrypted_private_key
        __props__.__dict__["fingerprint"] = fingerprint
        __props__.__dict__["name"] = name
        __props__.__dict__["name_prefix"] = name_prefix
        __props__.__dict__["pgp_key"] = pgp_key
        __props__.__dict__["private_key"] = private_key
        __props__.__dict__["public_key"] = public_key
        __props__.__dict__["tags"] = tags
        __props__.__dict__["tags_all"] = tags_all
        return KeyPair(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the Lightsail key pair.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="encryptedFingerprint")
    def encrypted_fingerprint(self) -> pulumi.Output[str]:
        """
        The MD5 public key fingerprint for the encrypted private key.
        """
        return pulumi.get(self, "encrypted_fingerprint")

    @property
    @pulumi.getter(name="encryptedPrivateKey")
    def encrypted_private_key(self) -> pulumi.Output[str]:
        """
        the private key material, base 64 encoded and encrypted with the given `pgp_key`. This is only populated when creating a new key and `pgp_key` is supplied.
        """
        return pulumi.get(self, "encrypted_private_key")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        The MD5 public key fingerprint as specified in section 4 of RFC 4716.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the Lightsail Key Pair. If omitted, a unique name will be generated by this provider
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namePrefix")
    def name_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name_prefix")

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> pulumi.Output[Optional[str]]:
        """
        An optional PGP key to encrypt the resulting private key material. Only used when creating a new key pair
        """
        return pulumi.get(self, "pgp_key")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        the private key, base64 encoded. This is only populated when creating a new key, and when no `pgp_key` is provided.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        The public key material. This public key will be imported into Lightsail
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A map of tags to assign to the collection. If configured with a provider `default_tags` configuration block present, tags with matching keys will overwrite those defined at the provider-level.

        > **NOTE:** a PGP key is not required, however it is strongly encouraged. Without a PGP key, the private key material will be stored in state unencrypted.`pgp_key` is ignored if `public_key` is supplied.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, str]]:
        warnings.warn("""Please use `tags` instead.""", DeprecationWarning)
        pulumi.log.warn("""tags_all is deprecated: Please use `tags` instead.""")

        return pulumi.get(self, "tags_all")


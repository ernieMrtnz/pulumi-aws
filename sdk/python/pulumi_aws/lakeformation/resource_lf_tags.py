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

__all__ = ['ResourceLfTagsArgs', 'ResourceLfTags']

@pulumi.input_type
class ResourceLfTagsArgs:
    def __init__(__self__, *,
                 lf_tags: pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]],
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']] = None,
                 table: Optional[pulumi.Input['ResourceLfTagsTableArgs']] = None,
                 table_with_columns: Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']] = None):
        """
        The set of arguments for constructing a ResourceLfTags resource.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]] lf_tags: Set of LF-tags to attach to the resource. See below.
               
               Exactly one of the following is required:
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        :param pulumi.Input['ResourceLfTagsDatabaseArgs'] database: Configuration block for a database resource. See below.
        :param pulumi.Input['ResourceLfTagsTableArgs'] table: Configuration block for a table resource. See below.
        :param pulumi.Input['ResourceLfTagsTableWithColumnsArgs'] table_with_columns: Configuration block for a table with columns resource. See below.
               
               The following arguments are optional:
        """
        ResourceLfTagsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            lf_tags=lf_tags,
            catalog_id=catalog_id,
            database=database,
            table=table,
            table_with_columns=table_with_columns,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]] = None,
             catalog_id: Optional[pulumi.Input[str]] = None,
             database: Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']] = None,
             table: Optional[pulumi.Input['ResourceLfTagsTableArgs']] = None,
             table_with_columns: Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if lf_tags is None and 'lfTags' in kwargs:
            lf_tags = kwargs['lfTags']
        if lf_tags is None:
            raise TypeError("Missing 'lf_tags' argument")
        if catalog_id is None and 'catalogId' in kwargs:
            catalog_id = kwargs['catalogId']
        if table_with_columns is None and 'tableWithColumns' in kwargs:
            table_with_columns = kwargs['tableWithColumns']

        _setter("lf_tags", lf_tags)
        if catalog_id is not None:
            _setter("catalog_id", catalog_id)
        if database is not None:
            _setter("database", database)
        if table is not None:
            _setter("table", table)
        if table_with_columns is not None:
            _setter("table_with_columns", table_with_columns)

    @property
    @pulumi.getter(name="lfTags")
    def lf_tags(self) -> pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]:
        """
        Set of LF-tags to attach to the resource. See below.

        Exactly one of the following is required:
        """
        return pulumi.get(self, "lf_tags")

    @lf_tags.setter
    def lf_tags(self, value: pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]):
        pulumi.set(self, "lf_tags", value)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']]:
        """
        Configuration block for a database resource. See below.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input['ResourceLfTagsTableArgs']]:
        """
        Configuration block for a table resource. See below.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input['ResourceLfTagsTableArgs']]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']]:
        """
        Configuration block for a table with columns resource. See below.

        The following arguments are optional:
        """
        return pulumi.get(self, "table_with_columns")

    @table_with_columns.setter
    def table_with_columns(self, value: Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']]):
        pulumi.set(self, "table_with_columns", value)


@pulumi.input_type
class _ResourceLfTagsState:
    def __init__(__self__, *,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']] = None,
                 lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]] = None,
                 table: Optional[pulumi.Input['ResourceLfTagsTableArgs']] = None,
                 table_with_columns: Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']] = None):
        """
        Input properties used for looking up and filtering ResourceLfTags resources.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        :param pulumi.Input['ResourceLfTagsDatabaseArgs'] database: Configuration block for a database resource. See below.
        :param pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]] lf_tags: Set of LF-tags to attach to the resource. See below.
               
               Exactly one of the following is required:
        :param pulumi.Input['ResourceLfTagsTableArgs'] table: Configuration block for a table resource. See below.
        :param pulumi.Input['ResourceLfTagsTableWithColumnsArgs'] table_with_columns: Configuration block for a table with columns resource. See below.
               
               The following arguments are optional:
        """
        _ResourceLfTagsState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            catalog_id=catalog_id,
            database=database,
            lf_tags=lf_tags,
            table=table,
            table_with_columns=table_with_columns,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             catalog_id: Optional[pulumi.Input[str]] = None,
             database: Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']] = None,
             lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]] = None,
             table: Optional[pulumi.Input['ResourceLfTagsTableArgs']] = None,
             table_with_columns: Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if catalog_id is None and 'catalogId' in kwargs:
            catalog_id = kwargs['catalogId']
        if lf_tags is None and 'lfTags' in kwargs:
            lf_tags = kwargs['lfTags']
        if table_with_columns is None and 'tableWithColumns' in kwargs:
            table_with_columns = kwargs['tableWithColumns']

        if catalog_id is not None:
            _setter("catalog_id", catalog_id)
        if database is not None:
            _setter("database", database)
        if lf_tags is not None:
            _setter("lf_tags", lf_tags)
        if table is not None:
            _setter("table", table)
        if table_with_columns is not None:
            _setter("table_with_columns", table_with_columns)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        """
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']]:
        """
        Configuration block for a database resource. See below.
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input['ResourceLfTagsDatabaseArgs']]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter(name="lfTags")
    def lf_tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]]:
        """
        Set of LF-tags to attach to the resource. See below.

        Exactly one of the following is required:
        """
        return pulumi.get(self, "lf_tags")

    @lf_tags.setter
    def lf_tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ResourceLfTagsLfTagArgs']]]]):
        pulumi.set(self, "lf_tags", value)

    @property
    @pulumi.getter
    def table(self) -> Optional[pulumi.Input['ResourceLfTagsTableArgs']]:
        """
        Configuration block for a table resource. See below.
        """
        return pulumi.get(self, "table")

    @table.setter
    def table(self, value: Optional[pulumi.Input['ResourceLfTagsTableArgs']]):
        pulumi.set(self, "table", value)

    @property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']]:
        """
        Configuration block for a table with columns resource. See below.

        The following arguments are optional:
        """
        return pulumi.get(self, "table_with_columns")

    @table_with_columns.setter
    def table_with_columns(self, value: Optional[pulumi.Input['ResourceLfTagsTableWithColumnsArgs']]):
        pulumi.set(self, "table_with_columns", value)


class ResourceLfTags(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsDatabaseArgs']]] = None,
                 lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceLfTagsLfTagArgs']]]]] = None,
                 table: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsTableArgs']]] = None,
                 table_with_columns: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsTableWithColumnsArgs']]] = None,
                 __props__=None):
        """
        Manages an attachment between one or more existing LF-tags and an existing Lake Formation resource.

        ## Example Usage
        ### Database Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example_lf_tag = aws.lakeformation.LfTag("exampleLfTag",
            key="right",
            values=[
                "abbey",
                "village",
                "luffield",
                "woodcote",
                "copse",
                "chapel",
                "stowe",
                "club",
            ])
        example_resource_lf_tags = aws.lakeformation.ResourceLfTags("exampleResourceLfTags",
            database=aws.lakeformation.ResourceLfTagsDatabaseArgs(
                name=aws_glue_catalog_database["example"]["name"],
            ),
            lf_tags=[aws.lakeformation.ResourceLfTagsLfTagArgs(
                key=example_lf_tag.key,
                value="stowe",
            )])
        ```
        ### Multiple Tags Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example_lf_tag = aws.lakeformation.LfTag("exampleLfTag",
            key="right",
            values=[
                "abbey",
                "village",
                "luffield",
                "woodcote",
                "copse",
                "chapel",
                "stowe",
                "club",
            ])
        example2 = aws.lakeformation.LfTag("example2",
            key="left",
            values=[
                "farm",
                "theloop",
                "aintree",
                "brooklands",
                "maggotts",
                "becketts",
                "vale",
            ])
        example_resource_lf_tags = aws.lakeformation.ResourceLfTags("exampleResourceLfTags",
            database=aws.lakeformation.ResourceLfTagsDatabaseArgs(
                name=aws_glue_catalog_database["example"]["name"],
            ),
            lf_tags=[
                aws.lakeformation.ResourceLfTagsLfTagArgs(
                    key="right",
                    value="luffield",
                ),
                aws.lakeformation.ResourceLfTagsLfTagArgs(
                    key="left",
                    value="aintree",
                ),
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        :param pulumi.Input[pulumi.InputType['ResourceLfTagsDatabaseArgs']] database: Configuration block for a database resource. See below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceLfTagsLfTagArgs']]]] lf_tags: Set of LF-tags to attach to the resource. See below.
               
               Exactly one of the following is required:
        :param pulumi.Input[pulumi.InputType['ResourceLfTagsTableArgs']] table: Configuration block for a table resource. See below.
        :param pulumi.Input[pulumi.InputType['ResourceLfTagsTableWithColumnsArgs']] table_with_columns: Configuration block for a table with columns resource. See below.
               
               The following arguments are optional:
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceLfTagsArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Manages an attachment between one or more existing LF-tags and an existing Lake Formation resource.

        ## Example Usage
        ### Database Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example_lf_tag = aws.lakeformation.LfTag("exampleLfTag",
            key="right",
            values=[
                "abbey",
                "village",
                "luffield",
                "woodcote",
                "copse",
                "chapel",
                "stowe",
                "club",
            ])
        example_resource_lf_tags = aws.lakeformation.ResourceLfTags("exampleResourceLfTags",
            database=aws.lakeformation.ResourceLfTagsDatabaseArgs(
                name=aws_glue_catalog_database["example"]["name"],
            ),
            lf_tags=[aws.lakeformation.ResourceLfTagsLfTagArgs(
                key=example_lf_tag.key,
                value="stowe",
            )])
        ```
        ### Multiple Tags Example

        ```python
        import pulumi
        import pulumi_aws as aws

        example_lf_tag = aws.lakeformation.LfTag("exampleLfTag",
            key="right",
            values=[
                "abbey",
                "village",
                "luffield",
                "woodcote",
                "copse",
                "chapel",
                "stowe",
                "club",
            ])
        example2 = aws.lakeformation.LfTag("example2",
            key="left",
            values=[
                "farm",
                "theloop",
                "aintree",
                "brooklands",
                "maggotts",
                "becketts",
                "vale",
            ])
        example_resource_lf_tags = aws.lakeformation.ResourceLfTags("exampleResourceLfTags",
            database=aws.lakeformation.ResourceLfTagsDatabaseArgs(
                name=aws_glue_catalog_database["example"]["name"],
            ),
            lf_tags=[
                aws.lakeformation.ResourceLfTagsLfTagArgs(
                    key="right",
                    value="luffield",
                ),
                aws.lakeformation.ResourceLfTagsLfTagArgs(
                    key="left",
                    value="aintree",
                ),
            ])
        ```

        :param str resource_name: The name of the resource.
        :param ResourceLfTagsArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceLfTagsArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ResourceLfTagsArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsDatabaseArgs']]] = None,
                 lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceLfTagsLfTagArgs']]]]] = None,
                 table: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsTableArgs']]] = None,
                 table_with_columns: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsTableWithColumnsArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ResourceLfTagsArgs.__new__(ResourceLfTagsArgs)

            __props__.__dict__["catalog_id"] = catalog_id
            database = _utilities.configure(database, ResourceLfTagsDatabaseArgs, True)
            __props__.__dict__["database"] = database
            if lf_tags is None and not opts.urn:
                raise TypeError("Missing required property 'lf_tags'")
            __props__.__dict__["lf_tags"] = lf_tags
            table = _utilities.configure(table, ResourceLfTagsTableArgs, True)
            __props__.__dict__["table"] = table
            table_with_columns = _utilities.configure(table_with_columns, ResourceLfTagsTableWithColumnsArgs, True)
            __props__.__dict__["table_with_columns"] = table_with_columns
        super(ResourceLfTags, __self__).__init__(
            'aws:lakeformation/resourceLfTags:ResourceLfTags',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            catalog_id: Optional[pulumi.Input[str]] = None,
            database: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsDatabaseArgs']]] = None,
            lf_tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceLfTagsLfTagArgs']]]]] = None,
            table: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsTableArgs']]] = None,
            table_with_columns: Optional[pulumi.Input[pulumi.InputType['ResourceLfTagsTableWithColumnsArgs']]] = None) -> 'ResourceLfTags':
        """
        Get an existing ResourceLfTags resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] catalog_id: Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        :param pulumi.Input[pulumi.InputType['ResourceLfTagsDatabaseArgs']] database: Configuration block for a database resource. See below.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ResourceLfTagsLfTagArgs']]]] lf_tags: Set of LF-tags to attach to the resource. See below.
               
               Exactly one of the following is required:
        :param pulumi.Input[pulumi.InputType['ResourceLfTagsTableArgs']] table: Configuration block for a table resource. See below.
        :param pulumi.Input[pulumi.InputType['ResourceLfTagsTableWithColumnsArgs']] table_with_columns: Configuration block for a table with columns resource. See below.
               
               The following arguments are optional:
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ResourceLfTagsState.__new__(_ResourceLfTagsState)

        __props__.__dict__["catalog_id"] = catalog_id
        __props__.__dict__["database"] = database
        __props__.__dict__["lf_tags"] = lf_tags
        __props__.__dict__["table"] = table
        __props__.__dict__["table_with_columns"] = table_with_columns
        return ResourceLfTags(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[str]:
        """
        Identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.
        """
        return pulumi.get(self, "catalog_id")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output['outputs.ResourceLfTagsDatabase']:
        """
        Configuration block for a database resource. See below.
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter(name="lfTags")
    def lf_tags(self) -> pulumi.Output[Sequence['outputs.ResourceLfTagsLfTag']]:
        """
        Set of LF-tags to attach to the resource. See below.

        Exactly one of the following is required:
        """
        return pulumi.get(self, "lf_tags")

    @property
    @pulumi.getter
    def table(self) -> pulumi.Output['outputs.ResourceLfTagsTable']:
        """
        Configuration block for a table resource. See below.
        """
        return pulumi.get(self, "table")

    @property
    @pulumi.getter(name="tableWithColumns")
    def table_with_columns(self) -> pulumi.Output['outputs.ResourceLfTagsTableWithColumns']:
        """
        Configuration block for a table with columns resource. See below.

        The following arguments are optional:
        """
        return pulumi.get(self, "table_with_columns")


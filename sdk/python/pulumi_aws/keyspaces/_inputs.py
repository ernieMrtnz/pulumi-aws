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
    'TableCapacitySpecificationArgs',
    'TableClientSideTimestampsArgs',
    'TableCommentArgs',
    'TableEncryptionSpecificationArgs',
    'TablePointInTimeRecoveryArgs',
    'TableSchemaDefinitionArgs',
    'TableSchemaDefinitionClusteringKeyArgs',
    'TableSchemaDefinitionColumnArgs',
    'TableSchemaDefinitionPartitionKeyArgs',
    'TableSchemaDefinitionStaticColumnArgs',
    'TableTtlArgs',
]

@pulumi.input_type
class TableCapacitySpecificationArgs:
    def __init__(__self__, *,
                 read_capacity_units: Optional[pulumi.Input[int]] = None,
                 throughput_mode: Optional[pulumi.Input[str]] = None,
                 write_capacity_units: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[int] read_capacity_units: The throughput capacity specified for read operations defined in read capacity units (RCUs).
        :param pulumi.Input[str] throughput_mode: The read/write throughput capacity mode for a table. Valid values: `PAY_PER_REQUEST`, `PROVISIONED`. The default value is `PAY_PER_REQUEST`.
        :param pulumi.Input[int] write_capacity_units: The throughput capacity specified for write operations defined in write capacity units (WCUs).
        """
        TableCapacitySpecificationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            read_capacity_units=read_capacity_units,
            throughput_mode=throughput_mode,
            write_capacity_units=write_capacity_units,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             read_capacity_units: Optional[pulumi.Input[int]] = None,
             throughput_mode: Optional[pulumi.Input[str]] = None,
             write_capacity_units: Optional[pulumi.Input[int]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if read_capacity_units is None and 'readCapacityUnits' in kwargs:
            read_capacity_units = kwargs['readCapacityUnits']
        if throughput_mode is None and 'throughputMode' in kwargs:
            throughput_mode = kwargs['throughputMode']
        if write_capacity_units is None and 'writeCapacityUnits' in kwargs:
            write_capacity_units = kwargs['writeCapacityUnits']

        if read_capacity_units is not None:
            _setter("read_capacity_units", read_capacity_units)
        if throughput_mode is not None:
            _setter("throughput_mode", throughput_mode)
        if write_capacity_units is not None:
            _setter("write_capacity_units", write_capacity_units)

    @property
    @pulumi.getter(name="readCapacityUnits")
    def read_capacity_units(self) -> Optional[pulumi.Input[int]]:
        """
        The throughput capacity specified for read operations defined in read capacity units (RCUs).
        """
        return pulumi.get(self, "read_capacity_units")

    @read_capacity_units.setter
    def read_capacity_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "read_capacity_units", value)

    @property
    @pulumi.getter(name="throughputMode")
    def throughput_mode(self) -> Optional[pulumi.Input[str]]:
        """
        The read/write throughput capacity mode for a table. Valid values: `PAY_PER_REQUEST`, `PROVISIONED`. The default value is `PAY_PER_REQUEST`.
        """
        return pulumi.get(self, "throughput_mode")

    @throughput_mode.setter
    def throughput_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "throughput_mode", value)

    @property
    @pulumi.getter(name="writeCapacityUnits")
    def write_capacity_units(self) -> Optional[pulumi.Input[int]]:
        """
        The throughput capacity specified for write operations defined in write capacity units (WCUs).
        """
        return pulumi.get(self, "write_capacity_units")

    @write_capacity_units.setter
    def write_capacity_units(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "write_capacity_units", value)


@pulumi.input_type
class TableClientSideTimestampsArgs:
    def __init__(__self__, *,
                 status: pulumi.Input[str]):
        """
        :param pulumi.Input[str] status: Shows how to enable client-side timestamps settings for the specified table. Valid values: `ENABLED`.
        """
        TableClientSideTimestampsArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("status", status)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        Shows how to enable client-side timestamps settings for the specified table. Valid values: `ENABLED`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class TableCommentArgs:
    def __init__(__self__, *,
                 message: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] message: A description of the table.
        """
        TableCommentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            message=message,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             message: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if message is not None:
            _setter("message", message)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        A description of the table.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)


@pulumi.input_type
class TableEncryptionSpecificationArgs:
    def __init__(__self__, *,
                 kms_key_identifier: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] kms_key_identifier: The Amazon Resource Name (ARN) of the customer managed KMS key.
        :param pulumi.Input[str] type: The encryption option specified for the table. Valid values: `AWS_OWNED_KMS_KEY`, `CUSTOMER_MANAGED_KMS_KEY`. The default value is `AWS_OWNED_KMS_KEY`.
        """
        TableEncryptionSpecificationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            kms_key_identifier=kms_key_identifier,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             kms_key_identifier: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if kms_key_identifier is None and 'kmsKeyIdentifier' in kwargs:
            kms_key_identifier = kwargs['kmsKeyIdentifier']

        if kms_key_identifier is not None:
            _setter("kms_key_identifier", kms_key_identifier)
        if type is not None:
            _setter("type", type)

    @property
    @pulumi.getter(name="kmsKeyIdentifier")
    def kms_key_identifier(self) -> Optional[pulumi.Input[str]]:
        """
        The Amazon Resource Name (ARN) of the customer managed KMS key.
        """
        return pulumi.get(self, "kms_key_identifier")

    @kms_key_identifier.setter
    def kms_key_identifier(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kms_key_identifier", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The encryption option specified for the table. Valid values: `AWS_OWNED_KMS_KEY`, `CUSTOMER_MANAGED_KMS_KEY`. The default value is `AWS_OWNED_KMS_KEY`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class TablePointInTimeRecoveryArgs:
    def __init__(__self__, *,
                 status: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] status: Valid values: `ENABLED`, `DISABLED`. The default value is `DISABLED`.
        """
        TablePointInTimeRecoveryArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):

        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Valid values: `ENABLED`, `DISABLED`. The default value is `DISABLED`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class TableSchemaDefinitionArgs:
    def __init__(__self__, *,
                 columns: pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionColumnArgs']]],
                 partition_keys: pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionPartitionKeyArgs']]],
                 clustering_keys: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionClusteringKeyArgs']]]] = None,
                 static_columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionStaticColumnArgs']]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionColumnArgs']]] columns: The regular columns of the table.
        :param pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionPartitionKeyArgs']]] partition_keys: The columns that are part of the partition key of the table .
        :param pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionClusteringKeyArgs']]] clustering_keys: The columns that are part of the clustering key of the table.
        :param pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionStaticColumnArgs']]] static_columns: The columns that have been defined as `STATIC`. Static columns store values that are shared by all rows in the same partition.
        """
        TableSchemaDefinitionArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            columns=columns,
            partition_keys=partition_keys,
            clustering_keys=clustering_keys,
            static_columns=static_columns,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionColumnArgs']]]] = None,
             partition_keys: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionPartitionKeyArgs']]]] = None,
             clustering_keys: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionClusteringKeyArgs']]]] = None,
             static_columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionStaticColumnArgs']]]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if columns is None:
            raise TypeError("Missing 'columns' argument")
        if partition_keys is None and 'partitionKeys' in kwargs:
            partition_keys = kwargs['partitionKeys']
        if partition_keys is None:
            raise TypeError("Missing 'partition_keys' argument")
        if clustering_keys is None and 'clusteringKeys' in kwargs:
            clustering_keys = kwargs['clusteringKeys']
        if static_columns is None and 'staticColumns' in kwargs:
            static_columns = kwargs['staticColumns']

        _setter("columns", columns)
        _setter("partition_keys", partition_keys)
        if clustering_keys is not None:
            _setter("clustering_keys", clustering_keys)
        if static_columns is not None:
            _setter("static_columns", static_columns)

    @property
    @pulumi.getter
    def columns(self) -> pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionColumnArgs']]]:
        """
        The regular columns of the table.
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionColumnArgs']]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter(name="partitionKeys")
    def partition_keys(self) -> pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionPartitionKeyArgs']]]:
        """
        The columns that are part of the partition key of the table .
        """
        return pulumi.get(self, "partition_keys")

    @partition_keys.setter
    def partition_keys(self, value: pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionPartitionKeyArgs']]]):
        pulumi.set(self, "partition_keys", value)

    @property
    @pulumi.getter(name="clusteringKeys")
    def clustering_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionClusteringKeyArgs']]]]:
        """
        The columns that are part of the clustering key of the table.
        """
        return pulumi.get(self, "clustering_keys")

    @clustering_keys.setter
    def clustering_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionClusteringKeyArgs']]]]):
        pulumi.set(self, "clustering_keys", value)

    @property
    @pulumi.getter(name="staticColumns")
    def static_columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionStaticColumnArgs']]]]:
        """
        The columns that have been defined as `STATIC`. Static columns store values that are shared by all rows in the same partition.
        """
        return pulumi.get(self, "static_columns")

    @static_columns.setter
    def static_columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableSchemaDefinitionStaticColumnArgs']]]]):
        pulumi.set(self, "static_columns", value)


@pulumi.input_type
class TableSchemaDefinitionClusteringKeyArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 order_by: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the clustering key column.
        :param pulumi.Input[str] order_by: The order modifier. Valid values: `ASC`, `DESC`.
        """
        TableSchemaDefinitionClusteringKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            order_by=order_by,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             order_by: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if order_by is None and 'orderBy' in kwargs:
            order_by = kwargs['orderBy']
        if order_by is None:
            raise TypeError("Missing 'order_by' argument")

        _setter("name", name)
        _setter("order_by", order_by)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the clustering key column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orderBy")
    def order_by(self) -> pulumi.Input[str]:
        """
        The order modifier. Valid values: `ASC`, `DESC`.
        """
        return pulumi.get(self, "order_by")

    @order_by.setter
    def order_by(self, value: pulumi.Input[str]):
        pulumi.set(self, "order_by", value)


@pulumi.input_type
class TableSchemaDefinitionColumnArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 type: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the column.
        :param pulumi.Input[str] type: The data type of the column. See the [Developer Guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) for a list of available data types.
        """
        TableSchemaDefinitionColumnArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            type=type,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             type: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")
        if type is None:
            raise TypeError("Missing 'type' argument")

        _setter("name", name)
        _setter("type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The data type of the column. See the [Developer Guide](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html#cql.data-types) for a list of available data types.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class TableSchemaDefinitionPartitionKeyArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the partition key column.
        """
        TableSchemaDefinitionPartitionKeyArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")

        _setter("name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the partition key column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TableSchemaDefinitionStaticColumnArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        :param pulumi.Input[str] name: The name of the static column.
        """
        TableSchemaDefinitionStaticColumnArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if name is None:
            raise TypeError("Missing 'name' argument")

        _setter("name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the static column.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class TableTtlArgs:
    def __init__(__self__, *,
                 status: pulumi.Input[str]):
        """
        :param pulumi.Input[str] status: Valid values: `ENABLED`.
        """
        TableTtlArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("status", status)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        Valid values: `ENABLED`.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)



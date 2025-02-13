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
    'AccessPointPosixUser',
    'AccessPointRootDirectory',
    'AccessPointRootDirectoryCreationInfo',
    'BackupPolicyBackupPolicy',
    'FileSystemLifecyclePolicy',
    'FileSystemSizeInByte',
    'ReplicationConfigurationDestination',
    'GetAccessPointPosixUserResult',
    'GetAccessPointRootDirectoryResult',
    'GetAccessPointRootDirectoryCreationInfoResult',
    'GetFileSystemLifecyclePolicyResult',
]

@pulumi.output_type
class AccessPointPosixUser(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "secondaryGids":
            suggest = "secondary_gids"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointPosixUser. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointPosixUser.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointPosixUser.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 gid: int,
                 uid: int,
                 secondary_gids: Optional[Sequence[int]] = None):
        """
        :param int gid: POSIX group ID used for all file system operations using this access point.
        :param int uid: POSIX user ID used for all file system operations using this access point.
        :param Sequence[int] secondary_gids: Secondary POSIX group IDs used for all file system operations using this access point.
        """
        AccessPointPosixUser._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            gid=gid,
            uid=uid,
            secondary_gids=secondary_gids,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             gid: Optional[int] = None,
             uid: Optional[int] = None,
             secondary_gids: Optional[Sequence[int]] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if gid is None:
            raise TypeError("Missing 'gid' argument")
        if uid is None:
            raise TypeError("Missing 'uid' argument")
        if secondary_gids is None and 'secondaryGids' in kwargs:
            secondary_gids = kwargs['secondaryGids']

        _setter("gid", gid)
        _setter("uid", uid)
        if secondary_gids is not None:
            _setter("secondary_gids", secondary_gids)

    @property
    @pulumi.getter
    def gid(self) -> int:
        """
        POSIX group ID used for all file system operations using this access point.
        """
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter
    def uid(self) -> int:
        """
        POSIX user ID used for all file system operations using this access point.
        """
        return pulumi.get(self, "uid")

    @property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Optional[Sequence[int]]:
        """
        Secondary POSIX group IDs used for all file system operations using this access point.
        """
        return pulumi.get(self, "secondary_gids")


@pulumi.output_type
class AccessPointRootDirectory(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "creationInfo":
            suggest = "creation_info"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointRootDirectory. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointRootDirectory.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointRootDirectory.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 creation_info: Optional['outputs.AccessPointRootDirectoryCreationInfo'] = None,
                 path: Optional[str] = None):
        """
        :param 'AccessPointRootDirectoryCreationInfoArgs' creation_info: POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
        :param str path: Path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
        """
        AccessPointRootDirectory._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            creation_info=creation_info,
            path=path,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             creation_info: Optional['outputs.AccessPointRootDirectoryCreationInfo'] = None,
             path: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if creation_info is None and 'creationInfo' in kwargs:
            creation_info = kwargs['creationInfo']

        if creation_info is not None:
            _setter("creation_info", creation_info)
        if path is not None:
            _setter("path", path)

    @property
    @pulumi.getter(name="creationInfo")
    def creation_info(self) -> Optional['outputs.AccessPointRootDirectoryCreationInfo']:
        """
        POSIX IDs and permissions to apply to the access point's Root Directory. See Creation Info below.
        """
        return pulumi.get(self, "creation_info")

    @property
    @pulumi.getter
    def path(self) -> Optional[str]:
        """
        Path on the EFS file system to expose as the root directory to NFS clients using the access point to access the EFS file system. A path can have up to four subdirectories. If the specified path does not exist, you are required to provide `creation_info`.
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class AccessPointRootDirectoryCreationInfo(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ownerGid":
            suggest = "owner_gid"
        elif key == "ownerUid":
            suggest = "owner_uid"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPointRootDirectoryCreationInfo. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPointRootDirectoryCreationInfo.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPointRootDirectoryCreationInfo.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 owner_gid: int,
                 owner_uid: int,
                 permissions: str):
        """
        :param int owner_gid: POSIX group ID to apply to the `root_directory`.
        :param int owner_uid: POSIX user ID to apply to the `root_directory`.
        :param str permissions: POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        AccessPointRootDirectoryCreationInfo._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            owner_gid=owner_gid,
            owner_uid=owner_uid,
            permissions=permissions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             owner_gid: Optional[int] = None,
             owner_uid: Optional[int] = None,
             permissions: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if owner_gid is None and 'ownerGid' in kwargs:
            owner_gid = kwargs['ownerGid']
        if owner_gid is None:
            raise TypeError("Missing 'owner_gid' argument")
        if owner_uid is None and 'ownerUid' in kwargs:
            owner_uid = kwargs['ownerUid']
        if owner_uid is None:
            raise TypeError("Missing 'owner_uid' argument")
        if permissions is None:
            raise TypeError("Missing 'permissions' argument")

        _setter("owner_gid", owner_gid)
        _setter("owner_uid", owner_uid)
        _setter("permissions", permissions)

    @property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> int:
        """
        POSIX group ID to apply to the `root_directory`.
        """
        return pulumi.get(self, "owner_gid")

    @property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> int:
        """
        POSIX user ID to apply to the `root_directory`.
        """
        return pulumi.get(self, "owner_uid")

    @property
    @pulumi.getter
    def permissions(self) -> str:
        """
        POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        """
        return pulumi.get(self, "permissions")


@pulumi.output_type
class BackupPolicyBackupPolicy(dict):
    def __init__(__self__, *,
                 status: str):
        """
        :param str status: A status of the backup policy. Valid values: `ENABLED`, `DISABLED`.
        """
        BackupPolicyBackupPolicy._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if status is None:
            raise TypeError("Missing 'status' argument")

        _setter("status", status)

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        A status of the backup policy. Valid values: `ENABLED`, `DISABLED`.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class FileSystemLifecyclePolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "transitionToIa":
            suggest = "transition_to_ia"
        elif key == "transitionToPrimaryStorageClass":
            suggest = "transition_to_primary_storage_class"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FileSystemLifecyclePolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FileSystemLifecyclePolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FileSystemLifecyclePolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 transition_to_ia: Optional[str] = None,
                 transition_to_primary_storage_class: Optional[str] = None):
        """
        :param str transition_to_ia: Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_1_DAY`, `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
        :param str transition_to_primary_storage_class: Describes the policy used to transition a file from infequent access storage to primary storage. Valid values: `AFTER_1_ACCESS`.
        """
        FileSystemLifecyclePolicy._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            transition_to_ia=transition_to_ia,
            transition_to_primary_storage_class=transition_to_primary_storage_class,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             transition_to_ia: Optional[str] = None,
             transition_to_primary_storage_class: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if transition_to_ia is None and 'transitionToIa' in kwargs:
            transition_to_ia = kwargs['transitionToIa']
        if transition_to_primary_storage_class is None and 'transitionToPrimaryStorageClass' in kwargs:
            transition_to_primary_storage_class = kwargs['transitionToPrimaryStorageClass']

        if transition_to_ia is not None:
            _setter("transition_to_ia", transition_to_ia)
        if transition_to_primary_storage_class is not None:
            _setter("transition_to_primary_storage_class", transition_to_primary_storage_class)

    @property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> Optional[str]:
        """
        Indicates how long it takes to transition files to the IA storage class. Valid values: `AFTER_1_DAY`, `AFTER_7_DAYS`, `AFTER_14_DAYS`, `AFTER_30_DAYS`, `AFTER_60_DAYS`, or `AFTER_90_DAYS`.
        """
        return pulumi.get(self, "transition_to_ia")

    @property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(self) -> Optional[str]:
        """
        Describes the policy used to transition a file from infequent access storage to primary storage. Valid values: `AFTER_1_ACCESS`.
        """
        return pulumi.get(self, "transition_to_primary_storage_class")


@pulumi.output_type
class FileSystemSizeInByte(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "valueInIa":
            suggest = "value_in_ia"
        elif key == "valueInStandard":
            suggest = "value_in_standard"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in FileSystemSizeInByte. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        FileSystemSizeInByte.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        FileSystemSizeInByte.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 value: Optional[int] = None,
                 value_in_ia: Optional[int] = None,
                 value_in_standard: Optional[int] = None):
        """
        :param int value: The latest known metered size (in bytes) of data stored in the file system.
        :param int value_in_ia: The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.
        :param int value_in_standard: The latest known metered size (in bytes) of data stored in the Standard storage class.
        """
        FileSystemSizeInByte._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            value=value,
            value_in_ia=value_in_ia,
            value_in_standard=value_in_standard,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             value: Optional[int] = None,
             value_in_ia: Optional[int] = None,
             value_in_standard: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if value_in_ia is None and 'valueInIa' in kwargs:
            value_in_ia = kwargs['valueInIa']
        if value_in_standard is None and 'valueInStandard' in kwargs:
            value_in_standard = kwargs['valueInStandard']

        if value is not None:
            _setter("value", value)
        if value_in_ia is not None:
            _setter("value_in_ia", value_in_ia)
        if value_in_standard is not None:
            _setter("value_in_standard", value_in_standard)

    @property
    @pulumi.getter
    def value(self) -> Optional[int]:
        """
        The latest known metered size (in bytes) of data stored in the file system.
        """
        return pulumi.get(self, "value")

    @property
    @pulumi.getter(name="valueInIa")
    def value_in_ia(self) -> Optional[int]:
        """
        The latest known metered size (in bytes) of data stored in the Infrequent Access storage class.
        """
        return pulumi.get(self, "value_in_ia")

    @property
    @pulumi.getter(name="valueInStandard")
    def value_in_standard(self) -> Optional[int]:
        """
        The latest known metered size (in bytes) of data stored in the Standard storage class.
        """
        return pulumi.get(self, "value_in_standard")


@pulumi.output_type
class ReplicationConfigurationDestination(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "availabilityZoneName":
            suggest = "availability_zone_name"
        elif key == "fileSystemId":
            suggest = "file_system_id"
        elif key == "kmsKeyId":
            suggest = "kms_key_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReplicationConfigurationDestination. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReplicationConfigurationDestination.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReplicationConfigurationDestination.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 availability_zone_name: Optional[str] = None,
                 file_system_id: Optional[str] = None,
                 kms_key_id: Optional[str] = None,
                 region: Optional[str] = None,
                 status: Optional[str] = None):
        """
        :param str availability_zone_name: The availability zone in which the replica should be created. If specified, the replica will be created with One Zone storage. If omitted, regional storage will be used.
        :param str kms_key_id: The Key ID, ARN, alias, or alias ARN of the KMS key that should be used to encrypt the replica file system. If omitted, the default KMS key for EFS `/aws/elasticfilesystem` will be used.
        :param str region: The region in which the replica should be created.
        """
        ReplicationConfigurationDestination._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            availability_zone_name=availability_zone_name,
            file_system_id=file_system_id,
            kms_key_id=kms_key_id,
            region=region,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             availability_zone_name: Optional[str] = None,
             file_system_id: Optional[str] = None,
             kms_key_id: Optional[str] = None,
             region: Optional[str] = None,
             status: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if availability_zone_name is None and 'availabilityZoneName' in kwargs:
            availability_zone_name = kwargs['availabilityZoneName']
        if file_system_id is None and 'fileSystemId' in kwargs:
            file_system_id = kwargs['fileSystemId']
        if kms_key_id is None and 'kmsKeyId' in kwargs:
            kms_key_id = kwargs['kmsKeyId']

        if availability_zone_name is not None:
            _setter("availability_zone_name", availability_zone_name)
        if file_system_id is not None:
            _setter("file_system_id", file_system_id)
        if kms_key_id is not None:
            _setter("kms_key_id", kms_key_id)
        if region is not None:
            _setter("region", region)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="availabilityZoneName")
    def availability_zone_name(self) -> Optional[str]:
        """
        The availability zone in which the replica should be created. If specified, the replica will be created with One Zone storage. If omitted, regional storage will be used.
        """
        return pulumi.get(self, "availability_zone_name")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> Optional[str]:
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        """
        The Key ID, ARN, alias, or alias ARN of the KMS key that should be used to encrypt the replica file system. If omitted, the default KMS key for EFS `/aws/elasticfilesystem` will be used.
        """
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        The region in which the replica should be created.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")


@pulumi.output_type
class GetAccessPointPosixUserResult(dict):
    def __init__(__self__, *,
                 gid: int,
                 secondary_gids: Sequence[int],
                 uid: int):
        """
        :param int gid: Group ID
        :param Sequence[int] secondary_gids: Secondary group IDs
        :param int uid: User Id
        """
        GetAccessPointPosixUserResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            gid=gid,
            secondary_gids=secondary_gids,
            uid=uid,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             gid: Optional[int] = None,
             secondary_gids: Optional[Sequence[int]] = None,
             uid: Optional[int] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if gid is None:
            raise TypeError("Missing 'gid' argument")
        if secondary_gids is None and 'secondaryGids' in kwargs:
            secondary_gids = kwargs['secondaryGids']
        if secondary_gids is None:
            raise TypeError("Missing 'secondary_gids' argument")
        if uid is None:
            raise TypeError("Missing 'uid' argument")

        _setter("gid", gid)
        _setter("secondary_gids", secondary_gids)
        _setter("uid", uid)

    @property
    @pulumi.getter
    def gid(self) -> int:
        """
        Group ID
        """
        return pulumi.get(self, "gid")

    @property
    @pulumi.getter(name="secondaryGids")
    def secondary_gids(self) -> Sequence[int]:
        """
        Secondary group IDs
        """
        return pulumi.get(self, "secondary_gids")

    @property
    @pulumi.getter
    def uid(self) -> int:
        """
        User Id
        """
        return pulumi.get(self, "uid")


@pulumi.output_type
class GetAccessPointRootDirectoryResult(dict):
    def __init__(__self__, *,
                 creation_infos: Sequence['outputs.GetAccessPointRootDirectoryCreationInfoResult'],
                 path: str):
        """
        :param Sequence['GetAccessPointRootDirectoryCreationInfoArgs'] creation_infos: Single element list containing information on the creation permissions of the directory
        :param str path: Path exposed as the root directory
        """
        GetAccessPointRootDirectoryResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            creation_infos=creation_infos,
            path=path,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             creation_infos: Optional[Sequence['outputs.GetAccessPointRootDirectoryCreationInfoResult']] = None,
             path: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if creation_infos is None and 'creationInfos' in kwargs:
            creation_infos = kwargs['creationInfos']
        if creation_infos is None:
            raise TypeError("Missing 'creation_infos' argument")
        if path is None:
            raise TypeError("Missing 'path' argument")

        _setter("creation_infos", creation_infos)
        _setter("path", path)

    @property
    @pulumi.getter(name="creationInfos")
    def creation_infos(self) -> Sequence['outputs.GetAccessPointRootDirectoryCreationInfoResult']:
        """
        Single element list containing information on the creation permissions of the directory
        """
        return pulumi.get(self, "creation_infos")

    @property
    @pulumi.getter
    def path(self) -> str:
        """
        Path exposed as the root directory
        """
        return pulumi.get(self, "path")


@pulumi.output_type
class GetAccessPointRootDirectoryCreationInfoResult(dict):
    def __init__(__self__, *,
                 owner_gid: int,
                 owner_uid: int,
                 permissions: str):
        """
        :param int owner_gid: POSIX owner group ID
        :param int owner_uid: POSIX owner user ID
        :param str permissions: POSIX permissions mode
        """
        GetAccessPointRootDirectoryCreationInfoResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            owner_gid=owner_gid,
            owner_uid=owner_uid,
            permissions=permissions,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             owner_gid: Optional[int] = None,
             owner_uid: Optional[int] = None,
             permissions: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if owner_gid is None and 'ownerGid' in kwargs:
            owner_gid = kwargs['ownerGid']
        if owner_gid is None:
            raise TypeError("Missing 'owner_gid' argument")
        if owner_uid is None and 'ownerUid' in kwargs:
            owner_uid = kwargs['ownerUid']
        if owner_uid is None:
            raise TypeError("Missing 'owner_uid' argument")
        if permissions is None:
            raise TypeError("Missing 'permissions' argument")

        _setter("owner_gid", owner_gid)
        _setter("owner_uid", owner_uid)
        _setter("permissions", permissions)

    @property
    @pulumi.getter(name="ownerGid")
    def owner_gid(self) -> int:
        """
        POSIX owner group ID
        """
        return pulumi.get(self, "owner_gid")

    @property
    @pulumi.getter(name="ownerUid")
    def owner_uid(self) -> int:
        """
        POSIX owner user ID
        """
        return pulumi.get(self, "owner_uid")

    @property
    @pulumi.getter
    def permissions(self) -> str:
        """
        POSIX permissions mode
        """
        return pulumi.get(self, "permissions")


@pulumi.output_type
class GetFileSystemLifecyclePolicyResult(dict):
    def __init__(__self__, *,
                 transition_to_ia: str,
                 transition_to_primary_storage_class: str):
        GetFileSystemLifecyclePolicyResult._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            transition_to_ia=transition_to_ia,
            transition_to_primary_storage_class=transition_to_primary_storage_class,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             transition_to_ia: Optional[str] = None,
             transition_to_primary_storage_class: Optional[str] = None,
             opts: Optional[pulumi.ResourceOptions] = None,
             **kwargs):
        if transition_to_ia is None and 'transitionToIa' in kwargs:
            transition_to_ia = kwargs['transitionToIa']
        if transition_to_ia is None:
            raise TypeError("Missing 'transition_to_ia' argument")
        if transition_to_primary_storage_class is None and 'transitionToPrimaryStorageClass' in kwargs:
            transition_to_primary_storage_class = kwargs['transitionToPrimaryStorageClass']
        if transition_to_primary_storage_class is None:
            raise TypeError("Missing 'transition_to_primary_storage_class' argument")

        _setter("transition_to_ia", transition_to_ia)
        _setter("transition_to_primary_storage_class", transition_to_primary_storage_class)

    @property
    @pulumi.getter(name="transitionToIa")
    def transition_to_ia(self) -> str:
        return pulumi.get(self, "transition_to_ia")

    @property
    @pulumi.getter(name="transitionToPrimaryStorageClass")
    def transition_to_primary_storage_class(self) -> str:
        return pulumi.get(self, "transition_to_primary_storage_class")



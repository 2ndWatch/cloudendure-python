"""
    CloudEndure API documentation

    © 2021 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    The version of the OpenAPI document: 5
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from cloudendure.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


def lazy_import():
    from cloudendure.model.replication_configuration_replication_tags import (
        ReplicationConfigurationReplicationTags,
    )

    globals()[
        "ReplicationConfigurationReplicationTags"
    ] = ReplicationConfigurationReplicationTags


class ReplicationConfiguration(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {}

    validations = {}

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            "volume_encryption_key": (str,),  # noqa: E501
            "replication_tags": (
                [ReplicationConfigurationReplicationTags],
            ),  # noqa: E501
            "disable_public_ip": (bool,),  # noqa: E501
            "subnet_host_project": (str,),  # noqa: E501
            "cost_optimized_burst_balance_delta_threshold": (int,),  # noqa: E501
            "replication_software_download_source": (str,),  # noqa: E501
            "cost_optimized_sc1_volumes_throughput_window_size_minutes": (
                int,
            ),  # noqa: E501
            "replication_server_type": (str,),  # noqa: E501
            "cost_optimized_burst_balance_window_size_minutes": (int,),  # noqa: E501
            "use_low_cost_disks": (bool,),  # noqa: E501
            "compute_location_id": (str,),  # noqa: E501
            "cloud_credentials": (str,),  # noqa: E501
            "subnet_id": (str,),  # noqa: E501
            "logical_location_id": (str,),  # noqa: E501
            "cost_optimized_default_volumes_throughput_window_size_minutes": (
                int,
            ),  # noqa: E501
            "bandwidth_throttling": (int,),  # noqa: E501
            "cost_optimized_burst_balance_threshold": (int,),  # noqa: E501
            "use_dedicated_server": (bool,),  # noqa: E501
            "daily_pit_number": (int,),  # noqa: E501
            "zone": (str,),  # noqa: E501
            "replicator_security_group_ids": ([str],),  # noqa: E501
            "use_private_ip": (bool,),  # noqa: E501
            "region": (str,),  # noqa: E501
            "id": (str,),  # noqa: E501
            "proxy_url": (str,),  # noqa: E501
            "volume_encryption_allowed": (bool,),  # noqa: E501
            "object_storage_location": (str,),  # noqa: E501
            "archiving_enabled": (bool,),  # noqa: E501
            "converter_type": (str,),  # noqa: E501
            "storage_location_id": (str,),  # noqa: E501
            "use_cost_optimized_disk_type": (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None

    attribute_map = {
        "volume_encryption_key": "volumeEncryptionKey",  # noqa: E501
        "replication_tags": "replicationTags",  # noqa: E501
        "disable_public_ip": "disablePublicIp",  # noqa: E501
        "subnet_host_project": "subnetHostProject",  # noqa: E501
        "cost_optimized_burst_balance_delta_threshold": "costOptimizedBurstBalanceDeltaThreshold",  # noqa: E501
        "replication_software_download_source": "replicationSoftwareDownloadSource",  # noqa: E501
        "cost_optimized_sc1_volumes_throughput_window_size_minutes": "costOptimizedSc1VolumesThroughputWindowSizeMinutes",  # noqa: E501
        "replication_server_type": "replicationServerType",  # noqa: E501
        "cost_optimized_burst_balance_window_size_minutes": "costOptimizedBurstBalanceWindowSizeMinutes",  # noqa: E501
        "use_low_cost_disks": "useLowCostDisks",  # noqa: E501
        "compute_location_id": "computeLocationId",  # noqa: E501
        "cloud_credentials": "cloudCredentials",  # noqa: E501
        "subnet_id": "subnetId",  # noqa: E501
        "logical_location_id": "logicalLocationId",  # noqa: E501
        "cost_optimized_default_volumes_throughput_window_size_minutes": "costOptimizedDefaultVolumesThroughputWindowSizeMinutes",  # noqa: E501
        "bandwidth_throttling": "bandwidthThrottling",  # noqa: E501
        "cost_optimized_burst_balance_threshold": "costOptimizedBurstBalanceThreshold",  # noqa: E501
        "use_dedicated_server": "useDedicatedServer",  # noqa: E501
        "daily_pit_number": "dailyPitNumber",  # noqa: E501
        "zone": "zone",  # noqa: E501
        "replicator_security_group_ids": "replicatorSecurityGroupIDs",  # noqa: E501
        "use_private_ip": "usePrivateIp",  # noqa: E501
        "region": "region",  # noqa: E501
        "id": "id",  # noqa: E501
        "proxy_url": "proxyUrl",  # noqa: E501
        "volume_encryption_allowed": "volumeEncryptionAllowed",  # noqa: E501
        "object_storage_location": "objectStorageLocation",  # noqa: E501
        "archiving_enabled": "archivingEnabled",  # noqa: E501
        "converter_type": "converterType",  # noqa: E501
        "storage_location_id": "storageLocationId",  # noqa: E501
        "use_cost_optimized_disk_type": "useCostOptimizedDiskType",  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set(
        [
            "_data_store",
            "_check_type",
            "_spec_property_naming",
            "_path_to_item",
            "_configuration",
            "_visited_composed_classes",
        ]
    )

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ReplicationConfiguration - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            volume_encryption_key (str): AWS only. ARN to private key for Volume Encryption. Possible values can be fetched from the Region object.. [optional]  # noqa: E501
            replication_tags ([ReplicationConfigurationReplicationTags]): AWS only. Tags that will be applied to every cloud resource created in the CloudEndure Staging Area.. [optional]  # noqa: E501
            disable_public_ip (bool): When private IP is used, do not allocate public IP for replication server. [optional]  # noqa: E501
            subnet_host_project (str): GCP only. Host project of cross project network subnet.. [optional]  # noqa: E501
            cost_optimized_burst_balance_delta_threshold (int): when using cost optimized disk type, threshold of delta between measurments to move to default. [optional]  # noqa: E501
            replication_software_download_source (str): [optional]  # noqa: E501
            cost_optimized_sc1_volumes_throughput_window_size_minutes (int): when using cost optimized disk type, size of window for sc1 volumes througput measurments. [optional]  # noqa: E501
            replication_server_type (str): [optional]  # noqa: E501
            cost_optimized_burst_balance_window_size_minutes (int): when using cost optimized disk type, size of window for burst balance measurments. [optional]  # noqa: E501
            use_low_cost_disks (bool): use low cost disks for replication whenever possible. [optional]  # noqa: E501
            compute_location_id (str): [optional]  # noqa: E501
            cloud_credentials (str): The ID for the cloudCredentials object containing the credentials to be used for accessing the target cloud.. [optional]  # noqa: E501
            subnet_id (str): Subnet where replication servers will be created. Possible values can be fetched from the Region object.. [optional]  # noqa: E501
            logical_location_id (str): vcenter = vmFolder. [optional]  # noqa: E501
            cost_optimized_default_volumes_throughput_window_size_minutes (int): when using cost optimized disk type, size of window for default volumes througput measurments. [optional]  # noqa: E501
            bandwidth_throttling (int): Mbps to use for Data Replication (zero means no throttling).. [optional]  # noqa: E501
            cost_optimized_burst_balance_threshold (int): when using cost optimized disk type, threshold of burst balance under which to move to default. [optional]  # noqa: E501
            use_dedicated_server (bool): [optional]  # noqa: E501
            daily_pit_number (int): Number of days to Keep PIT snapshots. [optional]  # noqa: E501
            zone (str): Relevant for GCP and Azure ARM. The Zone to replicate into.. [optional]  # noqa: E501
            replicator_security_group_ids ([str]): AWS only. The security groups that will be applied to the replication servers. Possible values can be fetched from the Region object.. [optional]  # noqa: E501
            use_private_ip (bool): Should the CloudEndure agent access the replication server using its private IP address.. [optional]  # noqa: E501
            region (str): [optional]  # noqa: E501
            id (str): [optional]  # noqa: E501
            proxy_url (str): The full URI for a proxy (schema, username, password, domain, port) if required for the CloudEndure agent.. [optional]  # noqa: E501
            volume_encryption_allowed (bool): [optional]  # noqa: E501
            object_storage_location (str): bucket in aws . [optional]  # noqa: E501
            archiving_enabled (bool): [optional]  # noqa: E501
            converter_type (str): [optional]  # noqa: E501
            storage_location_id (str): [optional]  # noqa: E501
            use_cost_optimized_disk_type (bool): use cost optimized disk type for replication. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop("_check_type", True)
        _spec_property_naming = kwargs.pop("_spec_property_naming", False)
        _path_to_item = kwargs.pop("_path_to_item", ())
        _configuration = kwargs.pop("_configuration", None)
        _visited_composed_classes = kwargs.pop("_visited_composed_classes", ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments."
                % (args, self.__class__.__name__,),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if (
                var_name not in self.attribute_map
                and self._configuration is not None
                and self._configuration.discard_unknown_keys
                and self.additional_properties_type is None
            ):
                # discard variable.
                continue
            setattr(self, var_name, var_value)
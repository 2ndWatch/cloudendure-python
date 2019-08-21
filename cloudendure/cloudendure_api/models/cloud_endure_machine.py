# coding: utf-8

"""
    CloudEndure API documentation

    © 2017 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    OpenAPI spec version: 5
    Contact: https://bit.ly/2T54hSc
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

from cloudendure.cloudendure_api.models.cloud_endure_machine_replication_configuration import (  # noqa: F401,E501
    CloudEndureMachineReplicationConfiguration
)
from cloudendure.cloudendure_api.models.cloud_endure_point_in_time import (
    CloudEndurePointInTime
)  # noqa: F401,E501


class CloudEndureMachine:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "source_properties": "object",
        "replication_info": "object",
        "license": "object",
        "tags": "list[str]",
        "restore_servers": "list[str]",
        "from_point_in_time": "CloudEndurePointInTime",
        "replication_status": "str",
        "replica": "str",
        "id": "str",
        "replication_configuration": "CloudEndureMachineReplicationConfiguration",
        "life_cycle": "object",
        "is_agent_installed": "bool",
    }

    attribute_map = {
        "source_properties": "sourceProperties",
        "replication_info": "replicationInfo",
        "license": "license",
        "tags": "tags",
        "restore_servers": "restoreServers",
        "from_point_in_time": "fromPointInTime",
        "replication_status": "replicationStatus",
        "replica": "replica",
        "id": "id",
        "replication_configuration": "replicationConfiguration",
        "life_cycle": "lifeCycle",
        "is_agent_installed": "isAgentInstalled",
    }

    def __init__(
        self,
        source_properties=None,
        replication_info=None,
        license=None,
        tags=None,
        restore_servers=None,
        from_point_in_time=None,
        replication_status=None,
        replica=None,
        id=None,
        replication_configuration=None,
        life_cycle=None,
        is_agent_installed=None,
    ):  # noqa: E501
        """CloudEndureMachine - a model defined in Swagger"""  # noqa: E501
        self._source_properties = None
        self._replication_info = None
        self._license = None
        self._tags = None
        self._restore_servers = None
        self._from_point_in_time = None
        self._replication_status = None
        self._replica = None
        self._id = None
        self._replication_configuration = None
        self._life_cycle = None
        self._is_agent_installed = None
        self.discriminator = None
        if source_properties is not None:
            self.source_properties = source_properties
        if replication_info is not None:
            self.replication_info = replication_info
        if license is not None:
            self.license = license
        if tags is not None:
            self.tags = tags
        if restore_servers is not None:
            self.restore_servers = restore_servers
        if from_point_in_time is not None:
            self.from_point_in_time = from_point_in_time
        if replication_status is not None:
            self.replication_status = replication_status
        if replica is not None:
            self.replica = replica
        if id is not None:
            self.id = id
        if replication_configuration is not None:
            self.replication_configuration = replication_configuration
        if life_cycle is not None:
            self.life_cycle = life_cycle
        if is_agent_installed is not None:
            self.is_agent_installed = is_agent_installed

    @property
    def source_properties(self):
        """Gets the source_properties of this CloudEndureMachine.  # noqa: E501

        Source machine properties.  # noqa: E501

        :return: The source_properties of this CloudEndureMachine.  # noqa: E501
        :rtype: object
        """
        return self._source_properties

    @source_properties.setter
    def source_properties(self, source_properties):
        """Sets the source_properties of this CloudEndureMachine.

        Source machine properties.  # noqa: E501

        :param source_properties: The source_properties of this CloudEndureMachine.  # noqa: E501
        :type: object
        """

        self._source_properties = source_properties

    @property
    def replication_info(self):
        """Gets the replication_info of this CloudEndureMachine.  # noqa: E501

        Detailed information on the state of replication.  # noqa: E501

        :return: The replication_info of this CloudEndureMachine.  # noqa: E501
        :rtype: object
        """
        return self._replication_info

    @replication_info.setter
    def replication_info(self, replication_info):
        """Sets the replication_info of this CloudEndureMachine.

        Detailed information on the state of replication.  # noqa: E501

        :param replication_info: The replication_info of this CloudEndureMachine.  # noqa: E501
        :type: object
        """

        self._replication_info = replication_info

    @property
    def license(self):
        """Gets the license of this CloudEndureMachine.  # noqa: E501

        Detailed machine license consumption information.  # noqa: E501

        :return: The license of this CloudEndureMachine.  # noqa: E501
        :rtype: object
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this CloudEndureMachine.

        Detailed machine license consumption information.  # noqa: E501

        :param license: The license of this CloudEndureMachine.  # noqa: E501
        :type: object
        """

        self._license = license

    @property
    def tags(self):
        """Gets the tags of this CloudEndureMachine.  # noqa: E501


        :return: The tags of this CloudEndureMachine.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this CloudEndureMachine.


        :param tags: The tags of this CloudEndureMachine.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def restore_servers(self):
        """Gets the restore_servers of this CloudEndureMachine.  # noqa: E501

        todo restoreServer ids  # noqa: E501

        :return: The restore_servers of this CloudEndureMachine.  # noqa: E501
        :rtype: list[str]
        """
        return self._restore_servers

    @restore_servers.setter
    def restore_servers(self, restore_servers):
        """Sets the restore_servers of this CloudEndureMachine.

        todo restoreServer ids  # noqa: E501

        :param restore_servers: The restore_servers of this CloudEndureMachine.  # noqa: E501
        :type: list[str]
        """

        self._restore_servers = restore_servers

    @property
    def from_point_in_time(self):
        """Gets the from_point_in_time of this CloudEndureMachine.  # noqa: E501


        :return: The from_point_in_time of this CloudEndureMachine.  # noqa: E501
        :rtype: CloudEndurePointInTime
        """
        return self._from_point_in_time

    @from_point_in_time.setter
    def from_point_in_time(self, from_point_in_time):
        """Sets the from_point_in_time of this CloudEndureMachine.


        :param from_point_in_time: The from_point_in_time of this CloudEndureMachine.  # noqa: E501
        :type: CloudEndurePointInTime
        """

        self._from_point_in_time = from_point_in_time

    @property
    def replication_status(self):
        """Gets the replication_status of this CloudEndureMachine.  # noqa: E501

        Is replication started, paused or stopped  # noqa: E501

        :return: The replication_status of this CloudEndureMachine.  # noqa: E501
        :rtype: str
        """
        return self._replication_status

    @replication_status.setter
    def replication_status(self, replication_status):
        """Sets the replication_status of this CloudEndureMachine.

        Is replication started, paused or stopped  # noqa: E501

        :param replication_status: The replication_status of this CloudEndureMachine.  # noqa: E501
        :type: str
        """
        allowed_values = ["STOPPED", "PAUSED", "STARTED"]  # noqa: E501
        if replication_status not in allowed_values:
            raise ValueError(
                "Invalid value for `replication_status` ({0}), must be one of {1}".format(  # noqa: E501
                    replication_status, allowed_values
                )
            )

        self._replication_status = replication_status

    @property
    def replica(self):
        """Gets the replica of this CloudEndureMachine.  # noqa: E501

        The ID of the target machine that has been previously launched, if such exists.  # noqa: E501

        :return: The replica of this CloudEndureMachine.  # noqa: E501
        :rtype: str
        """
        return self._replica

    @replica.setter
    def replica(self, replica):
        """Sets the replica of this CloudEndureMachine.

        The ID of the target machine that has been previously launched, if such exists.  # noqa: E501

        :param replica: The replica of this CloudEndureMachine.  # noqa: E501
        :type: str
        """

        self._replica = replica

    @property
    def id(self):
        """Gets the id of this CloudEndureMachine.  # noqa: E501


        :return: The id of this CloudEndureMachine.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureMachine.


        :param id: The id of this CloudEndureMachine.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def replication_configuration(self):
        """Gets the replication_configuration of this CloudEndureMachine.  # noqa: E501


        :return: The replication_configuration of this CloudEndureMachine.  # noqa: E501
        :rtype: CloudEndureMachineReplicationConfiguration
        """
        return self._replication_configuration

    @replication_configuration.setter
    def replication_configuration(self, replication_configuration):
        """Sets the replication_configuration of this CloudEndureMachine.


        :param replication_configuration: The replication_configuration of this CloudEndureMachine.  # noqa: E501
        :type: CloudEndureMachineReplicationConfiguration
        """

        self._replication_configuration = replication_configuration

    @property
    def life_cycle(self):
        """Gets the life_cycle of this CloudEndureMachine.  # noqa: E501

        Detailed machine lifecycle information.  # noqa: E501

        :return: The life_cycle of this CloudEndureMachine.  # noqa: E501
        :rtype: object
        """
        return self._life_cycle

    @life_cycle.setter
    def life_cycle(self, life_cycle):
        """Sets the life_cycle of this CloudEndureMachine.

        Detailed machine lifecycle information.  # noqa: E501

        :param life_cycle: The life_cycle of this CloudEndureMachine.  # noqa: E501
        :type: object
        """

        self._life_cycle = life_cycle

    @property
    def is_agent_installed(self):
        """Gets the is_agent_installed of this CloudEndureMachine.  # noqa: E501

        Whether a CloudEndure agent is currently installed on this machine.  # noqa: E501

        :return: The is_agent_installed of this CloudEndureMachine.  # noqa: E501
        :rtype: bool
        """
        return self._is_agent_installed

    @is_agent_installed.setter
    def is_agent_installed(self, is_agent_installed):
        """Sets the is_agent_installed of this CloudEndureMachine.

        Whether a CloudEndure agent is currently installed on this machine.  # noqa: E501

        :param is_agent_installed: The is_agent_installed of this CloudEndureMachine.  # noqa: E501
        :type: bool
        """

        self._is_agent_installed = is_agent_installed

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(CloudEndureMachine, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CloudEndureMachine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
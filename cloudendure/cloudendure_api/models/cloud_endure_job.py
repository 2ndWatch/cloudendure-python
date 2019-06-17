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


class CloudEndureJob:
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
        "status": "str",
        "participating_machines": "list[str]",
        "log": "list[object]",
        "type": "str",
        "end_date_time": "datetime",
        "creation_date_time": "datetime",
        "id": "str",
        "initiated_by": "str",
    }

    attribute_map = {
        "status": "status",
        "participating_machines": "participatingMachines",
        "log": "log",
        "type": "type",
        "end_date_time": "endDateTime",
        "creation_date_time": "creationDateTime",
        "id": "id",
        "initiated_by": "initiatedBy",
    }

    def __init__(
        self,
        status=None,
        participating_machines=None,
        log=None,
        type=None,
        end_date_time=None,
        creation_date_time=None,
        id=None,
        initiated_by=None,
    ):  # noqa: E501
        """CloudEndureJob - a model defined in Swagger"""  # noqa: E501
        self._status = None
        self._participating_machines = None
        self._log = None
        self._type = None
        self._end_date_time = None
        self._creation_date_time = None
        self._id = None
        self._initiated_by = None
        self.discriminator = None
        if status is not None:
            self.status = status
        if participating_machines is not None:
            self.participating_machines = participating_machines
        if log is not None:
            self.log = log
        if type is not None:
            self.type = type
        if end_date_time is not None:
            self.end_date_time = end_date_time
        if creation_date_time is not None:
            self.creation_date_time = creation_date_time
        if id is not None:
            self.id = id
        if initiated_by is not None:
            self.initiated_by = initiated_by

    @property
    def status(self):
        """Gets the status of this CloudEndureJob.  # noqa: E501


        :return: The status of this CloudEndureJob.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CloudEndureJob.


        :param status: The status of this CloudEndureJob.  # noqa: E501
        :type: str
        """
        allowed_values = ["PENDING", "STARTED", "COMPLETED", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}".format(  # noqa: E501
                    status, allowed_values
                )
            )

        self._status = status

    @property
    def participating_machines(self):
        """Gets the participating_machines of this CloudEndureJob.  # noqa: E501


        :return: The participating_machines of this CloudEndureJob.  # noqa: E501
        :rtype: list[str]
        """
        return self._participating_machines

    @participating_machines.setter
    def participating_machines(self, participating_machines):
        """Sets the participating_machines of this CloudEndureJob.


        :param participating_machines: The participating_machines of this CloudEndureJob.  # noqa: E501
        :type: list[str]
        """

        self._participating_machines = participating_machines

    @property
    def log(self):
        """Gets the log of this CloudEndureJob.  # noqa: E501


        :return: The log of this CloudEndureJob.  # noqa: E501
        :rtype: list[object]
        """
        return self._log

    @log.setter
    def log(self, log):
        """Sets the log of this CloudEndureJob.


        :param log: The log of this CloudEndureJob.  # noqa: E501
        :type: list[object]
        """

        self._log = log

    @property
    def type(self):
        """Gets the type of this CloudEndureJob.  # noqa: E501

        todo explian that cleanup is also for restore servers  # noqa: E501

        :return: The type of this CloudEndureJob.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CloudEndureJob.

        todo explian that cleanup is also for restore servers  # noqa: E501

        :param type: The type of this CloudEndureJob.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "CLEANUP",
            "CUTOVER_LAUNCH",
            "RECOVERY_LAUNCH",
            "RESTORE_LAUNCH",
            "TEST_LAUNCH",
            "CONSOLIDATE_VMDKS",
            "FILE_RESTORE",
            "RECOVERY_PLAN_RECOVERY",
            "RECOVERY_PLAN_TEST",
            "RECOVERY_PLAN_CUTOVER",
            "RECOVERY_PLAN_CLEANUP",
        ]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}".format(  # noqa: E501
                    type, allowed_values
                )
            )

        self._type = type

    @property
    def end_date_time(self):
        """Gets the end_date_time of this CloudEndureJob.  # noqa: E501


        :return: The end_date_time of this CloudEndureJob.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this CloudEndureJob.


        :param end_date_time: The end_date_time of this CloudEndureJob.  # noqa: E501
        :type: datetime
        """

        self._end_date_time = end_date_time

    @property
    def creation_date_time(self):
        """Gets the creation_date_time of this CloudEndureJob.  # noqa: E501


        :return: The creation_date_time of this CloudEndureJob.  # noqa: E501
        :rtype: datetime
        """
        return self._creation_date_time

    @creation_date_time.setter
    def creation_date_time(self, creation_date_time):
        """Sets the creation_date_time of this CloudEndureJob.


        :param creation_date_time: The creation_date_time of this CloudEndureJob.  # noqa: E501
        :type: datetime
        """

        self._creation_date_time = creation_date_time

    @property
    def id(self):
        """Gets the id of this CloudEndureJob.  # noqa: E501


        :return: The id of this CloudEndureJob.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CloudEndureJob.


        :param id: The id of this CloudEndureJob.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def initiated_by(self):
        """Gets the initiated_by of this CloudEndureJob.  # noqa: E501

        username of user who initiated the job  # noqa: E501

        :return: The initiated_by of this CloudEndureJob.  # noqa: E501
        :rtype: str
        """
        return self._initiated_by

    @initiated_by.setter
    def initiated_by(self, initiated_by):
        """Sets the initiated_by of this CloudEndureJob.

        username of user who initiated the job  # noqa: E501

        :param initiated_by: The initiated_by of this CloudEndureJob.  # noqa: E501
        :type: str
        """

        self._initiated_by = initiated_by

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
        if issubclass(CloudEndureJob, dict):
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
        if not isinstance(other, CloudEndureJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
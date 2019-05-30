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


class CloudEndureLicenseFeatures:
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
        'pit': 'bool',
        'dr_tier2': 'bool'
    }

    attribute_map = {
        'pit': 'pit',
        'dr_tier2': 'drTier2'
    }

    def __init__(self, pit=None, dr_tier2=None):  # noqa: E501
        """CloudEndureLicenseFeatures - a model defined in Swagger"""  # noqa: E501
        self._pit = None
        self._dr_tier2 = None
        self.discriminator = None
        if pit is not None:
            self.pit = pit
        if dr_tier2 is not None:
            self.dr_tier2 = dr_tier2

    @property
    def pit(self):
        """Gets the pit of this CloudEndureLicenseFeatures.  # noqa: E501


        :return: The pit of this CloudEndureLicenseFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._pit

    @pit.setter
    def pit(self, pit):
        """Sets the pit of this CloudEndureLicenseFeatures.


        :param pit: The pit of this CloudEndureLicenseFeatures.  # noqa: E501
        :type: bool
        """

        self._pit = pit

    @property
    def dr_tier2(self):
        """Gets the dr_tier2 of this CloudEndureLicenseFeatures.  # noqa: E501


        :return: The dr_tier2 of this CloudEndureLicenseFeatures.  # noqa: E501
        :rtype: bool
        """
        return self._dr_tier2

    @dr_tier2.setter
    def dr_tier2(self, dr_tier2):
        """Sets the dr_tier2 of this CloudEndureLicenseFeatures.


        :param dr_tier2: The dr_tier2 of this CloudEndureLicenseFeatures.  # noqa: E501
        :type: bool
        """

        self._dr_tier2 = dr_tier2

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CloudEndureLicenseFeatures, dict):
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
        if not isinstance(other, CloudEndureLicenseFeatures):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

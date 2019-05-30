# coding: utf-8

"""
    CloudEndure API documentation

    © 2017 CloudEndure All rights reserved  # General Request authentication in CloudEndure's API is done using session cookies. A session cookie is returned upon successful execution of the \"login\" method. This value must then be provided within the request headers of all subsequent API requests.  ## Errors Some errors are not specifically written in every method since they may always return. Those are: 1) 401 (Unauthorized) - for unauthenticated requests. 2) 405 (Method Not Allowed) - for using a method that is not supported (POST instead of GET). 3) 403 (Forbidden) - request is authenticated, but the user is not allowed to access. 4) 422 (Unprocessable Entity) - for invalid input.  ## Formats All strings with date-time format are according to RFC3339.  All strings with \"duration\" format are according to ISO8601. For example, a full day duration can be specified with \"PNNNND\".   # noqa: E501

    OpenAPI spec version: 5
    Contact: https://bit.ly/2T54hSc
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from cloudendure.cloudendure_api.api_client import ApiClient


class ReplicationApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def projects_project_id_machines_machine_id_bandwidth_throttling_get(self, project_id, machine_id, **kwargs):  # noqa: E501
        """Get value of network bandwidth throttling setting for Machine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_bandwidth_throttling_get(project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str machine_id: (required)
        :return: CloudEndureBandwidthThrottling
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_machines_machine_id_bandwidth_throttling_get_with_http_info(project_id, machine_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_machines_machine_id_bandwidth_throttling_get_with_http_info(project_id, machine_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_machines_machine_id_bandwidth_throttling_get_with_http_info(self, project_id, machine_id, **kwargs):  # noqa: E501
        """Get value of network bandwidth throttling setting for Machine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_bandwidth_throttling_get_with_http_info(project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str machine_id: (required)
        :return: CloudEndureBandwidthThrottling
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'machine_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_machines_machine_id_bandwidth_throttling_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_machines_machine_id_bandwidth_throttling_get`")  # noqa: E501
        # verify the required parameter 'machine_id' is set
        if ('machine_id' not in params or
                params['machine_id'] is None):
            raise ValueError("Missing the required parameter `machine_id` when calling `projects_project_id_machines_machine_id_bandwidth_throttling_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'machine_id' in params:
            path_params['machineId'] = params['machine_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/machines/{machineId}/bandwidthThrottling', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureBandwidthThrottling',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_machines_machine_id_bandwidth_throttling_patch(self, body, project_id, machine_id, **kwargs):  # noqa: E501
        """Set value of network bandwidth throttling setting for Machine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_bandwidth_throttling_patch(body, project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureBandwidthThrottling body: (required)
        :param str project_id: (required)
        :param str machine_id: (required)
        :return: CloudEndureBandwidthThrottling
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_machines_machine_id_bandwidth_throttling_patch_with_http_info(body, project_id, machine_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_machines_machine_id_bandwidth_throttling_patch_with_http_info(body, project_id, machine_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_machines_machine_id_bandwidth_throttling_patch_with_http_info(self, body, project_id, machine_id, **kwargs):  # noqa: E501
        """Set value of network bandwidth throttling setting for Machine  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_bandwidth_throttling_patch_with_http_info(body, project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureBandwidthThrottling body: (required)
        :param str project_id: (required)
        :param str machine_id: (required)
        :return: CloudEndureBandwidthThrottling
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'machine_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_machines_machine_id_bandwidth_throttling_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `projects_project_id_machines_machine_id_bandwidth_throttling_patch`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_machines_machine_id_bandwidth_throttling_patch`")  # noqa: E501
        # verify the required parameter 'machine_id' is set
        if ('machine_id' not in params or
                params['machine_id'] is None):
            raise ValueError("Missing the required parameter `machine_id` when calling `projects_project_id_machines_machine_id_bandwidth_throttling_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'machine_id' in params:
            path_params['machineId'] = params['machine_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/machines/{machineId}/bandwidthThrottling', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureBandwidthThrottling',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_machines_machine_id_delete(self, project_id, machine_id, **kwargs):  # noqa: E501
        """Uninstall agent  # noqa: E501

        Stops replication and removes the cloudendure agent from this machine. All cloud artifacts associated with those machines with the exception of launched target machine are deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_delete(project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str machine_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_machines_machine_id_delete_with_http_info(project_id, machine_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_machines_machine_id_delete_with_http_info(project_id, machine_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_machines_machine_id_delete_with_http_info(self, project_id, machine_id, **kwargs):  # noqa: E501
        """Uninstall agent  # noqa: E501

        Stops replication and removes the cloudendure agent from this machine. All cloud artifacts associated with those machines with the exception of launched target machine are deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_delete_with_http_info(project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str machine_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'machine_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_machines_machine_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_machines_machine_id_delete`")  # noqa: E501
        # verify the required parameter 'machine_id' is set
        if ('machine_id' not in params or
                params['machine_id'] is None):
            raise ValueError("Missing the required parameter `machine_id` when calling `projects_project_id_machines_machine_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'machine_id' in params:
            path_params['machineId'] = params['machine_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/machines/{machineId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_machines_machine_id_pointsintime_get(self, project_id, machine_id, **kwargs):  # noqa: E501
        """List Available Points-in-time  # noqa: E501

        Returns the list of available recovery points for this machine.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_pointsintime_get(project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str machine_id: (required)
        :param int offset: With which item to start (0 based).
        :param int limit: A number specifying how many entries to return.
        :return: CloudEndurePointInTimeList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_machines_machine_id_pointsintime_get_with_http_info(project_id, machine_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_machines_machine_id_pointsintime_get_with_http_info(project_id, machine_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_machines_machine_id_pointsintime_get_with_http_info(self, project_id, machine_id, **kwargs):  # noqa: E501
        """List Available Points-in-time  # noqa: E501

        Returns the list of available recovery points for this machine.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_machines_machine_id_pointsintime_get_with_http_info(project_id, machine_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str machine_id: (required)
        :param int offset: With which item to start (0 based).
        :param int limit: A number specifying how many entries to return.
        :return: CloudEndurePointInTimeList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'machine_id', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_machines_machine_id_pointsintime_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_machines_machine_id_pointsintime_get`")  # noqa: E501
        # verify the required parameter 'machine_id' is set
        if ('machine_id' not in params or
                params['machine_id'] is None):
            raise ValueError("Missing the required parameter `machine_id` when calling `projects_project_id_machines_machine_id_pointsintime_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'machine_id' in params:
            path_params['machineId'] = params['machine_id']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/machines/{machineId}/pointsintime', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndurePointInTimeList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_replication_configurations_get(self, project_id, **kwargs):  # noqa: E501
        """List Replication Configurations  # noqa: E501

        Returns the list of replication configuration objects defined in this project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_replication_configurations_get(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param int offset: With which item to start (0 based).
        :param int limit: A number specifying how many entries to return.
        :return: CloudEndureReplicationConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_replication_configurations_get_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_replication_configurations_get_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_replication_configurations_get_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """List Replication Configurations  # noqa: E501

        Returns the list of replication configuration objects defined in this project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_replication_configurations_get_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param int offset: With which item to start (0 based).
        :param int limit: A number specifying how many entries to return.
        :return: CloudEndureReplicationConfigurationList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_replication_configurations_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_replication_configurations_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/replicationConfigurations', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureReplicationConfigurationList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_replication_configurations_post(self, body, project_id, **kwargs):  # noqa: E501
        """Create Replication Configuration  # noqa: E501

        Control Data Replication parameters such as target cloud credentials, Staging Area and replication network configuration. A single configuration can exist per target region. Returns the newly created object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_replication_configurations_post(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureReplicationConfiguration body: (required)
        :param str project_id: (required)
        :return: CloudEndureReplicationConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_replication_configurations_post_with_http_info(body, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_replication_configurations_post_with_http_info(body, project_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_replication_configurations_post_with_http_info(self, body, project_id, **kwargs):  # noqa: E501
        """Create Replication Configuration  # noqa: E501

        Control Data Replication parameters such as target cloud credentials, Staging Area and replication network configuration. A single configuration can exist per target region. Returns the newly created object.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_replication_configurations_post_with_http_info(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureReplicationConfiguration body: (required)
        :param str project_id: (required)
        :return: CloudEndureReplicationConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_replication_configurations_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `projects_project_id_replication_configurations_post`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_replication_configurations_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/replicationConfigurations', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureReplicationConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_replication_configurations_replication_configuration_id_patch(self, body, project_id, replication_configuration_id, **kwargs):  # noqa: E501
        """Modify Replication Configuration  # noqa: E501

        Modifying volumeEncryptionKey or modifying cloudCredentials to ones matching a different cloud account will result in replication restarting from initial sync. Returns the modified object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_replication_configurations_replication_configuration_id_patch(body, project_id, replication_configuration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureReplicationConfiguration body: (required)
        :param str project_id: (required)
        :param str replication_configuration_id: (required)
        :return: CloudEndureReplicationConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_replication_configurations_replication_configuration_id_patch_with_http_info(body, project_id, replication_configuration_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_replication_configurations_replication_configuration_id_patch_with_http_info(body, project_id, replication_configuration_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_replication_configurations_replication_configuration_id_patch_with_http_info(self, body, project_id, replication_configuration_id, **kwargs):  # noqa: E501
        """Modify Replication Configuration  # noqa: E501

        Modifying volumeEncryptionKey or modifying cloudCredentials to ones matching a different cloud account will result in replication restarting from initial sync. Returns the modified object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_replication_configurations_replication_configuration_id_patch_with_http_info(body, project_id, replication_configuration_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureReplicationConfiguration body: (required)
        :param str project_id: (required)
        :param str replication_configuration_id: (required)
        :return: CloudEndureReplicationConfiguration
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'replication_configuration_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_replication_configurations_replication_configuration_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `projects_project_id_replication_configurations_replication_configuration_id_patch`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_replication_configurations_replication_configuration_id_patch`")  # noqa: E501
        # verify the required parameter 'replication_configuration_id' is set
        if ('replication_configuration_id' not in params or
                params['replication_configuration_id'] is None):
            raise ValueError("Missing the required parameter `replication_configuration_id` when calling `projects_project_id_replication_configurations_replication_configuration_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'replication_configuration_id' in params:
            path_params['replicationConfigurationId'] = params['replication_configuration_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectId}/replicationConfigurations/{replicationConfigurationId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureReplicationConfiguration',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

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


class BlueprintApi:
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def projects_project_id_blueprints_blueprint_id_get(self, project_id, blueprint_id, **kwargs):  # noqa: E501
        """Get Blueprint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_blueprint_id_get(project_id, blueprint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str blueprint_id: (required)
        :return: CloudEndureBlueprint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_blueprints_blueprint_id_get_with_http_info(project_id, blueprint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_blueprints_blueprint_id_get_with_http_info(project_id, blueprint_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_blueprints_blueprint_id_get_with_http_info(self, project_id, blueprint_id, **kwargs):  # noqa: E501
        """Get Blueprint  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_blueprint_id_get_with_http_info(project_id, blueprint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param str blueprint_id: (required)
        :return: CloudEndureBlueprint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_id', 'blueprint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_blueprints_blueprint_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_blueprints_blueprint_id_get`")  # noqa: E501
        # verify the required parameter 'blueprint_id' is set
        if ('blueprint_id' not in params or
                params['blueprint_id'] is None):
            raise ValueError("Missing the required parameter `blueprint_id` when calling `projects_project_id_blueprints_blueprint_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'blueprint_id' in params:
            path_params['blueprintId'] = params['blueprint_id']  # noqa: E501

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
            '/projects/{projectId}/blueprints/{blueprintId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureBlueprint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_blueprints_blueprint_id_patch(self, body, project_id, blueprint_id, **kwargs):  # noqa: E501
        """Configure Blueprint  # noqa: E501

        Configure target machine characteristics: machine and disk types, network configuration, etc. Returns the modified object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_blueprint_id_patch(body, project_id, blueprint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureBlueprint body: (required)
        :param str project_id: (required)
        :param str blueprint_id: (required)
        :return: CloudEndureBlueprint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_blueprints_blueprint_id_patch_with_http_info(body, project_id, blueprint_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_blueprints_blueprint_id_patch_with_http_info(body, project_id, blueprint_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_blueprints_blueprint_id_patch_with_http_info(self, body, project_id, blueprint_id, **kwargs):  # noqa: E501
        """Configure Blueprint  # noqa: E501

        Configure target machine characteristics: machine and disk types, network configuration, etc. Returns the modified object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_blueprint_id_patch_with_http_info(body, project_id, blueprint_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureBlueprint body: (required)
        :param str project_id: (required)
        :param str blueprint_id: (required)
        :return: CloudEndureBlueprint
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'project_id', 'blueprint_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method projects_project_id_blueprints_blueprint_id_patch" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `projects_project_id_blueprints_blueprint_id_patch`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_blueprints_blueprint_id_patch`")  # noqa: E501
        # verify the required parameter 'blueprint_id' is set
        if ('blueprint_id' not in params or
                params['blueprint_id'] is None):
            raise ValueError("Missing the required parameter `blueprint_id` when calling `projects_project_id_blueprints_blueprint_id_patch`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_id' in params:
            path_params['projectId'] = params['project_id']  # noqa: E501
        if 'blueprint_id' in params:
            path_params['blueprintId'] = params['blueprint_id']  # noqa: E501

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
            '/projects/{projectId}/blueprints/{blueprintId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureBlueprint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_blueprints_get(self, project_id, **kwargs):  # noqa: E501
        """List Blueprints  # noqa: E501

        Returns the list of available blueprints in the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_get(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param int offset: With which item to start (0 based).
        :param int limit: A number specifying how many entries to return.
        :return: CloudEndureBlueprintList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_blueprints_get_with_http_info(project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_blueprints_get_with_http_info(project_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_blueprints_get_with_http_info(self, project_id, **kwargs):  # noqa: E501
        """List Blueprints  # noqa: E501

        Returns the list of available blueprints in the project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_get_with_http_info(project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_id: (required)
        :param int offset: With which item to start (0 based).
        :param int limit: A number specifying how many entries to return.
        :return: CloudEndureBlueprintList
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
                    " to method projects_project_id_blueprints_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_blueprints_get`")  # noqa: E501

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
            '/projects/{projectId}/blueprints', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureBlueprintList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def projects_project_id_blueprints_post(self, body, project_id, **kwargs):  # noqa: E501
        """Create Blueprint  # noqa: E501

        Define the target machine characteristics: machine and disk types, network configuration, etc. There can be only one blueprint per machine per region. Returns the newly created object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_post(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureBlueprint body: (required)
        :param str project_id: (required)
        :return: CloudEndureBlueprint
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.projects_project_id_blueprints_post_with_http_info(body, project_id, **kwargs)  # noqa: E501
        else:
            (data) = self.projects_project_id_blueprints_post_with_http_info(body, project_id, **kwargs)  # noqa: E501
            return data

    def projects_project_id_blueprints_post_with_http_info(self, body, project_id, **kwargs):  # noqa: E501
        """Create Blueprint  # noqa: E501

        Define the target machine characteristics: machine and disk types, network configuration, etc. There can be only one blueprint per machine per region. Returns the newly created object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.projects_project_id_blueprints_post_with_http_info(body, project_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CloudEndureBlueprint body: (required)
        :param str project_id: (required)
        :return: CloudEndureBlueprint
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
                    " to method projects_project_id_blueprints_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `projects_project_id_blueprints_post`")  # noqa: E501
        # verify the required parameter 'project_id' is set
        if ('project_id' not in params or
                params['project_id'] is None):
            raise ValueError("Missing the required parameter `project_id` when calling `projects_project_id_blueprints_post`")  # noqa: E501

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
            '/projects/{projectId}/blueprints', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CloudEndureBlueprint',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

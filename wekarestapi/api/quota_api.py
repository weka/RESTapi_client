# coding: utf-8

"""
    @weka-api

    <div>The Weka system supports a RESTful API. This is useful when automating the interaction with the Weka system and when integrating it into your workflows or monitoring systems. The API is accessible at port 14000, via the /api/v2 URL, you can explore it via /api/v2/docs when accessing from the cluster (e.g. https://weka01:14000/api/v2/docs).<div style=\"margin-top: 15px;\">Note: Weka uses 64bit numbers. Please take special care when interacting with the API with different program languages (In JS for example you can use \"json-bigint\")</div></div>  # noqa: E501

    OpenAPI spec version: 3.14
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from wekarestapi.api_client import ApiClient


class QuotaApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_quota(self, uid, inode_context, **kwargs):  # noqa: E501
        """Remove the quota from a directory  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota(uid, inode_context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :param str path:
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_quota_with_http_info(uid, inode_context, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_quota_with_http_info(uid, inode_context, **kwargs)  # noqa: E501
            return data

    def delete_quota_with_http_info(self, uid, inode_context, **kwargs):  # noqa: E501
        """Remove the quota from a directory  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_quota_with_http_info(uid, inode_context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :param str path:
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'inode_context', 'path']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_quota" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `delete_quota`")  # noqa: E501
        # verify the required parameter 'inode_context' is set
        if ('inode_context' not in params or
                params['inode_context'] is None):
            raise ValueError("Missing the required parameter `inode_context` when calling `delete_quota`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'inode_context' in params:
            path_params['inode_context'] = params['inode_context']  # noqa: E501

        query_params = []
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fileSystems/{uid}/quota/{inode_context}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20023',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_quota(self, uid, inode_context, **kwargs):  # noqa: E501
        """Get the parameters of a specific directory quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota(uid, inode_context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_quota_with_http_info(uid, inode_context, **kwargs)  # noqa: E501
        else:
            (data) = self.get_quota_with_http_info(uid, inode_context, **kwargs)  # noqa: E501
            return data

    def get_quota_with_http_info(self, uid, inode_context, **kwargs):  # noqa: E501
        """Get the parameters of a specific directory quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_with_http_info(uid, inode_context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'inode_context']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_quota`")  # noqa: E501
        # verify the required parameter 'inode_context' is set
        if ('inode_context' not in params or
                params['inode_context'] is None):
            raise ValueError("Missing the required parameter `inode_context` when calling `get_quota`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'inode_context' in params:
            path_params['inode_context'] = params['inode_context']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fileSystems/{uid}/quota/{inode_context}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_quota_deprecated(self, type, uid, **kwargs):  # noqa: E501
        """Get file system quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_deprecated(type, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Quota type (required)
        :param str uid: File system uid (required)
        :param str next_token: Token to get the next page
        :return: InlineResponse20054
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_quota_deprecated_with_http_info(type, uid, **kwargs)  # noqa: E501
        else:
            (data) = self.get_quota_deprecated_with_http_info(type, uid, **kwargs)  # noqa: E501
            return data

    def get_quota_deprecated_with_http_info(self, type, uid, **kwargs):  # noqa: E501
        """Get file system quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_quota_deprecated_with_http_info(type, uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str type: Quota type (required)
        :param str uid: File system uid (required)
        :param str next_token: Token to get the next page
        :return: InlineResponse20054
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['type', 'uid', 'next_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_quota_deprecated" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `get_quota_deprecated`")  # noqa: E501
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `get_quota_deprecated`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'uid' in params:
            query_params.append(('uid', params['uid']))  # noqa: E501
        if 'next_token' in params:
            query_params.append(('next_token', params['next_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/quota', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20054',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_quotas(self, uid, **kwargs):  # noqa: E501
        """Get a list of quotas in the file system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_quotas(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str next_token: Token to get the next page
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_quotas_with_http_info(uid, **kwargs)  # noqa: E501
        else:
            (data) = self.list_quotas_with_http_info(uid, **kwargs)  # noqa: E501
            return data

    def list_quotas_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Get a list of quotas in the file system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_quotas_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str next_token: Token to get the next page
        :return: InlineResponse20020
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'next_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_quotas" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `list_quotas`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501

        query_params = []
        if 'next_token' in params:
            query_params.append(('next_token', params['next_token']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fileSystems/{uid}/quota/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20020',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_quota(self, uid, inode_context, **kwargs):  # noqa: E501
        """Patch the parameters of a directory quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_quota(uid, inode_context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :param str path:
        :param float hard_limit_bytes: 0 for unlimited
        :param float soft_limit_bytes: 0 for unlimited
        :param float grace_seconds:
        :param str owner:
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_quota_with_http_info(uid, inode_context, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_quota_with_http_info(uid, inode_context, **kwargs)  # noqa: E501
            return data

    def patch_quota_with_http_info(self, uid, inode_context, **kwargs):  # noqa: E501
        """Patch the parameters of a directory quota  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_quota_with_http_info(uid, inode_context, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :param str path:
        :param float hard_limit_bytes: 0 for unlimited
        :param float soft_limit_bytes: 0 for unlimited
        :param float grace_seconds:
        :param str owner:
        :return: InlineResponse20021
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'inode_context', 'path', 'hard_limit_bytes', 'soft_limit_bytes', 'grace_seconds', 'owner']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_quota" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `patch_quota`")  # noqa: E501
        # verify the required parameter 'inode_context' is set
        if ('inode_context' not in params or
                params['inode_context'] is None):
            raise ValueError("Missing the required parameter `inode_context` when calling `patch_quota`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'inode_context' in params:
            path_params['inode_context'] = params['inode_context']  # noqa: E501

        query_params = []
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501
        if 'hard_limit_bytes' in params:
            query_params.append(('hard_limit_bytes', params['hard_limit_bytes']))  # noqa: E501
        if 'soft_limit_bytes' in params:
            query_params.append(('soft_limit_bytes', params['soft_limit_bytes']))  # noqa: E501
        if 'grace_seconds' in params:
            query_params.append(('grace_seconds', params['grace_seconds']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fileSystems/{uid}/quota/{inode_context}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20021',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_quota(self, uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, **kwargs):  # noqa: E501
        """Set a quota on a directory  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_quota(uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :param float hard_limit_bytes: 0 for unlimited (required)
        :param float soft_limit_bytes: 0 for unlimited (required)
        :param float grace_seconds: (required)
        :param str path:
        :param str owner:
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.put_quota_with_http_info(uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, **kwargs)  # noqa: E501
        else:
            (data) = self.put_quota_with_http_info(uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, **kwargs)  # noqa: E501
            return data

    def put_quota_with_http_info(self, uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, **kwargs):  # noqa: E501
        """Set a quota on a directory  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_quota_with_http_info(uid, inode_context, hard_limit_bytes, soft_limit_bytes, grace_seconds, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uid: file system uid (required)
        :param str inode_context: directory's inode id (required)
        :param float hard_limit_bytes: 0 for unlimited (required)
        :param float soft_limit_bytes: 0 for unlimited (required)
        :param float grace_seconds: (required)
        :param str path:
        :param str owner:
        :return: InlineResponse20022
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uid', 'inode_context', 'hard_limit_bytes', 'soft_limit_bytes', 'grace_seconds', 'path', 'owner']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_quota" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uid' is set
        if ('uid' not in params or
                params['uid'] is None):
            raise ValueError("Missing the required parameter `uid` when calling `put_quota`")  # noqa: E501
        # verify the required parameter 'inode_context' is set
        if ('inode_context' not in params or
                params['inode_context'] is None):
            raise ValueError("Missing the required parameter `inode_context` when calling `put_quota`")  # noqa: E501
        # verify the required parameter 'hard_limit_bytes' is set
        if ('hard_limit_bytes' not in params or
                params['hard_limit_bytes'] is None):
            raise ValueError("Missing the required parameter `hard_limit_bytes` when calling `put_quota`")  # noqa: E501
        # verify the required parameter 'soft_limit_bytes' is set
        if ('soft_limit_bytes' not in params or
                params['soft_limit_bytes'] is None):
            raise ValueError("Missing the required parameter `soft_limit_bytes` when calling `put_quota`")  # noqa: E501
        # verify the required parameter 'grace_seconds' is set
        if ('grace_seconds' not in params or
                params['grace_seconds'] is None):
            raise ValueError("Missing the required parameter `grace_seconds` when calling `put_quota`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in params:
            path_params['uid'] = params['uid']  # noqa: E501
        if 'inode_context' in params:
            path_params['inode_context'] = params['inode_context']  # noqa: E501

        query_params = []
        if 'path' in params:
            query_params.append(('path', params['path']))  # noqa: E501
        if 'hard_limit_bytes' in params:
            query_params.append(('hard_limit_bytes', params['hard_limit_bytes']))  # noqa: E501
        if 'soft_limit_bytes' in params:
            query_params.append(('soft_limit_bytes', params['soft_limit_bytes']))  # noqa: E501
        if 'grace_seconds' in params:
            query_params.append(('grace_seconds', params['grace_seconds']))  # noqa: E501
        if 'owner' in params:
            query_params.append(('owner', params['owner']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/fileSystems/{uid}/quota/{inode_context}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20022',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

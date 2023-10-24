# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse

from .. import models


class DigitalTwinModelsOperations(object):
    """DigitalTwinModelsOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The requested API version. Constant value: "2023-10-31".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2023-10-31"

        self.config = config

    def add(
            self, models_to_add=None, digital_twin_models_add_options=None, custom_headers=None, raw=False, **operation_config):
        """Uploads one or more models. When any error occurs, no models are
        uploaded.
        Status codes:
        * 201 Created
        * 400 Bad Request
        * DTDLParserError - The models provided are not valid DTDL.
        * InvalidArgument - The model id is invalid.
        * LimitExceeded - The maximum number of model ids allowed in
        'dependenciesFor' has been reached.
        * ModelVersionNotSupported - The version of DTDL used is not supported.
        * 409 Conflict
        * ModelAlreadyExists - The model provided already exists.

        :param models: An array of models to add.
        :type models: list[object]
        :param digital_twin_models_add_options: Additional parameters for the
         operation
        :type digital_twin_models_add_options:
         ~dataplane.models.DigitalTwinModelsAddOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: list or ClientRawResponse if raw=true
        :rtype: list[~dataplane.models.DigitalTwinsModelData] or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<dataplane.models.ErrorResponseException>`
        """
        traceparent = None
        if digital_twin_models_add_options is not None:
            traceparent = digital_twin_models_add_options.traceparent
        tracestate = None
        if digital_twin_models_add_options is not None:
            tracestate = digital_twin_models_add_options.tracestate

        # Construct URL
        url = self.add.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", traceparent, 'str')
        if tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", tracestate, 'str')

        # @vilit - when regenerating the sdk, models the parameter should be changed so it does not conflict
        #          with the imported models.
        # Construct body
        if models_to_add is not None:
            body_content = self._serialize.body(models_to_add, '[object]')
        else:
            body_content = None

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        # @vilit - update the generated sdk to support both 200 and 201. Custom error message for 403.
        if response.status_code not in [200, 201]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code in [200, 201]:
            deserialized = self._deserialize('[DigitalTwinsModelData]', response)
            header_dict = {
                'x-ms-error-code': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    add.metadata = {'url': '/models'}

    def list(
            self, dependencies_for=None, include_model_definition=False, digital_twin_models_list_options=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves model metadata and, optionally, model definitions.
        Status codes:
        * 200 OK
        * 400 Bad Request
        * InvalidArgument - The model id is invalid.
        * LimitExceeded - The maximum number of model ids allowed in
        'dependenciesFor' has been reached.
        * 404 Not Found
        * ModelNotFound - The model was not found.

        :param dependencies_for: If specified, only return the set of the
         specified models along with their dependencies. If omitted, all models
         are retrieved.
        :type dependencies_for: list[str]
        :param include_model_definition: When true the model definition will
         be returned as part of the result.
        :type include_model_definition: bool
        :param digital_twin_models_list_options: Additional parameters for the
         operation
        :type digital_twin_models_list_options:
         ~dataplane.models.DigitalTwinModelsListOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of DigitalTwinsModelData
        :rtype:
         ~dataplane.models.DigitalTwinsModelDataPaged[~dataplane.models.DigitalTwinsModelData]
        :raises:
         :class:`ErrorResponseException<dataplane.models.ErrorResponseException>`
        """
        max_items_per_page = None
        if digital_twin_models_list_options is not None:
            max_items_per_page = digital_twin_models_list_options.max_items_per_page
        traceparent = None
        if digital_twin_models_list_options is not None:
            traceparent = digital_twin_models_list_options.traceparent
        tracestate = None
        if digital_twin_models_list_options is not None:
            tracestate = digital_twin_models_list_options.tracestate

        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']

                # Construct parameters
                query_parameters = {}
                if dependencies_for is not None:
                    # @vilit - the div should be "&dependenciesFor=" not ","
                    query_parameters['dependenciesFor'] = self._serialize.query("dependencies_for", dependencies_for, '[str]', div='&dependenciesFor=')
                if include_model_definition is not None:
                    query_parameters['includeModelDefinition'] = self._serialize.query("include_model_definition", include_model_definition, 'bool')
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Content-Type'] = 'application/json; charset=utf-8'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
            if max_items_per_page is not None:
                header_parameters['max-items-per-page'] = self._serialize.header("max_items_per_page", max_items_per_page, 'int')
            if traceparent is not None:
                header_parameters['traceparent'] = self._serialize.header("traceparent", traceparent, 'str')
            if tracestate is not None:
                header_parameters['tracestate'] = self._serialize.header("tracestate", tracestate, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters)
            response = self._client.send(
                request, header_parameters, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ErrorResponseException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.DigitalTwinsModelDataPaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.DigitalTwinsModelDataPaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/models'}

    def get_by_id(
            self, id, include_model_definition=False, digital_twin_models_get_by_id_options=None, custom_headers=None, raw=False, **operation_config):
        """Retrieves model metadata and optionally the model definition.
        Status codes:
        * 200 OK
        * 400 Bad Request
        * InvalidArgument - The model id is invalid.
        * MissingArgument - The model id was not provided.
        * 404 Not Found
        * ModelNotFound - The model was not found.

        :param id: The id for the model. The id is globally unique and case
         sensitive.
        :type id: str
        :param include_model_definition: When true the model definition will
         be returned as part of the result.
        :type include_model_definition: bool
        :param digital_twin_models_get_by_id_options: Additional parameters
         for the operation
        :type digital_twin_models_get_by_id_options:
         ~dataplane.models.DigitalTwinModelsGetByIdOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: DigitalTwinsModelData or ClientRawResponse if raw=true
        :rtype: ~dataplane.models.DigitalTwinsModelData or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<dataplane.models.ErrorResponseException>`
        """
        traceparent = None
        if digital_twin_models_get_by_id_options is not None:
            traceparent = digital_twin_models_get_by_id_options.traceparent
        tracestate = None
        if digital_twin_models_get_by_id_options is not None:
            tracestate = digital_twin_models_get_by_id_options.tracestate

        # Construct URL
        url = self.get_by_id.metadata['url']
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        if include_model_definition is not None:
            query_parameters['includeModelDefinition'] = self._serialize.query("include_model_definition", include_model_definition, 'bool')
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", traceparent, 'str')
        if tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", tracestate, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ErrorResponseException(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('DigitalTwinsModelData', response)
            header_dict = {
                'x-ms-error-code': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get_by_id.metadata = {'url': '/models/{id}'}

    def update(
            self, id, update_model, digital_twin_models_update_options=None, custom_headers=None, raw=False, **operation_config):
        """Updates the metadata for a model.
        Status codes:
        * 204 No Content
        * 400 Bad Request
        * InvalidArgument - The model id is invalid.
        * JsonPatchInvalid - The JSON Patch provided is invalid.
        * MissingArgument - The model id was not provided.
        * 404 Not Found
        * ModelNotFound - The model was not found.
        * 409 Conflict
        * ModelReferencesNotDecommissioned - The model refers to models that
        are not decommissioned.

        :param id: The id for the model. The id is globally unique and case
         sensitive.
        :type id: str
        :param update_model: An update specification described by JSON Patch.
         Only the decommissioned property can be replaced.
        :type update_model: list[object]
        :param digital_twin_models_update_options: Additional parameters for
         the operation
        :type digital_twin_models_update_options:
         ~dataplane.models.DigitalTwinModelsUpdateOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<dataplane.models.ErrorResponseException>`
        """
        traceparent = None
        if digital_twin_models_update_options is not None:
            traceparent = digital_twin_models_update_options.traceparent
        tracestate = None
        if digital_twin_models_update_options is not None:
            tracestate = digital_twin_models_update_options.tracestate

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json-patch+json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", traceparent, 'str')
        if tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", tracestate, 'str')

        # Construct body
        body_content = self._serialize.body(update_model, '[object]')

        # Construct and send request
        request = self._client.patch(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'x-ms-error-code': 'str',
            })
            return client_raw_response
    update.metadata = {'url': '/models/{id}'}

    def delete(
            self, id, digital_twin_models_delete_options=None, custom_headers=None, raw=False, **operation_config):
        """Deletes a model. A model can only be deleted if no other models
        reference it.
        Status codes:
        * 204 No Content
        * 400 Bad Request
        * InvalidArgument - The model id is invalid.
        * MissingArgument - The model id was not provided.
        * 404 Not Found
        * ModelNotFound - The model was not found.
        * 409 Conflict
        * ModelReferencesNotDeleted - The model refers to models that are not
        deleted.

        :param id: The id for the model. The id is globally unique and case
         sensitive.
        :type id: str
        :param digital_twin_models_delete_options: Additional parameters for
         the operation
        :type digital_twin_models_delete_options:
         ~dataplane.models.DigitalTwinModelsDeleteOptions
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ErrorResponseException<dataplane.models.ErrorResponseException>`
        """
        traceparent = None
        if digital_twin_models_delete_options is not None:
            traceparent = digital_twin_models_delete_options.traceparent
        tracestate = None
        if digital_twin_models_delete_options is not None:
            tracestate = digital_twin_models_delete_options.tracestate

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'id': self._serialize.url("id", id, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')
        if traceparent is not None:
            header_parameters['traceparent'] = self._serialize.header("traceparent", traceparent, 'str')
        if tracestate is not None:
            header_parameters['tracestate'] = self._serialize.header("tracestate", tracestate, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [204]:
            raise models.ErrorResponseException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'x-ms-error-code': 'str',
            })
            return client_raw_response
    delete.metadata = {'url': '/models/{id}'}

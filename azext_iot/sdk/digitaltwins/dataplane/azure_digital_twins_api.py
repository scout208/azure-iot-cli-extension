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

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.digital_twin_models_operations import DigitalTwinModelsOperations
from .operations.query_operations import QueryOperations
from .operations.digital_twins_operations import DigitalTwinsOperations
from .operations.event_routes_operations import EventRoutesOperations
from .operations.import_jobs_operations import ImportJobsOperations
from .operations.delete_jobs_operations import DeleteJobsOperations
from . import models


class AzureDigitalTwinsAPIConfiguration(AzureConfiguration):
    """Configuration for AzureDigitalTwinsAPI
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param operation_id: ID for the operation's status monitor. The ID is
     generated if header was not passed by the client.
    :type operation_id: str
    :param timeout_in_minutes: Desired timeout for the delete job. Once the
     specified timeout is reached, service will stop any delete operations
     triggered by the current delete job that are in progress, and go to a
     failed state. Please note that this will leave your instance in an unknown
     state as there won't be any rollback operation.
    :type timeout_in_minutes: int
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, operation_id=None, timeout_in_minutes=None, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://digitaltwins-hostname'

        super(AzureDigitalTwinsAPIConfiguration, self).__init__(base_url)

        self.add_user_agent('azuredigitaltwinsapi/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.operation_id = operation_id
        self.timeout_in_minutes = timeout_in_minutes


class AzureDigitalTwinsAPI(SDKClient):
    """A service for managing and querying digital twins and digital twin models.

    :ivar config: Configuration for client.
    :vartype config: AzureDigitalTwinsAPIConfiguration

    :ivar digital_twin_models: DigitalTwinModels operations
    :vartype digital_twin_models: dataplane.operations.DigitalTwinModelsOperations
    :ivar query: Query operations
    :vartype query: dataplane.operations.QueryOperations
    :ivar digital_twins: DigitalTwins operations
    :vartype digital_twins: dataplane.operations.DigitalTwinsOperations
    :ivar event_routes: EventRoutes operations
    :vartype event_routes: dataplane.operations.EventRoutesOperations
    :ivar import_jobs: ImportJobs operations
    :vartype import_jobs: dataplane.operations.ImportJobsOperations
    :ivar delete_jobs: DeleteJobs operations
    :vartype delete_jobs: dataplane.operations.DeleteJobsOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param operation_id: ID for the operation's status monitor. The ID is
     generated if header was not passed by the client.
    :type operation_id: str
    :param timeout_in_minutes: Desired timeout for the delete job. Once the
     specified timeout is reached, service will stop any delete operations
     triggered by the current delete job that are in progress, and go to a
     failed state. Please note that this will leave your instance in an unknown
     state as there won't be any rollback operation.
    :type timeout_in_minutes: int
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, operation_id=None, timeout_in_minutes=None, base_url=None):

        self.config = AzureDigitalTwinsAPIConfiguration(credentials, operation_id, timeout_in_minutes, base_url)
        super(AzureDigitalTwinsAPI, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2023-10-31'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.digital_twin_models = DigitalTwinModelsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.digital_twins = DigitalTwinsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.event_routes = EventRoutesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.import_jobs = ImportJobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.delete_jobs = DeleteJobsOperations(
            self._client, self.config, self._serialize, self._deserialize)

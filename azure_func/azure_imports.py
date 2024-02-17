from azure.identity import ClientSecretCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.sql import SqlManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.mgmt.keyvault import KeyVaultManagementClient
from azure.mgmt.loganalytics import LogAnalyticsManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.apimanagement import ApiManagementClient
from azure.mgmt.batch import BatchManagementClient
from azure.mgmt.botservice import AzureBotService
from azure.mgmt.containerregistry import ContainerRegistryManagementClient
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datalake.store import DataLakeStoreAccountManagementClient
from azure.mgmt.eventhub import EventHubManagementClient
from azure.mgmt.iothub import IotHubClient
from azure.mgmt.logic import LogicManagementClient
from azure.mgmt.redis import RedisManagementClient
from azure.mgmt.search import SearchManagementClient
from azure.mgmt.servicebus import ServiceBusManagementClient
from azure.mgmt.signalr import SignalRManagementClient
from azure.mgmt.streamanalytics import StreamAnalyticsManagementClient
from azure.mgmt.trafficmanager import TrafficManagerManagementClient
from azure.mgmt.containerservice import ContainerServiceClient
from azure.mgmt.cosmosdb import CosmosDBManagementClient
from azure.mgmt.servicefabric import ServiceFabricManagementClient
from azure.mgmt.cdn import CdnManagementClient
from azure.mgmt.cognitiveservices import CognitiveServicesManagementClient
from azure.mgmt.devtestlabs import DevTestLabsClient
from azure.mgmt.monitor import MonitorManagementClient
from azure.mgmt.scheduler import SchedulerManagementClient
from azure.mgmt.servicefabric import ServiceFabricManagementClient
from azure.mgmt.dns import DnsManagementClient

#import functions
from azure_func.auth import authenticate
from azure_func.vm import handle_virtual_machine
from azure_func.nic import handle_network_interface
from azure_func.sql import handle_sql_server
from azure_func.sqldb import handle_sql_db
from azure_func.link import link_nics_to_vms, link_dbs_to_servers,link_disks_to_vms,link_app_services_to_app_service_plans
from azure_func.disk import handle_disk
from azure_func.appservice import handle_app_service
from azure_func.appserviceplan import handle_app_service_plan
from azure_func.keyvault import handle_key_vault
from azure_func.loganalytics import handle_log_analytics_workspace
from azure_func.storageaccount import handle_storage_account
from azure_func.apim import handle_api_management
from azure_func.datalake import handle_data_lake_store
from azure_func.datafactory import handle_data_factory
from azure_func.streamanalyticsjob import handle_stream_analytics_job
from azure_func.searchservice import handle_search_service
from azure_func.signalr import handle_signalr_service
from azure_func.botservice import handle_bot_service
from azure_func.iothub import handle_iot_hub
from azure_func.aks import handle_aks_service
from azure_func.cdn import handle_cdn_profile
from azure_func.cogni import handle_cognitive_service
from azure_func.cosmosdb import handle_cosmosdb_account
from azure_func.devtestlabs import handle_devtest_lab
from azure_func.loadbalancer import handle_load_balancer
from azure_func.monitor import handle_monitor_action_group
from azure_func.scheduler import handle_scheduler_job_collection
from azure_func.servicefabric import handle_service_fabric_cluster
from azure_func.vnet import handle_virtual_network
from azure_func.dns import handle_dns_zone

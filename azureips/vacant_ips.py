from utilities.azure_apis import AzureAPI
from utilities.ip_address_utils import generate_next_ip
class VacantIP():
    def __init__(self, client_id, client_secret, subscription_id, tenant_id,
                 token_url, base_url, api_version, subnet, vnet, resource_group, count):
        self.client_id = client_id
        self.client_secret = client_secret
        self.subscription_id = subscription_id
        self.tenant_id = tenant_id
        self.token_url = token_url
        self.base_url = base_url
        self.subnet = subnet
        self.vnet = vnet
        self.api_version = api_version or "2018-08-01"
        self.resource_group = resource_group
        self.count = count

    def get_vacant_ips(self):
        api = AzureAPI(subscription_id=self.subscription_id, client_secret=self.client_secret, client_id=self.client_id,
                       tenant_id=self.tenant_id, base_url="https://management.azure.com",
                       token_url="https://login.microsoftonline.com/" + self.tenant_id + "/oauth2/token/",
                       api_version=self.api_version, subnet=self.subnet, vnet=self.vnet, resource_group=self.resource_group)
        return generate_next_ip(api.get_interfaces_for_subnet(), self.count)
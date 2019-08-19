import requests
import sys
from . import RateLimitException, AzureAPIException, AuthException, ResourceNotFound

class AzureAPI():

    def __init__(self, client_id, client_secret, subscription_id, tenant_id,
                 token_url, base_url, api_version, subnet, vnet, resource_group):
        self.client_id = client_id
        self.client_secret = client_secret
        self.subscription_id = subscription_id
        self.tenant_id = tenant_id
        self.token_url = token_url
        self.base_url = base_url
        self.subnet = subnet
        self.vnet = vnet
        self.api_version = api_version
        self.resource_group= resource_group
        self.network_interface_url = self.base_url+"/subscriptions/"+\
                                     self.subscription_id+"/providers/Microsoft.Network/networkInterfaces/?api-version="+\
                                     self.api_version
        self.subnet_url = self.base_url+"/subscriptions/"+\
                                     self.subscription_id+"/resourceGroups/"+self.resource_group+"/providers/Microsoft.Network/virtualNetworks/"+self.vnet+"/subnets/"+\
                                     self.subnet+"?api-version="+self.api_version

    def get_auth_headers(self):
        url = self.token_url
        data = {
            "resource": self.base_url,
            "client_id":self.client_id,
            "client_secret":self.client_secret,
            "grant_type":"client_credentials"
        }
        content = requests.post(url,data=data,headers={})
        if content.status_code == 200:
            response = content.json()
            headers = {"Authorization":"Bearer "+ response["access_token"], "Content-Type":"application/json"}
            return headers
        elif content.status_code==429:
            raise(RateLimitException("Azure Apis Rate Limited"))
            sys.exit(1)
        elif content.status_code==404:
            raise(ResourceNotFound())
        else:
            raise(AzureAPIException())
            sys.exit(1)

    def get_interfaces_for_subnet(self):
        list_ips = []
        headers = self.get_auth_headers()
        subnet = self.get_address_space_for_subnet(headers)
        url = self.network_interface_url
        while True:
            content = requests.get(url=url, headers=headers)
            if content.status_code == 200:
                nics = content.json()
                for nic in nics["value"]:
                    for ip in nic["properties"]["ipConfigurations"]:
                        if ip["properties"]["subnet"]["id"] == subnet["id"]:
                            list_ips.append(ip["properties"]["privateIPAddress"])
                if "nextLink" in nics:
                    url = nics["nextLink"]
                else:
                    break
            elif content.status_code == 429:
                raise (RateLimitException("Azure Apis Rate Limited"))
                sys.exit(1)
            elif content.status_code == 403:
                raise (AuthException)
            elif content.status_code==404:
                raise(ResourceNotFound())
            else:
                raise (AzureAPIException())
                sys.exit(1)
        return {"ips": list_ips, "address_space": subnet["address_space"]}

    def get_address_space_for_subnet(self, headers):
        content = requests.get(url=self.subnet_url, headers=headers)
        if content.status_code == 200:
            subnet = content.json()
            return {"name":subnet["name"], "id":subnet["id"], "address_space": subnet["properties"]["addressPrefix"]}
        elif content.status_code == 429:
            raise (RateLimitException("Azure Apis Rate Limited"))
            sys.exit(1)
        elif content.status_code == 403:
            raise (AuthException)
        elif content.status_code==404:
            raise(ResourceNotFound())
        else:
            print(content.status_code)
            raise (AzureAPIException())
            sys.exit(1)
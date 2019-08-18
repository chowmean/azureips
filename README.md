# Azure Vacant IPs

This package gives you the list of private ip address that are not allocated to any resource. This helps in below scenario.
If you want to make an ip static in azure you need to specify the IPs, this means you have to manage the IPs by yourself. This package helps you by
getting you the list of IPs that are not allocated and this saves you from cumbersome process of keeping track of IP addresses allowed.

Creating Network interfaces with dynamic ip is easy but for static ip address you need the ip that is not allocated.

## Usage and how it works.

This package works in both CLI manner and you can import it to use it with your python program.

### CLI Application:

```python azureips/azureipselector.py --client_id client_id --client_secret client_secret --subscription_id subscription_id --tenant_id tenant_id --subnet subnet_name --vnet vnet_name --resource_group resource_group_vnet --count no_of_ip_you_need```

### Importing in python application

```
from azureips.vacant_ips import VacantIP
vacant_ips = VacantIP(client_id, client_secret, subscription_id, tenant_id,
                 token_url, base_url, api_version, subnet, vnet, resource_group, count)
vacant_ips.get_vacant_ips()
```

This will return an array of ips
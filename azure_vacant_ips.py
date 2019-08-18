import click
from azureips.utilities.azure_apis import AzureAPI
from azureips.utilities.ip_address_utils import generate_next_ip
from azureips.utilities import print_newline
@click.command()
@click.option('--subscription_id', help='Subscription ID')
@click.option('--tenant_id', help='Tenant ID')
@click.option('--client_id', help='Client ID')
@click.option('--client_secret', help='Client Secret')
@click.option('--subnet', help='Subnet Name')
@click.option('--vnet', help='VPC Name')
@click.option('--resource_group', help='Resource groups Name')
@click.option('--count', default=1, help='Number of IPs to select.')
@click.option('--output', default="newline", help='newline for each ip in new line and array for ips in array')
def get_vacant_ips(subscription_id, tenant_id, client_id, client_secret, subnet, vnet, resource_group, count, output):
    api = AzureAPI(subscription_id=subscription_id, client_secret=client_secret, client_id=client_id,
                   tenant_id=tenant_id, base_url="https://management.azure.com",
                   token_url="https://login.microsoftonline.com/"+tenant_id+"/oauth2/token/",
                   api_version="2018-08-01", subnet =subnet, vnet=vnet, resource_group=resource_group)
    data = generate_next_ip(api.get_interfaces_for_subnet(), count)
    if output=="newline":
        print_newline(data)
    else:
        print(generate_next_ip(api.get_interfaces_for_subnet(), count))

if __name__ == '__main__':
    get_vacant_ips()
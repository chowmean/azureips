import ipaddress

def generate_next_ip(data, count):
    address_space = data["address_space"]
    all_ips = list(ipaddress.ip_network(address_space).hosts())
    all_ips.pop(0)
    all_ips.pop(0)
    all_ips.pop(0)
    for ip in data["ips"]:
        ip_to_remove = ipaddress.ip_address(ip)
        all_ips.remove(ip_to_remove)
    ips_to_return = []
    for ip in all_ips:
        ips_to_return.append(str(ip))
    return ips_to_return[:count]

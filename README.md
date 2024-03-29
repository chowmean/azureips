# Azure Vacant IPs

This package gives you the list of private ip address that are not allocated to any resource. This helps in below scenario.
If you want to make an ip static in azure you need to specify the IPs, this means you have to manage the IPs by yourself. This package helps you by
getting you the list of IPs that are not allocated and this saves you from cumbersome process of keeping track of IP addresses allowed.

Creating Network interfaces with dynamic ip is easy but for static ip address you need the ip that is not allocated.

## Usage and how it works.

### Installation

```pip install azureips```

You can import it to use it with your python program.

### Importing in python application

```
from azureips.vacant_ips import VacantIP
vacant_ips = VacantIP(client_id, client_secret, subscription_id, tenant_id,
                 token_url, base_url, api_version, subnet, vnet, resource_group, count)
vacant_ips.get_vacant_ips()
#base_url, api_version and token_url can be empty strings.
```

This will return an array of ips

### Options

`client_id` : Client id of the app generated in service principle

`client_secret` : Client Secret obtained from app

`subscription_id`

`tenant_id`

`token_url`: Not required

`base_url`: Not required

`api_version`: Not required

`subnet`: Subnet to search for unallocated IP

`vnet`: Vnet to which the subnet belongs

`resource_group`: Resource group in which vnet is present

`count`: Number of IPs that you want as output


# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you
   do not have permission to do that, you may request the second reviewer to merge it for you.

## Code of Conduct

### Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to making participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, gender identity and expression, level of experience,
nationality, personal appearance, race, religion, or sexual identity and
orientation.

### Our Standards

Examples of behavior that contributes to creating a positive environment
include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or
advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic
  address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

### Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable
behavior and are expected to take appropriate and fair corrective action in
response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or
reject comments, commits, code, wiki edits, issues, and other contributions
that are not aligned to this Code of Conduct, or to ban temporarily or
permanently any contributor for other behaviors that they deem inappropriate,
threatening, offensive, or harmful.

Thanks for your support!

class RateLimitException(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return (repr(self.value))

class AzureAPIException(Exception):

    def __str__(self):
        return (repr("Azure API exception."))

class AuthException(Exception):

    def __str__(self):
        return (repr("Azure API Authorization Exception. Please verify your credentials."))

class ResourceNotFound(Exception):

    def __str__(self):
        return (repr("Azure resource not found please check your resource group name, subnet name and vnet name."))


def print_newline(data):
    for ip in data:
        print(ip)
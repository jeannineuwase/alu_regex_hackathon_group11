import re
ip_address = input('Insert your ip address to check if it is valid: ')

pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
def matchIp(ip_address):
    if (re.match(pattern,ip_address)):
        print(f"{ip_address} is valid")
    else:
        print(f"{ip_address} is invalid")
matchIp(ip_address)
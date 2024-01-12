import os
import requests
import json
import sys

# ANSI escape code for green color
green_color = '\033[92m'

# ANSI escape code to reset color
reset_color = '\033[0m'

def get_subdomains(target):
    url = f'https://crt.sh/?q={target}&output=json'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        subdomains = [entry['name_value'] for entry in data]
        return subdomains
    else:
        print(f"{green_color}Error: {response.status_code}{reset_color}")
        return None

def save_to_file(domain, subdomains):
    directory = os.path.join('output', 'certificates_subdomains')
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = os.path.join(directory, f"{domain}_subdomains.txt")
    with open(filename, 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '\n')

    print(f"{green_color}Number of subdomains found: {len(subdomains)}{reset_color}")
    print(f"{green_color}Subdomains saved to {filename}{reset_color}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{green_color}Usage: python modules/script.py <target>{reset_color}")
        sys.exit(1)

    target = sys.argv[1]

    subdomains = get_subdomains(target)

    if subdomains:
        save_to_file(target, subdomains)

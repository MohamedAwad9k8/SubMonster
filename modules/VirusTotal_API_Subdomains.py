import requests
import json
import sys
import os

# ANSI escape code for green color
green_color = '\033[92m'

# ANSI escape code to reset color
reset_color = '\033[0m'

def get_subdomains(api_key, domain):
    url = f'https://www.virustotal.com/api/v3/domains/{domain}/subdomains?limit=1000'
    headers = {'x-apikey': api_key}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subdomains = data.get('data', [])

        if subdomains:
            return [subdomain['id'] for subdomain in subdomains]
        else:
            return []
    else:
        print(f"{green_color}Error: {response.status_code}{reset_color}")
        return None

def save_to_file(domain, subdomains):
    output_directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'output')  # 'output' directory adjacent to 'modules'
    
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    directory = os.path.join(output_directory, 'virustotal_subdomains')
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
        print(f"{green_color}Usage: python script.py <domain>{reset_color}")
        sys.exit(1)

    # Replace 'YOUR_API_KEY' with your actual VirusTotal API key
    #api_key = 'YOUR_API_KEY'

    domain_to_query = sys.argv[1]

    subdomains = get_subdomains(api_key, domain_to_query)

    if subdomains:
        save_to_file(domain_to_query, subdomains)

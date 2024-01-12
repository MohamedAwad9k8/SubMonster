import requests
import concurrent.futures

def validate_subdomain(subdomain):
    url = f'http://{subdomain}'  # You can change this to https:// if needed
    try:
        response = requests.get(url, timeout=10)  # Set a timeout to avoid hanging on unresponsive servers
        status = response.status_code
        if status in [200, 203, 204, 206, 207, 208, 226, 401, 402, 403, 405, 406, 407, 408, 300, 301, 302, 307, 308]:  # Add more status codes as needed
            result = True
        else:
            result = False
    except requests.RequestException:
        status = 'Error'
        result = False

    print(f"Subdomain: {subdomain}, Result: {'Valid' if result else 'Invalid'}, Status: {status}")
    return subdomain, result

def validate_subdomains(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        subdomains = [line.strip() for line in file if line.strip()]

    total_subdomains = len(subdomains)
    print(f"Total subdomains to check: {total_subdomains}")

    validated_subdomains = []

    # Adjust the number of threads (max_workers) as needed
    max_workers = 20
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(validate_subdomain, subdomain): subdomain for subdomain in subdomains}

        for i, future in enumerate(concurrent.futures.as_completed(futures), 1):
            subdomain, is_valid = future.result()
            if is_valid:
                validated_subdomains.append(subdomain)
            print(f"Progress: {i}/{total_subdomains}", end='\r')

    print("\nValidation completed.")

    with open(output_filename, 'w') as output_file:
        for validated_subdomain in validated_subdomains:
            output_file.write(validated_subdomain + '\n')

if __name__ == "__main__":
    input_filename = 'output/merged_subdomains.txt'  # Replace with your input filename
    output_filename = 'output/validated_subdomains.txt'  # Replace with your output filename

    validate_subdomains(input_filename, output_filename)

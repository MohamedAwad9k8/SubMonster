import os

# ANSI escape code for green color
green_color = '\033[92m'

# ANSI escape code to reset color
reset_color = '\033[0m'

def merge_and_count_subdomains():
    certificates_dir = os.path.join('output', 'certificates_subdomains')  # Adjusted path
    virustotal_dir = os.path.join('output', 'virustotal_subdomains')  # Adjusted path
    merged_filename = os.path.join('output', 'merged_subdomains.txt')  # Adjusted path

    # Get all text files from certificates_subdomains directory
    certificates_files = [os.path.join(certificates_dir, file) for file in os.listdir(certificates_dir) if file.endswith(".txt")]

    # Get all text files from virustotal_subdomains directory
    virustotal_files = [os.path.join(virustotal_dir, file) for file in os.listdir(virustotal_dir) if file.endswith(".txt")]

    # Combine all file paths
    all_files = certificates_files + virustotal_files

    # Set to store unique subdomains
    unique_subdomains = set()

    # Iterate through each file
    for file_path in all_files:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            unique_subdomains.update([line.strip() for line in lines])

    # Count the total number of subdomains
    total_subdomains = len(unique_subdomains)

    # Write unique subdomains to the merged file
    with open(merged_filename, 'w') as merged_file:
        for subdomain in unique_subdomains:
            merged_file.write(subdomain + '\n')

    print(f"{green_color}Total number of unique subdomains: {total_subdomains}{reset_color}")
    print(f"{green_color}Merged subdomains saved to {merged_filename}{reset_color}")

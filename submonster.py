import sys
import time
import logging
from modules import VirusTotal_API_Subdomains
from modules import Certificates_Subdomains
from modules import title
from modules import merge
import os

# ANSI escape code for green color
green_color = '\033[92m'

# ANSI escape code to reset color
reset_color = '\033[0m'

# Replace 'YOUR_API_KEY' with your actual VirusTotal API key
#api_key = 'YOUR_API_KEY'

# Counter for subdomains
subdomains_count = 0

def setup_logger(log_filename):
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Log to file inside the 'output' directory
    log_path = os.path.join('output', log_filename)
    if not os.path.exists('output'):
        os.makedirs('output')

    file_handler = logging.FileHandler(log_path)
    file_handler.setLevel(logging.DEBUG)

    # Log to console
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)

    # Set the formatter
    formatter = logging.Formatter(f'{green_color}%(asctime)s - %(levelname)s - %(message)s{reset_color}')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def process_domains():
    global subdomains_count
    filename = 'input_domains.txt'
    log_filename = 'log.txt'

    # Setup logger
    logger = setup_logger(log_filename)

    # Add a new line when starting the app
    logger.info(f"{green_color}===== NEW PROCESS STARTED ====={reset_color}")
    
    # Log starting time
    start_time = time.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"{green_color}Processing started at {start_time}{reset_color}")

    with open(filename, 'r') as file:
        domains = [line.strip() for line in file if line.strip()]

    for domain in domains:
        
        # Using functions from VirusTotal_API_Subdomains.py
        logger.info(f"{green_color}VirusTotal API Query: {domain}{reset_color}")
        subdomains_vt = VirusTotal_API_Subdomains.get_subdomains(api_key, domain)
        if subdomains_vt:
            subdomains_count += len(subdomains_vt)
            logger.info(f"{green_color}Number of VirusTotal subdomains found: {len(subdomains_vt)}{reset_color}")
            VirusTotal_API_Subdomains.save_to_file(domain, subdomains_vt)

        # Using functions from Certificates_Subdomains.py
        logger.info(f"{green_color}Certificates Query: {domain}{reset_color}")
        subdomains_cert = Certificates_Subdomains.get_subdomains(domain)
        if subdomains_cert:
            subdomains_count += len(subdomains_cert)
            logger.info(f"{green_color}Number of Certificate subdomains found: {len(subdomains_cert)}{reset_color}")
            Certificates_Subdomains.save_to_file(domain, subdomains_cert)

    # Log finishing time
    finish_time = time.strftime('%Y-%m-%d %H:%M:%S')
    logger.info(f"{green_color}Processing finished at {finish_time}{reset_color}")

    # Log the total number of subdomains found
    logger.info(f"{green_color}Total number of subdomains found: {subdomains_count}{reset_color}")

if __name__ == "__main__":
    title.print_tool_title()
    process_domains()
    merge.merge_and_count_subdomains()

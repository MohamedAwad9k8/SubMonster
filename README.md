# SubMonster
SubMonster ..... Passive Subdomain Enumeration Made Easy!!!

SubMonster is a simple and light yet effictive tool for the Recon phase during web security assessments.
It's a script that automates the process of passive subdomain enumeration to get a list of available subdomains on the given target within minutes.
The script is built using modular programming, allowing for ease of extensiotn, each module represents one source for data to be harvested from.
Currently I'm using two sources only. If you like the tool feel free to add more modules from your favorite data sources.

# How To Use

First, you will need to clone the reposotiry.

Second, you should open SubMonster.py and put your API key to Virustotal there.

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/e330263a-6411-4b15-bb88-da4294ccfb02)

Third, Add all the Apex domains to your target in "input_domains.txt".

Note: In this example I have only one Apex subdomain on the list, but you can have more Apex domains entered related to one target.

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/775fc244-819f-4ead-bf56-e42f1340e3eb)

Now you can run the the tool.

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/b145e361-c915-49e5-a92f-894420c1559a)

Note: This is the first step, the returned subdomians are not all accessible through http protocol, so the second step is to validate which subdomains you can access through http protocol (AKA through your web browser). However the other subdomains may be useful for other uses so they are still kept in "merged_subdomains.txt".

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/0c2d7e66-12c8-430f-be8a-bd3ad930ca99)

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/c79e70b4-ca6e-4e15-ba1d-9297e5255ca7)

Inside the folder "output" you will find 3 text files

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/408e8749-0bd8-4617-871b-9f71a6530990)

And finally all the subdomains are listed in "validated_subdomains"

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/8bef061d-3851-4201-99b7-ea49edd240ec)

Tip: I recommend that after finishing a scan on a target, you rename the output file to "output_targer-tname" so that the data is saved, and the tool is ready to start again from a clean start.

![image](https://github.com/MohamedAwad9k8/SubMonster/assets/75997594/26fa016a-8bb6-4164-9c79-e0f39b73e580)

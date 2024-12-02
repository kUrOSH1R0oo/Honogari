# Honogari: A penetration testing tool designed to identify and exploit misconfigured or publicly accessible Firebase databases vulnerable to unauthorized access or data manipulation

Honogari is a powerful and specialized penetration testing tool developed to identify, assess, and exploit vulnerabilities in misconfigured or publicly accessible Firebase databases. Firebase, being a widely used backend service for mobile and web applications, often holds sensitive data, making it an attractive target for attackers.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/kUrOSH1R0oo/Honogari
    ```

2. Navigate to the directory and install the requirements:
    ```bash
    pip3 install -r requirements.txt
    ```

3. Run Honogari
    ```bash
    ./honogari.py
    ```

## Parameters

| Parameters                  | Description                                                        |
|-------------------------|--------------------------------------------------------------------|
| `-u, --url`              | Target specific Firebase URL.                                      |
| `-uf, --url-file`        | File path containing a list of Firebase URLs.                      |
| `-e, --exploit`          | Exploit vulnerable URL(s).                                         |
| `-ef, --exploit-file`    | URI Filename For the Exploit (default: `honogari.json`).          |
| `-H, --headers`          | Custom HTTP headers in JSON format (default: `{}`).                 |
| `-to, --timeout`         | Timeout for HTTP requests (default: 10 seconds).                   |
| `-t, --threads`          | Number of concurrent threads (default: 10).                        |
| `-o, --output`           | Output file to save results.                                       |

## Usage

1. Specific URL
    ```bash
    ./honogari.py -u <URL>
    ```

2. File Containing Firebase URLs
    ```bash
    ./honogari.py -uf <URL_FILE_PATH>
    ```

3. Exploit a Vulnerable URL
    ```bash
    ./honogari.py -u <URL> -e
    ```
    or
    ```bash
    ./honogari.py -uf <URL_FILE_PATH> -e -ef <URI_FILE_NAME>
    ```

4. Customize HTTP Headers
    ```bash
    ./honogari.py -u <URL> -H '{"User-Agent": "Mozilla/5.0"}'
    ```

5. Timeout Configuration
    ```bash
    ./honogari.py -u <URL> -to 15
    ```

6. Multi-Threading
    ```bash
    ./honogari.py -uf <URL_FILE_PATH> -t 10
    ```

7. Output File
    ```bash
    ./honogari.py -u <URL> -o output.txt
    ```

## Caution

- The original author of this tool is not responsible for any misuse or malicious activities performed using this tool. You bear full responsibility for your actions and their consequences.
- Always obtain explicit permission before testing or interacting with any system, network, or application. Unauthorized access or testing may be considered illegal and could lead to severe consequences, including fines and imprisonment.
- Familiarize yourself with and adhere to the cybersecurity laws and regulations in your country or region. Ignorance of the law is not an excuse.

## License

- Honogari is licensed under MIT License

## Author
- KuroSh1ro (A1SBERG)


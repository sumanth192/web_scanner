# scanner.py
# Web Application Security Scanner
# Created by Sumanth

from sql_injection import test_sql_injection
from xss import test_xss

def scan(url):
    results = {
        'sql_injection': test_sql_injection(url),
        'xss': test_xss(url)
    }
    return results

if __name__ == "__main__":
    url = "http://example.com/search"
    results = scan(url)
    for vuln, found in results.items():
        if found:
            print(f"[!] Vulnerable to {vuln}")
        else:
            print(f"[+] Not vulnerable to {vuln}")

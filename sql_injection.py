# sql_injection.py
# Web Application Security Scanner
# Created by Sumanth

import requests

def test_sql_injection(url):
    payload = "' OR '1'='1"
    params = {'id': payload}
    response = requests.get(url, params=params)
    
    if "syntax error" in response.text.lower() or "sql" in response.text.lower():
        return True
    return False

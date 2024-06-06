# xss.py
# Web Application Security Scanner
# Created by Sumanth

import requests
from bs4 import BeautifulSoup

def test_xss(url):
    payload = "<script>alert('XSS');</script>"
    params = {'q': payload}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    if payload in str(soup):
        return True
    return False

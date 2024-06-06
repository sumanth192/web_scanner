# app.py
# Web Application Security Scanner
# Created by Sumanth

from flask import Flask, request, render_template
from scanner import scan

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan_site():
    url = request.form['url']
    results = scan(url)
    return render_template('report.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)

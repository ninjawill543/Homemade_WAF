# Homemade Web Application Firewall (WAF)

## Overview

This project implements a homemade Web Application Firewall (WAF) using Flask as a reverse proxy. The WAF is designed to protect an intentionally designed vulnerable Flask web server from common web security threats such as SQL injection and Cross-Site Scripting (XSS). It intercepts incoming requests, checks them for security vulnerabilities, and forwards them to the web server if they are deemed safe.

## Features

- **Intentionally Vulnerable Web Server**: To test our WAF, we implemented certain security vulnerabilities into our web server, such as:
    - SQL Injections: ```"INSERT INTO users (username, password) VALUES ('%s', '%s')" % (user, passw)```
    - Stored XSS: ```{% autoescape true %}``` and ```{{ c_text | safe }}```
    - Inprotected file upload:

- **Reverse Proxy**: Acts as a reverse proxy to the insecure Flask web server, intercepting incoming requests and forwarding them appropriately.

- **Content Security Policy (CSP)**: Implements CSP headers to mitigate against XSS attacks by controlling what content can be executed on the client-side.

- **SQL Injection Protection**: Checks incoming requests for SQL injection attempts, then based on the score given by the checker, either allows the request, logs it for suspicious activity, or simply blocks it.

- **Malicious IP and DDOS protection**: 

- **HTTP Verb Checking**: Only allows GET and POST requests to the site.

- **Anti-Bot Protection**:

- **File Upload Protection**: Makes sure that all uploaded files are images.

- **HTTPS Connection**


## Usage

...


## License

This project is licensed under the [MIT License](LICENSE).


## Hacking

https://github.com/ninjawill543/Homemade_WAF/assets/112950582/468efb5d-788e-4abf-826f-95f35d929369
s



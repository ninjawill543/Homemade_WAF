# Homemade WAF

-   Malicious ip / ddos
-   User agent, content type, http verb
-   Sql/xss 
-   Image upload check: gif/jpeg/jpg/png
-   Anti Bot



https://github.com/ninjawill543/Homemade_WAF/assets/112950582/468efb5d-788e-4abf-826f-95f35d929369


# Homemade Web Application Firewall (WAF)

## Overview

This project implements a homemade Web Application Firewall (WAF) using Flask as a reverse proxy. The WAF is designed to protect an intentionally designed vulnerable Flask web server from common web security threats such as SQL injection and Cross-Site Scripting (XSS). It intercepts incoming requests, checks them for security vulnerabilities, and forwards them to the web server if they are deemed safe.

## Features

- **Intentionally vulnerable web server**: 

- **Reverse Proxy**: Acts as a reverse proxy to the insecure Flask web server, intercepting incoming requests and forwarding them appropriately.

- **Content Security Policy (CSP)**: Implements CSP headers to mitigate against XSS attacks by controlling what content can be executed on the client-side.

- **SQL Injection Protection**: Checks incoming requests for SQL injection attempts, then based on the score given by the checker, either allows the request, logs it for suspicious activity, or simply blocks it.

- **Malicious IP and DDOS protection**: 

- **Upgrades HTTP connections to HTTPS**:

- **HTTP verb checking**:

- **Anti-Bot Protection**:

- **File upload Protection**:


## Usage

...


## License

This project is licensed under the [MIT License](LICENSE).



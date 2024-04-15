# Homemade Web Application Firewall (WAF)

## Overview

This project implements a homemade Web Application Firewall (WAF) using Flask as a reverse proxy. The WAF is designed to protect an intentionally designed vulnerable Flask web server from common web security threats such as SQL injection and Cross-Site Scripting (XSS). It intercepts incoming requests, checks them for security vulnerabilities, and forwards them to the web server if they are deemed safe.

## Features

- **Intentionally Vulnerable Web Server**: To test our WAF, we implemented certain security vulnerabilities into our web server, such as:
    - SQL Injections: ```"INSERT INTO users (username, password) VALUES ('%s', '%s')" % (user, passw)```
    - Stored XSS: ```{% autoescape true %}``` and ```{{ c_text | safe }}```
    - Unprotected file upload:

- **Reverse Proxy**: Acts as a reverse proxy to the insecure Flask web server, intercepting incoming requests and forwarding them appropriately.

- **Content Security Policy (CSP)**: Implements CSP headers to mitigate against XSS attacks by controlling what content can be executed on the client-side. These are the rules that we put in place: 
    - default-src 'none': Sets a default policy where nothing is allowed unless explicitly permitted.
    - script-src 'none': Specifies that no JavaScript can be executed.
    - object-src 'none': Prevents any plugins or embedded objects from being loaded.
    - base-uri 'none': Disallows the use of base URLs for relative links.
    - connect-src 'self': Only allows connections to the same origin for things like Ajax requests.
    - img-src 'self': Limits loading of images to those from the same origin.
    - style-src 'self': Permits stylesheets to be loaded only from the same origin.
    - frame-ancestors 'self': Restricts embedding of the page to the same origin frames.
    - form-action 'self': Specifies that form submissions can only be made to the same origin.
    - upgrade-insecure-requests : Automatically upgrades HTTP requests to HTTPS for enhanced security.
    - require-trusted-types-for 'script' 

    Same origin explained: The browser can only load content from itself, meaning that external websites and sources cannot be loaded.

- **SQL Injection Protection**: Checks incoming requests for SQL injection attempts by evaluating the content of each input, and giving it a score based on the amount of SQL keywords that are found. Some categories of words are worth 1 point, where others are worth 2, and if multiple words from the same category are found, the points for that category do not increase. If an input gets a score of 3, the request is allowed but logged, and if the score is 4 or higher, the request will be logged and then dropped. You can view the lists of words [here](code/checks/sql.json)

- **Malicious IP and DDOS protection**: 

- **HTTP Verb Checking**: Only allows GET and POST requests to the site. This is done by specifying the methods for each route: ```methods=['GET', 'POST']```

- **Anti-Bot Protection**:

- **File Upload Protection**: Makes sure that all uploaded files are images.

- **HTTPS Connection**: Please generate your own certificate and private key and place them in the certs folder. The current files should only be used for testing!


## Usage

...


## License

This project is licensed under the [MIT License](LICENSE).


## Hacking

https://github.com/ninjawill543/Homemade_WAF/assets/112950582/468efb5d-788e-4abf-826f-95f35d929369



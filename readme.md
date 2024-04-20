# Homemade Web Application Firewall (WAF)

## Overview

This project implements a homemade Web Application Firewall (WAF) using Flask as a reverse proxy. The WAF is designed to protect an intentionally designed vulnerable Flask web server from common web security threats such as SQL injection and Cross-Site Scripting (XSS). It intercepts incoming requests, checks them for security vulnerabilities, and forwards them to the web server if they are deemed safe.

## Features

- **Intentionally Vulnerable Web Server**: To test our WAF, we implemented certain security vulnerabilities into our web server, such as:
    - SQL Injections: ```"INSERT INTO users (username, password) VALUES ('%s', '%s')" % (user, passw)```
    - Stored XSS: ```{% autoescape true %}``` and ```{{ c_text | safe }}```

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

- **HTTP Verb Checking**: Only allows GET and POST requests to the site. This is done by specifying the methods for each route: ```methods=['GET', 'POST']```

- **Anti-Bot Protection**: Blocks malicious actors trying to spam the website by checking the client's IP addresses with VirusTotal, and banning clients sending too much requests. Two variables can be modified in the program : CHECK_LIMIT which defines when an IP will be looked up with VirusTotal, and BAN_LIMIT which defines when and IP will get banned for spamming. The code will look at the logs, and calculate the average rate of requests sent per client. If a specific client has sent over BAN_LIMIT\*average (average being the average rate of requests per client), he will be immediatly banned, all further requests will be dropped. He will also be added in /logs/blacklist.txt under the code 2. If a specific client has sent over CHECK_LIMIT\*average, it's IP address will be looked up by VirusTotal. In that case if the IP is deemed malicious, all further requests will be dropped and he's added in /logs/blacklist.txt under the code 2. If not, he added to /logs/blacklist.txt under the code 1 which means this IP has been checked, and will not get checked anymore.

- **HTTPS Connection**: Please generate your own certificate and private key and place them in the certs folder. The current files should only be used for testing!


## Usage

To use this project, you should run a python3 virtual environment. For example :

```console
$ git clone https://github.com/ninjawill543/Homemade_WAF.git
Cloning into 'Homemade_WAF'...
remote: Enumerating objects: 468, done.
remote: Counting objects: 100% (221/221), done.
remote: Compressing objects: 100% (158/158), done.
remote: Total 468 (delta 124), reused 145 (delta 62), pack-reused 247
Receiving objects: 100% (468/468), 72.30 KiB | 649.00 KiB/s, done.
Resolving deltas: 100% (255/255), done.
$ cd Homemade_WAF/
$ python3 -m venv env
$ source env/bin/activate
(env) $ pip install -r requirements.txt
```

If you're using Windows, the command to activate the environment is slighty different :

```console
 env/Scripts/activate.bat //In CMD
 env/Scripts/Activate.ps1 //In Powershel
```

Now that you've activated the environment and installed the requirements, you can run the programs (inside two different shells) :

```console
(env) $ cd code/
(env) $ python3 web_server.py
```

```console
(env) $ cd code/
(env) $ python3 WAF.py
```

You can now access the web site via the address given by the WAF.py application.

If you want the WAF to reverse lookup the IP's of the clients, the program will need an API key. Use [this documentation](https://docs.virustotal.com/docs/api-overview) to get yours. Once you have it, write it inside `code/apiKey.txt`. The program will automatically look for this file, if found it will use the key inside of it to send requests to VirusTotal.

If you want to modify the BAN_LIMIT or CHECK_LIMIT described above, you can find those global variables inside WAF.py :

```console
$ cat WAF.py | grep 'BAN_LIMIT ='
BAN_LIMIT = 2
$ cat WAF.py | grep 'CHECK_LIMIT ='
CHECK_LIMIT = 1
```

If you wish to disable the WAF protection to view the original site, simply change line 10 of WAF.py to False.

## License

This project is licensed under the [MIT License](LICENSE).


## Hacking

https://github.com/ninjawill543/Homemade_WAF/assets/112950582/468efb5d-788e-4abf-826f-95f35d929369



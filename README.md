anonymous_requests
=====
This project implements 2 classes -
**PyTor** and **PyVpn** which can be used for anonymzing web requests without revealing your identity.
It can be used for scraping the web without getting blocked by the sites.


**PyTor**
=====
python wrapper for anonymizing (web scraping?) requests using Tor.
PyTor allows you to channel simple http requests through a Tor proxy.
Intially forked from https://github.com/bdheath/pytor -  This code was not proper , So I am **rewriting** the entire thing
with extra features (#TODOs)

(some of the readme content is from readme at https://github.com/bdheath/pytor )

#### Requirements

* A functioning (and running) instance of Tor. 
This could be the basic Tor Browser Bundle. 
For more configuration options, consider using the Tor Expert Bundle, 
available from https://www.torproject.org/download/download.html.en.
*Install python dependancy modules, run: pip install -r requirements.txt in your shell.

#### Basic usage

Create a basic Pytor instance and send a simple http request:
```Python

#import depending on your folder structure
#from pytor import PyTor

import requests

r = requests.get(url='http://icanhazip.com/')
if (r.status_code == 200):
    ip = r.text
print("without TOR, ip = ",tor.ip())



tor = PyTor(host='10.140.5.78', need_control=True, control_port=9051, socks_port=9050, password='password')
# tor.ip() gives the ip address that the site (http://icanhazip.com/ in this case) sees which is one of the ips of tor exit nodes
print("With TOR,current ip = ",tor.ip())

# request through tor proxy
r = tor.get(url="http://www.thehindu.com/")

if (r.status_code == 200):
    print(r.text)
elif(r.status_code == 429):
    # get new ip address from tor proxy
    # You can call get_new_identity() when you get status code of 429 TOO MANY REQUESTS(https://httpstatuses.com/429)
    # from sites when you are scraping
    tor.get_new_ip()
    print("With TOR,new ip = ", tor.ip())

```

**PyVpn**
=====
python wrapper for anonymizing (web scraping?) requests using **free** VPNs available over the web.
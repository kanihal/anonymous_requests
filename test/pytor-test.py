import sys
sys.path.append('../')

from pytor import PyTor
import requests

r = requests.get(url='http://icanhazip.com/')
if (r.status_code == 200):
    ip = r.text

tor = PyTor(host='10.130.4.162', need_control=True, control_port=9051, socks_port=9050, password='password')

print("Without Tor, my IP address is     : " + str(ip))
print("With Tor, my IP address is        : " + tor.ip())
print("Getting new Ip from Tor #####")

#call get_new_identity when you get status code of 429 TOO MANY REQUESTS s( https://httpstatuses.com/429 )
tor.get_new_identity()
print("Now my IP address is              : " + tor.ip())


r=tor.get(url="http://www.thehindu.com/")

if(r.status_code==200):
    print(r.text)

r = tor.get(url="http://www.thehindu.com/")

if (r.status_code == 200):
    print(r.text)
elif(r.status_code == 429):
    # get new ip address from tor proxy
    tor.get_new_ip()
    print("With TOR,new ip = ", tor.ip())


#ua = UserAgent()
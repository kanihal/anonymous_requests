import requests

tor_proxy = 'socks5://10.130.4.162:9050' #lab machine
socks_proxy = { 'http': tor_proxy,
                'https': tor_proxy
                }

current_ip = requests.get(url='http://icanhazip.com/',proxies=socks_proxy,verify=False)

print(current_ip.text)
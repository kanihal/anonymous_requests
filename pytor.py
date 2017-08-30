"""
PyTor
python wrapper for anonymizing (web scraping?) requests using Tor.

Intially forked from https://github.com/bdheath/pytor -  This code was not proper , So I am rewriting the entire thing

"""

from stem.control import Controller
from stem import Signal
import requests

from datetime import datetime





class PyTor:
    def __init__(self, host='localhost', socks_port=9050, need_control=False, control_port=9051, password=''):

        self.host = host
        self.socks_port = socks_port
        self.need_control = need_control
        self.control_port = control_port
        self.password=password
        self.proxies = {}
        self.proxies['http'] = 'socks5://' + str(self.host) + ':' + str(self.socks_port)
        self.proxies['https'] = 'socks5://' + str(self.host) + ':' + str(self.socks_port)

        if self.need_control:
            self.controller = Controller.from_port(address=self.host, port=control_port)
            self.controller.authenticate(self.password)
        else:
            self.controller = None
        return


    def get(self, url, timeout=30):
        response = requests.get(url, timeout=timeout, proxies=self.proxies)
        return response

    def post(self):
        # TODO - get post : pass along the kwargs
        pass

    def ip(self):
        response = self.get('http://icanhazip.com/')  # standard url
        if response.status_code==200:
            self._ip=response.text
            return self._ip
        else:
            return None

    def get_new_ip(self):
        if not self.controller:
            self.controller = Controller.from_port(address=self.host, port=self.control_port)
            self.controller.authenticate(self.password)
        self.controller.signal(Signal.NEWNYM)
        return

    def get_new_user_agent(self):
        # TODO - some sites block tor exit nodes - add user agent randomizer etc to fix this
        pass

    def set_renew_period(self):
        # TODO - renew on certain intervals interval (multi threading)
        pass

    def get_new_identity(self):
        self.get_new_ip()
        self.get_new_user_agent()



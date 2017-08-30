from stem import Signal
from stem.control import Controller


def get_new_ip():
    """Change IP using TOR"""
    with Controller.from_port(address = '10.130.4.162', port=9051) as controller:
        controller.authenticate(password='password')
        controller.signal(Signal.NEWNYM)

get_new_ip()

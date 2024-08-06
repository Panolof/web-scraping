from itertools import cycle

def get_proxies():
    return [
        "http://username:password@proxy1:port",
        "http://username:password@proxy2:port",
        "http://username:password@proxy3:port"
    ]

def rotate_proxies():
    proxies = get_proxies()
    return cycle(proxies)

import ctypes
import threading
import proxy
import requests
from colorama import Fore, init



init()
def Download():
    global count
    global proxs


    timeout = "10000"
    print("\n")

    proxy.DownloadProxies(timeout=timeout)

    print("\n")
    proxs = proxy.proxies
    count = proxy.proxy_count

global counter
counter = 0

global working_proxies  
working_proxies = []

def gen_working_proxies(proxy, **kwargs):
    global counter
    proxies = {
        'https': 'http://' + proxy + '/'
    }
    try:
        r = requests.get("https://ifconfig.me/", proxies=proxies)
       
        print(f"{Fore.WHITE}Proxy : {Fore.MAGENTA}{proxy}{Fore.WHITE} Works!") 
        working_proxies.append(proxy)
    except:
        pass

    counter += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Checking Proxies : {counter} / {count}")


Download()

for proxies in proxs:
    args = f'{proxies}'
    thread = threading.Thread(target=gen_working_proxies, args=(args,))
    thread.start()


    

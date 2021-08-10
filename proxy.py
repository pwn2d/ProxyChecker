import requests
from colorama import Fore, init

init()

def DownloadProxies(anonymity="all", timeout="10000", ssl="all"):
    f=open("proxies.txt", "w+")
    url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country=all&ssl={ssl}&anonymity={anonymity}'
    r = requests.get(url)
    f.write(r.text)
    f.close()
    global proxies
    proxies = []
    f=open("proxies.txt", "r")
    for line in f:
        proxy = line.strip("\n")
        if proxy == "":
            pass
        else:
            proxies.append(proxy)
    global proxy_count
    proxy_count = str(len(proxies))
    proxy_count_int = len(proxies)
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Downloaded {Fore.GREEN}{str(len(proxies))} {Fore.WHITE}Proxies.")


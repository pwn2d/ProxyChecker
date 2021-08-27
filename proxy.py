import os

def install():
    print("[-] Installing Dependencies...")
    os.system("pip install colorama")
    os.system("pip uninstall urllib3")
    os.system("pip install urllib3==1.26.6")
    os.system("pip install requests")
    os.system("pip install requests[socks]")

try:
    import urllib3
    import requests
except:
    install()

try:
    from colorama import Fore, init

except:
    os.system("pip install colorama")

init()

def Check_Compatibility():
    try:
        import requests
        import urllib3
    except:
        install()
    print(f"Requests Version : {Fore.GREEN}" + requests.__version__ + Fore.RESET)
    try:
        if urllib3.__version__ != "1.26.6":
            print(f"Urllib3 Version {Fore.RED}: " + urllib3.__version__+f"{Fore.YELLOW}(Incompatible){Fore.RESET}")
        else:
            print(f"Urllib3 Version :{Fore.GREEN} " + urllib3.__version__ + f"{Fore.RESET}")
    except:
        pass

#os.system("pip uninstall urllib3")

try:
    if urllib3.__version__ != "1.26.6":
        install()
except:
    pass

try: 
    import requests
    from colorama import Fore, init
    import ctypes
    import threading
    import time
except:
    install()




try:
    init()
except NameError:
    print("[+] Installed Packages Successfully!")
    print("\n[+] Module Is Now Ready For Use!")

global working_proxies
global counter
working_proxies = []
counter = 0

def Download_Proxies(anonymity="all", timeout="10000", ssl="all", Download_Timeout=1000):
    f=open("proxies.txt", "w+")
    url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country=all&ssl={ssl}&anonymity={anonymity}'
    url2 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all'
    r = requests.get(url, timeout=Download_Timeout)
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
    global proxy_count_int
    proxy_count = str(len(proxies))
    proxy_count_int = len(proxies)
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Downloaded {Fore.GREEN}{str(len(proxies))} {Fore.WHITE}Proxies.")

def Download_Socks4_Proxies(anonymity="all", timeout="10000", ssl="all", Download_Timeout=1000):
    f=open("proxies.txt", "w+")
    url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout={timeout}&country=all&ssl={ssl}&anonymity={anonymity}'
    url2 = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all'
    r = requests.get(url2, timeout=Download_Timeout)
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
    global proxy_count_int
    proxy_count = str(len(proxies))
    proxy_count_int = len(proxies)
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}]{Fore.WHITE} Downloaded {Fore.GREEN}{str(len(proxies))} {Fore.WHITE}Proxies.")

def checker(proxy):
    global counter
    proxies = {
        'https': 'http://' + proxy + '/'
    }
    try:
        r = requests.get("https://ifconfig.me/", proxies=proxies, timeout=10)
        if len(r.content) > 50:
            pass
        else:
            #print(f"Response Content : {r.text}")
            working_proxies.append(proxy)
    except:
        pass

    counter += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Checking Proxies : {counter} / {proxy_count}")

def Checker_Socks4(proxy):
    global r
    global counter
    try:
        proxies = {'http': 'socks4://' + proxy}
        
        r = requests.get("https://ifconfig.me/", timeout=5, proxies=proxies)
        if len(r.content) > 50:
            pass
        else:
            #print(f"Response Content : {r.text}")
            working_proxies.append(proxy)
    except:
        pass

    counter += 1
    ctypes.windll.kernel32.SetConsoleTitleW(f"Checking Proxies : {counter} / {proxy_count}")

def Check_Proxies():
    global proxies
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}-{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Checking Downloaded Proxies...")
    for proxy in proxies:
        args = f'{proxy}'
        thread = threading.Thread(target=checker, args=(args,))
        thread.start()

def Check_Socks_Proxies():
    global proxies
    print(f"{Fore.LIGHTBLACK_EX}[{Fore.YELLOW}-{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Checking Downloaded Proxies...")
    for proxy in proxies:
        args = f'{proxy}'
        thread = threading.Thread(target=Checker_Socks4, args=(args,))
        thread.start()

def Append_Working_Proxies_to_File():
    try:
        os.remove("proxies.txt")
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Removed proxies.txt")
    except:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}-{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Couldn't Remove proxies.txt, Maybe It Doesn't Even Exist, Skipping...")
    
    time.sleep(1)
    
    try:
        file=open("proxies.txt", "w")
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}+{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Recreated proxies.txt, Writing Working Proxies Into File...")
    except:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}x{Fore.LIGHTBLACK_EX}] {Fore.WHITE}Couldn't ReAdd proxies.txt :/")
    
    time.sleep(0.5)

    for proxy in working_proxies:
        file.write(proxy + "\n")




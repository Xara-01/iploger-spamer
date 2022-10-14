import requests, threading; from pystyle import *; from os import system;import httpx; import random;

# Setup 

System.Size(110,30)                                                                                                                                                                                                                                ,System.Title("title x.e.r.t.a.s. .-. .x.a.r.a.".replace('.',''))
white = Col.white
green = Col.light_green
red = Col.red
purple = Col.light_blue
yelow = Col.yellow

faild = 0
scc = 0
sent = 0
lock = threading.Lock()
# Setup

def Body():
    try:
        system("cls")
    except:
        system("clear")
    banner = """
    \n
                                    ██╗  ██╗███████╗██████╗ ████████╗ █████╗ ██╗  ██╗
                                    ╚██╗██╔╝██╔════╝██╔══██╗╚══██╔══╝██╔══██╗╚██╗██╔╝
                                     ╚███╔╝ █████╗  ██████╔╝   ██║   ███████║ ╚███╔╝ 
                                     ██╔██╗ ██╔══╝  ██╔══██╗   ██║   ██╔══██║ ██╔██╗ 
                                    ██╔╝ ██╗███████╗██║  ██║   ██║   ██║  ██║██╔╝ ██╗
                                    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
                                                                                                         
                                                    Made by >_xara

    """
    print(Colorate.Horizontal(Colors.blue_to_purple, banner, 4))
Body()

url = Write.Input("link Graber -> ", Colors.purple, interval=0.02)
thread = Write.Input("Thread -> ", Colors.blue, interval=0.02)
Proxye = Write.Input("Proxy list -> ", Colors.purple, interval=0.03)
def proxy_list():
    with open(Proxye, "r+")as f:
        pro = random.choice(f.readlines())
        f.close()
        return pro


def Star():
    global scc
    global sent
    global faild
    sent += 1
    try:
        httpx.post(url,headers={'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",     'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin',}, proxies={"http://": "http://"+proxy_list(), "https://": "http://"+proxy_list()})
        lock.acquire()
        scc += 1
        lock.release()
    except:
        lock.acquire()
        faild += 1
        lock.release()


def Amaterasu():
    Body()

    for i in range(int(thread)):
        threading.Thread(target=Star).start()
        print(f"{purple}Sent -> {yelow}{sent}  {white}|  {purple}Failed -> {red}{faild}  {white}|  {purple}succes -> {green}{scc}", end="\r")
    print("\n")
    Write.Input(f"[!] Finished ", Colors.red, interval=0.03)
Amaterasu()

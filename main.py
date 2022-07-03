# -*- coding: utf-8 -*-
import time
from requests import request
import requests
import vk_api
import random
import urllib.request, json
from config import *

uquestions = []
uanswers = []
utoken = ''
lsat = ""
def send(answer):
    vk.method("messages.send", {"peer_id": peer_id, "message": answer, "random_id": random.randint(1, 2147483647)})

def proxies():
    all_proxies = requests.get('https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt').text.splitlines()
    i=0
    check = False
    while not chec:
        i+=1
        proxy = all_proxies[i]
        chec = requests.get("https://vk.com",{'https': 'http://%s' % (proxy)})
    return proxy





def phoneget(phone):
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
    try:
        infoPhone = urllib.request.urlopen( getInfo )
        send("телефон найден")
    except Exception:
        send("телефон не найден")
    infoPhone = json.load(infoPhone)
    send(f'Номер сотового: {phone} \n Страна: {infoPhone["country"]["name"]} \n Регион: {infoPhone["region"]["name"]} \n Округ: {infoPhone["region"]["okrug"]} \n Оператор: {infoPhone["0"]["oper"]} \n Часть света: {infoPhone["country"]["location"]}')


def ipget(getIP):
    url = "https://ipinfo.io/" + getIP + "/json"

    try:
        getInfo = urllib.request.urlopen( url )
        send( "IP найден!" )
    except Exception:
        send( "IP не найден!" )
    send( "Обработка...")
    send("Вывод:")
    infoList = json.load(getInfo)
    send(f"IP: {infoList['ip']} \n City: {infoList['city']} \n Region: {infoList['region']} \n Country: {infoList['country']} \n Hostname: {infoList['hostname']} ")

def cs(username):
    uls=[f'https://vk.com/{username}',f'https://www.youtube.com/user/{username}',f'https://www.pinterest.ru/{username}',f'https://www.twitch.tv/{username}',f'https://likee.video/@{username}',f'https://ok.ru/{username}',f'https://www.github.com/{username}',f'https://www.tiktok.com/@{username}']
    print("Проверка...")
    for site in uls:
        try:
            resp = requests.get(site)
        except Exception:
            print('error')
        if str(resp.status_code) == "200":
            send(str(site))
            print(str(site))


vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            peer_id = messages["items"][0]["last_message"]["from_id"]
            text = messages["items"][0]["last_message"]["text"]
            text = text.lower()
            
            if text == 'начать' or text == "help":
                send('Функции:')
                #send('Спам \n информация о номере \n Пример команды: \n спам +7********* ')
                send("Показать комманды - help")
                send("Информация о номере. \n Пример команды: \n +7********* ")
                send("Информация о ip адресе. \n Пример команды: \n ip 0.0.0.0 ")
                send("Поиск по соцсетям. \n Пример команды: \n social mishka324 ")
                
                
            elif "+" in text:
                print(text)
                send("Обработка...")
                phoneget(text)
                send('Конец данных.')
                
                
            elif "ip" in text:
                text = text.replace('ip ','')
                print(text)
                ipget(text)
                send('Конец данных.')
                
            elif "social" in text:
                text = text.replace('social ','')
                username = text
                cs(username)
                send('Конец данных.')

                
            else:
                send("Неверная команда!")
    except Exception as E:
        time.sleep(1)
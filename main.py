# -*- coding: utf-8 -*-
import time
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


def phoneget(phone):
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
    try:
        infoPhone = urllib.request.urlopen( getInfo )
        send("телефон найден")
    except:
        send("телефон не найден")
    infoPhone = json.load(infoPhone)
    send(f'Номер сотового: {phone} \n Страна: {infoPhone["country"]["name"]} \n Регион: {infoPhone["region"]["name"]} \n Округ: {infoPhone["region"]["okrug"]} \n Оператор: {infoPhone["0"]["oper"]} \n Часть света: {infoPhone["country"]["location"]}')


def ipget(getIP):
    url = "https://ipinfo.io/" + getIP + "/json"

    try:
        getInfo = urllib.request.urlopen( url )
        send( "IP найден!" )
    except:
        send( "IP не найден!" )
    send( "Обработка...")
    send("Вывод:")
    infoList = json.load(getInfo)
    send(f"IP: {infoList['ip']} \n City: {infoList['city']} \n Region: {infoList['region']} \n Country: {infoList['country']} \n Hostname: {infoList['hostname']} ")
    



vk = vk_api.VkApi(token=TOKEN)
vk._auth_token()
while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            peer_id = messages["items"][0]["last_message"]["from_id"]
            text = messages["items"][0]["last_message"]["text"]
            text = text.lower()
            
            if text == 'начать':
                send('Функции:')
                #send('Спам \n информация о номере \n Пример команды: \n спам +7********* ')
                send("Информация о номере. \n Пример команды: \n +7********* ")
                send("Информация о ip адресе. \n Пример команды: \n ip 127.0.0.1 ")
                
                
            if "+" in text:
                print(text)
                send("Обработка...")
                phoneget(text)
                
                
            if "ip" in text:
                text = text.replace('ip ','')
                print(text)
                ipget(text)
            else:
                send("Неверная команда!")
    except Exception as E:
        time.sleep(1)
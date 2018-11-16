from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime

Tag = '#container > div.substance > div.sub_contents > table > tbody > tr '
URL = 'http://ace.gachon.ac.kr/dormitory/reference/menu'
req = requests.get(URL)
html = req.text

soup = BeautifulSoup(html, 'html.parser')


def keyboard(request):
    return JsonResponse({
        "type": "buttons",
        "buttons": ["오늘",'내일']
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    time = datetime.now()
    date = time.day

    if datacontent == '오늘':
        return JsonResponse({
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침','점심','저녁']
            }
        })

    elif datacontent == '내일':
        date=date+1
        return JsonResponse({
            'keyboard': {
                'type': 'buttons',
                'buttons': ['아침','점심','저녁']
            }
        })

    if datacontent == '아침':
        menu = [0,0,0]
        i = 0
        for cho in soup.select(Tag):
            a = re.sub('월|일', ' ', cho.find('th').text)
            a[-3:]
            list = a.split()
            day = int(list[1])
            for cho2 in cho.select('td'):
                if day == date.day:
                    menu[i] = cho2.text
                    i+=1
        return JsonResponse({
            'message': {
                menu[0]
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘','내일']
            }
        })

    if datacontent == '점심':
        menu = [0,0,0]
        i = 0
        for cho in soup.select(Tag):
            a = re.sub('월|일', ' ', cho.find('th').text)
            a[-3:]
            list = a.split()
            day = int(list[1])
            for cho2 in cho.select('td'):
                if day == date.day:
                    menu[i] = cho2.text
                    i+=1
        return JsonResponse({
            'message': {
                menu[1]
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘','내일']
            }
        })

    if datacontent == '저녁'
        menu = [0,0,0]
        i = 0
        for cho in soup.select(Tag):
            a = re.sub('월|일', ' ', cho.find('th').text)
            a[-3:]
            list = a.split()
            day = int(list[1])
            for cho2 in cho.select('td'):
                if day == date.day:
                    menu[i] = cho2.text
                    i+=1
        return JsonResponse({
            'message': {
                menu[2]
            },
            'keyboard': {
                'type': 'buttons',
                'buttons': ['오늘','내일']
            }
        })

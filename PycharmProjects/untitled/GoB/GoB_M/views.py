from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import requests
from bs4 import BeautifulSoup
import re

Tag = '#container > div.substance > div.sub_contents > table > tbody > tr '
URL = 'http://ace.gachon.ac.kr/dormitory/reference/menu'
req = requests.get(URL)
html = req.text

soup = BeautifulSoup(html, 'html.parser')


def keyboard(request):
    return JsonResponse({
        "type": "buttons",
        "buttons":["오늘","내일"]
    })


@csrf_exempt
def answer(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent=='오늘':
        for cho in soup.select(Tag):
            a = re.sub('월|일', ' ', cho.find('th').text)
            a[-3:]
            list = a.split()
            day = int(list[1])
            date = datetime.now()
            for cho2 in cho.select('td'):
                    menu = cho2
        return JsonResponse({
            'message': {
                'text': menu
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['오늘','내일']
            }
        })

    elif datacontent=='내일':
        for cho in soup.select(Tag):
            a = re.sub('월|일', ' ', cho.find('th').text)
            a[-3:]
            list = a.split()
            day = int(list[1])
            date = datetime.now()
            for cho2 in cho.select('td'):
                if day == date.day + 1:
                    menu = cho2
        return JsonResponse({
            'message': {
                'text': menu
            },
            'keyboard': {
                'type': 'buttons',
                'buttons':['오늘','내일']
            }
        })

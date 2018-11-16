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
        "type":"text"
    })
 
@csrf_exempt
def answer(request):
 
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
    
    if datacontent=='오늘':
        for cho in soup.select(Tag):
            for cho2 in cho.select('td'):
                a = re.sub('월|일', ' ', cho.find('th').text)
                a[-3:]
                list = a.split()
                month = int(list[0])
                day = int(list[1])
                date = datetime.now()
                if month == date.month and day == date.day:
                    menu=cho2
        return JsonResponse({
                'message': {
                    'text': '오늘 메뉴' + menu
                },
                'keyboard':{
                    'type':'text'
                }
        })

    if datacontent :
        for cho in soup.select(Tag):
            for cho2 in cho.select('td'):
                a = re.sub('월|일', ' ', cho.find('th').text)
                a[-3:]
                list = a.split()
                month = int(list[0])
                day = int(list[1])
                date = datetime.now()
                if month == date.month and day == date.day+1:
                    menu=cho2
        return JsonResponse({
                'message': {
                    'text': '내일 메뉴' + menu
                },
                'keyboard':{
                    'type':'text'
                }
        }) 

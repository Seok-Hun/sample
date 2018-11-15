from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import urllib.request
 
def request(url):
 http_response = urllib.request(url)
 byte_data     = http_response.read()
 text_data     = byte_data.decode('utf-8')
 return text_data
 
shool_menu = request(http://ace.gachon.ac.kr/dormitory/reference/menu)

def keyboard(request):
 
    return JsonResponse({
        'type':'buttons',
        'buttons':['오늘','내일']
    })
 
@csrf_exempt
def answer(request):
 
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']
 
    if datacontent == '오늘':
        today = "오늘 급식"
 
        return JsonResponse({
                'message': {
                    'text': today
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘','내일']
                }
 
            })
 
    elif datacontent == '내일':
        tomorrow = "내일 급식"
 
        return JsonResponse({
                'message': {
                    'text': tomorrow
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['오늘','내일']
                }
        })

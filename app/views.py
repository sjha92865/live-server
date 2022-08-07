from django import http
from django.shortcuts import render,redirect
import requests
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json
# Create your views here.
import datetime

from bs4 import BeautifulSoup

def newproject(request):
    return render(request,'ticket_index.html')

def mend2(request):
    # datas=req
    # return JsonResponse({'data':datas})
    # print('hello')
    url= request.POST.get("first_name")

    r = requests.get(url)
    soup = BeautifulSoup(r.content,"html.parser")

    title = soup.find("meta", property="og:title")
    url = soup.find("meta", property="og:url")
    image = soup.find("meta", property="og:image")
    description = soup.find("meta", property="og:description")
    datas={
        "title":title["content"] if title else "No meta title given",
        "url":url["content"] if url else "No meta url given" ,       
        "image":image["content"] if url else "No meta image given",
        "description":description["content"] if url else "No meta description given"
    }
    
    # print(title["content"] if title else "No meta title given")
    # print(url["content"] if url else "No meta url given")
    # print(image["content"] if url else "No meta image given")

    # print(description["content"] if url else "No meta description given")
    # print(datas)
    return JsonResponse(datas)
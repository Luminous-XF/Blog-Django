from django.shortcuts import render, HttpResponse
from blogapp.models import UserInfo


def index(request):
    UserInfo.objects.create(name="蹦蹦", age="12", password="abc")
    return HttpResponse("Hello World!")

from django.shortcuts import render, HttpResponse
from blogapp.models import UserInfo


def index(request):
    return HttpResponse("Hello World!")


def insertData(request):
    UserInfo.objects.create(name="跳跳", age=13, password="def")
    UserInfo.objects.create(name="吵吵", age=14, password="ghi")

    return HttpResponse("Insert success!")


def queryAll(request):
    userList = UserInfo.objects.all()
    for user in userList:
        print(user.id, user.name, user.age, user.password)

    return HttpResponse("Query ok!")


def queryById(request):
    userList = UserInfo.objects.filter(id=2)
    for user in userList:
        print(user.id, user.name, user.age, user.password)

    return HttpResponse("Query ok!")


def updateById(request):
    UserInfo.objects.filter(id=2).update(password="123")

    return HttpResponse("Query ok!")


def deleteById(request):
    UserInfo.objects.filter(id=3).delete()

    return HttpResponse("Query ok!")

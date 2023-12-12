from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from blogapp.models import UserInfo
import uuid
from blogapp.models import Post
from blogapp.models import User


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


def queryData(request):
    data = dict()
    post = Post.objects.filter(id=1).first()
    data['title'] = post.title
    data['type'] = post.type

    res = dict()
    res["data"] = data
    res["code"] = "200"
    res["msg"] = "请求成功"

    return HttpResponse(JsonResponse(res))


def queryPostById(request):
    """
    查询 id 为 2 的帖子的所有信息
    :param request:
    :return:
    """
    data = dict()
    postList = Post.objects.filter(id=2).first()
    data['title'] = postList.title
    data['type'] = postList.type
    data['content'] = postList.content
    data['comment_count'] = postList.comment_count
    data['score'] = postList.score
    data['status'] = postList.status
    data['likes'] = postList.likes
    data['page_views'] = postList.page_views
    data['create_time'] = postList.create_time
    data['update_time'] = postList.update_time
    data['row_status'] = postList.row_status

    res = dict()
    res["data"] = data
    res["code"] = "200"
    res["msg"] = "请求成功"

    return HttpResponse(JsonResponse(res))


def queryPostList(request):
    """
    查询所有帖子信息
    :param request:
    :return:
    """
    data = dict()
    data["PostList"] = list()
    postList = Post.objects.all()
    for user in postList:
        postINfo = dict()
        postINfo['title'] = user.title
        postINfo['type'] = user.type
        postINfo['content'] = user.content
        postINfo['comment_count'] = user.comment_count
        postINfo['score'] = user.score
        postINfo['status'] = user.status
        postINfo['page_views'] = user.page_views
        postINfo['create_time'] = user.create_time
        postINfo['update_time'] = user.update_time
        postINfo['row_status'] = user.row_status
        postINfo['likes'] = user.likes
        data["PostList"].append(postINfo)
    res = dict()
    res["data"] = data
    res["code"] = "200"
    res["msg"] = "请求成功"

    return HttpResponse(JsonResponse(res))


def queryUserByUsername(request):
    """
    根据用户名查询某个用户的信息
    :param request:
    :return:
    """
    data = {}
    UserList = User.objects.filter(username="哈哈").first()
    postCount = Post.objects.filter(user_id=UserList.uuid).count()
    data["uuid"] = UserList.uuid
    data["nickname"] = UserList.nickname
    data["password"] = UserList.password
    data["salt"] = UserList.salt
    data["email"] = UserList.email
    data["user_type"] = UserList.user_type
    data["user_satus"] = UserList.user_satus
    data["activation_code"] = UserList.activation_code
    data["headerUrl"] = UserList.header_url
    data["create_time"] = UserList.create_time
    data["gender"] = UserList.gender
    data["brief"] = UserList.brief
    data["likes"] = UserList.likes
    data["pageViews"] = UserList.page_views
    data["postCount"] = postCount
    res = dict()
    res["data"] = data
    res["code"] = "200"
    res["msg"] = "请求成功"

    return HttpResponse(JsonResponse(res))
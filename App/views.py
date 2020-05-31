import os

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from App.models import User, Goods
from django0527 import settings


def index(request):
    username = request.COOKIES.get('user','')
    headimg_path = ''

    if username:
        users = User.objects.values_list("headimg").filter(username=username)
        # filter(username=username)
        if users.count():
            # 获取到数据库中的 头像名称
            headimg_name = users[0][0]
            headimg_path = os.path.join('upload',headimg_name)

    return render(request,'index.html',context={'user':username,'headimg':headimg_path})


def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        headimg = request.FILES.get('headimg')
        headimg_name = '{}-{}'.format(username,headimg.name)

        filepath = os.path.join(settings.upload_path,headimg_name)
        # 获取到的头像写到本地
        with open(filepath,'wb') as f:
            for i in headimg.chunks():
                f.write(i)


        user = User()
        user.username = username
        user.password = password
        user.tel = tel
        user.headimg = headimg_name
        user.save()

        response = redirect("app:login")

        response.set_cookie("user",username)


        # return HttpResponse('{}{}{}'.format(username,password,tel))

        return response

def goods(request,num=0):
    return HttpResponse("这里是商品页，这里访问的页码是 {}".format(num))


def detail(request,a,b):
    return HttpResponse("测试url中含有多个参数{}，{}".format(a,b))


def requesttest(request):
    data = {
        "path":request.path,
        "methor":request.method,
        "get参数":request.GET
    }
    return render(request,'requesttest.html',context=data)


def gettest(request):
    name = request.GET.get('name')
    age = request.GET.get('age',10)
    return HttpResponse("get参数是：名字：{},年龄：{}".format(name,age))


def responsetest(request):
    response = HttpResponse('常规的文本输出返回')
    # 模板的返回
    response = render(request,"index.html")
    # 重定向 ， 本应该访问该视图， 重定向别的连接去了
    response = HttpResponseRedirect('/goods.html')
    # 另外一种重定向的方法
    response = redirect('/goods.html')

    # 视图里面的反向解析,可添加参数
    response = redirect('app:goods',13)
    # 重定向页可以添加参数
    # response = redirect('/goods.html',13)

    str1 = {
        "name":"123",
        "age":19
    }

    response = JsonResponse(str1)
    return response


def logout(request):
    response = HttpResponse("已退出登录")
    response.delete_cookie('user')
    return response


def login(request):
    if request.method =='GET':
        return render(request,"login.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        users = User.objects.filter(username=username).filter(password=password)
        if users.count() > 0:
            response = redirect("app:index")
            response.set_cookie("user",username)
        else:
            response = HttpResponse("账号或密码错误")
        return response


def show_static(request):
    return render(request,"show_static.html")


def test_process_request(request):
    return HttpResponse('测试路由分配的view函数')


def goodlist(request,page=1):
    goodlist = Goods.objects.all()
    # 对goodlist 所有商品 按每页 5个商品来分页
    paginator = Paginator(list(goodlist),5)
    # 获取当前页的商品
    pageObj = paginator.page(page)
    # 所有的页码
    pagelist = pageObj.paginator.page_range

    # 参数为页码，返回该页码的所有商品 + 所有的页码列表
    return render(request,'goodlist.html',context={'pageObj':pageObj, 'pagelist':pagelist})
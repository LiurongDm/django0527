from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        tel = request.POST.get('tel')



        # return HttpResponse('{}{}{}'.format(username,password,tel))

        return render(request,"index.html")


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
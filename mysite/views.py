
from django.contrib import auth
from django.shortcuts import redirect, render
from django.urls import reverse

def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')

    user = auth.authenticate(request, username=username, password=password)

    # 获取请求的页面地址，如果无则返回首页
    referer = request.META.get('HTTP_REFERER',reverse('home')) #将首页别名 home 反向解析成正常的链接

    if user is not None:
        auth.login(request, user)
        # Redirect to a sucess page
        return redirect(referer)  #登录成功后返回到原来页面
    else:
        return render(request, 'error.html',{'message':'用户名或密码不正确'})

from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .models import MyUser
from .form import MyUserCreationForm
from django.contrib.auth.models import Permission
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required


# 使用表单实现用户注册
def registerView(request):
    userLogin = False
    if request.method == 'POST':
        user = MyUserCreationForm(request.POST)
        if user.is_valid():
            user.save()
            tips = '注册成功'
            # 添加权限
            u = user.instance
            p = Permission.objects.filter(codename='vip_myuser')[0]
            u.user_permissions.add(p)
            return redirect(reverse('user:login'))
        else:
            tips = '注册失败'
    user = MyUserCreationForm()
    return render(request, 'user.html', locals())


# 用户登录
def loginView(request):
    tips = '请登录'
    userLogin = True
    if request.method == 'POST':
        u = request.POST.get('username', '')
        p = request.POST.get('password1', '')
        if MyUser.objects.filter(username=u):
            user = authenticate(username=u, password=p)
            if user:
                if user.is_active:
                    # 登录当前用户
                    login(request, user)
                return redirect(reverse('user:info'))
            else:
                tips = '账号密码错误，请重新输入'
        else:
            tips = '用户不存在，请注册'
    user = MyUserCreationForm()
    return render(request, 'user.html', locals())


# 退出登录
def logoutView(request):
    logout(request)
    return redirect(reverse('user:login'))


# 用户中心
# login_required判断用户是否已登录。
# permission_required判断当前用户是否具备某个权限
@login_required(login_url='/login.html')
@permission_required(perm='user.vip_myuser', login_url='/login.html')
def infoView(request):
    return render(request, 'info.html', locals())

# # 使用函数has_perm实现装饰器permission_required功能
# from django.shortcuts import render, redirect
# @login_required(login_url='/login.html')
# def infoView(request):
#     u = request.user
#     if u.has_perm('user.vip_myuser'):
#         return render(request, 'info.html', locals())
#     else:
#         return redirect(reverse('user:login'))
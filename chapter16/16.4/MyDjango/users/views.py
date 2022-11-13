from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from rest_framework_jwt.utils import jwt_decode_handler
from django.forms.models import model_to_dict
from rest_framework_jwt.settings import api_settings
from django.contrib.auth import authenticate

def login(username, password):
    data = {'code': '400'}
    # 验证用户的账号密码是否正确
    vu = authenticate(username=username, password=password)
    if vu:
        user = User.objects.filter(username=username).first()
        # 根据用户创建对应的token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        data = {
            'username': user.username,
            'password': user.password,
            'token': token,
            'code': '200'
        }
    return data

# code=100代表是GET请求
# code=200代表登录成功
# code=400代表登录失败，密码不正确
# code=201代表用户注册成功
@csrf_exempt
def userView(request):
    data = {'code': '100'}
    if request.method == 'POST':
        serializer = UserSerializer(data=request.POST)
        # serializer.is_valid()验证成功说明用户尚未创建
        # 使用UserSerializer创建用户，触发自定义函数create()
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            data['code'] = '201'
        # serializer.is_valid()验证失败说明用户存在，调用函数login登录用户
        else:
            datas = login(request.POST['username'],
                          request.POST['password'])
        data.update(datas)
    print(data)
    return JsonResponse(data)

# code=200代表用户信息获取成功
# code=400代表用户信息获取失败，即jwt_decode_handler验证失败
def getView(request):
    data = {'code': '400'}
    username = ''
    token = request.GET.get('token')
    # 接收token解析后的值，即通过token获取用户信息
    try:
        toke_user = jwt_decode_handler(token)
        username = toke_user['username']
    except: pass
    if username:
        getUser = User.objects.filter(username=username).first()
        if getUser:
            # model_to_dict将模型字段转换为字典格式表示
            exclude = ['date_joined', 'last_login']
            getUser = model_to_dict(getUser, exclude=exclude)
            data['code'] = '200'
            data.update(getUser)
    return JsonResponse(data)
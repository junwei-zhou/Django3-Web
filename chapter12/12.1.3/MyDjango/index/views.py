from .models import PersonInfo, Vocation
from .serializers import VocationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def vocationDef(request):
    if request.method == 'GET':
        q = Vocation.objects.all().order_by('id')
        # 分页查询，需要在settings.py设置REST_FRAMEWORK属性
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request)
        # 将分页后的数据传递MySerializer，生成JSON数据对象
        serializer = VocationSerializer(instance=p, many=True)
        # 返回对象Response由Django Rest Framework实现
        return Response(serializer.data)
    elif request.method == 'POST':
        # 获取请求数据
        id = request.data.get('id', 0)
        # 判断请求参数id在模型Vocation是否存在
        # 若存在，则执行数据修改，反之新增数据
        operation = Vocation.objects.filter(id=id).first()
        # 数据验证
        serializer = VocationSerializer(data=request.data)
        if serializer.is_valid():
            if operation:
                data = request.data
                id = data['name']
                data['name'] = PersonInfo.objects.filter(id=id).first()
                serializer.update(operation, data)
            else:
                # 保存到数据库
                serializer.save()
            # 返回对象Response由Django Rest Framework实现
            return Response(serializer.data)
        return Response(serializer.errors, status=404)


class vocationClass(APIView):
    # GET请求
    def get(self, request):
        q = Vocation.objects.all().order_by('id')
        # 分页查询，需要在settings.py设置REST_FRAMEWORK属性
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request, view=self)
        serializer = VocationSerializer(instance=p, many=True)
        # 返回对象Response由Django Rest Framework实现
        return Response(serializer.data)

    # POST请求
    def post(self, request):
        # 获取请求数据
        id = request.data.get('id', 0)
        operation = Vocation.objects.filter(id=id).first()
        # 数据验证
        serializer = VocationSerializer(data=request.data)
        if serializer.is_valid():
            if operation:
                data = request.data
                id = data['name']
                data['name'] = PersonInfo.objects.filter(id=id).first()
                serializer.update(operation, data)
            else:
                # 保存到数据库
                serializer.save()
            # 返回对象Response由Django Rest Framework实现
            return Response(serializer.data)
        return Response(serializer.errors, status=404)

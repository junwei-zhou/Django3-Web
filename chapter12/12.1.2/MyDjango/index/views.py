from .models import PersonInfo, Vocation
from .serializers import MySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def vocationDef(request):
    if request.method == 'GET':
        q = Vocation.objects.all()
        # 分页查询，需要在settings.py设置REST_FRAMEWORK属性
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request)
        # 将分页后的数据传递MySerializer，生成JSON数据对象
        serializer = MySerializer(instance=p, many=True)
        # 返回对象Response由Django Rest Framework实现
        return Response(serializer.data)
    elif request.method == 'POST':
        # 获取请求数据
        data = request.data
        id = data['name']
        data['name'] = PersonInfo.objects.filter(id=id).first()
        instance = Vocation.objects.filter(id=data.get('id', 0))
        if instance:
            # 修改数据
            MySerializer().update(instance, data)
        else:
            # 创建数据
            MySerializer().create(data)
        return Response('Done', status=status.HTTP_201_CREATED)


class vocationClass(APIView):
    # GET请求
    def get(self, request):
        q = Vocation.objects.all()
        # 分页查询，需要在settings.py设置REST_FRAMEWORK属性
        pg = PageNumberPagination()
        p = pg.paginate_queryset(queryset=q, request=request, view=self)
        serializer = MySerializer(instance=p, many=True)
        # 返回对象Response由Django Rest Framework实现
        return Response(serializer.data)

    # POST请求
    def post(self, request):
        data = request.data
        id = data['name']
        data['name'] = PersonInfo.objects.filter(id=id).first()
        instance = Vocation.objects.filter(id=data.get('id', 0))
        if instance:
            # 修改数据
            MySerializer().update(instance, data)
        else:
            # 创建数据
            MySerializer().create(data)
        return Response('Done', status=status.HTTP_201_CREATED)

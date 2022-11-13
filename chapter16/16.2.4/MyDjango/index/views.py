from .models import Product
from .serializers import ProductSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class index(APIView):
    # GET请求
    def get(self, request):
        u = request.GET.get('username', '')
        if u:
            q = Product.objects.filter(user__username=u).order_by('id')
        else:
            q = Product.objects.order_by('id')
        serializer = ProductSerializer(instance=q, many=True)
        return Response(serializer.data)
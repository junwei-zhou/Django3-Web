from django.urls import path, include

urlpatterns = [
    path('', include(('index.urls', 'index'), namespace='index')),
]



from django.urls import path, re_path

from App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    re_path('goods/(\d+)', views.goods, name='goods'),
    re_path('goods', views.goods, name='goods'),
    re_path('detail/(\d+)/(\d+)', views.detail, name='detail'),
    path('requesttest', views.requesttest, name='requesttest'),
    path('responsetest', views.responsetest, name='responsetest'),
    path('gettest', views.gettest, name='gettest'),
]

from django.urls import path, re_path

from App import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),

    re_path('goods/(\d+)', views.goods, name='goods'),
    re_path('goods', views.goods, name='goods'),
    re_path('detail/(\d+)/(\d+)', views.detail, name='detail'),
    path('requesttest', views.requesttest, name='requesttest'),
    path('responsetest', views.responsetest, name='responsetest'),
    path('gettest', views.gettest, name='gettest'),
    path('show_static', views.show_static, name='show_static'),
    path('test_process_request', views.test_process_request, name='test_process_request'),


    path('goodlist', views.goodlist, name='goodlist'),
    re_path('goodlist/(\d+)', views.goodlist, name='goodlist'),

]

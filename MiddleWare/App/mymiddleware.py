from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

from django0527 import settings


class AppMiddleWare(MiddlewareMixin):
# 路由分发之前，每一个都会。
    def process_request(self,request):
        # 获取ip todo 这里测试失败，访问不了
        print(request.META['REMOTE_ADDR'])


        #黑名单设置

        if request.META['REMOTE_ADDR'] in getattr(settings,'BLOCKED_IPS',[]):
            return HttpResponse("请求错误，在黑名单")

        # 抢购
        username = request.POST.get('username')

        if request.path == '/test/': # 抽奖页
            if username == 'zyz':
                return HttpResponse("一等奖")
            else:
                return HttpResponse("不中奖")


        if request.path == '/test_process_request/':
            if True:
                # 中间键一般用于前置的检查， 正常可以接下去执行的时候就设置返回True
                return None
            else:
                # 需要做出反应的时候，可以返回一个HttpResponse对象
                return HttpResponse("测试失败")






        # process_view
        # process_templae_response
        # process_response
        # process_exception


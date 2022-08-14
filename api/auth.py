from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request


class MyAuth(BaseAuthentication):

    def authenticate(self, request: Request):
        """登录验证

        Args:
            request (Request): request对象

        Raises:
            AuthenticationFailed: 抛出认证失败异常 将请求中断掉 返回元组 tuple(user,token) 表示登录成功
        """
        print("中间件 被执行")
        print(request.request.headers, type(request))
        print(request.request.get_raw_uri)
        # return super().authenticate(request)
        # return None

        raise AuthenticationFailed({"code": 1000, "data": "认证失败"})

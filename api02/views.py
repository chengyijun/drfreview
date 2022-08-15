from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from api02.models import UserInfo, Role


class RoleSeri(serializers.ModelSerializer):
    # view_name="api02:role" 指定哪个路由来进行反向生成
    # lookup_field = "id"  表示用Role模型类中的id字段 作为参数 传递给上一步的路由 作为路由参数
    # lookup_url_kwarg="id" 表示路由中使用什么参数名来接受主键参数的 path("role/<int:id>/", RoleView.as_view(), name="role"),
    # 这里是id 所以该参数为id 默认是pk如果使用默认则无需指定

    hyp = serializers.HyperlinkedIdentityField(view_name="api02:role", lookup_field="id",
                                               lookup_url_kwarg="id")

    class Meta:
        model = Role
        fields = "__all__"


class UserInfoSeri(serializers.ModelSerializer):
    roles = RoleSeri(many=True)

    class Meta:
        model = UserInfo
        fields = "__all__"


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        users = UserInfo.objects.all()
        ser = UserInfoSeri(instance=users, many=True, context={'request': request})
        data = ser.data
        return Response(data=data)


class RoleView(APIView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")

        role = Role.objects.filter(id=id).first()
        # 反向生成
        # res = reverse(viewname="api02:role", kwargs={"id": 1}, request=request)
        # print(res)
        ser = RoleSeri(instance=role, many=False, context={'request': request})
        data = ser.data
        return Response(data=data)

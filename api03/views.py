# Create your views here.
from rest_framework import serializers
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.pagination import PageNumberPagination, CursorPagination
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from api03.models import Dog


class DogSeri(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"


class MyPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = "size"
    max_page_size = 10


class MyPagination2(CursorPagination):
    ordering = "id"


class T1View(APIView):
    def get(self, request, *args, **kwargs):
        res = Dog.mm.raw_sql_query("select * from api03_dog")
        print(res)

        data = {"code": 1}
        dogs = Dog.mm.all()
        pagination = MyPagination2()
        qs = pagination.paginate_queryset(queryset=dogs, request=request, view=self)
        seri = DogSeri(instance=qs, many=True)
        # return Response(data=seri.data)
        return pagination.get_paginated_response(seri.data)


class T2View(GenericAPIView):
    queryset = Dog.mm.all()
    serializer_class = DogSeri
    pagination_class = MyPagination

    def get(self, request, *args, **kwargs):
        dogs = self.get_queryset()
        # pagination = MyPagination2()
        qs = self.paginate_queryset(dogs)
        # qs = pagination.paginate_queryset(queryset=dogs, request=request, view=self)
        seri = self.get_serializer(instance=qs, many=True)
        return Response(data=seri.data)
        # return pagination.get_paginated_response(seri.data)


class T3View(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Dog.mm.all()
    serializer_class = DogSeri
    pagination_class = MyPagination

    # def list(self, request, *args, **kwargs):
    #     dogs = self.get_queryset()
    #     qs = self.paginate_queryset(dogs)
    #     seri = self.get_serializer(instance=qs, many=True)
    #     return Response(data=seri.data)

    # def create(self, request, *args, **kwargs):
    #     seri = self.get_serializer(data=request.data)
    #     if seri.is_valid():
    #         seri.save()
    #         data = {"code": 1}
    #     else:
    #         data = {"code": 0}
    #     return Response(data=data)


class MyPermission(BasePermission):

    def has_permission(self, request, view):
        print("视图权限检查")
        return True

    def has_object_permission(self, request, view, obj):
        print("对单独对象的权限检查", view, obj)
        return True


class T4View(ModelViewSet):
    permission_classes = [MyPermission]
    queryset = Dog.mm.all()
    serializer_class = DogSeri
    pagination_class = MyPagination

    def get_object(self):
        print(self.lookup_url_kwarg, self.kwargs, self.lookup_field)
        obj = self.get_queryset().filter(pk=self.kwargs.get("id")).first()
        self.check_object_permissions(self.request, obj)
        return obj

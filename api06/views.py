# Create your views here.
from rest_framework.request import Request
from rest_framework.response import Response

from rest_framework.views import APIView


class MyVersion:

    def determine_version(self, request, *args, **kwargs):
        print(111)
        return request.GET.get("version")


class TestView(APIView):
    # versioning_class = MyVersion

    # versioning_class = QueryParameterVersioning

    def get(self, request, *args, **kwargs):
        # version = request.GET.get("version")
        print(request.version, request.versioning_scheme)
        data = {"code": 777}
        return Response(data=data)


class MyVersion2:
    def determine_version(self, request, *args, **kwargs):
        return kwargs.get("version")


class Test2View(APIView):
    # versioning_class = URLPathVersioning

    # versioning_class = MyVersion2

    def get(self, request, *args, **kwargs):
        # version = request.GET.get("version")
        print(request.version, request.versioning_scheme)
        data = {"code": 456}
        return Response(data=data)


class Test3View(APIView):
    # versioning_class = QueryParameterVersioning

    def get(self, request: Request, *args, **kwargs):
        # version = request.GET.get("version")
        print(request.version, request.versioning_scheme)
        data = {"code": 4567}
        return Response(data=data)

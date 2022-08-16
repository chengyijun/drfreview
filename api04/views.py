# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from api04.models import DegreeCourse


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        obj = DegreeCourse.objects.filter(name="Java").first()
        # PricePolicy.objects.create(price=9.9, content_object=obj)
        # PricePolicy.objects.create(price=19.9, content_object=obj)
        # PricePolicy.objects.create(price=29.9, content_object=obj)
        print(obj.prices.all())
        return Response({"code": 1})

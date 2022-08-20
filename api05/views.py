# Create your views here.
import time

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.throttling import SimpleRateThrottle
from rest_framework.views import APIView


class MT2(SimpleRateThrottle):
    scope = "scope"
    THROTTLE_RATES = {
        "scope": "3/m"
    }

    def get_cache_key(self, request, view):
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip


VISIT_RECORD = {

}


# from rest_framework.throttling import BaseThrottle
class MyThrottle:
    def __init__(self):
        self.records = None
        self.duration = 10

    def allow_request(self, request: Request, view):

        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip = request.META.get("HTTP_X_FORWARDED_FOR")
        else:
            ip = request.META.get("REMOTE_ADDR")
        print(ip)
        now = time.time()
        if ip not in VISIT_RECORD:
            VISIT_RECORD.update({ip: [now]})
            return True
        else:
            records = VISIT_RECORD.get(ip)
            self.records = records
            while records and now - records[-1] > self.duration:
                records.pop()

            if len(records) < 3:
                records.insert(0, now)
                return True
        return False

    def wait(self):
        return self.duration - (time.time() - self.records[-1])


class TestView(APIView):
    throttle_classes = [MT2]

    def get(self, request, *args, **kwargs):
        data = {"code": 111}
        return Response(data=data)

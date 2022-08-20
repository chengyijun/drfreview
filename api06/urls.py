from django.urls import path, re_path

from api06.views import TestView, Test2View, Test3View

app_name = "api06"
urlpatterns = [
    path("test/", TestView.as_view(), name="test"),
    # path("test2/<version>/", Test2View.as_view(), name="test2"),
    re_path(r'^test2/(?P<version>[v1|v2|v3]+)/$', Test2View.as_view(), name="test2"),
    path("test3/", Test3View.as_view(), name="test3"),

]

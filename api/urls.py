from django.urls import path, re_path

from api.views import Test2View, Test3View, Test4View, TestView

app_name = "api"
urlpatterns = [
    path("test/", TestView.as_view(), name="test"),
    path("test2/", Test2View.as_view(), name="test2"),
    path("test3/<int:id>/", Test3View.as_view(), name="test3"),
    path("test4/", Test4View.as_view(), name="test4"),
]

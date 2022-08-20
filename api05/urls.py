from django.urls import path

from api05.views import TestView

app_name = "api05"
urlpatterns = [
    path("test/", TestView.as_view(), name="test"),

]

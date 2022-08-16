from django.urls import path

from api04.views import TestView

app_name = "api04"
urlpatterns = [
    path("test/", TestView.as_view(), name="test"),

]

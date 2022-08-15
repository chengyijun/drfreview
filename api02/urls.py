from django.urls import path

from api02.views import TestView, RoleView

app_name = "api02"
urlpatterns = [
    path("test/", TestView.as_view(), name="test"),
    path("role/<int:id>/", RoleView.as_view(), name="role"),

]

from django.urls import include, path
from rest_framework import routers

from api03.views import T4View

router = routers.DefaultRouter()
router.register("t4", T4View)

app_name = "api03"
urlpatterns = [
    # path("t1/", T1View.as_view(), name="t1"),
    # path("t2/", T2View.as_view(), name="t2"),
    # path("t3/", T3View.as_view({'get': 'list', "post": "create"}), name="t3"),
    # path("t4/", T4View.as_view({'get': 'list', "post": "create"}), name="t4"),
    # path("t4/<int:id>/", T4View.as_view({'get': "retrieve"}), name="t4_detail"),
    # # path("role/<int:id>/", RoleView.as_view(), name="role"),
    path("", include(router.urls))
]

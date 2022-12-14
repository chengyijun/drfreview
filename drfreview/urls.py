"""drfreview URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("api02/", include("api02.urls", namespace="api02")),
    path("api03/", include("api03.urls", namespace="api03")),
    path("api04/", include("api04.urls", namespace="api04")),
    path("api05/", include("api05.urls", namespace="api05")),
    path("api06/", include("api06.urls", namespace="api06")),
    path("api07/", include("api07.urls", namespace="api07")),
    path("api08/", include("api08.urls", namespace="api08")),
]

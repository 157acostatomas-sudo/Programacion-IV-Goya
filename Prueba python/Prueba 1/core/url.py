from . import views
from django.urls import path, include

urlpatterns = [
    path("estado/", views.health_check, name="health_check"),
    #$path("api/", include("core.url")),
]

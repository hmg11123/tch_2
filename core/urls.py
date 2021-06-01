from django.urls import path
from core import views as core_models

app_name = "core"

urlpatterns = [
    path("", core_models.homeRender)
]
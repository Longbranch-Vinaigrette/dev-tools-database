from django.urls import path

from . import views
from .views import RepositorySettings

urlpatterns = [
    path("", views.index, name="index"),
    path("RepositorySettings/getAll", RepositorySettings.get_all, name="RepositorySettings/getAll")
]

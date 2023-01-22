"""
Create app
python manage.py startapp sql
Reference/s:
https://docs.djangoproject.com/en/4.1/intro/tutorial01/
"""
from django.urls import path

from . import views
from .views import RepositorySettings

urlpatterns = [
    # ex: /sql/
    path("", views.index, name="index"),
    # ex: /sql/RepositorySettings/getAll
    path("RepositorySettings/getAll/", RepositorySettings.get_all, name="RepositorySettings/getAll/")
]

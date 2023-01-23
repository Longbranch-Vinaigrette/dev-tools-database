"""
Create app
python manage.py startapp sql
Reference/s:
https://docs.djangoproject.com/en/4.1/intro/tutorial01/
"""
import os
import pprint

from django.urls import path

from . import views
from .views import RepositorySettings
from src.submodules.dev_tools_utils.dynamic_imports.django_routes import DjangoRoutes

app_name = "sql"
# urlpatterns = [
#     # ex: /sql/
#     path("", views.index, name="index"),
#     # ex: /sql/RepositorySettings/getAll
#     path("RepositorySettings/getAll/", RepositorySettings.get_all, name="RepositorySettings/getAll/"),
#     path("RepositorySettings/discoverAndReset/",
#          RepositorySettings.discover_and_reset,
#          name="RepositorySettings/discoverAndReset/"),
#     path("RepositorySettings/getRepository/",
#          RepositorySettings.get_repository,
#          name="RepositorySettings/getRepository/"),
# ]
routes_path = f"{os.getcwd()}{os.path.sep}src{os.path.sep}routes"
djroutes = DjangoRoutes(routes_path, handle_request=False)
urlpatterns = djroutes.get_routes_as_urlpatterns()
print("Urlpatterns:")
pprint.pprint(urlpatterns)

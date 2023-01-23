"""
Create app
python manage.py startapp sql
Reference/s:
https://docs.djangoproject.com/en/4.1/intro/tutorial01/
"""
import os
import pprint

from src.submodules.dev_tools_utils.dynamic_imports.django_routes import DjangoRoutes

app_name = "sql"

routes_path = f"{os.getcwd()}{os.path.sep}src{os.path.sep}routes"
djroutes = DjangoRoutes(routes_path, handle_request=False, debug=True)
urlpatterns = djroutes.get_routes_as_urlpatterns()

debug = False
if debug:
    print("Urlpatterns:")
    pprint.pprint(urlpatterns)

import json
from django.http import HttpResponse

from src.dbs.RepositorySettings import RepositorySettings


def get_all(request):
    try:
        rep_settings = RepositorySettings()
        data = {
            "debug": {
                "message": "Success"
            },
            "route": "RepositorySettings/get_all",
            "data": rep_settings.get_all(),
        }
    except:
        data = {
            "debug": {
                "message": "Error: Maybe the table doesn't exist.",
                "error": True,
                "field": "",
                "state": "danger"
            }
        }

    res = HttpResponse(json.dumps(data))
    res.headers["Content-Type"] = "application/json"
    return res

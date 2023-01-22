import json
from django.http import HttpResponse

from src.dbs.RepositorySettings import RepositorySettings


def get_all(request):
    print("Request body: ")
    print(request.body)
    data = {
        "debug": {
            "message": "Success"
        },
        "route": "RepositorySettings/get_all",
    }
    res = HttpResponse(json.dumps(data))
    res.headers["Content-Type"] = "application/json"

    return res

import json

from django.http import HttpResponse


def index(request):
    print("Request body: ")
    print(request.body)
    data = {
        "debug": {
            "message": "Success"
        }
    }
    res = HttpResponse(json.dumps(data))
    res.headers["Content-Type"] = "application/json"

    return res

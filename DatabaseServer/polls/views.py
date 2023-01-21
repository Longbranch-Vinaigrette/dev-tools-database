import json
import os

# Create your views here.
from django.http import HttpResponse
print("CWD: ", os.getcwd())


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

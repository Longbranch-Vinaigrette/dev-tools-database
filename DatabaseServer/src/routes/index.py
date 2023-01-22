import json

from django.http import HttpResponse, HttpRequest


class Main:
    def __init__(self, route: str):
        self.route = route

    def get(self, request: HttpRequest):
        """Discover repositories and reset data to default values"""
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

import json

from django.http import HttpResponse, HttpRequest


class Main:
    def __init__(self, route: str):
        self.route = route

    def get(self, request: HttpRequest):
        print("\nindex -> get():")

        """Discover repositories and reset data to default values"""
        print("Request body: ")
        print(request.body)
        data = {
            "debug": {
                "message": "Success"
            },
            "route": self.route,
        }
        res = HttpResponse(json.dumps(data))
        res.headers["Content-Type"] = "application/json"

        return res

    def handle_request(self, req: HttpRequest):
        """Handle request"""
        if req.method == "GET":
            return self.get(req)
        else:
            raise Exception("This route doesn't handle the given method.")

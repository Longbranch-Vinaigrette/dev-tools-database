import json

from django.http import HttpRequest, HttpResponse

from src.dbs.RepositorySettings import RepositorySettings


class Main:
    def __init__(self, route):
        self.route = route

    def get(self, request: HttpRequest):
        try:
            rep_settings = RepositorySettings()
            data = {
                "debug": {
                    "message": "Success"
                },
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

    def handle_request(self, req: HttpRequest):
        if req.method == "GET":
            return self.get(req)
        else:
            raise Exception("Method not handled by server.")

import json

from django.http import HttpRequest, HttpResponse

from src.dbs.RepositorySettings import RepositorySettings


class Main:
    def __init__(self, route):
        self.route = route

    def post(self, request: HttpRequest):
        """Get local repository settings by username and repository name"""
        try:
            if "Content-Type" in request.headers:
                if request.headers["Content-Type"] == "application/json":
                    # Reference/s:
                    # https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
                    body = json.loads(request.body.decode("utf-8"))
                    rep_settings = RepositorySettings()
                    rep_settings.upsert(body["data"], body["filter"])
                    data = {
                        "debug": {
                            "message": "Success"
                        },
                    }
                else:
                    msg = f"Content-Type not supported, given " \
                          f"Content-Type: {request.headers['Content-Type']}"
                    data = {
                        "debug": {
                            "message": msg,
                            "error": True,
                            "field": "",
                            "state": "danger"
                        }
                    }
            else:
                data = {
                    "debug": {
                        "message": "Content-Type not given",
                        "error": True,
                        "field": "",
                        "state": "danger"
                    }
                }
        except Exception as ex:
            data = {
                "debug": {
                    "message": "Unknown error, it's likely that the table doesn't exist.",
                    "error": True,
                    "field": "",
                    "state": "danger"
                }
            }
            print("Exception: ")
            print(ex)

        res = HttpResponse(json.dumps(data))
        res.headers["Content-Type"] = "application/json"
        return res

    def handle_request(self, req: HttpRequest):
        if req.method == "POST":
            return self.post(req)
        else:
            raise Exception("Method not handled by server.")

import json

from django.http import HttpResponse, HttpRequest

from src.submodules.dev_tools_utils.django_utils import DjangoUtils
from src.submodules.dev_tools_utils.Debug import Debug
from src.submodules.dev_tools_utils.dbs.SettingsTable import SettingsTable


def send_response(data: dict):
    res = HttpResponse(json.dumps(data))
    res.headers["Content-Type"] = "application/json"
    return res


class Main:
    def __init__(self, route: str):
        self.route = route

    def post(self, request: HttpRequest):
        """Check whether an app is DevTools compatible"""
        data = DjangoUtils().validate_json_content_type(request)

        # If there is "debug" in data it means that there was an error
        if not "debug" in data:
            body: dict = json.loads(request.body.decode("utf-8"))

            # Check if the required data was given
            try:
                # This is just to inform the user in case that no data was given.
                if len(list(body.keys())) <= 0:
                    raise Exception("No data given.")
            except Exception as ex:
                print("Exception: ", ex)
                data = {
                    "debug": Debug("Bad data format a key was not given correctly, the key: "
                                   f"{str(ex)}",
                                   state="danger").get_message(),
                }
                return send_response(data)

            # Try to execute the command
            try:
                settings_table = SettingsTable()

                # To set multiple keys at once
                for key in list(body.keys()):
                    settings_table.upsert({
                        "key": key,
                        "value": body[key]
                    }, {
                        "key": key,
                    })

                return send_response(data)
            except Exception as ex:
                print("Exception: ", ex)
                data = {
                    "debug": Debug("Data not set.", error=True,
                                   state="error").get_message(),
                }

        return send_response(data)

    def handle_request(self, req: HttpRequest):
        """Handle request"""
        if req.method == "POST":
            return self.post(req)
        else:
            raise Exception("This route doesn't handle the given method.")

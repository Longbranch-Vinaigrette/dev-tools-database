import json
from django.http import HttpResponse

from src.dbs.RepositorySettings import RepositorySettings
from src.submodules.dev_tools_utils.data_configuration import DataLocation
from src.submodules.dev_tools_utils.local_repository_manager import LocalRepositoryManager


def discover_and_reset(request):
    """Discover repositories and reset data to default values"""
    try:
        # Database
        repository_settings = RepositorySettings()

        # Get local repositories data
        repository_manager = LocalRepositoryManager(DataLocation.get_repositories_path())
        repositories_data = repository_manager.get_all_repos_info()

        for rep_data in repositories_data:
            repository_settings.upsert(
                rep_data,
                {
                    "user": rep_data["user"],
                    "name": rep_data["name"]
                }
            )

        data = {
            "debug": {
                "message": "Success"
            }
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


def get_all(request):
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



import json
import os

from ..submodules.sqlite3_utils import Sqlite3Utils
from ..submodules.dev_tools_utils.data_configuration import DataLocation, LocalData, DBPath


class RepositorySettings:
    repositories_path = f"{DataLocation.get_data_path()}/repositories"

    def __init__(self, debug: bool = False):
        self.debug = debug

        if self.debug:
            print("\nRepositorySettings -> __init__():")

        # Get the filename of the DB
        db_filename = "devtools.db"
        try:
            with open(LocalData.get_local_settings_path(), "r") as f:
                local_data = json.load(f)
                db_filename = local_data["DBFilename"] if local_data["DBFilename"] else "devtools.db"
        except:
            db_filename = "devtools.db"
        db_path = DBPath.get_sql_db_path(db_filename)
        self.sql_repository_settings = Sqlite3Utils(
            db_path,
            "repository_settings",
            debug=self.debug)

    def get_all(self):
        """Get every repository settings data"""
        data = self.sql_repository_settings.run_query(
            f"""SELECT * FROM repository_settings""",
            # Decode json data automatically
            True)
        return data

    def get_repository(self, username: str, repository_name: str):
        """Get repository settings data"""
        data = self.sql_repository_settings.run_query(f"""
            SELECT * FROM repository_settings
                WHERE user='{username}'
            INTERSECT
                SELECT * FROM repository_settings
                    WHERE name='{repository_name}'
            """,
            True)
        return data

    def upsert(self, data: dict, filterA: dict):
        """Insert or replace data"""
        if self.debug:
            print("RepositorySettings -> upsert():")
        return self.sql_repository_settings.insert_replace_v2(data, filterA)

    def set_default_path(self, username: str, repository_name: str):
        """Set path to default path"""
        self.sql_repository_settings.insert_replace({
                "path": f"{self.repositories_path}/{username}/{repository_name}"
            },
            "user",
            username,
            {
                "name": repository_name,
            })

    def set_default_path_for_every_repository(self):
        """Set default path for every repository"""
        data = self.sql_repository_settings.get_all()
        for item in data:
            username = item["user"]
            repository_name = item["name"]
            sep = os.path.sep

            # Update path
            path = f"{self.repositories_path}{sep}{item['user']}{sep}{item['name']}"
            self.sql_repository_settings.insert_replace_v2(
                {
                    "path": path
                },
                {
                    "user": username,
                    "name": repository_name
                }
            )

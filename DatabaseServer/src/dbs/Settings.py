from src.submodules.sub_sqlite3_utils import Sqlite3Utils

from src.utils import LocalData


class Settings:
    def __init__(self):
        db_path = LocalData.load_data("DBPath")
        self.sql_settings_table = Sqlite3Utils(db_path, "settings")

    def upsert(self, data: dict, filterA: dict):
        """Alias for insert replace"""
        return self.sql_settings_table.insert_replace_v2(data, filterA)

    def get(self, key: str):
        """Get data from the settings table"""
        return self.sql_settings_table.get("key", key, True)["value"]

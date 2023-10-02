import json
import shortuuid

class URLShortener:
    def __init__(self, database_path="database.json"):
        self.database_path = database_path
        self.url_mappings = self.load_database()

    def load_database(self):
        try:
            with open(self.database_path, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_database(self):
        with open(self.database_path, 'w') as file:
            json.dump(self.url_mappings, file, indent=2)

    def shorten_url(self, long_url):
        short_url = shortuuid.uuid()[:8]
        self.url_mappings[short_url] = long_url
        self.save_database()
        return short_url

import json


class StorageManager:
    def load_data(self, data_name):
        filename = self.get_filename(data_name)
        file = open(filename, "r")
        data_content = file.read()
        file.close()

        return json.loads(data_content)

    def save_data(self, data_name, data_content):
        filename = self.get_filename(data_name)
        data_content_str = json.dumps(data_content)
        file = open(filename, "w")
        file.write(data_content_str)
        file.close()

    def get_filename(self, data_name):
        # permet de definir une seule fois le nom du fichier au bon format
        return data_name + ".json"


import os

class FileService:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    async def fetch(self, file_type):
        file_path = f".{file_type}"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        return content

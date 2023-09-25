import json

class lib():
    def write(data) -> None:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
    
    def read() -> dict:
        with open('data.json', 'r') as file:
            DICT = json.load(file)
        return DICT
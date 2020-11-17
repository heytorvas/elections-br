import json

def get_file_json(file_json):
    with open(file_json, 'r') as f:
        party_json = json.load(f)
        f.close()
        return party_json
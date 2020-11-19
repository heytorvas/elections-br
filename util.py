import json, requests

def get_geojson_state(uf):
    r = requests.get('https://raw.githubusercontent.com/luizpedone/municipal-brazilian-geodata/master/data/{}.json'.format(uf)).json()
    return r

def get_file_json(file_json):
    with open(file_json, 'r') as f:
        party_json = json.load(f)
        f.close()
        return party_json

def largest_votes(arr): 
    n = len(arr)
    max = arr[0] 
    for i in range(1, n): 
        if arr[i] > max: 
            max = arr[i] 
    return max
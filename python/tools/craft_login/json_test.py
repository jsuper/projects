import json

json_data = open('config.cfg').read()
jsons = json.loads(json_data)

print jsons['root_path']

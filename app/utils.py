import json
import sys

sys.path.append('./')

def load_json():
    with open('app/data/role_avatar.json', 'r') as f:
        return json.load(f)
import json, os
import sys
from twilio.rest import Client

sys.path.append('./')

def load_json():
    with open('app/data/role_avatar.json', 'r') as f:
        return json.load(f)

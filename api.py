import requests
import json
from environs import Env
env =Env()
env.read_env()
URL = env.str('URL')
# Create user
def create_user(name:str,telegram_id):
    try:
        data = {
            'name':name,
            "telegram_id": telegram_id
        }
        response = requests.post(url=f"{URL}/user/", data=data)
        return response.status_code
    except:
        pass
# Get All User
def get_users():
    try:
        response = requests.get(url=f"{URL}/user/")
        return json.loads(response.text)
    except:
        return []
def create_group(name:str,telegram_id):
    try:
        data = {
            'name':name,
            "telegram_id": telegram_id
        }
        response = requests.post(url=f"{URL}/group/", data=data)
        return response.status_code
    except:
        pass
def get_groups():
    try:
        response = requests.get(url=f"{URL}/group/")
        return json.loads(response.text)
    except:
        return []
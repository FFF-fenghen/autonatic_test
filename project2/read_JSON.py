import json
from pprint import pprint

with open('file/user_info.json', 'r') as f:
    data = f.read()

user_list = json.loads(data)
for user in user_list:
    print(user['username']+user['password']+'***')

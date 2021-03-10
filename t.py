import json

import requests

uri = 'http://wuhe.21dodo.com/video/upload/'
token_api = 'account/login_admin/'

if __name__ == '__main__':
    data = {
        'username': 'even',
        'userpassword': '123'
    }
    headers = {'key': 'wuhe'}
    res = requests.get(uri, data, headers=headers)

    with open('out.json', 'w') as f:
        f.write(json.dumps(res.json()))
    print(res.json())
    # res = requests.get(uri)
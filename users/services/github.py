import requests

base_url = 'https://api.github.com'


def get_user(username):
    url = '{}/users/{}'.format(base_url, username)
    res = requests.get(url)
    return res.status_code, res.json()

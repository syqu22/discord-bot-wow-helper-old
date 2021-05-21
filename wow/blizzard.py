import requests


CLIENT_ID = "a30c40f5dba24d53bff5201464f92e8d"


class BlizzardAPI():

    def __init__(self):
        ...

    def get_secret(self):
        with open("secret.txt") as f:
            return f.readline().strip()

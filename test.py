import json
import requests

import urllib.request, json

with urllib.request.urlopen("https://www.reddit.com/user/CheekyXD.json") as url:
    userJSON = json.loads(url.read())

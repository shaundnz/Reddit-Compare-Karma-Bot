import json
from urllib import request


def userData():
    username = input("Enter the reddit username you would like to compare here: ")
    url = "https://www.reddit.com/user/" + username + ".json"
    print(username)
    req = request.Request(url)
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')
    resp = request.urlopen(req)
    user_data = resp.read().decode("utf-8")
    user_data_obj = json.loads(user_data)
    print(type(user_data_obj))
    print(user_data_obj["data"]["children"][0]["kind"])



userData()




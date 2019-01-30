import json
from urllib import request, error




def userData(username):
    try:
        currentIndex = 0
        commentType = ""
        url = "https://www.reddit.com/user/" + username + ".json"
        print("Finding Data for " + username)
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)')
        resp = request.urlopen(req)
    except :
        print("Error retrieving user data. Did you type that in right??")
        quit()
    user_data = resp.read().decode("utf-8")
    user_data_obj = json.loads(user_data)
    # Loop repeats until post with type t3 is found
    try:
        while commentType != "t3":
            commentType = str(user_data_obj["data"]["children"][currentIndex]["kind"])
            currentIndex += 1
    except:
        print("User: " + username + " has no post data in the json file that can be found")
        quit()
    postKarma = user_data_obj["data"]["children"][currentIndex-1]["data"]["ups"]
    return postKarma





def compareKarma():
    print("Welcome to the karma comparing tool, Enter 2 Reddit usernames and compare the karma on their last post")
    user1 = input("Enter the first username: ")
    user2 = input("Enter the second username: ")
    user1Karma = userData(user1)
    user2Karma = userData(user2)
    print("The difference in karma on their most recent post is for users " + user1 + " and " + user2 + " is " + str(abs(user1Karma - user2Karma)))
    print(str(user1Karma) + " Karma for " + user1 + " and " + str(user2Karma) + " Karma for " + user2)


compareKarma()














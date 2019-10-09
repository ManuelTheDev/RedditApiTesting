import sys
import praw
import json

client_id = "c6jR8eRWQ0RtaA"
client_secret = "yQ55W5ku_3sah67xkZ_PIPaFrw4"
user_agent = "testingAPI"
username = "Manubilo"
password = "werfault96"


reddit = praw.Reddit(client_id=client_id, #
client_secret=client_secret,
user_agent=user_agent,
username=username,
password=password,)


subred = reddit.subreddit("ios")
hot= subred.hot(limit=11)

type(hot)

x= next(hot)

dir(x)

for i in hot:
    print(i.title, i.url)

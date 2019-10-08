import praw
import json

client_id = "c6jR8eRWQ0RtaA"
client_secret = "yQ55W5ku_3sah67xkZ_PIPaFrw4"
user_agent = "testingAPI"
username = "Manubilo"
password = "werfault96"

reddit = praw.Reddit(client_id=user_values['client_id'],
client_secret=user_values['client_secret'],
user_agent=user_values['user_agent'],
username=user_values['username'],
password=user_values['password'],)

def create_reddit_object(json_file="reddit_config.json", json_key="reddit"):
    with open(json_file) as f:
        data = json.load(f)
    
    user_values = data[json.key]

    reddit = praw.Reddit(client_id=user_values['client_id'],
    client_secret=user_values['client_secret'],
    user_agent=user_values['user_agent'],
    username=user_values['username'],
    password=user_values['password'],)

    return reddit

reddit = create_reddit_object()

subred = reddit.subreddit("learnprogramming")

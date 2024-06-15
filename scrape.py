import praw
from cfg import client_id,client_secret,user_agent

# Initialize Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Set the username of the user you want to fetch posts from

# Fetch user submissions
def get_comments(subreddit_name):
  subreddit = reddit.subreddit(subreddit_name)
  return subreddit.stream.comments()


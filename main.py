# Take video url and post it to a set of subreddits all at once

import praw
video_url=str(input("Your video url:"))
post_msg = str(input("Your post message"))
reddit=praw.Reddit(client_id="***************",
      client_secret="************",
      user_agent="**********",
      username="************",
      password="***********")
subreddit_list =["Python","PytonProjects","learningprogramming"]
for i in subreddit_list:
    subreddit=reddit.subreddit(i)
    print("Posting video to" + i)
    subreddit.submit(post_msg, url=video_url)
    print("Done")
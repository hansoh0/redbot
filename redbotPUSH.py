#! /usr/bin/env python3

# FILE: redbotPUSH.py
# PURPOSE: Sarcastic communist reddit reply bot
# AUTHOR: Canyon Bishop

import praw
import pdb
import re
import os
import random

quotelist = ["The revolution will be glorious, comrade.","Believe in yourself comrade! Our time will come.", "The revolution is coming, comrade."]
# reddit instance login and password
reddit = praw.Reddit(client_id='',
client_secret='',
password='',
username='redthecomrade')


#creating a list for repeats
if not os.path.isfile("posts_replied_to.txt"):
	posts_replied_to = []

#or load list of posts replied to
else:
	with open("posts_replied_to.txt","r") as f:
		posts_replied_to = f.read()
		posts_replied_to = posts_replied_to.split("\n")
		posts_replied_to = list(filter(None, posts_replied_to))

#top 10 newest entries
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.new(limit=100):
	#looks through replied to 
	if submission.id not in posts_replied_to:
		#ignores case
		if re.search("our", submission.title, re.IGNORECASE): 
			#replies
			red_says = random.choice(quotelist)
			submission.reply("> ", submission.title, red_says)
			print ("Bot replying to : ", submission.title)
			#store id
			posts_replied_to.append(submission.id)

with open("posts_replied_to.txt", "w") as f:
	for post_id in posts_replied_to:
		f.write(post_id + "\n")

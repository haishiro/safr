import praw	
import csv
import pandas as pd
from bs4 import BeautifulSoup

## Attempt to load wider range of dates

# IDs are secret! Insert your own to try it out
reddit = praw.Reddit(client_id='', client_secret='',
                     password='', user_agent='testscript by /u/haishiro',
                     username='')
					 
ful = reddit.subreddit('futurology') # subreddit

reddit_comments = pd.DataFrame(columns=['title','body_html'])

for submission in ful.submissions(start=1514764800,end=None): # Modify filter/sort ful.top('all',limit=20) #1518220800
	subtitle = submission.title
	print(subtitle)
	submission.comments.replace_more(limit=2) # Get more comments to depth level	
	comment_list = list(submission.comments)	
	# Save all comments into df
	for idx, comment in enumerate(comment_list):
		if comment.stickied == 0:
			soup = BeautifulSoup(comment.body_html,"html5lib")
			icomment = {'title':subtitle,'body_html':soup.get_text()}
			#removal_reason
			reddit_comments = reddit_comments.append(icomment,ignore_index=True)

	# Write to csv 	
with open('E:\\David\\Documents\\Northwestern\\W2018\\PRED 453\\Python Explore\\comments_full.csv', 'w', encoding='utf-8') as cfile:
	reddit_comments.to_csv(cfile)
		
	#https://www.reddit.com/r/announcements/comments/3cbo4m/we_apologize/?sort=controversial
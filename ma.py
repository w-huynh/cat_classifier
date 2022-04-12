import praw
import requests

client_id = "ZaJ8KPo_WXoL0NtQtYd_cw"
client_secret = "mV1sFzGSPCc1QDOZMPNucsKJnh7Llw"
user_agent = "cc_test"

reddit_read_only = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)

sic = reddit_read_only.subreddit("standardissuecat")

hot = sic.hot(limit = 5)
'''
for i in hot:
    print(i.title, i.url)
    print(i.secure_media)
    print(i.id)
    print()
    #with open(i.title+'.jpg', 'wb') as f:
        #f.write(requests.get(i.url).content)
'''
x=dir(next(hot))
for i in x:
    print(i)
    #

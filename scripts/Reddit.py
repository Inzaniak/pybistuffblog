import time
import os
import requests
import json

path = r'C:\Users\Inzaniak\Documents\myblog\posts\20{}\{}\{}'.format(
     time.strftime("%y")
    ,time.strftime("%m")
    ,time.strftime("%d"))
file_name=r'\python-reddit-{}.md'.format(time.strftime("%y%m%d"))

if not os.path.exists(path):
    os.makedirs(path)


url = 'https://www.reddit.com/r/Python/top/.json?sort=top&t=week'
data = json.loads(requests.get(url,headers={'user-agent':'redditcrawl'}).text)

out_dict = {'posts':[]}
for el in data['data']['children']:
    out_dict['posts'].append({'Title':el['data']['title']
                            ,'Score':el['data']['score']
                            ,'Author':el['data']['author']
                            ,'RedditUrl':'http://www.reddit.com'+el['data']['permalink']
                            ,'Url':el['data']['url']})
    
html = '<ol>\n'
for post in out_dict['posts'][0:5]:
    html+=('<li>Title:<strong> {}</strong><br />Author:<strong> {}</strong><br />Score:<strong> {}</strong><br />Url:<strong> <a href=" {}">Reddit</a>/<a href="{}">Direct</a></strong><strong><br /></strong>Description:<br />\nsimpletext\n<br /><br /></li>').format(
                post['Title']
                ,post['Author']
                ,post['Score']
                ,post['RedditUrl']
                ,post['Url'])
html+='\n</ol>'

file_meta = r'\python-reddit-{}.meta'.format(time.strftime("%y%m%d"))
meta ="""
.. title: Python: News from Reddit, {}
.. slug: python-reddit-{}
.. date: {}
.. tags: Python
.. description: 
.. wp-status: publish
""".format(time.strftime("%y/%m/%d")
            ,time.strftime("%y%m%d")
            ,time.strftime("20%y-%m-%d %H:%M:%S")).strip()

open(path+file_meta,'w',encoding='utf-8').write(meta)
open(path+file_name,'w',encoding='utf-8').write(html)
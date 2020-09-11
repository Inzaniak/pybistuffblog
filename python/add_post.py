import arrow
import os
from pygments import highlight
from pygments.lexers import PythonLexer, BatchLexer,TransactSqlLexer, VbNetLexer, JsonLexer
from pygments.formatters import HtmlFormatter
import string
import sqlite3

conn = sqlite3.connect(':memory:')
conn.execute('create table t(date,url,title,subtitle,author)')
conn.commit()

MAIN_DIR = R"C:\Users\inzan\OneDrive\pybistuffblog"
os.chdir(MAIN_DIR+R'\python')


class Post:
    def __init__(self,filepath):
        self.filepath = filepath
        self.rawtext = open(filepath,'r',encoding='utf-8').read()
        # Gestione \n nel codice
        #temp_txt = self.rawtext.replace("'\n","'/n").replace('"\n','"/n')
        self.header_list = self.rawtext.split('---PostStart---')[0].splitlines()
        self.content_list = self.rawtext.split('---PostStart---')[1].splitlines()
        # Recupero informazioni dall'header
        self.title = self.header_list[0].split(': ',1)[1].strip()
        self.html_title = ''.join([c.lower() for c in self.title if c not in string.punctuation])
        self.html_title = self.html_title.replace(' ','-')
        self.subtitle = self.header_list[1].split(': ',1)[1].strip()
        self.year = self.header_list[2].split(': ',1)[1].strip()
        self.month = self.header_list[3].split(': ',1)[1].strip()
        self.date_str = self.header_list[4].split(': ',1)[1].strip()
        self.date = arrow.get(self.date_str)
        self.author = self.header_list[5].split(': ',1)[1].strip()
        self.url = '/posts/{}/{}/{}.html'.format(self.year,self.month,self.html_title)
        self.tags = self.header_list[6].split(':',1)[1].strip()

    def decode_content(self):
        html_out = []
        # |IMG çHeader §Codice
        special_chars = ['|','ç','§']
        temp_code = []
        img_template = open('template/sub/image.html','r',encoding='utf-8').read()
        for r in self.content_list:
            try:
                if r[0] == '§':
                    # print('§',r)
                    temp_code.append(r.split('§',1)[1])
                else:
                    # print(r)
                    if temp_code != []:
                        html_out.append(highlight('\n'.join(temp_code[1:]), PythonLexer(), HtmlFormatter()))
                        temp_code = []
                    if r[0] not in special_chars:
                        html_out.append('<p>{}</p>'.format(r))
                    elif r[0] == '|':
                        img_out = img_template.replace('|IMGPATH|','/img/posts/{}/{}/{}'.format(
                            self.year
                            ,self.month.lower()
                            ,r.split('|')[1]
                        ))
                        html_out.append(img_out)
                    elif r[0] == 'ç':
                        html_out.append('<h2>{}</h2>'.format(r.split('ç')[1]))
            except:
                pass
        if len(temp_code)>0 and temp_code[0] == 'batch':
            html_out.append(highlight('\n'.join(temp_code[1:]), BatchLexer(), HtmlFormatter()))
        elif len(temp_code)>0 and temp_code[0] == 'tsql':
            html_out.append(highlight('\n'.join(temp_code[1:]), TransactSqlLexer(), HtmlFormatter()))
        elif len(temp_code)>0 and temp_code[0] == 'visualbasic':
            html_out.append(highlight('\n'.join(temp_code[1:]), VbNetLexer(), HtmlFormatter()))
        elif len(temp_code)>0 and temp_code[0] == 'json':
            html_out.append(highlight('\n'.join(temp_code[1:]), JsonLexer(), HtmlFormatter()))
        elif temp_code != []:
            html_out.append(highlight('\n'.join(temp_code[1:]), PythonLexer(), HtmlFormatter()))
        return '\n'.join(html_out)

posts_list = []
years = os.listdir('posts/')
for y in years:
    months = os.listdir('posts/{}'.format(y))
    for m in months:
        files = os.listdir('posts/{}/{}'.format(y,m))
        for f in files:
            posts_list.append(Post('posts/{}/{}/{}'.format(y,m,f)))

post_template = open('template/post.html','r',encoding='utf-8').read()
for post in posts_list:
    print(post.title)
    # post.date
    # print(post.title)
    # print(post.year,'-',post.month)
    # print(post.rawtext)
    post_content = post.decode_content()
    curr_path = MAIN_DIR+'/posts/{}/{}/'.format(post.year,post.month)
    if not os.path.exists(curr_path):
        os.makedirs(curr_path)
    page = post_template.replace('|TITLE|',post.title)
    page = page.replace('|SUBTITLE|',post.subtitle)
    page = page.replace('|AUTHOR|',post.author)
    page = page.replace('|MONTH|',post.month)
    page = page.replace('|YEAR|',post.year)
    page = page.replace('|POST|',post_content)
    page = page.replace('|KEYWORDS|',post.tags)
    open(curr_path+'/{}.html'.format(post.html_title),'w',encoding='utf-8').write(page)
    conn.execute('insert into t values(?,?,?,?,?)',
        (post.date_str,post.url,post.title,post.subtitle,post.author))
conn.commit()

# Ordine Post
rows = conn.execute('''select * from t order by strftime('%Y-%m-%d', [date]) desc''').fetchall()
print("N° Articoli:",len(rows))
page = 1
idx_posts_list = []
idx_post_template = open('template/sub/index_post.html','r',encoding='utf-8').read()
idx_template = open('template/index.html','r',encoding='utf-8').read()
prev_page = ''
for num,r in enumerate(rows):
    if (num+1) % 9 == 0:
        idx = idx_template.replace('|POSTS|','\n<hr>\n'.join(idx_posts_list))
        # idx = idx.replace('|NEXTPAGE|','/pages/index/page{}.html'.format(page+1))
        idx = idx.replace('<!-- NEXTPAGE -->',"""<a class="btn btn-primary float-right" href="/pybistuffblog/pages/index/page{}.html">Older Posts &rarr;</a>""".format(page+1))
        if page != 1:
            idx = idx.replace('<!-- PREVPAGE -->',"""<a class="btn btn-primary float-left" href="/pybistuffblog/pages/index/page{}.html">&larr; Newer Posts</a>""".format(prev_page))
            open(MAIN_DIR+'/pages/index/page{}.html'.format(page),'w',encoding='utf-8').write(idx)
        else:
            open(MAIN_DIR+'/index.html','w',encoding='utf-8').write(idx)        
        prev_page = page
        page += 1
        idx_posts_list = []
    idx_post = idx_post_template.replace('|TITLE|',r[2])
    idx_post = idx_post.replace('|SUBTITLE|',r[3])
    idx_post = idx_post.replace('|AUTHOR|',r[4])
    idx_post = idx_post.replace('|DATE|',r[0])
    idx_post = idx_post.replace('|HREF|',r[1].replace('.html',''))
    idx_posts_list.append(idx_post)
    # print(idx_post)
if len(rows) % 9 != 0:
    idx = idx_template.replace('|POSTS|','\n<hr>\n'.join(idx_posts_list))
    # idx = idx.replace('|NEXTPAGE|','/pages/index/page{}.html'.format(page+1))
    # idx = idx.replace('<!-- NEXTPAGE -->',"""<a class="btn btn-primary float-right" href="/pages/index/page{}.html">Older Posts &rarr;</a>""".format(page+1))
    if page != 1:
        idx = idx.replace('<!-- PREVPAGE -->',"""<a class="btn btn-primary float-left" href="/pybistuffblog/pages/index/page{}.html">&larr; Newer Posts</a>""".format(prev_page))
        open(MAIN_DIR+'/pages/index/page{}.html'.format(page),'w',encoding='utf-8').write(idx)
    else:
        open(MAIN_DIR+'/index.html','w',encoding='utf-8').write(idx)    

conn.close()
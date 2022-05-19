import pandas
import time
import requests
from bs4 import BeautifulSoup
import bs4

df = pandas.DataFrame()
dir = {}
domain = "https://bestpractices.coreinfrastructure.org"
path = "/en/projects"
head = []
max_pages = 1
s = requests.session()
s.keep_alive = False

def getInfo(tag):
    str = ""
    if isinstance(tag, bs4.element.NavigableString)==True:
        str += tag.string
    else:
        for el in tag.children:
            str += getInfo(el)
    return str
def addRow(dic):
    global df, dir
    df = df.append(dic,ignore_index=True)
    dir[dic['Name']]=len(df.index)-1

def addColumn(columnName):
    global df
    df[columnName] = pandas.Series(dtype='str')

def updateCell(idx,col,content):
    df.at[idx,col]=content

#   预处理: 表头、最大页数
html = s.get(domain+path+"?page=1").text
document = BeautifulSoup(html,'html.parser')

max_pages = document.find("ul",class_="pagination").find_all("li")[-2].string

thead = document.table.thead
ths = thead.find_all("th")
for th in ths:
    head.append(th.string)
    addColumn(th.string)
# print(head)
#   处理每一页的基础信息数据
for i in range(1,int(max_pages)+1):
    print('Request page ',i)
    res = s.get(domain+path+"?page="+str(i))
    print(res.status_code)
    html = res.text
    document = BeautifulSoup(html,'html.parser')

    print('OK, resolving page ',i)
    trows = document.table.tbody.find_all('tr')
    for tr in trows:
        idx = 0
        row = {}
        for td in tr.find_all('td'):
            row[head[idx]]=getInfo(td)
            idx+=1
        addRow(row)
    print('done...')

timestamp = time.strftime("%Y-%m-%d_%H:%M:%S", time.localtime())
df.to_csv('./result/'+timestamp+'.csv')
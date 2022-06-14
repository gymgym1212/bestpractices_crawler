import pandas as pd

domain = "https://bestpractices.coreinfrastructure.org"
path = "/en/projects.csv"
max_pages = 158
lst = []

for i in range(1,int(max_pages)+1):
    lst.append( pd.read_csv('./result/page'+str(i)+'.csv') )
df = pd.concat(lst,ignore_index=True)
df.to_csv('./result/projects.csv')
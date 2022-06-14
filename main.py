import pandas as pd
import numpy as np
import datetime

df = pd.read_csv('./result/projects_github.csv')
levels = ['first_achieved_gold_at','first_achieved_silver_at','first_achieved_passing_at']
cnts = {'on_progress':[0,0,0,0],}

for idx, row in df.iterrows():
    level = 'on_progress'
    year = '0'
    for i in range(len(levels)):
        tmp = row[levels[i]]
        if tmp != tmp:
            continue
        # print(tmp,type(tmp),tmp is np.nan)
        date = datetime.datetime.strptime(tmp,'%Y-%m-%d %H:%M:%S %Z')
        level = i
        year = date.year
        break

    if level == 'on_progress':
        cnts['on_progress'][3]+=1
    else:
        if year not in cnts:
            cnts[year]=[0,0,0,0]
        cnts[year][i]+=1

print(cnts)


print(len(df))
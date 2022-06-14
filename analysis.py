import pandas as pd
from matplotlib import pyplot as plt

# 绘制最佳实践徽章数据散点图，表示不同成熟度的项目数量
# 这里把 0 - 300 的成熟度换算成了 0% - 100%，更容易理解

df2 = pd.read_csv('./result/projects_github.csv')
x = []
y = []
for i in range(11):
    x.append(i*10)
    y.append(0)
for index,row in df2.iterrows():
    y[int(row['tiered_percentage'])//30]+=1

plt.scatter(x,y,color='b')

plt.ylabel('Amount')
plt.xlabel('Percentage')
plt.title('Best Practice')

for i in range(len(x)):
    plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.1,y[i]+0.1))
plt.legend()

plt.show()



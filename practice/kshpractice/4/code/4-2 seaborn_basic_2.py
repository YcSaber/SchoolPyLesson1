#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
# 忽略警告
import warnings
warnings.filterwarnings('ignore')

# 使用seaborn库绘图
sns.set_style('whitegrid', {'font.sans-serif':['simhei', 'Arial']})
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 加载数据
hr = pd.read_csv('../data/hr.csv', encoding='gbk')
# 提取部门为产品开发部、离职为1的数据
product = hr.iloc[(hr['部门'].values=='产品开发部') & (hr['离职'].values==1), :]
ax = sns.scatterplot(x='评分', y='每月平均工作小时数（小时）', data=product)
plt.title('评价分数与平均工作时间散点图')
plt.show()


# In[2]:


# 通过对点着色和改变标记凸显类别
markers = {'低' : 'o', '中' : 'D', '高' : 's'}
sns.scatterplot(x='评分', y='每月平均工作小时数（小时）',
                     hue='薪资', style='薪资', markers=markers, data=product)
plt.title('评价分数与平均工作时间散点图')
plt.show()


# In[3]:


boston = pd.read_csv('../data/boston_house_prices.csv', encoding='gbk')
sns.lineplot(x='房间数（间）', y='房屋价格（千美元）', data=boston, ci=0)
plt.title('房间数与房屋价格')
plt.show()


# In[4]:


# 提取部门为IT部的数据
IT = hr.iloc[hr['部门'].values=='IT部', :]
sns.lineplot(x='工龄（年）', y='评分', hue='离职', data=IT, ci=0)
plt.title('工龄与上年度评价')
plt.show()


# In[5]:


plt.rcParams['axes.unicode_minus'] = False
corr = boston.corr()  # 特征的相关系数矩阵
sns.heatmap(corr)
plt.title('特征矩阵热力图')
plt.savefig("1.png",dpi=200)
plt.show()


# In[6]:


plt.figure(figsize=(10, 10))
sns.heatmap(corr, annot=True, fmt='.2f')
plt.title('特征矩阵热力图')
plt.show()


# In[7]:


g = sns.PairGrid(boston, vars=['犯罪率', '一氧化氮含量（ppm）', '房间数（间）', '房屋价格（千美元）'])
g = g.map(plt.scatter)
plt.suptitle('矩阵网格图', verticalalignment='bottom' , y=1)
plt.show()


# In[8]:


# 提取部门为销售部，离职为1的数据
sell = hr.iloc[(hr['部门'].values=='销售部') & (hr['离职'].values==1), :]
g = sns.PairGrid(sell,
                 vars=['满意度', '评分', '每月平均工作小时数（小时）'],
                 hue='薪资', palette='Set3')
g = g.map_diag(sns.kdeplot)
g = g.map_offdiag(plt.scatter)
plt.suptitle('不同颜色的矩阵网格图', verticalalignment='bottom' , y=1)
plt.show()


# In[9]:


sns.relplot(x='满意度', y='评分', hue='薪资',
            data=sell)
plt.title('满意度水平与上年度评价')
plt.show()


# In[10]:


sns.relplot(x='满意度', y='评分', hue='5年内升职', row='薪资',
            col='工作事故', data=IT)
plt.show()


# In[11]:


sns.relplot(x='满意度', y='评分', hue='5年内升职', col='工作事故',
            col_wrap=1, data=IT)
plt.show()


# In[ ]:





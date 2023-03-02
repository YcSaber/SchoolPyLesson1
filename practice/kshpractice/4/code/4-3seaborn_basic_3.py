#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import math

# 加载数据
boston = pd.read_csv('../data/boston_house_prices.csv', encoding='gbk')
hr = pd.read_csv('../data/hr.csv', encoding='gbk')

# 使用seaborn库绘图
sns.set_style('whitegrid', {'font.sans-serif':['simhei', 'Arial']})
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 设置正常显示负号
plt.rcParams['axes.unicode_minus']=False

count = hr['部门'].value_counts()
index = count.index
sns.barplot(x=count, y=index)
plt.xticks(rotation=70)
plt.xlabel('部门')
plt.ylabel('总数')
plt.title('各部门人数对比')
plt.show()


# In[2]:


# 绘制x轴与y轴显示数据的计数图
plt.figure(figsize=(8, 4))
plt.subplot(121)
sns.countplot(x='工龄（年）', data=hr)
plt.title('x轴显示数据的计数图')
plt.ylabel('计数')
plt.subplot(122)
sns.countplot(y='工龄（年）', data=hr)
plt.title('y轴显示数据的计数图')
plt.xlabel('计数')
plt.show()


# In[3]:


# 多分类嵌套
sns.countplot(x='5年内升职', hue='薪资', data=hr, palette='Set2')
plt.suptitle('多变量散点图')
plt.ylabel('总数')
plt.show()


# In[4]:


sns.histplot(boston['财产税'], kde=False)
plt.title('单变量的分布图')
plt.ylabel('数量')
plt.show()


# In[5]:


# 提取部门为销售部、离职为1的数据
sale = hr.iloc[(hr['部门'].values=='销售部') & (hr['离职'].values==1), :]
sns.stripplot(x=sale['每月平均工作小时数（小时）'])
plt.title('简单水平分布散点图')
plt.show()


# In[6]:


# 添加随机噪声抖动
# 提取离职为1的数据
hr1 = hr.iloc[hr['离职'].values==1, :]
plt.figure(figsize=(10, 5))
plt.subplot(121)
plt.xticks(rotation=70)
sns.stripplot(x='部门', y='每月平均工作小时数（小时）', data=hr1)  # 默认添加随机噪声
plt.title('默认随机噪声抖动')
plt.subplot(122)
plt.xticks(rotation=70)
sns.stripplot(x='部门', y='每月平均工作小时数（小时）',
                 data=hr1, jitter=False)  # 不添加随机噪声
plt.title('无随机噪声抖动')
plt.show()


# In[7]:


# 提取高薪在职的数据
hr2 = hr.iloc[(hr['薪资'].values=='高') & (hr['离职'].values==0), :]
sns.stripplot(x='5年内升职', y='每月平均工作小时数（小时）',
              hue='部门', data=hr2, jitter=True)
plt.title('前5年是否晋升与平均每月工作时长')
plt.show()


# In[8]:


# 变量沿分类轴方向分类
plt.figure(figsize=(10, 13))
plt.subplot(211)
plt.xticks(rotation=70)
plt.title('不同部门的平均每月工作时长')
sns.stripplot(x='部门', y='每月平均工作小时数（小时）', hue='5年内升职', data=hr2)
plt.subplot(212)
plt.xticks(rotation=70)
sns.stripplot(x='部门', y='每月平均工作小时数（小时）', hue='5年内升职', 
              data=hr2, dodge=True)
plt.show()


# In[9]:


# 简单分布密度散点图
sns.swarmplot(x='部门', y='每月平均工作小时数（小时）', data=hr2)
plt.xticks(rotation=70)
plt.title('不同部门的平均每月工作时长')
plt.show()


# In[10]:


# 添加多个嵌套分类变量
sns.swarmplot(x='部门', y='每月平均工作小时数（小时）',
                 hue='5年内升职', data=hr2)
plt.xticks(rotation=30)
plt.title('不同部门的平均每月工作时长')
plt.show()


# In[11]:


# 绘制普通箱线图与增强箱线图
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].set_title('普通箱线图')
boston['房间数(取整)'] = boston['房间数（间）'].map(math.floor)  # 对房间数取整
sns.boxplot(x='房间数(取整)', y='房屋价格（千美元）', 
            data=boston, orient='v', ax=axes[0])  # 普通
axes[1].set_title('增强箱线图')
sns.boxenplot(x='房间数(取整)', y='房屋价格（千美元）', 
              data=boston, orient='v', ax=axes[1])  # 增强
plt.show()


# In[12]:


# 绘制波士顿房价多变量散点图
sns.pairplot(boston[['犯罪率', '一氧化氮含量（ppm）', '房间数（间）', '低收入人群', '房屋价格（千美元）']])
plt.suptitle('多变量散点图', verticalalignment='bottom', y=1)
plt.show()


# In[13]:


# 指定分类变量散点图
hr3 = sale[['满意度', '总项目数', '工龄（年）', '薪资']]
sns.pairplot(hr3, hue='薪资')
plt.suptitle('多变量分类散点图', verticalalignment='bottom')
plt.show()


# In[ ]:





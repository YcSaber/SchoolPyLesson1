#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] =' SimHei'
# 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_csv('../data/people.csv')
name = data.columns  # 提取其中的columns字段，视为数据的标签
values = data.values  # 提取其中的values字段，数据的存在位置
plt.figure(figsize=(9, 7))  # 设置画布
plt.scatter(values[:, 0], values[:, 1], marker='o')  # 绘制散点图
plt.xlabel('年份')  # 添加横轴标签
plt.ylabel('年末总人口（万人）')  # 添加y轴名称
plt.xticks(range(0, 20), values[range(0, 20), 0], rotation=45)
plt.title('2000-2019年年末总人口散点图')  # 添加图表标题
plt.savefig('../tmp/2000-2019年年末总人口散点图.png')
plt.show()


# In[2]:


# 绘制2000-2019各年龄段年末总人口散点图
plt.figure(figsize=(9, 7))  # 设置画布
plt.scatter(values[:, 0], values[:, 2], marker='o', c='red')  # 绘制散点图
plt.scatter(values[:, 0], values[:, 3], marker='D', c='blue')  # 绘制散点图
plt.scatter(values[:, 0], values[:, 4], marker='v', c='black')  # 绘制散点图
plt.xlabel('年份')  # 添加横轴标签
plt.ylabel('年末总人口（万人）')  # 添加纵轴标签
plt.xticks(range(0, 20), values[range(0, 20), 0], rotation=45)
plt.title('2000-2019年各年龄段年末总人口散点图')  # 添加图表标题
plt.legend(['0-14岁人口', '15-64岁人口', '65岁及以上人口'])  #添加图例
plt.savefig('../tmp/2000-2019年各年龄段年末总人口散点图.png')
plt.show()


# In[3]:


# 2000-2019总人口折线图
plt.figure(figsize=(9, 7))  # 设置画布
plt.plot(values[:, 0], values[:, 1], color='r', linestyle='--')  # 绘制折线图
plt.xlabel('年份')  #添加横轴标签
plt.ylabel('年末总人口（万人）')  # 添加y轴名称
plt.xticks(range(0, 20), values[range(0, 20), 0], rotation=45)
plt.title('2000-2019年年末总人口折线图')  # 添加图表标题
plt.savefig('../tmp/2000-2019年年末总人口折线图.png')
plt.show()


# In[4]:


# 2000-2019各年龄段总人口折线图
plt.figure(figsize=(8, 7))  # 设置画布
plt.plot(values[:, 0], values[:, 2], 'bs-',
       values[:, 0], values[:,3], 'ro-.',
       values[:, 0], values[:, 4], 'gH--')  # 绘制折线图
plt.xlabel('年份')  # 添加横轴标签
plt.ylabel('年末总人口（万人）')  # 添加y轴名称
plt.xticks(range(0, 20), values[range(0, 20), 0], rotation=45)
plt.title('2000-2019年各年龄段总人口点线图')  # 添加图表标题
plt.legend(['0-14岁人口', '15-64岁人口', '65岁及以上人口'])
plt.savefig('../tmp/2000-2019年各年龄段总人口点线图.png')
plt.show()


# In[ ]:





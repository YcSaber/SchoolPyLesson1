#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
data = pd.read_csv('../data/people.csv')
name = data.columns  # 提取其中的columns字段，视为数据的标签
values = data.values  # 提取其中的values字段，数据的存在位置
label = ['0-14岁人口', '15-64岁人口', '65岁及以上人口']  # 刻度标签
plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆
explode = [0.01, 0.01, 0.01]  # 设定各项离心n个半径
plt.pie(values[-1, 2:5], explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
plt.title('2019年各年龄段年末总人口饼图')  # 添加图表标题
plt.savefig('../tmp/2019年各年龄段年末总人口饼图.png')
plt.show()


# In[2]:


label = ['0-14岁人口', '15-64岁人口', '65岁及以上人口']  # 刻度标签
plt.figure(figsize=(9, 7), dpi=60)
plt.bar(range(3), values[-1, 2: 5],width=0.4)
plt.xlabel('年龄段')  # 添加横轴标签
plt.ylabel('年末总人口(万人)')  # 添加y轴名称
plt.xticks(range(3),label)
plt.title('2019年各年龄段年末总人口柱形图')  # 添加图表标题
plt.savefig('../tmp/2019年各年龄段年末总人口柱形图.png')
plt.show()


# In[3]:


# 绘制箱型图
label= ['0-14岁人口', '15-64岁人口', '65岁及以上人口']  # 定义标签
gdp = (list(values[:, 2]), list(values[:, 3]), list(values[:, 4]))
plt.figure(figsize=(7, 6))
plt.boxplot(gdp, notch=True, labels=label, meanline=True)
plt.title('2000-2019年各年龄段年末总人口箱线图')
plt.savefig('../tmp/2000-2019年各年龄段年末总人口箱线图.png')
plt.show()


# In[ ]:





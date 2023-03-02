#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# 设置中文字体
sns.set_style('whitegrid', {'font.sans-serif':['simhei', 'Arial']})

# 忽略警告
import warnings
warnings.filterwarnings('ignore')

# 加载数据
boston = pd.read_csv('../data/boston_house_prices.csv', encoding='gbk')

fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].set_title('修改前的线性回归拟合图')
axes[1].set_title('修改后的线性回归拟合图')
sns.regplot(x='房间数（间）', y='房屋价格（千美元）', data=boston, ax=axes[0])
sns.regplot(x='房间数（间）', y='房屋价格（千美元）', data=boston, ci=50, ax=axes[1])
plt.show()


# In[2]:


sns.lmplot(x='低收入人群', y='房屋价格（千美元）', col='河流穿行', data=boston)
plt.show()


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
sns.set_style({'font.sans-serif':['simhei', 'Arial']})

# 加载数据
hr = pd.read_csv('../data/hr.csv', encoding='gbk')

data = hr.head(100)
# 使用Matplotlib库绘图
color_map = dict(zip(data['薪资'].unique(), ['b', 'y', 'r']))
for species, group in data.groupby('薪资'):
    plt.scatter(group['每月平均工作小时数（小时）'],
                group['满意度'],
                color=color_map[species], alpha=0.4,
                edgecolors=None, label=species)
plt.legend(frameon=True, title='薪资')
plt.xlabel('平均每个月工作时长（小时）')
plt.ylabel('满意度水平')
plt.title('满意度水平与平均每个月工作小时')
plt.show()


# In[2]:


# 使用seaborn库绘图
sns.lmplot('每月平均工作小时数（小时）', '满意度', data, hue='薪资', fit_reg=False, height=4)
plt.xlabel('平均每个月工作时长（小时）')
plt.ylabel('满意度水平')
plt.title('满意度水平与平均每个月工作小时')
plt.show()


# In[3]:


plt.rcParams['axes.unicode_minus'] = False
x = np.arange(1, 10, 2)
y1 = x + 1
y2 = x + 3
y3 = x + 5
# 绘制3条不同的直线
# 第1部分
plt.title('Matplotlib库的绘图风格')
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()

# 第2部分
# 使用seaborn库绘图
sns.set_style('darkgrid')  # 全黑风格
sns.set_style({'font.sans-serif':['simhei', 'Arial']})
sns.lineplot(x=x, y=y1)
sns.lineplot(x=x, y=y2)
sns.lineplot(x=x, y=y3)
plt.title('seaborn库的绘图风格')
plt.show()


# In[4]:


x = np.arange(1, 10, 2)
y1 = x + 1
y2 = x + 3
y3 = x + 5
def showLine(flip=1):
    sns.lineplot(x=x, y=y1)
    sns.lineplot(x=x, y=y2)
    sns.lineplot(x=x, y=y3)
pic = plt.figure(figsize=(12, 8))
with sns.axes_style('darkgrid'):  # 使用darkgrid主题
    pic.add_subplot(2, 3, 1)
    showLine()
    plt.title('darkgrid')
with sns.axes_style('whitegrid'):  # 使用whitegrid主题
    pic.add_subplot(2, 3, 2)
    showLine()
    plt.title('whitegrid')
with sns.axes_style('dark'):  # 使用dark主题
    pic.add_subplot(2, 3, 3)
    showLine()
    plt.title('dark')
with sns.axes_style('white'):  # 使用white主题
    pic.add_subplot(2, 3, 4)
    showLine()
    plt.title('white')
with sns.axes_style('ticks'):  # 使用ticks主题
    pic.add_subplot(2, 3, 5)
    showLine()
    plt.title('ticks')
sns.set_style(style='darkgrid', rc={'font.sans-serif': ['MicrosoftYaHei', 'SimHei'],
                            'grid.color': 'black'})  # 修改主题中参数
pic.add_subplot(2, 3, 6)
showLine()
plt.title('修改参数')
plt.show()


# In[5]:


# 展示四种不同缩放类型的图形
sns.set()
x = np.arange(1, 10, 2)
y1 = x + 1
y2 = x + 3
y3 = x + 5
def showLine(flip=1):
    sns.lineplot(x=x, y=y1)
    sns.lineplot(x=x, y=y2)
    sns.lineplot(x=x, y=y3)
pic = plt.figure(figsize=(8, 8))
# 恢复默认参数
pic = plt.figure(figsize=(8, 8), dpi=100)
with sns.plotting_context('paper'):  # 选择paper类型
    pic.add_subplot(2, 2, 1)
    showLine()
    plt.title('paper')
with sns.plotting_context('notebook'):  # 选择notebook类型
    pic.add_subplot(2, 2, 2)
    showLine()
    plt.title('notebook')
with sns.plotting_context('talk'):  # 选择talk类型
    pic.add_subplot(2, 2, 3)
    showLine()
    plt.title('talk')
with sns.plotting_context('poster'):  # 选择poster类型
    pic.add_subplot(2, 2, 4)
    showLine()
    plt.title('poster')
plt.show()


# In[6]:


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
sns.set_style({'font.sans-serif':['simhei', 'Arial']})
with sns.axes_style('white'):
    showLine()
    sns.despine()  # 默认无参数状态，就是删除上方和右方的边框
    plt.title('控制图形边框')
plt.show()


# In[7]:


with sns.axes_style('white'):
    data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
    sns.boxplot(data=data)
    sns.despine(offset=10, left=False, bottom=False)
    plt.title('控制图形边框')
plt.show()


# In[8]:


# seaborn默认颜色
sns.palplot(sns.color_palette())


# In[9]:


# 导入颜色主题
palette = sns.color_palette('muted')
sns.palplot(palette)


# In[10]:


# HLS颜色空间
sns.palplot(sns.color_palette('hls', 8))


# In[11]:


# 控制颜色亮度以及饱和度
sns.palplot(sns.hls_palette(8, l=.3, s=.8))  # l控制亮度，s控制饱和度


# In[12]:


# 调节颜色亮度和饱和度在视觉上一致
sns.palplot(sns.color_palette('husl', 8))


# In[13]:


# xkcd颜色使用示例
plt.plot(x, y1, sns.xkcd_rgb['pale red'], lw=3)
plt.plot(x, y2, sns.xkcd_rgb['medium green'], lw=3)
plt.plot(x, y3, sns.xkcd_rgb['denim blue'], lw=3)
plt.title('线条颜色示例')
plt.show()


# In[14]:


# 自定义定性调色板
colors = ['windows blue', 'amber', 'greyish', 'faded green', 'dusty purple']
sns.palplot(sns.xkcd_palette(colors))


# In[15]:


# 绘制连续调色板、亮度反转、切换面板的示例
sns.palplot(sns.color_palette('Greens'))
sns.palplot(sns.color_palette('YlOrRd_r'))
sns.palplot(sns.color_palette('YlOrRd_d'))


# In[16]:


# cubehelkix_palette函数
sns.palplot(sns.cubehelix_palette(8, start=1, rot=0))


# In[17]:


x, y = np.random.multivariate_normal([0, 0], [[1, -.5], [-.5, 1]], size=300).T
cmap = sns.cubehelix_palette(as_cmap=True)  # 生产调色板对象
sns.kdeplot(x, y, cmap=cmap, shade=True)
plt.title('连续调色板')
plt.show()


# In[18]:


sns.palplot(sns.light_palette('blue'))
sns.palplot(sns.dark_palette('yellow'))


# In[19]:


# 使用husl颜色空间作为种子
pal = sns.dark_palette((200, 80, 60), input='husl', reverse=True, as_cmap=True)
sns.kdeplot(x, y, cmap=pal)
plt.title('自定义连续调色板')
plt.show()


# In[20]:


# color brewer库中离散调色板
sns.palplot(sns.color_palette('BrBG', 7))
sns.palplot(sns.color_palette('RdBu_r', 7))


# In[21]:


sns.palplot(sns.color_palette('coolwarm', 7))


# In[22]:


sns.palplot(sns.diverging_palette(240, 10, n=7))


# In[23]:


sns.palplot(sns.diverging_palette(150, 275, s=80, l=55, n=7))


# In[24]:


# 创建中间是暗色的调色板
sns.palplot(sns.diverging_palette(250, 15, s=75, l=40, n=7, center='dark'))


# In[25]:


# 通过sep参数控制中间区域渐变宽度
sns.palplot(sns.diverging_palette(150, 275, s=80, l=55, n=7, sep=80))


# In[26]:


x = np.arange(1, 10, 2)
y1 = x + 1
y2 = x + 3
y3 = x + 5
def showLine(flip=1):
    sns.lineplot(x=x, y=y1)
    sns.lineplot(x=x, y=y2)
    sns.lineplot(x=x, y=y3)
# 使用默认调色板
showLine()
plt.title('默认调色板')
plt.show()


# In[27]:


# sns.set_palette函数设置调色板
sns.set_palette('YlOrRd_d')
showLine()
plt.title('使用set_palette设置调色板')
plt.show()


# In[28]:


sns.set()  # 恢复所有默认设置
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pic = plt.figure(figsize=(8, 4))
with sns.color_palette('PuBuGn_d'):  # 临时配置调色板
    pic.add_subplot(1, 2, 1)
    showLine()
    plt.title('使用color_palette设置调色板')
pic.add_subplot(1, 2, 2)  # 使用默认调色板
showLine()
plt.title('默认调色板')
plt.show()


# In[ ]:





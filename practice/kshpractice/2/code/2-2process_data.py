#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_excel('../data/data.xlsx')
print('data中元素是否为空值的布尔型DataFrame为：\n', data.isnull())
print('data中元素是否为非空值的布尔型DataFrame为：\n', data.notnull())


# In[3]:


print('data中每个特征对应的非空值数为：\n', data.count())
print('data中每个特征对应的缺失率为：\n', 1-data.count() / len(data))


# In[4]:


import numpy as np
arr = (18.02, 63.77, 79.52, 29.89, 68.86, 54.49, 92.59, 376.04, 5.92, 83.75, 70.12, 459.38,
       82.96, 37.81, 65.08, 59.07, 47.56, 86.96, 38.38, 1100.34, 7.98, 2.82, 74.76, 87.64,
       67.90, 89.9, 2000.67)
# 利用箱型图的四分位距（IQR）对异常值进行检测
Percentile = np.percentile(arr, [0, 25, 50, 75, 100])  # 计算百分位数
IQR = Percentile[3] - Percentile[1]  # 计算箱型图四分位距
UpLimit = Percentile[3] + IQR*1.5  # 计算临界值上界
arrayownLimit = Percentile[1] - IQR * 1.5  # 计算临界值下界
# 判断异常值，大于上界或小于下界的值即为异常值
abnormal = [i for i in arr if i > UpLimit or i < arrayownLimit] 
print('箱型图的四分位距（IQR）检测出的array中异常值为：\n', abnormal)
print('箱型图的四分位距（IQR）检测出的异常值比例为：\n', len(abnormal) / len(arr))


# In[5]:


# 利用3sigma原则对异常值进行检测
array_mean = np.array(arr).mean()  # 计算平均值
array_sarray = np.array(arr).std()  # 计算标准差
array_cha = arr - array_mean  # 计算元素与平均值之差
# 返回异常值所在位置
ind = [i for i in range(len(array_cha)) if np.abs(array_cha[i]) > array_sarray]
abnormal = [arr[i] for i in ind]  # 返回异常值
print('3sigma原则检测出的array中异常值为：\n', abnormal)
print('3sigma原则检测出的异常值比例为：\n', len(abnormal) / len(arr))


# In[6]:


data1 = pd.read_csv('../data/销售流水记录1.csv', encoding='gb18030')
# 使用列表（list）去重
# 定义去重函数
def delRep(list1):
    list2 = []
    for i in list1:
        if i not in list2:
            list2.append(i)
    return list2 
# 去重
sku_names = list(data1['sku_name'])  # 将sku_name从数据框中提取出来
print('去重前商品总数为：', len(sku_names))
sku_name = delRep(sku_names)  # 使用自定义的去重函数去重
print('使用列表（list）去重后商品的总数为：', len(sku_name))


# In[7]:


# 使用集合（set）去重
print('去重前商品总数为：', len(sku_names))
sku_name_set = set(sku_names)  # 利用set的特性去重
print('使用集合（set）重后商品总数为：', len(sku_name_set))


# In[8]:


# 使用drop_duplicates()方法对sku_name去重
sku_name_pandas = data1['sku_name'].drop_duplicates()  # 对sku_name去重
print('drop_duplicates方法去重之后商品总数为：', len(sku_name_pandas))


# In[9]:


# 使用drop_duplicates()方法对多列去重
print('去重之前销售流水记录表的形状为：', data1.shape)
shapeDet = data1.drop_duplicates(subset=['order_id', 'sku_id']).shape
print('依照订单编号，商品编号去重之后销售流水记录表大小为：', shapeDet)


# In[10]:


# 求取标价和卖价的相似度
corrDet = data1[['sku_prc', 'sku_sale_prc']].corr(method='kendall')
print('标价和卖价的kendall相似度为：\n', corrDet)


# In[11]:


# 求出sku_name,sku_prc,sku_sale_prc三个特征的相似度
corrDet1 = data1[['sku_name', 'sku_prc', 'sku_sale_prc']].corr(method='pearson')
print('商品名称，标价和卖价价的pearson相似度为：\n', corrDet1)


# In[12]:


# 使用DataFrame.equals()进行特征去重
def FeatureEquals(df):
    dfEquals = pd.DataFrame([], columns=df.columns, index=df.columns)
    for i in df.columns:
       for j in df.columns:
           dfEquals.loc[i, j] = df.loc[: , i].equals(df.loc[: , j])
    return dfEquals
# 应用上述函数
detEquals = FeatureEquals(data1)
print('data1的特征相等矩阵的前5行5列为：\n', detEquals.iloc[: 5, : 5])


# In[13]:


# 遍历所有数据
lenDet = detEquals.shape[0]
dupCol = []
for k in range(lenDet):
    for l in range(k+1, lenDet):
        if detEquals.iloc[k, l] & (detEquals.columns[l] not in dupCol):
            dupCol.append(detEquals.columns[l])
# 进行去重操作
print('需要删除的列为：', dupCol)
data1.drop(dupCol, axis=1, inplace=True)
print('删除多余列后detail的特征数目为：', data1.shape[1])


# In[14]:


# 使用dropna()方法删除缺失值
print('去除含缺失的列前detail的形状为：', data1.shape)
print('去除含缺失的列后detail的形状为：', data1.dropna(axis=1, how='any').shape)


# In[16]:


# 使用filena()方法替换缺失值
print('datal每个特征缺失的数目为：\n', data1.isnull().sum())
data1 = data1.fillna(-99)
print('datal每个特征缺失的数目为：\n', data1.isnull().sum())


# In[17]:


# 线性插值
import numpy as np
from scipy.interpolate import interp1d
x = np.array([1, 2, 4, 5, 6, 8, 10])  # 创建自变量x
y1 = np.array([3, 17, 129, 251, 433, 1025, 2001])  # 创建因变量y1
y2 = np.array([5, 8, 14, 17, 20, 26, 32])  # 创建因变量y2
LinearInsValue1 = interp1d(x, y1, kind='linear')  # 线性插值拟合x, y1
LinearInsValue2 = interp1d(x, y2, kind='linear')  # 线性插值拟合x, y2
print('当x为3、7、9时，使用线性插值y1为：', LinearInsValue1([3, 7, 9]))
print('当x为3、7、9时，使用线性插值y2为：', LinearInsValue2([3, 7, 9]))


# In[18]:


# 拉格朗日插值
from scipy.interpolate import lagrange
LargeInsValue1 = lagrange(x, y1)  # 拉格朗日插值拟合x, y1
LargeInsValue2 = lagrange(x, y2)  # 拉格朗日插值拟合x, y2
print('当x为3、7、9时，使用拉格朗日插值y1为：', LargeInsValue1([3, 7, 9]))
print('当x为3、7、9时，使用拉格朗日插值y2为：', LargeInsValue2([3, 7, 9]))


# In[19]:


# 样条插值
from scipy.interpolate import splrep, splev
tck1 = splrep(x, y1)
x_new = np.array([3, 7, 9])
SplineInsValue1 = splev(x_new, tck1)  # 样条插值拟合x, y1
tck2 = splrep(x, y2)
SplineInsValue2 = splev(x_new, tck2)  # 样条插值拟合x, y2
print('当x为3、7、9时，使用样条插值y1为：', SplineInsValue1)
print('当x为3、7、9时，使用样条插值y2为：', SplineInsValue2)


# In[20]:


# 索引完全相同时使用concat函数横向堆叠
import pandas as pd
# 创建数据
data1 = pd.DataFrame({
    'A': ['A1', 'A2', 'A3', 'A4'], 'B': ['B1', 'B2', 'B3', 'B4'], 'C': ['C1', 'C2','C3', 'C4'],
    'D': ['D1', 'D2', 'D3', 'D4']}, index=[1, 2, 3, 4])
data2 = pd.DataFrame({
    'B': ['B2', 'B4', 'B6', 'B8'], 'D': ['D2', 'D4', 'D6', 'D8'], 'F': ['F2', 'F4','F6', 'F8']},
    index=[2, 4, 6, 8])
print('内连接合并后的数据框为：\n', pd.concat([data1, data2], axis=1, join='inner'))
print('外连接合并后的数据框为：\n', pd.concat([data1, data2], axis=1, join='outer'))


# In[21]:


# 表名完全相同时使用concat函数纵向堆叠
print('内连接纵向合并后的数据框为：\n', pd.concat([data1, data2], axis=0, join='inner'))
print('外连接纵向合并后的数据框为：\n', pd.concat([data1, data2], axis=0, join='outer'))


# In[22]:


# 使用append()方法纵向表堆叠
data1 = pd.read_csv('../data/销售流水记录1.csv', encoding='gb18030')
print('堆叠前data1数据框的大小：', data1.shape)
data2 = pd.read_csv('../data/销售流水记录2.csv', encoding='gb18030')
print('堆叠前data2数据框的大小：', data2.shape)
print('append纵向堆叠后的数据框大小为：', data1.append(data2).shape)


# In[23]:


# 使用merge()函数合并数据
import pandas as pd
data1 = pd.read_csv('../data/销售流水记录1.csv', encoding='gb18030', low_memory=False)
print('销售流水记录表的原始形状为：', data1.shape)
goods_info = pd.read_excel('../data/商品信息表.xlsx')
print('商品信息表的原始形状为：', goods_info.shape)
sale_detail = pd.merge(data1, goods_info, on='sku_id')
print('销售流水记录表和商品信息表主键合并后的形状为：', sale_detail.shape)


# In[24]:


# 使用join()方法实现主键合并
sale_detail2 = data1.join(goods_info, on='sku_id', rsuffix='1')
print('销售流水记录表和商品信息表join合并后的形状为：', sale_detail2.shape)


# In[25]:


# 重叠合并
# 生成两个数据框
df1 = pd.DataFrame({'a': [2., np.nan, 1., np.nan], 'b': [np.nan, 6., np.nan, 8.],
'c': range(1, 8, 2)})
df2 = pd.DataFrame({'a': [6., 2., np.nan, 1., 8.], 'b': [np.nan, 2., 5., 8., 9.]})
# 采取不同的方式
print('\ndf1.combine_first(df2)的结果：\n', df1.combine_first(df2))
print('\ndf2.combine_first(df1)的结果：\n', df2.combine_first(df1))


# In[ ]:





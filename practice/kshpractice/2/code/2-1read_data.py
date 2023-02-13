#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 使用read_csv读取销售流水记录表
import pandas as pd
data1 = pd.read_csv('../data/销售流水记录1.csv', encoding='gb18030')
print('使用read_csv读取的销售流水记录表的长度为：', len(data1))


# In[3]:


# 使用read_csv读取销售流水记录表, header=None
data2 = pd.read_csv('../data/销售流水记录2.csv', header=None, encoding='gb18030')
print('使用read_csv读取的销售流水记录表的长度为：', len(data2))
print('列名为None时订单信息表为：')
data2.iloc[0:5,0:4]


# In[4]:


# 使用to_csv函数将销售流水记录表写入csv文件
import os
print('销售流水记录表写入文本文件前目录内文件列表为：\n', os.listdir('../tmp'))
data1.to_csv('../tmp/SaleInfo.csv', sep=';', index=False)  # 将data1以CSV格式存储
print('销售流水记录表表写入文本文件后目录内文件列表为：\n', os.listdir('../tmp'))


# In[5]:


# 使用read_excel函数读取折扣信息表
data3 = pd.read_excel('../data/折扣信息表.xlsx')  # 读取折扣信息表的数据
print('data3信息长度为：', len(data3))


# In[6]:


# 使用to_excel函数将折扣信息表存储为excel文件
print('data3写入Excel文件前目录内文件列表为：\n', os.listdir('../tmp'))
data3.to_excel('../tmp/data_save.xlsx')
print('data3写入Excel文件后目录内文件列表为：\n', os.listdir('../tmp'))


# In[20]:


import sqlalchemy
# 创建一个mysql连接器，用户名为root，密码为123456
# 地址为127.0.0.1，数据库名称为test1
sqlalchemy_db = sqlalchemy.create_engine(
            'mysql+pymysql://root:syccsn0305@127.0.0.1:3306/test1')
print(sqlalchemy_db)


# In[23]:


# 使用read_sql_query函数查看test中的数据表数目
formlist = pd.read_sql_query('show tables', con=sqlalchemy_db)
print('testdb数据库数据表清单为：', '\n', formlist)


# In[24]:


# 使用read_sql_table函数读取销售流水记录表sale2
detail1 = pd.read_sql_table('sale2', con=sqlalchemy_db)
print('使用read_sql_table读取销售流水记录表的长度为：', len(detail1))


# In[25]:


# 使用read_sql函数读取销售流水记录表
detail2 = pd.read_sql('select * from sale2', con=sqlalchemy_db)
print('使用read_sql函数 + sql语句读取销售流水记录表的长度为：', len(detail2))
detail3 = pd.read_sql('sale2', con=sqlalchemy_db)
print('使用read_sql函数+表格名称读取的销售流水记录表的长度为：', len(detail3))


# In[26]:


# 使用to_sql方法存储orderData
detail1.to_sql('sale_copy', con=sqlalchemy_db, index=False, if_exists='replace')
# 使用read_sql读取test表格
formlist1 = pd.read_sql_query('show tables', con=sqlalchemy_db)
print('新增一个表格后test数据库数据表清单为：', '\n', formlist1)


# In[ ]:





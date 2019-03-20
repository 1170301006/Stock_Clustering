import pandas as pd
from sqlalchemy import create_engine
import tushare as ts

#从tushare接口读入数据
pro = ts.pro_api()
data = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
 # 初始化数据库，使用pymysql模块，
engine = create_engine('mysql+pymysql://root:hanxiao912@localhost:3307/stock')

#写入MySQL数据库
data.to_sql("stock_list", engine, index=False)

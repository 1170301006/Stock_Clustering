import pandas as pd
from sqlalchemy import create_engine
import tushare as ts

pro = ts.pro_api()
data =pro.stock_company(exchange='SZSE', fields='ts_code,chairman,manager,secretary,reg_capital,setup_date,province')
 # 初始化数据库，使用pymysql模块，
engine = create_engine('mysql+pymysql://root:hanxiao912@localhost:3307/stock')


data.to_sql("stock_list1", engine, index=False)
import tushare as ts
import pandas as pd
from sqlalchemy import create_engine

pro = ts.pro_api()
engine = create_engine('mysql+pymysql://root:hanxiao912@localhost:3307/stock')
sql = '''
      select ts_code from stock_info 
       '''
result = pd.read_sql_query(sql, engine)

for x in range(result.size):
    df = pro.daily(ts_code=result.loc[x, 'ts_code'], start_date='20140101', end_date='20190320')
    df.to_sql(result.loc[x, 'ts_code'], engine, index=False)


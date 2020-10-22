import sqlalchemy as sa
import pandas as pd
import pyodbc
from pandas.io.json import json_normalize
import sqlalchemy
from sqlalchemy import create_engine
import pandas.io.sql as psql
import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import pyodbc
import urllib

#from flask_sqlalchemy import SQLAlchemy

#
params = urllib.parse.quote_plus("DRIVER={ODBC Driver 13 for SQL Server};"
                                 "SERVER=CHY-GPSQL16P3;"
                                 "DATABASE=Fiber;"
                                 "UID=SvcFiberDB_read_Python;"
                                 "PWD=6fKxOZe74PD5Zb2uifXA;"
                                 "Trusted_Connection=yes"
                                )
#
engine = sa.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))

#
# # In[6]:
with engine.connect() as conn, conn.begin():
    sql = 'select * from sentinel_test'
    df = psql.read_sql_query(sql, conn)

    for row in df:
        print(f'Rows = {row}')
    print()

# import pyodbc
# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=CHY-GPSQL16P3;DATABASE=Fiber;UID=SvcFiberDB_read_Python;PWD=6fKxOZe74PD5Zb2uifXA')
#
# #putting to use
# SQL = "select Field1, Field2 from someTable"
# cursor = cnxn.cursor()
# cursor.execute(SQL)
# row = cursor.fetchall()
# for r in row:
#     print r[0] #field1
#     print r[1] #field2
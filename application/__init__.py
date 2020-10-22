from flask import Flask  # import flask
#from flask_sqlalchemy import SQLAlchemy

import urllib
from sqlalchemy import create_engine

params = urllib.parse.quote_plus("DRIVER={ODBC Driver 13 for SQL Server};"
                                 "SERVER=CHY-GPSQL16P3;"
                                 "DATABASE=Fiber;"
                                 "UID=SvcFiberDB_read_Python;"
                                 "PWD=6fKxOZe74PD5Zb2uifXA;"
                                 "Trusted_Connection=yes"
                                )

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)

app = Flask(__name__)  # create an app instance

@app.route("/")  # at the end point /
def hello():  # call method hello
    return "Hello World! This is test. Debugger mode is on"  # which returns "hello world"


if __name__ == "__main__":  # on running python app.py
    app.run(debug=True)  # run the flask app

with engine.connect() as conn, conn.begin():
    sql = 'select * from sentinel_test'
    df = sql.read_sql_query(sql, conn)
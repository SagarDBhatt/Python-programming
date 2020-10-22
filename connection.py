import pyodbc


def read(conn):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("select * from sentinel_test")

    for row in cursor:
        print(f'row = {row}')
    print()


conn = pyodbc.connect(
                "DRIVER={ODBC Driver 13 for SQL Server};"
                "SERVER=CHY-GPSQL16P3;"
                "DATABASE=Fiber;"
                "UID=SvcFiberDB_read_Python;"
                "PWD=6fKxOZe74PD5Zb2uifXA;"
                "Trusted_Connection=yes"
)

read(conn)

conn.close()

from ExcelCalc import year, TouristsPerYear, countries, values, TransportArray, transport, \
    trimina
import sqlite3
from sqlite3 import Error
def create_connection(db_file):  #dhmiourgoume thn sunarthsh create_connection me orisma db file, h opoia kanei connect sth vash sqlite tou db file allios typonei to error
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

def create_table(conn,create_table_sql): #dhmiourgoume thn sunarthsh create_table me orisma  to connection ths vashs pou theloume  kai ton sql kwdika gia thn dhmiourgeia vashs.
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
#dhmiourgw tis sunarthseis insert_values pou exoun ton sql kwdika gia insert sto kathe  table . otan tis kalw me orisma insert= oi times pou thelw na boun ston pinaka , kai mou epistrefei to id ths grammhs pou ekane insert
def insert_values(conn,insert):
    sql = """ INSERT INTO touristsperyear(year,tourists) VALUES(?,?) """
    cur = conn.cursor()
    cur.execute(sql,insert)
    return cur.lastrowid
def insert_values1(conn,insert):
    sql = """ INSERT INTO topcountries(year,tourists,country) VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql,insert)
    return cur.lastrowid
def insert_values2(conn,insert):
    sql = """ INSERT INTO touristsTransported(year,tourists,Transport) VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, insert)
    return cur.lastrowid
def insert_values3(conn,insert):
    sql = """ INSERT INTO touristsEvery3months(year,trimino,tourists) VALUES(?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql,insert)
    return cur.lastrowid
def main():
    database = r"Touristes.db" #to onoma tis vashs pou tha dhmiourghsw
    # ustera grafw ton sql kwdika gia thn dhmiourgia ton tables
    sql_create_touristsperyear_table =  """ CREATE TABLE IF NOT EXISTS touristsperyear(
                                     year integer,
                                     tourists integer 
                                     ); """
    sql_create_topcountries_table = """ CREATE TABLE IF NOT EXISTS topcountries(
                                    year integer,
                                    tourists integer,
                                    country text 
                                    ); """
    sql_create_touristsTransported_table = """CREATE TABLE IF NOT EXISTS touristsTransported(
                                                year integer,
                                                tourists integer,
                                                Transport text
    );"""
    sql_create_touristsEvery3months =""" CREATE TABLE IF NOT EXISTS touristsEvery3months(
                                        year integer,
                                        trimino integer,
                                        tourists integer
                                        );"""
    conn = create_connection(database)

    if conn is not None:
        create_table(conn,sql_create_touristsperyear_table)
        create_table(conn,sql_create_topcountries_table)
        create_table(conn,sql_create_touristsTransported_table)
        create_table(conn,sql_create_touristsEvery3months)
    else:
        print('Error ! cannot create database')
    with conn:
        for i in range(len(TouristsPerYear)):
            insert_values(conn,[year[i], TouristsPerYear[i]])
        for z in range(len(year)):
            for i in range(4):
                insert_values1(conn,[year[z],values[z][i],countries[z][i]])
        for r in range(4):
            for o in range(4):
                insert_values2(conn,[year[r], transport[o], TransportArray[r][o]])
                insert_values3(conn,[year[r],o+1,trimina[r][o]])
if __name__ == '__main__':
    main()
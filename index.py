import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Successfully connected")
        return conn
    except Error as e:
        print(e)
    
    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def insert_client(conn, query):
    try:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
        print("Successfully inserted")
        print(c.lastrowid)
        return c.lastrowid
    except Error as e:
        print(e)

def main():
    database = r"./pythonsqlite.db"

    sql_create_clients_table = """ CREATE TABLE IF NOT EXISTS clients (id integer PRIMARY KEY, name
                                        name text NOT NULL, begin_date text, end_date text); """

    sql_insert_clients_table = """ INSERT INTO clients (name, begin_date, end_date) VALUES ('Jose', '2020-07-07', '2020-07-07'); """

    conn = create_connection(database)
    # create tables
    if conn is not None:
        #create clients table
        create_table(conn, sql_create_clients_table)

        #insert clients table
        insert_client(conn, sql_insert_clients_table)
    else:
        print("Error! cannot create the database connection")

if __name__ == '__main__':
    main()
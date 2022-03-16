import sqlite3

with sqlite3.connect('data.db') as sql_conn:
    cursor  =  sql_conn.cursor()

    tbl_query='''DROP TABLE IF EXISTS employees;

        CREATE TABLE employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image VARCHAR(250),
            first_name VARCHAR(20), 
            last_name VARCHAR(30),
            email VARCHAR(50)NOT NULL,
            department TEXT,
            leave_days INTEGER,
            created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
            
        );
    '''

    cursor.executescript(tbl_query)

sql_conn.commit()

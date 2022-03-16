import sqlite3

def create_data_base_connection():
    with sqlite3.connect('data.db') as sql_conn:
        cursor  =  sql_conn.cursor()

        # create table 
        tbl_query='''DROP TABLE IF EXISTS MOCK_DATA;

            CREATE TABLE MOCK_DATA (
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

    # fetch data from the sql file and load to the DB
    with open('MOCK_DATA.sql') as fp:
        print("Data loading")
        sql_conn.executescript(fp.read())
        print("data has been loaded")

    sql_conn.commit()

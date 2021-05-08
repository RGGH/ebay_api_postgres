#!/usr/bin/python
import psycopg2
from config import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')
    
        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
        
        cur.execute('SELECT * from api_data')
        rows = cur.fetchall()
        for row in rows:
            print(row)

	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
            
def api_ins(api_data):
    """ Connect to the PostgreSQL database server and insert api data """
    
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database to insert values...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        
        # insert multiple rows of api data
        cur.executemany(
         """INSERT INTO api_data (title,current_price,buy_now,country,url) 
            VALUES(%(title)s,%(current_price)s,%(buy_now)s,%(country)s,%(url)s)""",api_data
        )
        
        conn.commit()
        print('Successfully data inserted in to the table...\n')
        
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
            print('Database connection closed.')
            
def sold_ins(sold_data):
    """ Connect to the PostgreSQL database server and insert api data """
    
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database to insert values...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        
        # insert multiple rows of api data
        cur.executemany(
         """INSERT INTO sold_data (description, bid) 
            VALUES(%(description)s,%(bid)s)""",sold_data
        )
        
        conn.commit()
        print('Successfully data inserted in to the table...\n')
        
    # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
            print('Database connection closed.')

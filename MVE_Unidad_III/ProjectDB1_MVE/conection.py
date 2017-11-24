import psycopg2
from config import config

def connect():
    """Connect to the postgresql database server"""
    conn = None

    try:
        params = config()

        print('Connection to the Postgresql database....')
        conn= psycopg2.connect(**params)

        #create cursor
        cursor = conn.cursor()

        print('Postgrestql database version:')
        cursor.execute('SELECT version()')

        #display the postgrestql database server version
        db_version = cursor.fetchone()
        print(db_version)
        cursor.close()

        #close the comunicationn wiyh the postgrsql
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    connect()

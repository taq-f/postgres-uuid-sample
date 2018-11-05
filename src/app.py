import uuid
import psycopg2
import psycopg2.extras
psycopg2.extras.register_uuid()

def insert(connect_info):
    with psycopg2.connect(**connect_info) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            id = uuid.uuid4()
            cur.execute('INSERT INTO uuid_sample VALUES (%s, %s)', (id, str(id)))

def select(connect_info):
    with psycopg2.connect(**connect_info) as conn:
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute('SELECT id, value FROM uuid_sample')
            for row in cur:
                print('=============================')
                print('type(row[0])', type(row[0]))
                print(row[0])
                print('type(row[1])', type(row[1]))
                print(row[1])

if __name__ == '__main__':
    connect_info = dict(
        host='postgres',
        user='postgres',
        password='postgres',
        port=5432,
    )
    insert(connect_info)
    select(connect_info)

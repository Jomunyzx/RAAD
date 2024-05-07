import mysql.connector
from mysql.connector import pooling
import time
import base64

db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    host='mysql.hostify.cz',
    database='db_44046_CP_x_MySQL_test',
    user='db_44046_CP_x_MySQL_test',
    password=base64.b64decode('QWRtaW4x').decode()
)

def check_item(x_coord, y_coord, z_coord, query):
    row = None
    try:
        conn = db_pool.get_connection()

        cursor = conn.cursor()
        cursor.execute(query, (x_coord, y_coord, z_coord))
        row = cursor.fetchone()

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return row

while True:
    block_o = check_item(0, 101, 0, "SELECT * FROM co_block WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1")
    chest_o = check_item(0, 101, 0, "SELECT * FROM co_container WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1")

    time.sleep(0.5)

    block_n = check_item(0, 101, 0, "SELECT * FROM co_block WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1")
    chest_n = check_item(0, 101, 0, "SELECT * FROM co_container WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1")

    if chest_o != chest_n:
        if chest_o[11] == 0 and chest_n[11] == 1:
            print(f'\n ADDED {chest_o} | {chest_n} \n')
        elif chest_o[11] == 1 and chest_n[11] == 0:
            print(f'\n REMOVED {chest_o} | {chest_n} \n')
    elif block_o != block_n:
        if block_o[11] == 1 and block_n[11] == 0:
            print(f"\n| DESTROYED  |  {block_o}  |  {block_n} \n")
        elif block_o[11] == 0 and block_n[11] == 1:
            print(f"\n | PLACED  |  {block_o}  |  {block_n} \n")
        elif block_o[11] == 2 or block_n[11] == 2:
            print(f"\n | ACTION |  {block_o}  |  {block_n} \n")
        else:
            print("something changed")
    else:
        print(f"{chest_o} | {chest_n}")
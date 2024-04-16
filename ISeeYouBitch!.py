import mysql.connector
from mysql.connector import pooling
import time
import base64


# Create connection pool
db_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=5,
    pool_reset_session=True,
    host='mysql.hostify.cz',
    database='db_44046_CP_x_MySQL_test',
    user='db_44046_CP_x_MySQL_test',
    password=base64.b64decode('QWRtaW4x').decode()
)

def check_item(x_coord, y_coord, z_coord):
    row_it = None
    try:
        conn = db_pool.get_connection() 

        cursor = conn.cursor()
        query = "SELECT * FROM co_container WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1"
        cursor.execute(query, (x_coord, y_coord, z_coord))
        row_it = cursor.fetchone()

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return row_it

def check_block(x_coord, y_coord, z_coord):
    row_bl = None
    try:
        conn = db_pool.get_connection() 

        cursor = conn.cursor()
        query = "SELECT * FROM co_block WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1"
        cursor.execute(query, (x_coord, y_coord, z_coord))
        row_bl = cursor.fetchone()

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals():
            conn.close()

    return row_bl




while True:
    tmp_row_it = check_item(0, 101, 0)
    tmp_row_bl = check_block(0, 101, 0)
    time.sleep(1)
    new_row_it = check_item(0, 101, 0)
    new_row_bl = check_block(0, 101, 0)

    if tmp_row_it != new_row_it:
        if tmp_row_it[9] > new_row_it[9]:
            print(f"!! SOMEONE IS STEALING !! (amount: {tmp_row_it[9] - new_row_it[9]})")
        elif tmp_row_it[9] < new_row_it[9]:
            print(f"SOMEONE IS ADDING ITEMS (amount: {new_row_it[9] - tmp_row_it[9]})")
    elif tmp_row_bl != new_row_bl:
        if tmp_row_bl[11] == 1 and new_row_bl[11] == 0:
            print(f"| CHANGED |  DESTROYED  |  {tmp_row_bl}  |  {new_row_bl}")
        elif tmp_row_bl[11] == 0 and new_row_bl[11] == 1:
            print(f"| CHANGED |  PLACED  |  {tmp_row_bl}  |  {new_row_bl}")
        elif tmp_row_bl[11] == 2 or new_row_bl[11] == 2:
            print(f"| ACTION |  CHEST  |  {tmp_row_bl}  |  {new_row_bl}")
        else:
            print("something changed")
    else:
        print(f"| NOTHING | {tmp_row_it[9]}")

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
    row = None
    try:
        conn = db_pool.get_connection()

        cursor = conn.cursor()
        query = "SELECT * FROM co_container WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1"
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
    tmp_row = check_item(0, 101, 0)
    time.sleep(0.5)
    new_row = check_item(0, 101, 0)

    if tmp_row != new_row:
        if tmp_row[11] == 0 and new_row[11] == 1:
            print(f'\n ADDED {tmp_row} | {new_row} \n')
        elif tmp_row[11] == 1 and new_row[11] == 0:
            print(f'\n REMOVED {tmp_row} | {new_row} \n')
        

    else:
        print(f"| NOTHING | {tmp_row} | {new_row}")

import mysql.connector, time

def check_item(database_name, x_coord, y_coord, z_coord):
    row = None  # Initialize row variable
    try:
        conn = mysql.connector.connect(
            host='mysql.hostify.cz',
            user='db_44046_CP_x_MySQL_test',
            password='Admin1',
            database=database_name
        )

        cursor = conn.cursor()
        query = "SELECT * FROM co_block WHERE x = %s AND y = %s AND z = %s ORDER BY rowid DESC LIMIT 1"
        cursor.execute(query, (x_coord, y_coord, z_coord))
        row = cursor.fetchone()

    except mysql.connector.Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass

    return row  # Return the fetched row


while True:
    tmp_row = check_item("db_44046_CP_x_MySQL_test", 0, 101, 0)
    time.sleep(1)
    new_row = check_item("db_44046_CP_x_MySQL_test", 0, 101, 0)

    if tmp_row != new_row:
        print(f"| CHANGED |  {new_row}  |  {tmp_row}")
    else:
        print(f"| NOTHING |")
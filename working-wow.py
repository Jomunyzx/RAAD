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
    tmp_row = check_item("db_44046_CP_x_MySQL_test", -859, 71, -2667)
    time.sleep(1)
    new_row = check_item("db_44046_CP_x_MySQL_test", -859, 71, -2667)

    if tmp_row != new_row:
        if tmp_row[11] == 1 and new_row[11] == 0:
            print(f"| CHANGED |  DESTROYED  |  {tmp_row}  |  {new_row}")
        elif tmp_row[11] == 0 and new_row[11] == 1:
            print(f"| CHANGED |  PLACED  |  {tmp_row}  |  {new_row}")
        elif tmp_row[11] == 2 or new_row[11] == 2:
            print(f"| CHANGED |  CHEST  |  {tmp_row}  |  {new_row}")
    else:
        print(f"| NOTHING |")


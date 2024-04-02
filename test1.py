import mysql.connector

def check_item(database_name, x_coord, y_coord, z_coord):
    try:
        # Connect to MySQL database
        conn = mysql.connector.connect(
            host='mysql.hostify.cz',
            user='db_44046_CP_x_MySQL_test',
            password='Admin1',
            database=database_name
        )

        # Create cursor
        cursor = conn.cursor()

        # Execute query to check for any changes in the specific row
        query = "SELECT * FROM co_block WHERE x = %s AND y = %s AND z = %s"
        cursor.execute(query, (x_coord, y_coord, z_coord))

        # Fetch the row
        row = cursor.fetchone()

        if row:
            print("Item found:")
            print(row)
        else:
            print("No item found with the specified coordinates.")

    except mysql.connector.Error as e:  
        print("Error connecting to MySQL:", e)

    finally:
        # Close cursor and connection
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass

# Call the function with the database name and specific coordinates
check_item("db_44046_CP_x_MySQL_test", 0, 101, 1)

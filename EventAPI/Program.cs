using System;
using MySqlConnector;

class Program
{
    static void Main(string[] args)
    {
        // MySQL database connection parameters
        string server = "mysql.hostify.cz";
        string database = "db_44046_CP_x_MySQL_test";
        string uid = "db_44046_CP_x_MySQL_test";
        string password = "Admin1";

        string connectionString = $"Server={server};Database={database};Uid={uid};Pwd={password};";

        try
        {
            // Connect to MySQL database
            using (var connection = new MySqlConnection(connectionString))
            {
                connection.Open();

                // SQL query to select data from the co_block table
                string query = "SELECT * FROM co_block";

                // Execute the query
                using (var cmd = new MySqlCommand(query, connection))
                {
                    using (var reader = cmd.ExecuteReader())
                    {
                        // Loop through the results and print them
                        while (reader.Read())
                        {
                            // Assuming there are two columns in the co_block table
                            Console.WriteLine($"Column 1: {reader.GetString(0)}, Column 2: {reader.GetString(1)}");
                            // You can access other columns similarly using reader.GetXXX methods
                        }
                    }
                }
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }

        Console.ReadLine();
    }
}

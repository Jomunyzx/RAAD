using System;
using MySql.Data.MySqlClient;

class Program
{
    static void Main()
    {
        string server = "mysql.hostify.cz";
        string username = "db_44046_CP_x_MySQL_test";
        string password = "Admin1";
        string database = "db_44046_CP_x_MySQL_test";

        var connectionStringBuilder = new MySqlConnectionStringBuilder
        {
            Server = server,
            UserID = username,
            Password = password,
            Database = database
        };

        string connectionString = connectionStringBuilder.ToString();

        try
        {
            using (MySqlConnection connection = new MySqlConnection(connectionString))
            {
                connection.Open();
                string query = "SELECT COUNT(*) FROM co_block WHERE `user` = 17";

                using (MySqlCommand command = new MySqlCommand(query, connection))
                {
                    int count = Convert.ToInt32(command.ExecuteScalar()); // ExecuteScalar returns the first column of the first row
                    Console.WriteLine($"Number of rows where user = 17: {count}");
                }
            }
        }
        catch (MySqlException ex)
        {
            Console.WriteLine($"MySQL Error: {ex.Message}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }

        Console.WriteLine("Press any key to exit...");
        Console.ReadKey();
    }
}
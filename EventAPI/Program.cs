using System;
using McQueryLib.Net;


// https://chat.openai.com/share/b947ff38-f6bf-4b59-a376-b7b412f4aafb

class Program
{
    static void Main(string[] args)
    {
        string serverIp = "kingdoms.mc.hostify.cz";
        int serverPort = 25565;

        McQueryClient client = new McQueryClient(serverIp, serverPort);

        client.PlayerJoined += (sender, e) =>
        {
            Console.WriteLine($"Player {e.PlayerName} joined the server.");
        };

        try
        {
            client.Connect();

            Console.WriteLine("Listening for player join events. Press any key to exit...");
            Console.ReadKey();
        }
        catch (Exception ex)
        {
            Console.WriteLine($"An error occurred: {ex.Message}");
        }
        finally
        {
            client.Disconnect();
        }
    }
}

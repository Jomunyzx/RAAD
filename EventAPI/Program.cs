using System;
using System.Threading.Tasks;
using BukkitNET;
using BukkitNET.Events;
using BukkitNET.Events.PlayerEvents;

public class MyListener : BukkitNET.Events.Listener
{
    private string apiKey = "YOUR_API_KEY_HERE"; // Replace with your actual API key

    [EventHandler]
    public void OnPlayerJoin(PlayerJoinEvent e)
    {
        string welcomeMessage = GetWelcomeMessage();
        Bukkit.BroadcastMessage(welcomeMessage);
    }

    private string GetWelcomeMessage()
    {
        return "Welcome to the server!";
    }
}

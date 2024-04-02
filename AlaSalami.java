import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.Locale;
import org.bukkit.Material;


public class Util {
    public static String byteDataToString(byte[] data, int type) {
        String result = "";
        if (data != null) {
            Material material = Util.getType(type);
            if (material == null) {
                return result;
            }

            result = new String(data, StandardCharsets.UTF_8);
            if (result.length() > 0) {
                if (result.matches("\\d+")) {
                    result = result + ",";
                }
                if (result.contains(",")) {
                    String[] blockDataSplit = result.split(",");
                    ArrayList<String> blockDataArray = new ArrayList<>();
                    for (String blockData : blockDataSplit) {
                        String block = getBlockDataString(Integer.parseInt(blockData));
                        if (block.length() > 0) {
                            blockDataArray.add(block);
                        }
                    }

                    if (material == Material.PAINTING || BukkitAdapter.ADAPTER.isItemFrame(material)) {
                        result = String.join(",", blockDataArray);
                    }
                    else {
                        result = NAMESPACE + material.name().toLowerCase(Locale.ROOT) + "[" + String.join(",", blockDataArray) + "]";
                    }
                }
                else {
                    result = "";
                }
            }
        }

        return result;
    }

    private static String getBlockDataString(int blockData) {
        // Implement this method according to your requirements
        return ""; // Placeholder return statement
    }

    private static Material getType(int type) {
        // Implement this method according to your requirements
        return null; // Placeholder return statement
    }

    public static void main(String[] args) {
        // Example usage
        byte[] data = "Example Data".getBytes(StandardCharsets.UTF_8);
        int type = 0; // Example type
        String result = byteDataToString(data, type);
        System.out.println("Result: " + result);
    }
}

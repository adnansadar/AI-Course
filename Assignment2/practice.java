import java.util.*;

public class practice {
    // Java program to demonstrate
    // getOrDefault(Object key, V defaultValue) method

    // Main method
    public static void main(String[] args) {

        // Create a HashMap and add some values
        HashMap<String, Integer> map = new HashMap<>();
        map.put("a", 100);
        map.put("b", 200);
        map.put("c", 300);
        map.put("d", 400);
        String s = map.toString();
        char arr[] = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            System.out.println(arr[i]);
        }

        // print map details
        System.out.println("HashMap: " + s);

        // provide key whose value has to be obtained
        // and default value for the key. Store the
        // return value in k
        int k = map.getOrDefault("e", 500);

        // print the value of k returned by
        // getOrDefault(Object key, V defaultValue) method
        System.out.println("Returned Value: " + k);
    }
}

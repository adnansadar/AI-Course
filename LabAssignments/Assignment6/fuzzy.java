/**
 * fuzzy
 */
public class fuzzy {

    public static void main(String[] args) {
        for (int g = 1; g <= 4; g++) {
            System.out.println("Gamma: " + g);
            for (int x = 1; x <= 10; x++) {
                float val = membershipfunction(x, g);
                System.out.format("For x=" + x + ", Membership Value: %.4f \n", val);
            }
            System.out.println("*******************************************************************");
        }
    }

    private static float membershipfunction(int x, int g) {
        float membership = g * (5.0000f / (float) Math.max(x, 5.0000f) - (float) x / (float) Math.max(x, 5.0000f));
        if (membership == 0)
            return 1.0000f;
        if (membership < 0)
            membership = -membership;
        if (0 < membership && membership <= 1)
            return (1.0000f - membership);
        else
            return 0.0000f;
    }
}
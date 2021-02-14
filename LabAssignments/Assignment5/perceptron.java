import java.util.Arrays;

public class perceptron {

    public static void main(String[] args) {
        int[] d = { 1, -1, 1 };
        int[] o = { 0, 0, 0 };
        int c = 1;
        float[] w = { 1, -1, 0, 0.5f };
        float[] x1 = { 1, -2, 1.5f, 0 };
        float[] x2 = { 1, -0.5f, -2, -1.5f };
        float[] x3 = { 0, 1, -1, 1.5f };
        System.out.println("Desired Output:");
        System.out.println(Arrays.toString(d));
        System.out.printf("c: %s\n", c);
        System.out.println("x1: " + Arrays.toString(x1));
        System.out.println("x2: " + Arrays.toString(x2));
        System.out.println("x3: " + Arrays.toString(x3));
        System.out.println("***************************************************************************");
        int flag = 0;
        int count = 0;
        int len = w.length;
        float n = 0.0f;
        float[] wnext = Arrays.copyOf(w, len);
        System.out.println("w: " + Arrays.toString(wnext));
        while (flag != 1) {
            for (int i = 0; i < 3; i++) {
                if (i == 0) {
                    n = net(x1, wnext);
                    o[0] = sgnfunc(n);
                    wnext = weightcal(wnext, c, d[0], o[0], x1);
                }
                if (i == 1) {
                    n = net(x2, wnext);
                    o[1] = sgnfunc(n);
                    wnext = weightcal(wnext, c, d[1], o[1], x2);
                }
                if (i == 2) {
                    n = net(x3, wnext);
                    o[2] = sgnfunc(n);
                    wnext = weightcal(wnext, c, d[2], o[2], x3);
                }
            }
            count += 1;
            System.out.println("Actual Output: " + Arrays.toString(o));
            flag = computation(d, o);
            // System.out.println("Flag: " + computation(d, o));
            System.out.println("epoch: " + count);
            System.out.println("***********************************************************************************");
        }
    }

    private static int computation(int[] d, int[] o) {
        for (int i = 0; i < 3; i++) {
            if (d[i] != o[i])
                return 0;
        }
        return 1;
    }

    private static float[] weightcal(float[] wnext, int c, int i, int j, float[] x1) {
        if (i == j) {
            System.out.println("w: " + Arrays.toString(wnext));
            return wnext;
        }
        float[] w = { 0.0f, 0.0f, 0.0f, 0.0f };
        int mul = i - j;
        for (int k = 0; k < 4; k++) {
            w[k] = wnext[k] + (mul * x1[k]);
        }
        System.out.println("w: " + Arrays.toString(w));
        return w;
    }

    private static int sgnfunc(float n) {
        int o = 0;
        if (n > 0.0f)
            o = 1;
        if (n < 0.0f)
            o = -1;
        System.out.println("sgnfunc(net): " + o);
        return o;
    }

    private static float net(float[] x1, float[] wnext) {
        float n = 0;
        for (int i = 0; i < 4; i++) {
            n += x1[i] * wnext[i];
        }
        System.out.println("net: " + n);
        return n;
    }
}
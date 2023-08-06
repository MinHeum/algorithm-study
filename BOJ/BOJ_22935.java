import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_22935 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int[] strawberries = new int[28];
        for (int i = 1; i < 16; i++) {
            strawberries[i-1] = i;
        }
        for (int i = 15, k = i-1; i < 28; i++, k--) {
            strawberries[i] = k;
        }
        StringBuilder sb = new StringBuilder();
        while (T --> 0) {
            int N = Integer.parseInt(br.readLine());
            int num = strawberries[(N-1)%28];
            String _a = num%2==0?"V":"딸기";
            num /= 2;
            String _b = num%2==0?"V":"딸기";
            num /= 2;
            String _c = num%2==0?"V":"딸기";
            num /= 2;
            String _d = num%2==0?"V":"딸기";
            sb.append(_d).append(_c).append(_b).append(_a).append("\n");
        }
        System.out.println(sb);
    }
}

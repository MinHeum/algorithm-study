import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_14697 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int a = Integer.parseInt(s.split(" ")[0]);
        int b = Integer.parseInt(s.split(" ")[1]);
        int c = Integer.parseInt(s.split(" ")[2]);
        int n = Integer.parseInt(s.split(" ")[3]);
        int i = 0;
        int j = 0;
        int k = 0;

        boolean isPossible = false;
        for (i = 0; i * c <= n; i++) {
            for (j = 0; j * b <= n; j++) {
                for (k = 0; k * a <= n; k++) {
                    if (i * c + j * b + k * a == n) {
                        isPossible = true;
                    }
               }
            }
        }
        System.out.println(isPossible? 1 : 0);
    }
}

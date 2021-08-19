import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution2 {
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        sb = new StringBuilder();

        for (int i = 0; i < T; i++) {
            solve(Integer.parseInt(br.readLine()));
        }
        System.out.println(sb);

    }
    private static void solve(int n) {
        int rStart = (int) Math.sqrt(n-0.1);
        int cStart = 0;
        int step = ((int) Math.pow(rStart+1,2)) - n;
        boolean go = false;
        while (step > 0) {
            if (rStart == cStart) {
                go = true;
            }
            if (go == false) {
                cStart++;
            }
            if (go == true) {
                rStart--;
            }
            step--;
        }
        sb.append(rStart+1).append(" ").append(cStart+1).append("\n");
    }
}

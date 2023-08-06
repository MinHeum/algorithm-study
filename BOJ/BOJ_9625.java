import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_9625 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        int dp[][] = new int[2][K+1];
        dp[0][0] = 1;
        dp[1][0] = 0;
        for (int i = 1; i <= K; i++) {
            dp[0][i] = dp[1][i-1];
            dp[1][i] = dp[0][i-1]+dp[1][i-1];
        }
        System.out.println(dp[0][K] + " " + dp[1][K]);
    }
}

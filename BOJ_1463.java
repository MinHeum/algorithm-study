import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1463 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] memo;
        if ( n >= 5){
            memo = new long[n+1];
        }else {
            memo = new long[5];
        }
        memo[1] = 0; memo[2] = 1; memo[3] = 1; memo[4] = 2;
        for (int i = 5; i <= n; i++) {
            memo[i] = memo[i-1]+1;
            if (i%2==0){
                memo[i] = Math.min(memo[i], memo[i/2]+1);
            }
            if (i%3==0){
                memo[i] = Math.min(memo[i], memo[i/3]+1);
            }
        }
        System.out.println(memo[n]);
    }
}

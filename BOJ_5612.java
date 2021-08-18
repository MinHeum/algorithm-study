import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_5612 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        int answer = m;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            m += Integer.parseInt(st.nextToken());
            m -= Integer.parseInt(st.nextToken());
            if ( answer < m ) {
                answer = m;
            }
            if ( m < 0 ) {
                answer = 0;
                break;
            }
        }
        System.out.println(new StringBuilder(String.valueOf(answer)));
    }
}

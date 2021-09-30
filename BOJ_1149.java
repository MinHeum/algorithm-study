import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1149 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] r = new int[N+1];
        int[] g = new int[N+1];
        int[] b = new int[N+1];
        StringTokenizer st;
        for (int i = 1; i <= N; i++) {
            st = new StringTokenizer(br.readLine());
            r[i] = Integer.parseInt(st.nextToken());
            g[i] = Integer.parseInt(st.nextToken());
            b[i] = Integer.parseInt(st.nextToken());
        }
        int[][] D = new int[N+1][3];

        for (int i = 1; i <= N; i++) {
            D[i][0] = Math.min(D[i-1][1], D[i-1][2]) + r[i];
            D[i][1] = Math.min(D[i-1][0], D[i-1][2]) + g[i];
            D[i][2] = Math.min(D[i-1][0], D[i-1][1]) + b[i];
        }

        int min = D[N][0];
        if (min > D[N][1]) {
            min = D[N][1];
        }
        if (min > D[N][2]) {
            min = D[N][2];
        }
        System.out.println(min);
    }
}

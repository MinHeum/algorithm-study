import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_11404 {

    private static final int INF = Integer.MAX_VALUE >> 1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(map[i], INF);
            map[i][i] = 0;
        }
        StringTokenizer st;
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1; // 출발지점
            int b = Integer.parseInt(st.nextToken()) - 1; // 도착지점
            int c = Integer.parseInt(st.nextToken());     // 비용
            map[a][b] = Math.min(c, map[a][b]);           // 노선이 여러개일 경우 항상 작은값만 사용
        }

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    map[i][j] = Math.min(map[i][j], map[i][k] + map[k][j]);
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] >= INF) {
                    sb.append(0);
                } else {
                    sb.append(map[i][j]);
                }
                if (j != n-1) {
                    sb.append(' ');
                }else {
                    sb.append('\n');
                }
            }
        }
        System.out.println(sb);
    }
}

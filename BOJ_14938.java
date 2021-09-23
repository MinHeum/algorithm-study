import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_14938 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); // 지역의 개수
        int m = Integer.parseInt(st.nextToken()); // 예은이의 수색범위
        int r = Integer.parseInt(st.nextToken()); // 길의 개수

        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(map[i], Integer.MAX_VALUE >> 2);
            map[i][i] = 0;
        }

        int[] items = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            items[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < r; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()) - 1;
            int b = Integer.parseInt(st.nextToken()) - 1;
            int l = Integer.parseInt(st.nextToken());

            map[a][b] = map[b][a] = l;
        }
        // 입력받기 완료

        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    map[i][j] = Math.min(map[i][k] + map[k][j], map[i][j]);
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            int sum = 0;
            for (int j = 0; j < n; j++) {
                if (map[i][j] <= m) {
                    sum += items[j];
                }
            }
            answer = Math.max(answer, sum);
        }
        System.out.println(answer);
    }
}

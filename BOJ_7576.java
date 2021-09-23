import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_7576 {
    static int[][] darr = {{-1,0}, {0,1}, {1,0}, {0,-1}}, map;
    static int M, N, cnt; // cnt: 익지 않은 토마토의 개수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                }
                else if (map[i][j] == 0) {
                    ++cnt;
                }
            }
        }

        int answer = 0;
        while (cnt > 0 && !queue.isEmpty()) {
            for (int i = queue.size(); i > 0; i--) {
                int[] cur = queue.poll();

                for (int d = 0; d < 4; d++) {
                    int nr = cur[0] + darr[d][0];
                    int nc = cur[1] + darr[d][1];

                    if (nr < 0 || nc < 0 || nr > N-1 || nc > M-1 || map[nr][nc] != 0) continue;

                    --cnt;
                    map[nr][nc] = 1;
                    queue.offer(new int[] {nr, nc});
                }
            }
            answer++;
        }
        System.out.println(cnt == 0 ? answer : -1);
    }
}

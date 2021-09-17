import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_2636 {
    private static int[][] darr = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}, map;
    private static int N, M, cheese;
    private static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        cheese = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (map[i][j] == 1) {
                    cheese++;
                }
            }
        }

        int count = 0;
        int step = 0;
        while (cheese != 0) {
            step++;
            count = cheese;
            bfs();
        }

        System.out.println(step);
        System.out.println(count);
    }

    private static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        visited = new boolean[N][M];
        queue.offer(new int[]{0, 0});
        visited[0][0] = true;
        while (!queue.isEmpty()) {
            int cur[] = queue.poll();
            int r = cur[0];
            int c = cur[1];

            for (int d = 0; d < 4; d++) {
                int nr = r + darr[d][0];
                int nc = c + darr[d][1];

                if (nr < 0 || nc < 0 || nr > N-1 || nc > M-1 || visited[nr][nc]) continue;
                if (map[nr][nc] == 1) { // 치즈 녹이기
                    map[nr][nc] = 0;
                    cheese--;
                } else {
                    queue.offer(new int[] {nr, nc});
                }
                visited[nr][nc] = true; // 방문처리
            }
        }
    }
}

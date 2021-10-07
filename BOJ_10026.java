import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10026 {
    private static final int[] dr = {0, 0, -1, 1};
    private static final int[] dc = {1, -1, 0, 0};
    private static int N;
    private static char[][] map;
    private static boolean[][] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        map = new char[N][N];
        for (int r = 0; r < N; r++) {
            String str = br.readLine();
            for (int c = 0; c < N; c++) {
                map[r][c] = str.charAt(c);
            }
        }
        visited = new boolean[N][N];
        int ans1 = 0;
        int ans2 = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (!visited[r][c]) {   // 방문 안했을때만 dfs 돌리고 ans1++
                    dfs(r,c);
                    ans1++;
                }
            }
        }
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (map[r][c] == 'R')
                    map[r][c] = 'G';
            }
        }
        visited = new boolean[N][N];
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (!visited[r][c]) {   // 방문 안했을때만 dfs 돌리고 ans2++
                    dfs(r,c);
                    ans2++;
                }
            }
        }
        System.out.printf("%d %d%n", ans1, ans2);
    }

    private static void dfs(int r, int c) {
        visited[r][c] = true;
        char curColor = map[r][c];
        for (int d = 0; d < 4; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];

            if (nr < 0 || nc < 0 || nr > N-1 || nc > N-1 || visited[nr][nc])
                continue;
            if (map[nr][nc] == curColor) {
                dfs(nr, nc);
            }
        }
    }
}

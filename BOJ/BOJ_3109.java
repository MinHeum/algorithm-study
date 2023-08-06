import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3109 {
    static int R, C, answer = 0;
    static char[][] map;
    static int[] dr = {-1, 0, 1};
    static int[] dc = { 1, 1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken()); C = Integer.parseInt(st.nextToken());
        map = new char[R][C];
        for (int i = 0; i < R; i++) {
            String str = br.readLine();
            for (int j = 0; j < C; j++) {
                map[i][j] = str.charAt(j);
            }
        }
        //입력 끝
        for (int i = 0; i < R; i++) {
            dfs(i, 0);
        }
        System.out.println(answer);
    }

    private static boolean dfs(int r, int c) {
        if (c == C-1) {
            answer++;
            return true;
        }
        for (int d = 0; d < 3; d++) {
            int nr = r + dr[d];
            int nc = c + dc[d];
            if (nr > -1 && nc > -1 && nr < R && nc < C && map[nr][nc] == '.') {
                map[r][c] = 'x';
                if (dfs(nr, nc)){
                    return true;
                }
            }
        }
        return false;
    }
}

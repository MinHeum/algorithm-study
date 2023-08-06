import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_1194 {
    private static class Node{
        int r, c, key;
        public Node(int r, int c, int key) {
            this.r = r;
            this.c = c;
            this.key = key;
        }
    }
    private static final int[][] darr = {{0,-1},{-1,0},{0,1},{1,0}};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        char[][] map = new char[N][M];
        int[][][] visited = new int[N][M][64];
        Queue<Node> queue = new LinkedList<>();
        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            for (int j = 0; j < M; j++) {
                map[i][j] = s.charAt(j);
                if (map[i][j] == '0') {
                    queue.offer(new Node(i,j,0));
                }
            }
        }
        visited = new int[N][M][64]; // 64 == 2 ^ 6

        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            int r = cur.r;
            int c = cur.c;
            int key = cur.key;
            if (map[r][c] == '1') {
                System.out.println(visited[r][c][key]);
                return;
            }
            for (int d = 0; d < 4; d++) {
                int nr = r + darr[d][0];
                int nc = c + darr[d][1];
                if (nr < 0 || nc < 0 || nr > N - 1 || nc > M- 1 ||
                        visited[nr][nc][key] > 0 || map[nr][nc] == '#') { // 맵을 벗어나거나 벽일때
                    continue;
                }
                if (map[nr][nc] <= 'f' && map[nr][nc] >= 'a') { // pick Key
                    int newKey = key | (1 << (map[nr][nc] - 'a'));
                    visited[nr][nc][newKey] = visited[r][c][key] + 1;
                    queue.offer(new Node(nr, nc, newKey));
                } else if (map[nr][nc] <= 'F' && map[nr][nc] >= 'A') { // when Door
                    if ((key & (1 << map[nr][nc] - 'A')) > 0) {
                        visited[nr][nc][key] = visited[r][c][key] + 1;
                        queue.offer(new Node(nr, nc, key));
                    }
                } else { // 일반 타일
                    visited[nr][nc][key] = visited[r][c][key] + 1;
                    queue.offer(new Node(nr, nc, key));
                }
            }
        }
        System.out.println("-1");
    }
}

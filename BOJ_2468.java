import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_2468 {
    private static final int[][] DARR = {{0,1}, {1,0}, {0,-1}, {-1,0}};
    private static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int map[][] = new int[N][N];
        StringTokenizer st;
        int start = 100;
        int end = 0;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                if (start > map[i][j]) start = map[i][j];
                if (end < map[i][j]) end = map[i][j];
            }
        }
        int answer = 0;
        for (int h = start-1; h <= end; h++) {
            boolean[][] visited = new boolean[N][N];    // 방문 체크용 boolean 배열
            int count = 0;      // 잠기지 않은 영역의 수를 count 할 변수 선언
            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    if (!visited[r][c] && map[r][c] > h) { // 방문한 적이 없으며, 잠기지 않았을 때
                        Queue<int[]> queue = new LinkedList<>();
                        visited[r][c] = true;
                        count++;
                        queue.offer(new int[]{r,c});
                        while (!queue.isEmpty()) {
                            int[] cur = queue.poll();
                            for (int d = 0; d < 4; d++) {
                                int nr = cur[0] + DARR[d][0];
                                int nc = cur[1] + DARR[d][1];
                                if (nr > -1 && nc > -1 && nr < N && nc < N && !visited[nr][nc] && map[nr][nc] > h) {
                                    queue.offer(new int[]{nr, nc});
                                    visited[nr][nc] = true;
                                }
                            }
                        }
                    }
                }
            }
            answer = Math.max(answer, count); // answer 갱신
        }
        System.out.println(answer);           // answer 출력
    }
}

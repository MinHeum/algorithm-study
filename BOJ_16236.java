import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_16236 {
    private static class Target implements Comparable<Target>{
        int r, c, dist;

        public Target(int r, int c, int dist) {
            this.r = r;
            this.c = c;
            this.dist = dist;
        }

        @Override
        public int compareTo(Target o) {
            if (this.dist - o.dist != 0) return this.dist - o.dist;
            else if (this.r - o.r != 0) return this.r - o.r;
            else return this.c - o.c;
        }

        @Override
        public String toString() {
            return "Target{" +
                    "r=" + r +
                    ", c=" + c +
                    ", dist=" + dist +
                    '}';
        }
    }

    private static int N, map[][], sharkR, sharkC, sharkSize, sharkEat, answer;
    private static PriorityQueue<Target> pq;
    private static final int[] dr = {0, 1, 0, -1};
    private static final int[] dc = {-1, 0, 1, 0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        pq = new PriorityQueue<>();
        map = new int[N][N];
        sharkSize = 2;
        sharkEat = 0;
        StringTokenizer st;
        for (int r = 0; r < N; r++) {
            st = new StringTokenizer(br.readLine());
            for (int c = 0; c < N; c++) {
                map[r][c] = Integer.parseInt(st.nextToken());
                if (map[r][c] == 9) {
                    map[r][c] = 0;
                    sharkR = r;
                    sharkC = c;
                }
            }
        }
        //입력받기 끝
        answer = 0;
        while (true){
            find();
            if (pq.isEmpty()) break;
            go();
            pq.clear();
        }
        System.out.println(answer);
    }

    // 맵에서 사냥감 찾기 함수
    private static void find(){
        //bfs 탐색으로 먹잇감을 찾는다.
        boolean[][] visited = new boolean[N][N];
        visited[sharkR][sharkC] = true;
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{sharkR, sharkC});
        int dist = 0;
        while (!queue.isEmpty()) {
            int temp = queue.size();
            for (int i = 0; i < temp; i++) {
                int[] cur = queue.poll();
                if (map[cur[0]][cur[1]] != 0 && map[cur[0]][cur[1]] < sharkSize) {
                    pq.offer(new Target(cur[0],cur[1],dist));
                }
                for (int d = 0; d < 4; d++) {
                    int nr = cur[0] + dr[d];
                    int nc = cur[1] + dc[d];
                    if (nr < 0 || nc < 0 || nr > N-1 || nc > N-1 || visited[nr][nc]) {
                        continue;
                    }
                    if (map[nr][nc] > sharkSize) continue; // 아기상어보다 큰 고기는 못지나감
                    queue.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
            dist++;
        }
    }

    private static void go() {
        Target target = pq.poll();
        sharkR = target.r;
        sharkC = target.c;
        map[sharkR][sharkC] = 0; // 먹기 처리
        sharkEat++;             // 상어가 먹은 갯수 증가
        if (sharkEat == sharkSize) { // 상어 성장 처리
            sharkSize++;
            sharkEat = 0;
        }
        answer += target.dist; // 이동거리 증가
    }

}

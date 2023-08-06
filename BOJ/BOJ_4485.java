import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_4485 {
    private static int map[][], N;
    private static final int INF = Integer.MAX_VALUE >> 2;
    private static final int[][] darr = {{1,0},{0,1},{-1,0},{0,-1}};

    private static class Node implements Comparable<Node> {
        int r, c, cost;

        public Node(int r, int c, int cost) {
            this.r = r;
            this.c = c;
            this.cost = cost;
        }

        @Override
        public int compareTo(Node o) {
            return this.cost - o.cost;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int cnt = 1;
        while (true) {
            N = Integer.parseInt(br.readLine());
            if (N==0) break; // break loop when N == 0

            map = new int[N][N];
            StringTokenizer st;
            for (int i = 0; i < N; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < N; j++) {
                    map[i][j] = Integer.parseInt(st.nextToken());
                }
            } // end map input
            int answer = dijkstra();
            sb.append("Problem ").append(cnt++).append(": ").append(answer).append('\n');
        }
        System.out.println(sb);
    }
    private static int dijkstra() {
        Queue<Node> queue = new PriorityQueue<>();
        int[][] dist = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                dist[i][j] = INF;
            }
        }
        queue.add(new Node(0, 0, map[0][0]));
        dist[0][0] = map[0][0];
        while (!queue.isEmpty()) {
            Node cur = queue.poll();
            if (cur.r == N-1 && cur.c == N-1) return cur.cost;

            for (int d = 0; d < 4; d++) {
                int nr = cur.r + darr[d][0];
                int nc = cur.c + darr[d][1];

                if (nr < 0 || nc < 0 || nr > N-1 || nc > N-1) continue;
                int temp = cur.cost + map[nr][nc];
                if (temp < dist[nr][nc]) {
                    dist[nr][nc] = temp;
                    queue.offer(new Node(nr, nc, temp));
                }
            }
        }
        return -1;
    }
}

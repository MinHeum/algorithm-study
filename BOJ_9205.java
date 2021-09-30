import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_9205 {
    private static int T;
    private static class Node{
        int x, y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        T = Integer.parseInt(br.readLine());
        int tc = 0;
        StringBuilder sb = new StringBuilder();
        top:
        while (tc ++ < T) {
            int N = Integer.parseInt(br.readLine());
            Node[] map = new Node[N+2];
            for (int i = 0; i <= N+1; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                map[i] = new Node(Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
            }

            boolean[][] dist = new boolean[N+2][N+2];
            for (int i = 0; i < N + 2; i++) {
                for (int j = 0; j < N + 2; j++) {
                    if (Math.abs(map[i].x - map[j].x) + Math.abs(map[i].y - map[j].y) < 1001) {
                        dist[i][j]  = true;
                    }
                }
            }

            for (int k = 0; k < N+2; k++) { // 경
                for (int i = 0; i < N+2; i++) {  // 찰
                    if (i==k) continue; // 경유지와 출발지가 같다면
                    for (int j = 0; j < N+2; j++) { // 도둑
                        if (i==j || k==j) continue; // 출발지와 도착지가 같거나, 경유지와 도착지가 같으면 갱신할 필요가 없다.
                        if (dist[i][k] && dist[k][j]) {
                            dist[i][j] = true;
                        }
                    }
                }
            }
            sb.append(dist[0][N+1]?"happy":"sad").append('\n');
        }
        System.out.print(sb);
    }
}

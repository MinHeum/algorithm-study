import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_15661 {
    static int N, answer = Integer.MAX_VALUE;
    static int[][] arr;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N][N];
        visited = new boolean[N];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        fun(0,0);
        System.out.println(answer);
    }

    private static void fun(int num, int count){
        if (num == N) return;
        if (count > 0) {
            int a = 0, b = 0;
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    if (visited[i] && visited[j]) {
                        a += arr[i][j];
                    }
                    if (!visited[i] && !visited[j]) {
                        b += arr[i][j];
                    }
                }
            }
            answer = Math.min(answer, Math.abs(a-b));
        }
        visited[num] = true;
        fun(num+1, count+1);
        visited[num] = false;
        fun(num+1, count);
    }
}

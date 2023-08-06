import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_10163 {
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        StringTokenizer st;

        int[][] map = new int[1001][1001];

        for (int i = 1; i < N+1; i++) {
            st = new StringTokenizer(br.readLine());

            int r = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());
            for (int y = r; y < r+w; y++) {
                for (int x = c; x < c+h; x++) {
                    map[y][x] = i;
                }
            }
        }

        int[] arr = new int[N+1];

        for (int i = 0; i < 1001; i++) {
            for (int j = 0; j < 1001; j++) {
                arr[map[i][j]]++;
            }
        }
        for (int i = 1; i < N+1; i++) {
            System.out.println(arr[i]);
        }
    }
}

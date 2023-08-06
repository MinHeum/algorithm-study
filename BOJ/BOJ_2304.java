import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2304 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] arr = new int[1001];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int L = Integer.parseInt(st.nextToken());
            int H = Integer.parseInt(st.nextToken());
            arr[L] = H;
        }
        int maxH = 0;
        int maxIdx = -1;
        for (int i = 0; i < 1001; i++) {
            if (arr[i] > maxH) {
                maxH = arr[i];
                maxIdx = i;
            }
        }

        int answer = 0;
        int currentH = 0;
        for (int i = 0; i < maxIdx; i++) {
            if (arr[i] > currentH) {
                currentH = arr[i];
            }
            answer += currentH;
        }
        currentH = 0;
        for (int i = arr.length-1; i > maxIdx ; i--) {
            if (arr[i] > currentH) {
                currentH = arr[i];
            }
            answer += currentH;
        }
        answer += maxH;
        System.out.println(answer);
    }
}

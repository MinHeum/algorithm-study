import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.math.*;

public class BOJ_13300 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        int[] arr = new int[12];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int isBoy = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());
            arr[(num-1)*2 + isBoy] += 1;
        }
        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            answer += Math.ceil((double)arr[i] / K);
        }
        System.out.println(answer);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2477 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());

        int[] arr = new int[6];
        for (int i = 0; i < 6; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            st.nextToken();
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int maxIdx = -1;
        int maxValue = -1;
        for (int i = 0; i < 6; i++) {
            if (arr[i] > maxValue) {
                maxIdx = i;
                maxValue = arr[i];
            }
        }
        int secondMax, min1, min2;
        if (arr[(6 + maxIdx - 1 ) % 6] <= arr[(6 + maxIdx + 1 ) % 6]) {
            secondMax = arr[(6 + maxIdx + 1) % 6];
            min1 = arr[(6 + maxIdx + 3) % 6];
            min2 = arr[(6 + maxIdx + 4) % 6];
        }
        else {
            secondMax = arr[(6 + maxIdx - 1) % 6];
            min1 = arr[(6 + maxIdx + 2) % 6];
            min2 = arr[(6 + maxIdx + 3) % 6];
        }
        System.out.println((maxValue * secondMax - min1 * min2) * K);

    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_3020 {
    static int N, H, arr1[], arr2[];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        arr1 = new int[H+1];
        arr2 = new int[H+1];
        for (int i = 0; i < N/2; i++) {
            arr1[Integer.parseInt(br.readLine())]++;
            arr2[Integer.parseInt(br.readLine())]++;
        }

        for (int i = 1; i < H+1; i++) {
            arr1[i] += arr1[i-1];
            arr2[i] += arr2[i-1];
        }
        int min = N;
        int count = 0;
        for (int i = 1; i < H+1; i++) {
            int sum = 0;
            sum += arr1[H] - arr1[i-1];
            sum += arr2[H] - arr2[H-i];
            if (min > sum) {
                min = sum;
                count = 1; // 최소값이 처음 발견되었으니 count 를 1로 초기화
            }
            else if (min == sum) {
                count++;
            }
        }
        System.out.println(min+" "+count);
    }
}

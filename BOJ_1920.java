import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1920 {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        arr = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        int Q = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < Q; i++) {
            int input = Integer.parseInt(st.nextToken());
            sb.append(binarySearch(0,N-1, input)+"\n");
        }
        System.out.println(sb);
    }
    private static int binarySearch(int low, int high, int target) {
        while (low <= high) {
            int mid = (low + high) >> 1;
            if (arr[mid] == target) return 1;
            if (arr[mid] > target) {
                high = mid - 1;
            }else {
                low = mid + 1;
            }
        }
        return 0;
    }
}

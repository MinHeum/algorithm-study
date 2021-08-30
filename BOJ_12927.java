import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_12927 {
    static char[] arr;
    static int N;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        N = str.length();
        arr = new char[N+1];
        for (int i = 1; i < N+1; i++) {
            arr[i] = str.charAt(i-1);
        }
        int count = 0;
        for (int i = 1; i < N+1; i++) {
            if (arr[i] == 'Y') {
                fun(i);
                count++;
            }
        }
        System.out.println(count);
    }
    private static void fun(int n){
        for (int i = n; i < N+1; i++) {
            if (i % n == 0) {
                if (arr[i] == 'Y') {
                    arr[i] = 'N';
                }
                else {
                    arr[i] = 'Y';
                }
            }
        }
    }
}

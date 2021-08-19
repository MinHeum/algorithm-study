import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution3 {
    static StringBuilder sb;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        for (int i = 0; i < T; i++) {
            //algorithms
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            sb.append(solve(a,b,c)+"\n");
        }
        System.out.println(sb);
    }

    static private int solve(int a, int b, int key) {
        int numA, numB;
        if (a > b) {
            numA = b;
            numB = a;
        }else {
            numA = a;
            numB = b;
        }
        int size = (numB - numA) * 2;
        if (numB <= size && key <= size) {
            return ((key + numB - numA - 1) % size) + 1;
        }
        else {
            return -1;
        }
    }
}

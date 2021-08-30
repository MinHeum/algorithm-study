import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1002 {
    static int T;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        T = Integer.parseInt(br.readLine());
        int testCase = 0;
        StringTokenizer st;
        while (testCase++ < T) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int r1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int r2 = Integer.parseInt(st.nextToken());

            int distance = (x2-x1) * (x2-x1) + (y2-y1) * (y2-y1);
            int a = (r1+r2) * (r1+r2);
            int b = (r1-r2) * (r1-r2);
            if (x1==x2 && y1==y2 && r1==r2) {
                sb.append(-1);
            } else if (a == distance || b == distance ){
                sb.append(1);
            } else if (a < distance || b > distance) {
                sb.append(0);
            } else {
                sb.append(2);
            }
            sb.append('\n');
        }
        System.out.print(sb);
    }
}

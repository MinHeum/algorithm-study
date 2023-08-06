import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ_2605 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        LinkedList<Integer> lst = new LinkedList();
        for (int i = 1; i <= N; i++) {
            lst.add(Integer.parseInt(st.nextToken()), i);
        }
        StringBuilder sb = new StringBuilder();
        while (!lst.isEmpty()){
            sb.append(lst.pollLast());
            sb.append(" ");
        }
        System.out.println(sb);
    }
}

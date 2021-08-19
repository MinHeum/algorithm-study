import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Solution1 {
    public static void main(String[] args) throws Exception {
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i = 1; i < 10000; i++) {
            if (i % 3 == 0 || i % 10 == 3){
                continue;
            }
            else {
                arr.add(i);
            }
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for (int i = 0; i < N; i++) {
            sb.append(arr.get(Integer.parseInt(br.readLine())-1)+"\n");
        }
        System.out.println(sb);
    }
}
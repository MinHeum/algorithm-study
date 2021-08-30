import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1213 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        int[] arr = new int[26];
        for (int i = 0, len = s.length(); i < len; i++) {
            arr[s.charAt(i) - 'A']++;
        }
        // 개수 처리 완료
        // count 된 알파벳 중 홀수는 하나만 있거나 없어야 한다.
        // 홀수개를 카운트하고 안되면 break 처리
        int count = 0;
        int oddIdx = -1;
        boolean sorry = false;
        for (int i = 0; i < 26; i++) {
            if (arr[i] % 2 != 0) {
                oddIdx = i;
                count++;
            }
            if (count > 1) {
                sorry = true;
                break;
            }
        }
        if (sorry) {
            System.out.println("I'm Sorry Hansoo");
        } else {
            char oddChar = oddIdx == -1 ? '\u0000' : (char) ('A' + oddIdx);
            int oddCount = 0;
            if (oddIdx != -1) {
                oddCount = arr[oddIdx];
                arr[oddIdx] = arr[oddIdx]-1;
            }
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 26; i++) {
                for (int j = 0; j < arr[i] / 2; j++) {
                    sb.append((char) ('A' + i));
                }
            }
            if(oddIdx != -1)
                sb.append(oddChar);
            for (int i = 25; i >= 0 ; i--) {
                for (int j = 0; j < arr[i] / 2; j++) {
                    sb.append((char)('A'+i));
                }
            }
            System.out.println(sb);
        }
    }
}

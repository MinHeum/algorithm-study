import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_1718 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        String key = br.readLine();
        StringBuilder answer = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == ' ') {
                answer.append(' ');
            }
            else {
                char c = (char) (96 + input.charAt(i) - key.charAt(i%key.length()));
                if (c < 'a') {
                    c += 26;
                }
                answer.append(c);
            }
        }
        System.out.println(answer);
    }
}

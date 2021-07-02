import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10162{
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long T = Long.parseLong(br.readLine());

        // 300초, 60초, 10초
        if (T % 10 != 0){
            System.out.println("-1");
        }
        else {
            long A = 0L;
            long B = 0L;
            long C = 0L;

            A = T / 300;
            T -= 300 * A;
            
            B = T / 60;
            T -= 60 * B;

            C = T / 10;
            T -= 10 * C;

            System.out.printf("%d %d %d\n", A,B,C);
        }
    }
}
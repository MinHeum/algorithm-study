import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_10988 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        boolean is_palindrom = true;
        for(int i=0; i<(s.length()/2)+1; i++){
            if(s.charAt(i)!=s.charAt(s.length()-(i+1)))
                is_palindrom = false;
        }
        System.out.println(is_palindrom?"1":"0");
    }
}

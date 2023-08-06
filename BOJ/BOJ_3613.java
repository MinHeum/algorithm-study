import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class BOJ_3613 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        Pattern cppPattern = Pattern.compile("([a-z])+(_[a-z]*)*");
        Pattern javaPattern = Pattern.compile("([a-z])+([a-zA-Z])*");
        Pattern cppErrorPattern = Pattern.compile("(__)+");

        Matcher cppMatcher = cppPattern.matcher(str);
        Matcher javaMatcher = javaPattern.matcher(str);
        Matcher cppErrorMatcher = cppErrorPattern.matcher(str);

        boolean isPossible = (cppMatcher.matches() | javaMatcher.matches())
                && !cppErrorMatcher.find() && !(str.charAt(str.length()-1)=='_');

//        System.out.println(cppMatcher.matches());
//        System.out.println(javaMatcher.matches());
//        System.out.println(cppErrorMatcher.find());

        boolean isJava = javaMatcher.matches();

        StringBuilder answer = new StringBuilder();
        if (isPossible) {
            if (isJava) { // When Java -> C++
                for (int i = 0; i < str.length(); i++) {
                    char cur = str.charAt(i);
                    if (cur < 91) { // when UpperCase
                        answer.append('_');
                        answer.append((char)(cur + 32));
                    }else {
                        answer.append(cur);
                    }
                }
            } else { // When C++ -> Java
                for (int i = 0; i < str.length(); i++) {
                    char cur = str.charAt(i);
                    if (cur == '_' && i != str.length()-1){
                        answer.append((char)(str.charAt(++i) - 32));
                    }else {
                        answer.append(cur);
                    }
                }

            }
        }else {
            answer.append("Error!");
        }
        System.out.println(answer);
    }
}

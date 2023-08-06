import java.util.Scanner;

public class BOJ_1152 {
    public static void main(String args[]) {
          Scanner sc = new Scanner(System.in);
          String st = sc.nextLine();
          st = st.replaceAll("(^\\p{Z}+|\\p{Z}+$)", "");
          String[] words = st.split("\\s");
          if (st.length()==0)
              System.out.println("0");
          else
              System.out.println(words.length);
    }
}
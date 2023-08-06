import java.util.Scanner;

public class BOJ_8958 {
    public static void main(String args[]) {
          Scanner sc = new Scanner(System.in);
          int n = sc.nextInt();
          sc.nextLine();
          for(int i=0; i<n; i++){
              String st = sc.nextLine();
              int count=1;
              int score=0;
              for(int j=0; j<st.length(); j++){
                  if(st.charAt(j)=='O')
                  {
                      score+=count;
                      count++;
                  }
                  if(st.charAt(j)=='X')
                      count = 1 ;
              }
              System.out.println(score);
          }
    }
}
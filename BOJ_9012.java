import java.util.Scanner;

public class BOJ_9012 {
    public static void main(String avgs[]) {
        int t;
        Scanner sc = new Scanner(System.in);
        t = sc.nextInt();
        for(int i=0; i<t; i++){
            int takoyaki=0;
            int error = 0;
            String map = sc.next();
            for(int j=0; j<map.length(); j++){
                char ch = map.charAt(j);
                if (ch == '(')
                    takoyaki++;
                else if (takoyaki==0 && ch ==')')
                    error = 1;
                else if (ch == ')')
                    takoyaki--;
                }
                if(takoyaki==0 && error!=1)
                    System.out.println("YES");
                else
                    System.out.println("NO");
        }
    }
}
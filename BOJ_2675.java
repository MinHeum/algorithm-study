import java.util.Scanner;

public class BOJ_2675 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for(int i=0; i<t; i++)
        {
            int n = sc.nextInt();
            String s = sc.nextLine();
            for(int k=1; k<s.length(); k++)
                for(int j=0; j<n; j++)
                    System.out.print(s.charAt(k));
            System.out.println();
        }
    }
}
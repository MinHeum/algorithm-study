import java.util.Scanner;

public class BOJ_2753{
    public static void main(String[] argv) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        if(n%4==0)
        {
            if (n%100!=0||n%400==0)
                System.out.println("1");
            else
                System.out.println("0");
        }
        else
            System.out.println("0");
    }
}
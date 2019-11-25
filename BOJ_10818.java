// BOJ_10818.java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        int a = 0;
        while (n > 0) {
            a = sc.nextInt();
            if (max < a) max = a;
            if (min > a) min = a;
            n--;
        }
        System.out.println(min + " " + max);
    }
}
// BOJ_1330.java
import java.util.Scanner;

public class BOJ_1330 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        int a = Integer.parseInt(input.split(" ")[0]);
        int b = Integer.parseInt(input.split(" ")[1]);

        if (a>b) System.out.println('>');
        else if (a<b) System.out.println('<');
        else System.out.println("==");
    }
}
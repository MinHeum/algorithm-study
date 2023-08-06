// BOJ_3052.java
import java.util.Scanner;

public class BOJ_3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] lst = new int[10];
        for (int i = 0; i < 10; i++) {
            lst[i] = sc.nextInt();
        }
        int[] modLst = new int[10];
        for (int i = 0; i < 10; i++) {
            modLst[i] = lst[i] % 42;
        }
        int[] countLst = new int[42];
        for (int i = 0; i < 10; i++) {
            countLst[modLst[i]]++;
        }
        int count = 0;
        for (int i = 0; i < 42; i++) {
            if(countLst[i] > 0) count++;
        }
        System.out.println(count);
    }
}
import java.util.Scanner;

public class BOJ_2292 {
    public static void main(String avgs[]) {
        int count=1,x=1;
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        while(x<n){
            x = x + 6 * count;
            count++;
        }
        System.out.println(count);
    }
}
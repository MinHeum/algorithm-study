import java.util.Scanner;

public class BOJ_1934 {
    public static void main(String avgs[]) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for(int i=0; i<T; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            if(b>a){
                int temp;
                temp = a;
                a = b;
                b = temp;
            }
            int t_a = a, t_b = b;
            while(t_a % t_b !=0){
                int temp = t_b;
                t_b = t_a % t_b;
                t_a = temp;
            }
            System.out.println((a/t_b)*(b/t_b)*t_b);
        }
    }
}

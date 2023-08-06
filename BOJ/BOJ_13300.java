import java.util.Scanner;

public class BOJ_13300 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); int K = sc.nextInt();
        int[] arr = new int[12];
        for (int i = 0; i < N; i++) {
            int isBoy = sc.nextInt(); int num = sc.nextInt();
            arr[(num-1)*2 + isBoy] += 1;
        }
        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            answer += Math.ceil((double)arr[i] / K);
        }
        System.out.println(answer);
    }
}

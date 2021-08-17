import java.util.Scanner;

public class BOJ_11047 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();   // 동전의 종류 수
        int k = sc.nextInt();   // 동전 가치의 합
        int[] arr = new int[n]; // 동전의 종류만큼 배열 생성
        int count = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int i = n-1;
        if (n==1) {
            while (k>0) {
                k -= arr[0];
                count++;
            }
        }
        else
            while(k>0){
                while (k >= arr[i]){
                    k -= arr[i];
                    count++;
                }
                if (i>0)
                    i--;
            }
        System.out.println(count);
    }
}
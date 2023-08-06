import java.util.Scanner;

public class BOJ_2748 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        System.out.println(fibo(n));
    }
    private static long fibo(int n) {
        long memo[]=new long[n+1]; return fiboMemo(n, memo);
    }

    private static long fiboMemo(int n, long[] memo) {
        if (memo[n] > 0) return memo[n];
        if (n < 2) memo[n] = n;
        else memo[n] = fiboMemo(n - 2, memo) + fiboMemo(n - 1, memo);
        return memo[n];
    }
}
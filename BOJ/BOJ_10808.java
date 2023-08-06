import java.util.Scanner;

public class BOJ_10808 {
    public static void main (String argv[]) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int[] arr = new int[26];
        for(int i=0; i<s.length(); i++){
            int n = (int)s.charAt(i);
            arr[n-97]++;
        }
        for(int i=0; i<arr.length; i++)
            System.out.print(arr[i]+" ");
    }
}
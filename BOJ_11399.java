import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        for (int i=0; i<n; i++)
            arr.add(sc.nextInt());

        Collections.sort(arr);
        int[] acc = new int[n];
        int size = 0;
        for (int k: arr) {
            acc[size++] = k;
        }
        for (int i = 0; i < n-1; i++) {
            acc[i+1] += acc[i];
        }
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += acc[i];
        }
        System.out.println(sum);
    }
}
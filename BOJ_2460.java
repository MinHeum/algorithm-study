import java.util.Scanner;

public class Main {
    public static void main (String argv[]) {
        int[][] arr = new int[10][3];
        Scanner sc = new Scanner(System.in);
        for(int i=0; i<10; i++){
            arr[i][0] = sc.nextInt();
            arr[i][1] = sc.nextInt();
            if(i==0)
                arr[i][2] = arr[i][1] - arr[i][0];
            else
                arr[i][2] = arr[i][1] - arr[i][0] + arr[i-1][2];
        }
        int max = arr[0][2];
        for(int i=0; i<10; i++){
            if(max<arr[i][2])
                max = arr[i][2];
        }
        System.out.println(max);
    }
}
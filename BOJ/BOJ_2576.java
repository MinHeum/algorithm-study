import java.util.Scanner;

public class BOJ_2576{
    public static void main(String[] argv) {
        Scanner sc = new Scanner(System.in);
        int[] arr = new int[7];
        for(int i=0; i<arr.length; i++)
            arr[i] = sc.nextInt();
        int sum = 0, min = 0;
        for(int i=0; i<arr.length; i++){
            if(arr[i]%2==1)
                sum += arr[i];
            if(arr[i]%2==1&&min==0||arr[i]%2==1&&arr[i]<min)
                min = arr[i];
        }
        if(sum==0)
            System.out.println("-1");
        else
        {
            System.out.println(sum);
            System.out.println(min);
        }

    }
}
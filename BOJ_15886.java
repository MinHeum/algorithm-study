import java.util.Scanner;

public class BOJ_15886 {
    public static void main(String avgs[]){
        Scanner sc = new Scanner(System.in);
        int count=0;
        int n = sc.nextInt();
        sc.nextLine();
        String arr;
        arr = sc.nextLine();
        for(int i=0; i<n-1; i++){
            if(arr.charAt(i)=='E')
                if(arr.charAt(i+1)=='W')
                    count++;
        }
        System.out.println(count);
    }
}
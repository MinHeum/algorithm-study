import java.util.Scanner;

public class BOJ_1546 {
    public static void main(String[] args){
        float sum=0;
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        float arr[] = new float[n];
        for(int i=0; i<n; i++)
        {
            arr[i] = Float.parseFloat(sc.next());
        }
        float max = arr[0];
        for(int i=0; i<n; i++){
            if(max < arr[i])
                max = arr[i];
        }
        for(int i=0; i<n; i++){
            if(max!=0)
                arr[i] = (arr[i]/max)*100;
        }
        for(int i=0; i<n; i++){
            sum += arr[i];
        }
        System.out.println(sum/n);
    }
}
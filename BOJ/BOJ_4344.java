import java.util.Scanner;

public class BOJ_4344 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int c = sc.nextInt(); // Test Case 받아오기
        for(int i=0; i<c; i++){  // c만큼 반복시킬거임
            int n = sc.nextInt();
            float arr[]= new float[n];
            for(int j=0; j<n; j++){
                arr[j]= sc.nextFloat();
            }
            float sum = 0;
            for(int j=0; j<n; j++){ //배열의 평균 구하기
                sum += arr[j];
            }
            float avr = sum/n;
            int count = 0;
            for(int j=0; j<n; j++){
                if(arr[j]>avr){
                    count++;
                }
            }
            System.out.printf("%.3f",(float)100*count/(float)n);
            System.out.println("%");
       }
    }
}

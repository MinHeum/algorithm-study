import java.util.Scanner;

public class BOJ_2577 {
    public static void main (String args[]){
        long a,b,c;
        Scanner sc = new Scanner(System.in);
        a=sc.nextLong(); b=sc.nextLong(); c=sc.nextLong();
        long result = a*b*c;
        int[] q = new int[10];

        for(int i=(int)Math.log10(result); i>=0;i--){
            for(int j=0; j<=9; j++) {
                if ((result / (int)Math.pow(10,i))%10== j)
                    q[j]++;
            }
        }
        //결과출력
        for(int i=0; i<=9; i++){
            System.out.println(q[i]);
        }
    }
}
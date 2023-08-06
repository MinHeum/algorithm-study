import java.util.Scanner;

public class BOJ_2920 {
    public static void main(String avgs[]){
        Scanner sc = new Scanner(System.in);
        int[] n = new int[8];
        int boo=1;
        for(int i=0; i<8; i++)
        {
            n[i] = sc.nextInt();
        }

        if(n[0]==8) {
            boo = 2;
            for (int i = 0; i < n.length - 1; i++) {
                if (n[i] < n[i + 1])
                    boo = 1;

            }
        }
        else if(n[0]==1){
            boo = 3;
            for(int i=0; i<n.length-1; i++){
                if(n[i]>n[i+1])
                    boo = 1;

            }
        }
        switch (boo){
            case (1) :
                System.out.println("mixed");
                break;
            case (2) :
                System.out.println("descending");
                break;
            case (3) :
                System.out.println("ascending");
                break;
            default:
                break;
        }
    }
}

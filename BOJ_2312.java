import java.util.Scanner;

class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for (int i=0; i<n; i++){
            int data = sc.nextInt();
            for (int j = 2; j<=data; j++){
                if (data%j == 0){
                    int count = 0;
                    System.out.print(j+" ");
                    while (data % j == 0){
                        data /= j;
                        count++;
                    }
                    System.out.println(count);
                }
            }
        }
    }
}
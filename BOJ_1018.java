import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();
        char[][] arr = new char[n][m];
        for (int i=0; i<n; i++){
            String s = sc.nextLine();
            for (int j=0; j<m; j++){
                arr[i][j] = s.charAt(j);
            }
        }
        int min = 64;

        for (int i=0; i<=n-8; i++){
            for (int j=0; j<=m-8; j++){
                int comp = howMany(returnArr(arr,i,j));
                if (comp < min)
                    min = comp;
            }
        }
        System.out.println(min);
    }
    private static int howMany(char[][] check){
        int count = 0;
        char checker = 'B';
        for(int i=0; i<8; i++){
            for (int j=0; j<8; j++){
                if (check[i][j] != checker)
                    count++;
                else {
                }
                if (checker == 'B')
                    checker = 'W';
                else
                    checker = 'B';
            }
            if (checker == 'B')
                checker = 'W';
            else
                checker = 'B';
        }
        if (64-count > count)
            return count;
        else
            return 64-count;
    }

    private static char[][] returnArr (char[][] arr, int i, int j){
        char[][] returnArr = new char[8][8];
        int bi = 0, bj = 0;
        for (int t=i; t<i+8; t++){
            bj = 0;
            for (int u=j; u<j+8; u++){
                returnArr[bi][bj] = arr[t][u];
                bj++;
            }
            bi++;
        }
        return returnArr;
    }
}

import java.util.Scanner;

class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String s = Integer.toBinaryString(n);
        int count = 0;
        for (int i = 0; i<s.length(); i++){
            if (s.charAt(i)=='1')
                count++;
        }
        System.out.println(count);
    }
}
import java.util.Scanner;

public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int overlap = 0, count = 0;
        s += " ";
        for (int i=0; i<s.length(); i++){
            if (s.charAt(i)=='('){
                if (s.charAt(i+1)==')') {
                    count += overlap;
                }
                else {
                    overlap++;
                }
            }
            if (s.charAt(i)==')')
                if (s.charAt(i-1)!='('){
                    count++;
                    overlap--;
                }
        }
        System.out.println(count);
    }
}

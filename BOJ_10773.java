import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Stack<Integer> stk = new Stack<>();
        for(int i=0; i<n; i++){
            int t = sc.nextInt();
            if(t==0)
                stk.pop();
            else
                stk.push(t);
        }
        int sum = 0;
        while (stk.isEmpty()!=true){
            sum += stk.pop();
        }
        System.out.print(sum);
    }
}

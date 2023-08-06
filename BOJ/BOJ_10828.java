import java.util.Scanner;

class Stack{
    int top;
    int[] stack;
    int amount;

    public Stack(int amount){
        top = -1;
        stack = new int[amount];
        this.amount = amount;
    }

    public void push(int value) {
        stack[++top] = value;
    }

    public void pop() {
        if(top<0)
            System.out.println(-1);
        else
            System.out.println(stack[top--]);
    }

    public void size(){
        System.out.println(top+1);
    }

    public void empty(){
        if(this.top == -1)
            System.out.println(1);
        else
            System.out.println(0);
    }

    public void top(){
        if(top!=-1)
            System.out.println(stack[top]);
        else
            System.out.println(-1);
    }


}
public class BOJ_10828 {
    public static void main(String avgs[])
    {
        Stack st = new Stack(10000);
        Scanner sc = new Scanner(System.in);
        int n;
        String command;
        n = sc.nextInt();

        for(int i=0; i<n; i++){
            command = sc.next();
            switch (command){
                case("push") : {
                    int x;
                    x = sc.nextInt();
                    st.push(x);
                    break;
                }
                case("pop") :{
                    st.pop();
                    break;
                }
                case("size") :{
                    st.size();
                    break;
                }
                case("empty") :{
                    st.empty();
                    break;
                }
                case("top") :{
                    st.top();
                    break;
                }
                default:
                    break;
            }
        }
    }
}
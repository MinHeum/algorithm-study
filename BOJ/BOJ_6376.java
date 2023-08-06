public class BOJ_6376   {
    public static void main(String args[]){
        System.out.println("n e");
        System.out.println("- -----------");
        double sig = 0;
        for(int i=0; i<10; i++){
            for(int j=i; j<=i; j++)
                sig += 1/fact(i);
            System.out.print(i+" ");
            if(i<=1)
                System.out.print((int)sig);
            else if (i == 2)
                System.out.printf("%.1f",sig);
            else
                System.out.printf("%.9f",sig);
            System.out.println();
        }
    }
    private static double fact(int n) {
        if(n==0||n==1) return 1;
        return n*fact(n-1);
    }
}

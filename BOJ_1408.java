import java.util.Scanner;

public class BOJ_1408 {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();

        int t1 =
                Integer.parseInt(s1.split(":")[0])*3600
              + Integer.parseInt(s1.split(":")[1])*60
              + Integer.parseInt(s1.split(":")[2]);
        int t2 =
                Integer.parseInt(s2.split(":")[0])*3600
              + Integer.parseInt(s2.split(":")[1])*60
              + Integer.parseInt(s2.split(":")[2]);
        int t3 = t2 - t1;
        if (t3<0)
            t3+=24*3600;
        int hour = t3/3600;
        t3 = t3 - hour*3600;
        int min = t3/60;
        t3 = t3 - min * 60;
        System.out.format("%02d:%02d:%02d",hour,min,t3);
    }
}
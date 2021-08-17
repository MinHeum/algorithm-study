// BOJ_2884.java
import java.util.Scanner;

public class BOJ_2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        int hour = Integer.parseInt(input.split(" ")[0]);
        int minute = Integer.parseInt(input.split(" ")[1]);

        int times = hour * 60 + minute;
        times -= 45;
        if (times < 0) times += 1440;

        int hourNew = times / 60;
        int minuteNew = times % 60;

        System.out.println(hourNew+" "+minuteNew);
    }
}
// BOJ_2530.java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int second = sc.nextInt();

        int addSecond = sc.nextInt();

        int time = hour * 3600 + minute * 60 + second;

        int newSec = time + addSecond;

        int newHour = newSec / 3600;
        newSec -= newHour * 3600;
        int newMinute = newSec / 60;
        newSec -= newMinute * 60;
        while (newHour >=24)
            newHour-=24;
        System.out.println(newHour+" "+newMinute+" "+newSec);
    }
}
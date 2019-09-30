import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        String[] arr = s.split("[+,-]");
        int result = 0;

        int[] intArr = new int[arr.length];
        for (int i = 0; i < intArr.length; i++)
            intArr[i] = Integer.valueOf(arr[i]); //정수배열에 숫자들만 다 담기완료

        boolean[] opers = new boolean[intArr.length-1];
        int temp = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == '-') {
                opers[temp] = true;
                temp++;
            }
            else if (s.charAt(i) == '+')
                temp++;
        }
        boolean flag = false; // flag가 true 이면 + 라도 빼버림
        result = intArr[0];
        for (int i = 0; i < opers.length; i++) {
            if (opers[i] == true) flag = true;
            if (flag == true) {
                result -= intArr[i+1];
            }
            else {
                result += intArr[i+1];
            }
        }
        System.out.println(result);
    }
}
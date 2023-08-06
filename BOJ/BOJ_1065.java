// BOJ_1065.java

import java.util.Scanner;

public class BOJ_1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0; // 만족하는 한수의 개수를 저장할 배열
        for (int i = 1; i<=n; i++) {
            String s = String.valueOf(i); // s 는 해당 문자열이 등차수열 조건을 만족하는 데 쓰임
            boolean isHanNum = true;
            if (s.length() > 2) { // 한 자리 수, 두자리 수는 무조건 한수임
                int diff = s.charAt(1) - s.charAt(0);
                for (int j = 1; j < s.length()-1; j++) { // 문자열의 각 인덱스를 순회
                    if (s.charAt(j+1)-s.charAt(j) != diff) {
                        isHanNum = false;
                    }
                }
                if (isHanNum) count++;
            }
            else count++;
        }
        System.out.println(count);
    }
}
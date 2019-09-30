import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] pack = new int[m];
        int[] single = new int[m];
        for (int i = 0; i < m; i++) {
            pack[i] = sc.nextInt();
            single[i] = sc.nextInt();
        }

        int packMin = pack[0];
        for (int i = 0; i < pack.length; i++) {
            if (packMin > pack[i]) packMin = pack[i];
        }

        int singleMin = single[0];
        for (int i = 0; i < single.length; i++) {
            if (singleMin > single[i]) singleMin = single[i];
        }

        int packNum = 0;
        if (packMin > singleMin * 6) // 낱개 사는게 가성비가 좋다면
            System.out.println(singleMin*n);
        else {                         // 패키지로 사는게 가성비가 좋다면
            // 패키지로 살 수 있을만큼 일단 산 다음에
            packNum = n/6;
            if (packMin > (n-packNum*6)*singleMin) // 나머지를 살 때 낱개로 사는게 싸면
                System.out.println(packNum * packMin + (n-packNum*6)*singleMin);
            else
                System.out.println(packMin * (packNum+1));
        }


    }
}
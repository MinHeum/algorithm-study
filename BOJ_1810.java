package com.solved;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int n, r, numbers[], inputs[] = new int[9];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        numbers = new int[7];
        for (int i = 0; i < 9; i++) {
            inputs[i] = Integer.parseInt(br.readLine());
        }

        combination(9,7);

    }
    private static int sum(int[] arr){
        int result = 0;
        for (int n : arr)
            result += n;
        return result;
    }

    private static void combination(int n, int r) {
        if (r==0) {
            if(sum(numbers) == 100)
                for (int k:numbers
                     ) {
                    System.out.println(k);
                }
            return;
        }

        if (n<r) return;
        numbers[r-1] = inputs[n-1];
        combination(n-1, r-1);
        combination(n-1, r);
    }
}

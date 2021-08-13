package com.solved;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int N, M, answer;
    static ArrayList<int[]> houses, chickens;
    static int[][] selectedChickens;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        answer = Integer.MAX_VALUE;
        houses = new ArrayList<>();
        chickens = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                int val = Integer.parseInt(st.nextToken());
                if (val == 0) continue;
                if (val == 1) houses.add(new int[]{i,j});
                if (val == 2) chickens.add(new int[]{i,j});
            }
        }
        selectedChickens = new int[M][];
        comb(chickens.size(), M);
        System.out.println(answer);
    }
    private static void comb(int n, int r) {
        if (r == 0) {
            getChickenLength();
            return;
        }
        if(n < r) return;
        selectedChickens[r-1] = new int[]{chickens.get(n-1)[0], chickens.get(n-1)[1]};
        comb(n-1, r-1);
        comb(n-1,r);
    }

    private static void getChickenLength(){
        int sum = 0;
        for (int i = 0; i < houses.size(); i++) {
            int min = Integer.MAX_VALUE;
            for (int j = 0; j < selectedChickens.length; j++) {
                int dist = getLength(houses.get(i), selectedChickens[j]);
                if (dist < min) min = dist;
            }
            sum += min;
        }
        answer = Math.min(sum, answer);
    }

    private static int getLength(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
}

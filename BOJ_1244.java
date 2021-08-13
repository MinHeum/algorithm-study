package com.solved;

import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	static int N;
	static int[] arr;

	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N+1]; // 0번은 비울예정
		for (int i = 1, arrLength = arr.length; i < arrLength; i++) {
			arr[i] = sc.nextInt();
		}
		int K = sc.nextInt();
		for(int i = 0; i < K; i++) {
			if(sc.nextInt() == 1) {
				boy(sc.nextInt());
			}
			else {
				girl(sc.nextInt());
			}
		}
		for (int i = 1; i < arr.length; i++) {
			if(i == arr.length-1)
				System.out.print(arr[i]);
			else
				System.out.print(arr[i] + " ");
			if (i % 20 == 0) System.out.println();
		}
		sc.close();
	}
	
	public static void boy(int n) {
		for (int i = 1; i < arr.length; i++) {
			if(i % n == 0) {
				arr[i] = arr[i] == 1? 0:1;
			}
		}
	}
	
	public static void girl(int n) {
		arr[n] = arr[n] == 1? 0:1;

		int i = 0;
		while(true) {
			i++;
			if (n+i >= arr.length || n-i <= 0 || arr[n+i]!=arr[n-i])
				break;
			arr[n+i] = arr[n+i] == 1? 0:1;
			arr[n-i] = arr[n-i] == 1? 0:1;
		}
	}

}

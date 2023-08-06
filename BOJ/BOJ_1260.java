package com.solved;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class BOJ_1260 {
    static int N, M, V;
    static boolean[] visited;
    static int[][] adj;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        adj = new int[N+1][N+1];
        visited = new boolean[N+1];

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());

            adj[v1][v2] = 1;
            adj[v2][v1] = 1;
        }

        dfs(V);
        visited = new boolean[N+1];
        System.out.println();
        bfs(V);
    }

    private static void dfs(int v) {
        visited[v] = true;
        System.out.print(v+" ");
        for (int i = 1; i < adj.length; i++) {
            if (adj[v][i] == 1 && !visited[i])
                dfs(i);
        }
    }

    private static void bfs(int v) {
        LinkedList<Integer> queue = new LinkedList<>();
        visited[v] = true;
        queue.add(v);
        while (!queue.isEmpty()) {
            v = queue.poll();
            System.out.print(v + " ");

            for (int i = 1; i <= N; i++) {
                if (adj[v][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}

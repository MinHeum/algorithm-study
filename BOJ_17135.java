import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_17135 {
    private static int N, M, D, map[][], mapSave[][], answer;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        D = Integer.parseInt(st.nextToken());
        map = new int[N][M];
        mapSave = new int[N][M];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                mapSave[i][j] = map[i][j];
            }
        }
        /*
         * 각 턴 제거할 수 있는 최대 적 수는 3명
         * 적이 내려가는것보다는 성이 올라가는게 편하다.
         */
        answer = 0;
        fun();
        System.out.println(answer);
    }
    private static void fun(){
        // M 개 중 3개를 정하는 함수
        for (int k1 = 0; k1 < M; k1++) {
            for (int k2 = k1; k2 < M; k2++) {
                if (k1 == k2) continue;
                for (int k3 = k2; k3 < M; k3++) {
                    if (k2 == k3 || k1 == k3) continue;
                    int[] archer = new int[]{k1,k2,k3}; // 궁수 c 위치 선정
                    int kill = 0;
                    int castle = N;
                    while (castle > 0) {
                        int[][] target = setTarget(archer, castle);
                        for (int i = 0; i < 3; i++) { // i번째 타겟 순회
                            int targetR = target[i][0];
                            int targetC = target[i][1];
                            if (targetR == -1 || targetC == -1)continue;
                            if (map[targetR][targetC] == 1) {
                                map[targetR][targetC] = 0;
                                kill++;
                            }
                        }
                        castle--;
                    }
                    answer = Math.max(kill, answer);
                    for (int i = 0; i < N; i++) {
                        map[i] = Arrays.copyOf(mapSave[i], mapSave[i].length);
                    }
                }
            }
        }
    }

    private static int[][] setTarget(int[] archers, int castle) {
        int[][] target = new int[3][2];
        for (int i = 0; i < 3; i++) {
            Arrays.fill(target[i], -1);
        }
        top:
        for (int k = 0; k < 3; k++) { // k 번째 궁수의 타겟 찾기
            for (int dist = 1; dist <= D; dist++) {
                for (int c = 0; c < M; c++) {
                    for (int r = castle - 1; r >= 0 && r >= castle-dist-1; r--) { // 타겟은 궁수가 있는 r 좌표값보다 1 작은 좌표부터
                        if (getDistance(castle, archers[k], r, c) == dist && map[r][c] == 1) { // 거리 내에 있고 적이 있는 경우
                            target[k][0] = r;
                            target[k][1] = c;
                            continue top; // 타겟을 선정했으면 다음 타겟 선정
                        }
                    }
                }
            }
        }
        return target;
    }

    private static int getDistance(int r1, int c1, int r2, int c2) {
        return Math.abs(r1-r2) + Math.abs(c1-c2);
    }
}

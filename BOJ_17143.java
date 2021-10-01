import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_17143 {
    private static int R, C, M;
    private static int[][] map;
    private static Shark[] sharks;
    private static final int[][] DARR = new int[][] {{}, {-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    private static class Shark{
        int r, c, speed, direction, size;

        public Shark(int r, int c, int speed, int direction, int size) {
            this.r = r;
            this.c = c;
            this.direction = direction;
            this.size = size;
            if (direction < 3) {
                this.speed = speed % ((R-1) * 2);
            }else {
                this.speed = speed % ((C-1) * 2);
            }
        }

        @Override
        public String toString() {
            return "Shark{" +
                    "r=" + r +
                    ", c=" + c +
                    ", speed=" + speed +
                    ", direction=" + direction +
                    ", size=" + size +
                    '}';
        }
    }

    private static int changeDirection(int direction) {
        if (direction % 2 == 0) {
            return direction-1;
        }else {
            return direction+1;
        }
    }

    private static void fun(){
        int[][] newMap = new int[R][C];
        for (int i = 1; i <= M; i++) {
            if (sharks[i] == null) continue;
            int nr = sharks[i].r;
            int nc = sharks[i].c;
            for (int step = 0; step < sharks[i].speed; step++) {
                if (sharks[i].direction == 4 && nc == 0 ||
                    sharks[i].direction == 3 && nc == C-1 ||
                    sharks[i].direction == 2 && nr == R-1 ||
                    sharks[i].direction == 1 && nr == 0
                ) {
                    sharks[i].direction = changeDirection(sharks[i].direction);
                }
                nr += DARR[sharks[i].direction][0];
                nc += DARR[sharks[i].direction][1];
            }
            if (newMap[nr][nc] != 0) { // 이동 후 상어 중복일 때
                if (sharks[i].size > sharks[newMap[nr][nc]].size) {
                    sharks[newMap[nr][nc]] = null;
                    newMap[nr][nc] = i;
                    sharks[i].r = nr;
                    sharks[i].c = nc;
                }else {
                    sharks[i] = null;
                }
            }
            else {
                newMap[nr][nc] = i;
                sharks[i].r = nr;
                sharks[i].c = nc;
            }

        }
        map = newMap;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[R][C];
        sharks = new Shark[M+1];
        sharks[0] = null;
        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken())-1;
            int c = Integer.parseInt(st.nextToken())-1;
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            int z = Integer.parseInt(st.nextToken());
            sharks[i] = new Shark(r,c,s,d,z);
            map[r][c] = i;
        }
        int answer = 0;
        int cur = 0;
        do {
            for (int i = 0; i < R; i++) {
                if (map[i][cur] != 0) {
                    answer += sharks[map[i][cur]].size;
                    sharks[map[i][cur]] = null;
                    map[i][cur] = 0;
                    break;
                }
            }
            fun();
            cur++;
        }while (cur < C);

        System.out.println(answer);
    }
}

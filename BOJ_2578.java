import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2578 {
    static int[][] map, chk;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        map = new int[5][5];
        StringTokenizer st;
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        chk = new int[5][5];

        top:
        for (int i = 0; i < 5; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                find(Integer.parseInt(st.nextToken()));
                if (check() > 2) {
                    System.out.println(i * 5 + j + 1);
                    break top;
                }
            }
        }

    }
    private static void find(int n) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (map[i][j] == n) {
                   chk[i][j] = 1;
                }
            }
        }
    }

    private static int check(){
        // row check
        int ret = 0;
        for (int i = 0; i < 5; i++) {
            int cntA = 0, cntB = 0;
            for (int j = 0; j < 5; j++) {
                cntA += chk[i][j];
                cntB += chk[j][i];
            }
            if (cntA == 5) ret++;
            if (cntB == 5) ret++;
        }
        {
            int cntA = 0, cntB = 0;
            for (int i = 0; i < 5; i++) {
                cntA += chk[i][i];
                cntB += chk[4 - i][i];
                if (cntA == 5) ret++;
                if (cntB == 5) ret++;
            }
        }
        return ret;
    }
}

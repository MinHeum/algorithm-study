import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1449 {

    static class Tape{
        int start, end;

        public Tape(int start, int end) {
            this.start = start;
            this.end = end;
        }

    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int[] holes = new int[N];
        for (int i = 0; i < N; i++) {
            holes[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(holes);
        ArrayList<Tape> tapes = new ArrayList<>();
        tapes.add(new Tape(holes[0], holes[0]));
        for (int i = 1; i < N; i++) {
            Tape cur = tapes.get(tapes.size()-1);
            if (holes[i] - cur.start < L) {
                tapes.set(tapes.size()-1, new Tape(cur.start, holes[i]));
            }
            else {
                tapes.add(new Tape(holes[i],holes[i]));
            }
        }
        System.out.println(tapes.size());
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_10825 {
    private static class Score implements Comparable<Score>{
        String name;
        int kor;
        int eng;
        int math;

        public Score(String name, int kor, int eng, int math) {
            this.name = name;
            this.kor = kor;
            this.eng = eng;
            this.math = math;
        }

        @Override
        public int compareTo(Score o) {
            int val = o.kor - this.kor;
            if (val != 0) return val;
            val = this.eng - o.eng;
            if (val != 0) return val;
            val = o.math - this.math;
            if (val != 0) return val;
            return this.name.compareTo(o.name);
        }
    }


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Score[] scores = new Score[N];
        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            scores[i] = new Score(st.nextToken(), Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()),Integer.parseInt(st.nextToken()));
        }
        Arrays.sort(scores);
        for(Score s : scores) System.out.println(s.name);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class BOJ_16211_NOTSOLVED{
    static double good_good, good_bad, bad_good, bad_bad;
    static int N, good, bad;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int mood = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        good_good = Double.parseDouble(st.nextToken());
        good_bad = Double.parseDouble(st.nextToken());
        bad_good = Double.parseDouble(st.nextToken());
        bad_bad = Double.parseDouble(st.nextToken());
        good = 0;
        bad = 0;
        func(0, mood, 1.0);
        System.out.println(good);
        System.out.println(bad);
    }

    private static void func(int day, int mood, double chance) {
        if (day == N) {
            if (mood == 0) {
                good += chance * 1000;
                return;
            }
            else{
                bad += chance * 1000;
                return;
            }
        }
        if (mood == 0) {
            func(day+1, 0, chance * good_good);
            func(day+1, 1, chance * good_bad);
        }
        else{
            func(day+1, 0, chance * bad_good);
            func(day+1, 1, chance * bad_bad);
        }
    }
}
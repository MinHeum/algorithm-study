import java.util.ArrayList;
import java.util.List;

// BOJ_4673.java
public class BOJ_4673 {
    public static void main(String[] args) {
        List<Long> lst = new ArrayList<>();
        lst.add((long)1);
        int count = 1;
        long[] selfLst = new long[10000];
        for (int i = 0; i < 10000; i++) {
            selfLst[i] = selfNum(i);
        }
        long[] resultLst = new long[10000];
        for (int i = 0; i < 10000; i++) {
            resultLst[i] = i+1;
        }
        for (int i = 0; i < 10000; i++) {
            for (int j = 0; j < 10000; j++) {
                if (resultLst[i] == selfLst[j]) {
                    resultLst[i] = -1;
                    break;
                }
            }
        }
        for (int i = 0; i < 10000; i++) {
            if(resultLst[i] > 0)
                System.out.println(resultLst[i]);
        }
    }
    private static long selfNum(long input) {
        int len = (int) Math.log10(input)+1;
        long result = 0;
        for (int i = 0; i < len; i++) {
            result += (long)(input / Math.pow(10, i)) % 10;
        }
        result += input;
        return result;
    }
}
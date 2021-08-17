import java.util.Scanner;

class Stat{
    int hp = 1;
    int mp = 1;
    int atk = 0;
    int def = 0;
    int hpEnv = 0;
    int mpEnv = 0;
    int atkEnv = 0;
    int defEnv = 0;
    public Stat(){
        this.hp = 1;
        this.mp = 1;
        this.atk = 0;
        this.def = 0;
        this.hpEnv = 0;
        this.mpEnv = 0;
        this.atkEnv = 0;
        this.defEnv = 0;
    }
    public Stat(String s) {
        this.hp = Integer.parseInt(s.split(" ")[0]);
        this.mp = Integer.parseInt(s.split(" ")[1]);
        this.atk = Integer.parseInt(s.split(" ")[2]);
        this.def = Integer.parseInt(s.split(" ")[3]);
        this.hpEnv = Integer.parseInt(s.split(" ")[4]);
        this.mpEnv = Integer.parseInt(s.split(" ")[5]);
        this.atkEnv = Integer.parseInt(s.split(" ")[6]);
        this.defEnv = Integer.parseInt(s.split(" ")[7]);
    }
    void getPow(){
        int sumHp = this.hp+this.hpEnv;
        int sumMp = this.mp+this.mpEnv;
        int sumAtk = this.atk+this.atkEnv;
        int sumDef = this.def+this.defEnv;
        if (sumHp<1)
            sumHp = 1;
        if (sumMp<1)
            sumMp = 1;
        if (sumAtk<0)
            sumAtk = 0;

        System.out.println(1*(sumHp) + 5*(sumMp) + 2*(sumAtk) + 2*(sumDef));
    }
}
public class BOJ_12790 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.next());
        sc.nextLine();
        Stat art[] = new Stat[n];
        for(int i=0; i<n; i++){
            art[i] = new Stat(sc.nextLine());
        }
        for(int i=0; i<n; i++){
            art[i].getPow();
        }
    }
}

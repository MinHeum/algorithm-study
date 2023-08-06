import java.util.LinkedList;
import java.util.Scanner;

class BOJ_10845{
    public static void main(String asgs[]){
        LinkedList<Integer> que = new LinkedList<>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        for (int i = 0; i<n; i++){
            String s = sc.nextLine();
            if (s.split(" ").length == 2){
                que.addLast(Integer.valueOf(s.split(" ")[1]));
            }
            else{
                if (s.contains("front")){
                    if (que.isEmpty())
                        System.out.println("-1");
                    else
                        System.out.println(que.getFirst());
                }
                else if (s.contains("back")){
                    if (que.isEmpty())
                        System.out.println("-1");
                    else
                        System.out.println(que.getLast());
                }
                else if (s.contains("size")){
                    System.out.println(que.size());
                }
                else if (s.contains("empty")){
                    System.out.println(que.isEmpty()?"1":"0");
                }
                else if (s.contains("pop")){
                    if (que.isEmpty())
                        System.out.println("-1");
                    else{
                        System.out.println(que.getFirst());
                        que.removeFirst();
                    }
                }
                else {
                    System.out.println("Something is wrong");
                }
            }
        }
    }
}
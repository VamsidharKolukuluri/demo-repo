package Programming.Java;

import java.util.ArrayList;

public class ReverseArray {

    public ArrayList<Integer> reverseArray(ArrayList<Integer> al) {
        int j = al.size();
        for (int i = 0; i < al.size(); i++) {
            int temp = al.get(j - 1);
            al.add(j - 1, al.get(i));
            al.add(i, temp);
            j -= 1;
        }
        return al;
    }

    public static void main(String[] args) {
        ArrayList<Integer> al = new ArrayList<Integer>();
        al.add(1);
        al.add(2);
        al.add(3);
        al.add(4);
        al.add(5);
        ReverseArray ra = new ReverseArray();
        for (Integer i : ra.reverseArray(al)) {
            System.out.println(i + " ");
        }
    }
}

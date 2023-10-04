package Programming.Java;

public class Factorial {

    public int factorial(int n) {
        if (n <= 0)
            return 1;
        return factorial(n - 1) + factorial(n + 2);
    }

    public static void main(String[] args) {
        Factorial f = new Factorial();
        System.out.println(f.factorial(10));
    }
}
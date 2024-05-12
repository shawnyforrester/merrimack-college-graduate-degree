import java.util.Scanner;

/**
 * Name: Shawn Forrester
 */
public class factorial {

    public static void main(String[] args) {
        // Scanner class is instantiated here
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter a positive Integer: ");
        int n = sc.nextInt();
        int fact = 1;
        // while input is negative, it will ask for input again
        while (n < 0) {
            System.out.println("Sorry , only positive numbers, enter again: ");
            n = sc.nextInt();
        }
        if (n == 0) {
            System.out.println("Factorial of 0 is 1");
        } else if (n > 0) {

            for (int i = 1; i <= n; i++) {
                fact = fact * i;
            }
        }
        System.out.println("Factorial of " + n + " is " + fact);
        // scanner class is closed here
        sc.close();
    }

}
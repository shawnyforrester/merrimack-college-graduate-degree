import java.util.Scanner;

/**
 * Name: Shawn Forrester
 * Date: 1/28/2021
 * Program: prime.java
 */

public class prime {

    public static void main(String[] args) {
        System.out.println("Enter a postive number (0 or negative exit): ");
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        while (num > 0) {
            int count = 0;
            for (int i = 1; i <= num; i++) {
                if (num % i == 0) {
                    count++;
                }
            }
            if (count == 2) {
                System.out.println(num + " is a prime number.");
            } else {
                System.out.println(num + " is not a prime number.");
            }
            System.out.println("Enter a postive number (0 or negative exit): ");
            num = sc.nextInt();
        }
        sc.close();

    }
}

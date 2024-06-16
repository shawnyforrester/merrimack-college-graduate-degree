package src;

import java.util.Collections;
import java.util.Scanner;
import java.util.Stack;

/**
 * This class is a concrete class that extends the StackBuilder class. It is
 * used to create a Stack of Integers.
 */
public class StackIntegers extends StackBuilder<Integer> {

    /**
     * The LinkedList that will store the Integers.
     */
    private static Stack<Integer> stack;

    /**
     * Creates a a stack of Integers.
     */
    @Override
    public Stack<Integer> createStack() {
        Stack<Integer> stack = new Stack<Integer>();
        return stack;
    }

    /**
     * The main method that creates a Stack of Integers.
     * 
     * @param args
     */
    public static void main(String[] args) {
        StackIntegers stackInt = new StackIntegers();
        stack = stackInt.createStack();
        stackInt.readIntegers(stack);
        Collections.sort(stack);
        stackInt.printList(stack);
    }

    /**
     * Reads the integers from the user and adds them to the list.
     * 
     * @param stack
     */

    private void readIntegers(Stack<Integer> stack) {
        StackIntegers stackInt = new StackIntegers();
        Scanner scanner = new Scanner(System.in);
        System.out.println(
                "\n Enter the number of integers you want to add to the list Please separate your integers by a space. Hit Enter when you are finished:");
        String input = scanner.nextLine();
        String[] numbers = input.split(" ");
        for (String number : numbers) {
            Integer element = Integer.parseInt(number);
            try {
                stack = stackInt.addToStack(element, stack);
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid integer.");
            }
        }
        scanner.close();
    }

}

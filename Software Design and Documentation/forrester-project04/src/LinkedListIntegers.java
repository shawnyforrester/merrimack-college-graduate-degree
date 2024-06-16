package src;

import java.util.LinkedList;
import java.util.Scanner;
import java.util.Collections;

/**
 * This class is a concrete class that extends the LinkedListBuilder class. It
 * is used to create a LinkedList of Integers.
 * 
 */

public class LinkedListIntegers extends LinkedListBuilder<Integer> {

    /**
     * The LinkedList that will store the Integers.
     */
    private static LinkedList<Integer> list;

    /**
     * The main method that creates a LinkedList of Integers.
     * 
     * @param args
     */
    public static void main(String[] args) {
        LinkedListIntegers listInt = new LinkedListIntegers();
        list = listInt.createContainer();
        listInt.readIntegers(list);
        Collections.sort(list);
        listInt.printList(list);
    }

    /**
     * Reads the integers from the user and adds them to the list.
     * 
     * @param list
     */

    private void readIntegers(LinkedList<Integer> list) {
        LinkedListIntegers listInt = new LinkedListIntegers();
        Scanner scanner = new Scanner(System.in);
        System.out.println(
                "\n Enter the number of integers you want to add to the list Please separate your integers by a space. Hit Enter when you are finished:");
        String input = scanner.nextLine();
        String[] numbers = input.split(" ");
        for (String number : numbers) {
            Integer element = Integer.parseInt(number);
            try {
                list = listInt.addToList(element, list);
            } catch (NumberFormatException e) {
                System.out.println("Please enter a valid integer.");
            }
        }
        scanner.close();
    }

}
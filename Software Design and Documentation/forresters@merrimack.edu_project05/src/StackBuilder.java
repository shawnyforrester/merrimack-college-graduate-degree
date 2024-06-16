package src;

import java.util.LinkedList;
import java.util.Stack;

/**
 * This new builderclass will implement the Container Interface, providing
 * functionality to create a Stack of objects of type T.
 */
public class StackBuilder<T> implements Container<T> {

    /**
     * Creates a Stack of objects of type T.
     */
    @Override
    public Stack<T> createStack() {
        Stack<T> stack = new Stack<T>();
        return stack;
    }

    /**
     * The LinkedList that will store the objects of type T.
     */
    @Override
    public LinkedList<T> createContainer() {
        LinkedList<T> list = new LinkedList<T>();
        return list;
    }

    /**
     * Adds an object of type T to the Stack.
     *
     * @param input
     * @param stack
     * @return
     */

    public Stack<T> addToStack(T input, Stack<T> stack) {
        stack.add(input);
        return stack;
    }

    public boolean popFromStack(T input, Stack<T> stack) {
        return stack.pop().equals(input);
    }

    /**
     * Prints the elements of the Stack.
     * 
     * @param list
     */

    public void printList(Stack<T> list) {
        System.out.println("Here is your list of elements:");
        for (T element : list) {
            System.out.println(element);
        }
    }

}

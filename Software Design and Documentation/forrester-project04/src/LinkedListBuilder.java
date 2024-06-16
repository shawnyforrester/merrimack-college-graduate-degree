package src;

import java.util.LinkedList;

/**
 * This class is a generic class that implements the Container interface.
 * It is used to create a LinkedList of any type of object.
 *
 * @param <T> the type of object to be stored in the LinkedList
 */

public abstract class LinkedListBuilder<T> implements Container<T> {

    /**
     * The LinkedList that will store the objects of type T.
     */

    protected LinkedList<T> list;

    /**
     * Creates a LinkedList of objects of type T.
     */

    @Override
    public LinkedList<T> createContainer() {
        list = new LinkedList<T>();
        return list;
    }

    /**
     * Adds an object of type T to the LinkedList.
     * 
     * @param input
     */

    public LinkedList<T> addToList(T input, LinkedList<T> list) {
        list.add(input);
        return list;
    }

    /**
     * Removes an object of type T from the LinkedList.
     * 
     * @param input
     * @return
     */
    public boolean removeFromList(T input) {
        return list.remove(input);
    }

    /**
     * Prints the elements of the LinkedList.
     * 
     * @param list
     */

    public void printList(LinkedList<T> list) {
        System.out.println("Here is your list of elements:");
        for (T element : list) {
            System.out.println(element);
        }
    }

}

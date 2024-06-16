package src;

/*
 * Container interface
 * The previous Container interface was  implemented with just a LinkedList. 
 * In this updated version a Stack  method is added.
 */

import java.util.LinkedList;
import java.util.Stack;

public interface Container<T> {
    LinkedList<T> createContainer();

    Stack<T> createStack();
}

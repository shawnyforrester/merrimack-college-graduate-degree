/***
 * 
 * This Bubble Sort Class is written in Java version 22.0.1
 * The class contains a method bubbleSort which takes an array of integers as input and sorts 
 * the array in ascending order.
 * Javadoc formatting guidlelines according to Google https://google.github.io/styleguide/javaguide.html
 * 
 */

public class BubbleSort {

    /**
     * The main method is the entry point of the program.
     * The method creates an array of integers and calls the bubbleSort method to sort the array.
     * The sorted array is then printed to the console.
     * 
     * @param Args
     * 
     */

    public static void main( String Args[]) {
        int[] arr = {2, 45, 37, 21, 31, 50, 29, 22, 67, 88, 56};
        bubbleSort(arr);
        System.out.print("\n" + "Sorted array ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }

    /**
     * The bubbleSort method takes an array of integers as input and sorts the array in ascending order.
     * The method uses the bubble sort algorithm to sort the array.
     * 
     * @param arr
     * 
     */

    private static void bubbleSort(int[] arr) {
        int n = arr.length;      
        for (int i = 0; i < n-1; i++) {
            for (int j = 0; j < n-i-1; j++) {
                if (arr[j] > arr[j+1]) {
                    // swap arr[j+1] and arr[i]
                    int temp = arr[j];
                    arr[j] = arr[j+1];
                    arr[j+1] = temp;
                }
            }
        }
    }
}
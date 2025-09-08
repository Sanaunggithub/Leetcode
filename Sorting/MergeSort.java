import java.util.Arrays;

public class MergeSort {

    // Merge Sort function
    public static int[] mergeSort(int[] arr) {
        // Base case
        if (arr.length <= 1) {
            return arr;
        }

        // Split into two halves
        int mid = arr.length / 2;
        int[] left = Arrays.copyOfRange(arr, 0, mid);
        int[] right = Arrays.copyOfRange(arr, mid, arr.length);

        // Recursively sort both halves
        left = mergeSort(left);
        right = mergeSort(right);

        // Merge the two sorted halves
        return merge(left, right);
    }

    // Merge function
    public static int[] merge(int[] a, int[] b) {
        int[] c = new int[a.length + b.length];
        int i = 0, j = 0, k = 0;

        // Compare elements and add the smaller one
        while (i < a.length && j < b.length) {
            if (a[i] <= b[j]) {
                c[k++] = a[i++];
            } else {
                c[k++] = b[j++];
            }
        }

        // Add remaining elements from a
        while (i < a.length) {
            c[k++] = a[i++];
        }

        // Add remaining elements from b
        while (j < b.length) {
            c[k++] = b[j++];
        }

        return c;
    }

    // Test the algorithm
    public static void main(String[] args) {
        int[] arr = {38, 27, 43, 3, 9, 82, 10};

        System.out.println("Original: " + Arrays.toString(arr));
        int[] sorted = mergeSort(arr);
        System.out.println("Sorted:   " + Arrays.toString(sorted));
    }
}


// mergeSort([38, 27, 43, 3])
//     mergeSort([38, 27])
//         mergeSort([38])  → returns [38]
//         mergeSort([27])  → returns [27]
//         merge([38], [27]) → [27, 38]
//     mergeSort([43, 3])
//         mergeSort([43])  → returns [43]
//         mergeSort([3])   → returns [3]
//         merge([43], [3]) → [3, 43]
//     merge([27, 38], [3, 43]) → [3, 27, 38, 43]

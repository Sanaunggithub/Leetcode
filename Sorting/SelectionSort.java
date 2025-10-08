public class SelectionSort {
    public static void main(String[] args){
        int[] array = {8, 7, 9, 2, 3, 1, 5, 4, 6};

        selctionSort(array);
        for (int i : array) {
            System.out.println(array[i]);
        }
    }

    private static void selctionSort(int[] array){
        for (int i = 0; i < array.length - 1; i++) {
            int min = i; // assume the first element is min
            for (int j = i + 1; j < array.length; j++) {
                if (array[min] > array[j]) {
                    min = j; // update min index if found smaller element
                }
            }  
            int tmp = array[i];
            array[i] = array[min];
            array[min] = tmp; 
        }
    }
}



class Solution {
    public int[] sortedSquares(int[] nums) {
        
        for(int i = 0; i < nums.length; i++){
            nums[i] = nums[i] * nums[i];
        }

        mSort(nums, 0, nums.length -1);

        return nums;
    }

    public void mSort(int[] arr, int low, int high){
        if(low >= high) return;
        int mid = low + ((high - low) >> 1);

        mSort(arr, low, mid);
        mSort(arr, mid + 1, high);
        merge(arr, low, mid, high);
    }


    public void merge(int[] arr, int low, int mid, int high){
        int [] tmp = new int[high - low + 1];

        int i = low, j = mid + 1, k = 0;

        while(i <= mid && j <= high){
            if(arr[i] <= arr[j]){
                tmp[k++] = arr[i++];
            }else {
                tmp[k++] = arr[j++];
            }
        }

        while(i <= mid){
            tmp[k++] = arr[i++];
        }

        while (j <= high) {
            tmp[k++] = arr[j++];
        }

        for (int c = 0; c < tmp.length; c++) {
            arr[low + c] = tmp[c];
        }
    }
}
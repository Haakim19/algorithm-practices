public class TwoNumberSum {
    public static void main(String[] args) {
        int[] arr = {3, 5, -4, 8, 11, 1, -1, 6};
        int targetsum = 10;
        for (int i = 0; i < arr.length; i++){
            int num1 = targetsum-arr[i];
            for(int j = 0; j < arr.length; j++){
                if (num1 == arr[j]){
                    System.out.println(arr[i] + " " + arr[j]);
                }
            }
        }
    }
}
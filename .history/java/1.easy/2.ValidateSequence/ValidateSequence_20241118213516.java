public class ValidateSequence {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int[] sequence = {2, 3, 5};
        for(int i = 0 ; i < arr.length; i++){
            if (arr[i] == sequence[0]){
                for(int j = 0 ; j < arr.length; j++){
                    if (arr[j] == sequence[1]){
                        for(int k = 0 ; k < arr.length; k++){
                            if (arr[k] == sequence[2]){
                                System.out.println("Sequence is valid");
                                return;
                            }
                        }
                    }
                }
            }
        }
    }
    
}
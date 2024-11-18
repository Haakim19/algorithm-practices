public class ValidateSequence {
    public static void main(String[] args) {
        int[] arr = {1, 2, 3, 4, 5, 6};
        int[] sequence = {2, 5, 6};

        System.out.println(isValidSubsequence(arr, sequence));
    }

    public static boolean isValidSubsequence(int[] arr, int[] sequence) {
        int seqIndex = 0;

        for (int num : arr) {
            if (seqIndex == sequence.length) {
                break; // We've matched the entire sequence.
            }
            if (num == sequence[seqIndex]) {
                seqIndex++; // Move to the next element in the sequence.
            }
        }

        // Check if we've matched all elements in the sequence.
        return seqIndex == sequence.length;
    }
}

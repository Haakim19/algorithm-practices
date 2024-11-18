def is_subsequence(array, sequence):
  """
  This function checks if the sequence is a subsequence of the array.

  Args:
      array: The main array.
      sequence: The subsequence to find.

  Returns:
      True if the sequence is found in the array in the correct order, False otherwise.
  """
  i = 0
  for num in array:
    if num == sequence[i]:
      i += 1
      if i == len(sequence):
        return True
  return False

# Example usage
array = [2, 4, 6, 8, 3, 1]
sequence = [1, 2, 3]

result = is_subsequence(array, sequence)
print("[1, 2, 3] is subsequence of [2, 4, 6, 8, 3, 1]:", result)
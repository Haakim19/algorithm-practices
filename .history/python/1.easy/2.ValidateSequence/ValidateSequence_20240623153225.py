array = [2, 4, 6, 8, 3, 1]
sequence = [1,2,3]
newsequence = []
i = 0
for num in array:
    for num2 in sequence:
        if num == sequence[i]:
            newsequence.append(num)
            i += 1
        
    if i == len(sequence):
        bool = True
print(bool)
print(newsequence)
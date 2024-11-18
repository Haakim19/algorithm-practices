array = [2, 4, 6, 8, 3, 1]
sequence = [1,2,3]

i = 0
for i in array:
    if i == sequence[i]:
        i += 1
    
    if i == len(sequence):
        bool = True
print(bool)
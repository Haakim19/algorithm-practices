array = [2, 4, 6, 8, 3, 1]
sequence = [4, 8, 6]

for i in range(len (array)):
    for j in range (len (sequence)):
        if array[i] + sequence[j]:
            bool = True
        else:
            bool = False
print(bool)
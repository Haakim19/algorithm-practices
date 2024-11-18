array = [2, 4, 6, 8, 3, 1]
sequence = [1,2,3]

for i in range(len (array)):
    for j in range (len (sequence)):
        if array[i] + sequence[j]:
            bool = True
        else:
            bool = False
print(bool)
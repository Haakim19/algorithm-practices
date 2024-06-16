array = [3, 6, 5, 2, 8, -7]
targetNum = 12

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] + array[j] == targetNum:
           finalOutput = array[i] , array[j]

print (finalOutput)
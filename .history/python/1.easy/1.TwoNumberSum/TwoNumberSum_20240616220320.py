array = [3, 6, 5, 4, 1, 8, -7]
targetNum = 10

for i in range(len(array)):
    for j in range(i+1, len(array)):
        if array[i] + array[j] == targetNum:
           finalOutput = array[i] , array[j]

print (finalOutput)
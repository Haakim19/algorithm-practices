# from inspect import _empty


# array = [3, 6, 5, 2, 8, -7]
# targetNum = 1

# for i in range(len(array)):
#     for j in range(i+1, len(array)):
#         if array[i] + array[j] == targetNum:
#            finalOutput = array[i] , array[j]

# print (finalOutput)

#taking the targetnum from user

# arr = [2, 5, 8, 9, 4, 1, -4, -1]
# targetNumber = int (input("Enter the target number: "))
# bool  = False
# for i in range(len (arr)):
#     for j in range (i+1,len(arr)):
#         if arr[i] + arr[j] == targetNumber:
#             bool = True
#             final = arr[i] , arr[j]
#         else:
#             final2 = arr[i], arr[j]
# if bool == True:
#     print (final)
# else:
#     print(final2)

#taking the array numbers from the user and the target number
arraySize = 5
arr = []
for i in range (arraySize):
    num = int (input("Enter a number: "))
    arr.append(num)
targetNumber1 = int (input("Enter nuber to ba find: "))

for a in range(len (arr)):
    for b in range (a+1, len (arr)):
        if arr[a] + arr [b] == targetNumber1:
            print(f'numbers are {arr[a] , arr[b]}')


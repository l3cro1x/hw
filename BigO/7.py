def bubbleSort(arr):
    for i in range(len(arr)):
        flag = False
        for j in range(0,len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
        if not flag:
            return arr


print(bubbleSort([1,3,2,5,4]))

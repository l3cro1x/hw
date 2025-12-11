def moveZeros(n):
    idx = 0
    i = 0
    while i<len(n):
        if n[i] != 0:
            n[idx] = n[i]
            idx +=1
        i +=1
    while idx < len(n):
        n[idx] = 0
        idx +=1
    return n

print(moveZeros([1,2,4,0,6,4,0,0,3,7]))
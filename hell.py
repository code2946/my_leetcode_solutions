def destroyer(arr : list [int] , target: int )-> int :
    for i in range(len(arr)):
        if arr [i ]== target:
            return i 
    return  -1
arr = [ 1,3,454,56,67,78]
target=56
print(destroyer(arr,target))    
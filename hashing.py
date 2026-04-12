def hashing(nums:list[int],arr:list[int])->list[int]:
    frequency ={}
    result={}
    for i in nums:
        if i in frequency :
            frequency[i]+=1
        elif i not in frequency :
            frequency[i]=1
    for j in arr:
        if j in frequency:
             result[j]=frequency[j]
    return result        
arr=[10,111,1,9,5,67,2]
nums=[5,3,2,2,1,5,5,7,5,10]                    
print(hashing(nums,arr))

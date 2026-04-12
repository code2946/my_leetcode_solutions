def hash_map(nums:list[int])->dict:
    frequency ={}
    for num in nums:
        if num in frequency:
            frequency[num]+=1
        elif num not in frequency:
            frequency[num]=1 
    for key in frequency :
        print(key) 
    for value in frequency.values():
        print( value )             
    return frequency
nums=[1,2,3,1,2,3,4,4,3,2,1]
print (hash_map(nums))        
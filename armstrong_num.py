def armstrong(n:int)->bool:
    nums=n
    pop=0
    power=len(str(n))
    while nums>0:
        last_digit=nums%10
        nums=nums//10
        pop=pop + last_digit**power
    print (pop)    
    return n==pop

print(armstrong(1634))
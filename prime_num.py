from math import isqrt
def prime_num(n:int)->bool:
    num=n
    if num<2:
        return False
    for i in range(2,isqrt(num)+1):
        if num%i==0:
            return False
    return True
print(prime_num())
from math import sqrt

def factor_num(n: int) -> list:
    factors = []
    num = n
    
    for i in range(1,int(sqrt(num))+1):
        if num%i ==0:
            factors.append(i)
            if i!=num//i:
                factors.append(num//i)
            
    for j in factors:
        if j ==1 or j ==n:
            print("n is a prine number ")    
    factors.sort()  
    return factors      


n = 
print(factor_num(n))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
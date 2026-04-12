from math import sqrt

def factor_num(n: int) -> list:
    factors = []
    num = n
    
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:                    # ✅ check divisibility first
            factors.append(i)
            if num // i != i:               # ✅ nested inside — only runs if i is a factor
                factors.append(num // i)
    
    factors.sort()                          # ✅ parentheses added
    return factors

n = 36
print(factor_num(n))  # [1, 2, 3, 4, 6, 9, 12, 18, 36]
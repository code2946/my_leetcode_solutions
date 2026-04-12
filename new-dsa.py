def palindrome(n: int) -> bool:
    if n < 0:
        return False
    
    nums = n
    pop = 0
    
    for i in range(len(str(n))):
        last_digit = nums % 10
        nums = nums // 10
        pop = pop * 10 + last_digit
    
    return n == pop


# Test cases
print(palindrome(1234))   # False
print(palindrome(121))    # True
print(palindrome(1))      # True
print(palindrome(-121))   # False
print(palindrome(12321))  # True
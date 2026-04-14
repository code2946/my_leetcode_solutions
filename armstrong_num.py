def armstrong_num(n:int)->bool:
    num=n
    pop =0
    power = len(str(num))
    while num!=0:
        last_digit = num%10
        pop=pop + last_digit**power
        num = num//10
    return n==pop
print(armstrong_num(153))    
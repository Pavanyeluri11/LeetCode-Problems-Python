def subtractProductAndSum( n):
    summ,product = 0,1
    while n:
        summ += n%10
        product *= n%10
        n //= 10
    return product-summ

print(subtractProductAndSum(234))

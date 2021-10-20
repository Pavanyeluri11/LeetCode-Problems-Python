def singleNumber(nums):
    return (3*sum(set(nums)) - sum(nums))//2

print(singleNumber([2,2,3,4,4,4,2]))
        

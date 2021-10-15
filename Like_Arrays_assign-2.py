def numIdenticalPairs(nums):
    count={}
    for i in nums:
        if i in count:
            count[i]+=1
        else:
            count[i] = 1
    pairs=0
    for i in list(count.values()):
        pairs += (i-1)*i//2
    return pairs

print(numIdenticalPairs([1,2,3,2,1,1]))

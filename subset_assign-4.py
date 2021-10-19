def subsets(nums):
    subset = []
    for i in range(2 ** len(nums)):
        choose = bin(i)[2:].rjust(len(nums), '0')
        temp = []
        for idx in range(len(choose)):
            if choose[idx] == '1':
                temp.append(nums[idx])
        subset.append(temp)
    return subset

def smallerNumbersThanCurrent(nums):
    new =[]
    for i in range(len(nums)):
        count=0
        for j in range(len(nums)):
            if (nums[j] < nums[i]) and (j!=i):
                count+=1
        new.append(count)
    return new

if __name__=='__main__':
    print(smallerNumbersThanCurrent([8,2,2,4,6]))

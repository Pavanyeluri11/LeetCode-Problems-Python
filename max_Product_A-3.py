def maxProduct(nums):
    nums.sort(reverse=True)
    return (nums[0]-1)*(nums[1]-1)

print(maxProduct([2,4,5,7]))

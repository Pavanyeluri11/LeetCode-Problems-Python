def singleNumber(nums):
    ele = 0
    for i in nums:
        ele = ele^i
    return ele

if __name__=='__main__':
    print(singleNumber([1,2,3,3,2]))

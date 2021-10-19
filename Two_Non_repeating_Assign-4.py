def singleNumber(nums):
    a_xor_b = 0
    for i in nums:
        a_xor_b = a_xor_b^i
    mask_of_rmb = a_xor_b & -a_xor_b
    a,b = 0,0
    for i in nums:
        if (i & mask_of_rmb ==0):
            a = a^i
        else:
            b = b^i
    arr=[]
    arr.extend([a,b])
    return arr


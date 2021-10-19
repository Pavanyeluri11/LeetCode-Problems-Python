def sortByBits(arr):
    count_arr=[]
    for i in arr:
        count=0
        while i:
            count+=i%2
            i= i//2
        count_arr.append(count)
    mapping = zip(arr,count_arr)
    mapping.sort(key=lambda x: (x[1],x[0]))
    #rint(mapping)
    for i in range(len(arr)):
        arr[i] = mapping[i][0]
    return arr

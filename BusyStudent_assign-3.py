def busyStudent(startTime, endTime, queryTime):
    count = 0
    for i in range(len(startTime)):
        if(startTime[i] <= queryTime <= endTime[i]):
            count+=1
    return count
    
print(busyStudent([1,2,3],[4,5,6],3))

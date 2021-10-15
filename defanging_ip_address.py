def defanging(address):
    s=''
    for i in range(len(address)):
        if address[i] == '.':
            s+='[.]'
        else:
            s+=address[i]
    del address  
    return s

print(defanging('1.1.1.1'))

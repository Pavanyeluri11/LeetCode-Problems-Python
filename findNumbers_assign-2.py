def findNumbers(nums):
        
    str_list = list( map( str, nums) )
    list_even_num_of_digits =  list( filter( lambda x: (len(x)%2==0),  str_list) )
    return len( list_even_num_of_digits )

print(findNumbers([12,345,2,6,7896]))

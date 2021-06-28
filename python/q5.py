def is_consecutive(a_list):
    consecutive_numbers=list(range(min(a_list),max(a_list)+1))
    if consecutive_numbers == a_list:
        return print('True')
    else:
        return print('False')
is_consecutive([1,2,3,4])
is_consecutive([3,8,9,10])
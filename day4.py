# write a fuction that taked two string , and returns a message saying how many
# time the second string appeared in the first string and in what locations

# Example
# input : big_string = 'hello world and hello world again!'
# Output : Number of times 'hello world' appear in 'hellow world and hello world again!' is : 2


def my_fact(n):
    if ( n == 1) | ( n == 0):
        return 1
    else:
        return n * my_fact(n -1)

def my_sum(n):
    if ( n== 1 ) | ( n == 0):
     return 1
    else:
     return n + my_sum(n-1)


def get_all_sub_recursive(big_string, small_string):
    '''return the indices of small_string occurance in big_string'''
    return

def smallest_in_list( list_in ):
    smallest_out = list_in[0]
    for i in list_in:
        if i < smallest_out:
            smallest_out = i

    return smallest_out

# Exercise to Remove the Duplicates from list

def rem_duplicates( list_in ):
    # Remove duplicates
    # Example list_in = [1,3,6,3,1,4,5]
    # retrun  list_out = [1,2,4,6,5]

    # set1 = set ( list_in )
    # set1

    new_list = []
    for l in list_in:
        if l not in new_list:
            new_list.append(l)
    return new_list

# Exercise , give a dict d1 create a new dict d2
#   such that d2 maps every value in d1 to its correspoding Key
#   and if an value in d1 appear under more than on diffrent key,
#   them d2 will map the value to list , containing each of its corresponding keys

# d1 = {'key1':3 , 'key2':5 , 'key3':3 , 'key4': 8}
# then the output should be :
# d2 = {3: ['key1', 'key3'], 5:['key2'], 8: ['key4']}

def flip_dict( dict_in ):

    new_dict = {}
    for i in dict_in.items():
        if i[1] in new_dict.keys():
            new_dict[ i[1] ].append( i[0])
        else:
            new_dict [ i[1] ] = [ i[0] ]

    return new_dict


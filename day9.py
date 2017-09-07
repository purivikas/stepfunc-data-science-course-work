import csv

# File Handler fh

def my_copy(file_1, file_2):

    '''copies content of file1 into file2'''

    fh1 = open(file_1,'r')
    fh2 = open(file_2,'w')

    fh2.write(fh1.read())

    fh1.close()
    fh2.close()
    return

def my_copy_lines(linetext):
    fh = open('lined_file','w')
    fh.writelines(linetext)
    return

# CSV file

def read_csv(csv_file_in, seperator):
    '''Read the CSV file into of the list, where every nnner list contain a row fro the csv file , and the item '''

    fh = open(csv_file_in,'r')

    new_list = []
    for linetext in fh.readlines():
        new_list.append(linetext.split(seperator))
    return new_list

# CSV inport CSV class
# import csv

def csv_reader():
    with open('my_file_csv', 'r') as csvfile:
        my_csv = csv.reader(csvfile, delimiter=';')
        print(list(my_csv))
    return

def csv_writer():
    list_ = ['spam' , 'spam2', 'spam3']
    with open('my_file_csv3', 'w') as csvfile:
        my_csv_writer = csv.writer(csvfile, delimiter=' ' , quotechar='|')
        my_csv_writer.writerow(list_)
        my_csv_writer.writerow(['line2', 'line2 agian', 'line2 again again'])
    return



#import itertools
#list_ = [1,2,3,4,5]
#list2 = [1,2,3]

# list(itertools.combinations(list_,5))
# list(itertools.permutations(list_))
# list(itertools.permutations(list_))
#
# list(itertools.permutations(list_))



import random
import itertools

def gen_millions_selection():
    # Function that generate - randomly - everytime you call it a correct euro million draw,
    # to use for your next lottery ticket
    # lotto rules pick 5 numbers from 1 to 50 , and two more from 1 to 12

    my_lotto_selection = []
    first_five  = np.random.randint(1,50 , size=(5))
    second_two = np.random.randint(1,12 , size=(2))

    my_lotto_selection.append(first_five)
    my_lotto_selection.append(second_two)

    return my_lotto_selection



# Out[162]: [array([23, 30, 41, 22, 33]), array([10,  3])]
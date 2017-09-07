# Functional Programming
# Hadoop  -  FaaS

my_nums = range(100)

my_new_num = []

for i in my_nums:
    my_new_num.append( (i+1)*(i+1))

my_new_num = [ (i+1)*(i+1)  for i in my_nums ]

def weired_sqr(n):
    return (n+1)*(n+1)

my_new_num = [weired_sqr(m) for m in my_nums if (weired_sqr(m) % 2 == 0) and (weired_sqr(m) %3 == 0)]

student_jobs = [('ahmed','teacher') , ('ben','hacker') ,('tom','trader'),('vikas','trader'),('alex','trader')]
concise_jobs = [(u[0],v[:3]) for (u,v) in student_jobs]



my_string = 'quick brown fox jumps over the lazy dog.'
''' Return a list conatining for every'''

new_string = [ ( i.upper() ,len(i),i[-1]) for i in my_string.split()  if i[1] != 'r' and i[1] != 'o']

new_string = [ ( i.upper() ,len(i),i[-1]) for i in my_string.split()  if ( 'r' not in i)  and ('o' not in i)]


# Map Reduce Filter -
# Mapping value to function ...

def weired_sqr(n):
    return (n+1)*(n+1)

list( map(weired_sqr,range(10)))

# Cons - first has to def function

# annonmous

list ( map( lambda x: (x+1)*(x+1), [1,2,3,4,5] ))

list ( map( lambda x: (x.upper(),len(x),x[-1]), 'quick brown fox jumps over the lazy dog'.split() ))

list ( map( lambda x: (x,x+1), [1,2,3,4,5] ))

list ( map( lambda x: (x,x+1), range(10) ))

def my_criteria(n):
    if ( n % 2 == 0 ) and ( n % 3 == 0):
        return True
    return False

list(filter(my_criteria,range(0,100)))

my_str = 'quick brown fox jumps over the lazy dog'

list ( map( lambda x: (x.upper(),len(x),x[-1]),
            filter( lambda x: ((x[1] != 'r' ) and (x[1] != 'o')),
            'quick brown fox jumps over the lazy dog'.split()) ))

# Reduce Function
from functools import reduce

import functools

reduce( lambda x,y: x*y ,range (1,20))


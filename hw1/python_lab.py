# version code ef5291f09f60+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

## 1: (Task 1) Minutes in a Week
minutes_in_week = 60*24*7

## 2: (Task 2) Remainder
#For this task, your expression must use //
remainder_without_mod = int(47 * ((2304811 / 47 ) - 2304811 // 47))

## 3: (Task 3) Divisibility
divisible_by_3 = (((673 + 909) // 3) == 0)

## 4: (Task 4) Conditional Expression
x = -9
y = 1/2
expression_val = 2**(y+1/2) if x+10<0 else 2**(y-1/2)

## 5: (Task 5) Squares Set Comprehension
first_five_squares = { x*x for x in {1,2,3,4,5} }

## 6: (Task 6) Powers-of-2 Set Comprehension
first_five_pows_two = { 2**y for y in {0,1,2,3,4} }

## 7: (Task 7) Double comprehension evaluating to nine-element set
# Assign three-element sets to X1 and Y1 so that
# {x*y for x in X1 for y in Y1} evaluates to a nine-element set.

X1 = { 1, 2, 3 }
Y1 = { 7, 13, 17 }
{x*y for x in X1 for y in Y1 if x != y }


## 8: (Task 8) Double comprehension evaluating to five-element set
# Assign disjoint three-element sets to X1 and Y1 so that
# {x*y for x in X1 for y in Y1} evaluates to a five-element set.

X2 = { 2, 6, 18 }
Y2 = { 1, 3, 9 }
{x*y for x in X2 for y in Y2 if x + y < 28 }


## 9: (Task 9) Set intersection as a comprehension
S = {1, 2, 3, 4}
T = {3, 4, 5, 6}
# Replace { ... } with a one-line set comprehension that evaluates to the intersection of S and T
S_intersect_T = {x for x in S for y in T if x == y }



## 10: (Task 10) Average
list_of_numbers = [20, 10, 15, 75]
# Replace ... with a one-line expression that evaluates to the average of list_of_numbers.
# Your expression should refer to the variable list_of_numbers, and should work
# for a list of any length greater than zero.
list_average = sum(list_of_numbers)/len(list_of_numbers)

## 11: (Task 11) Cartesian-product comprehension
# Replace ... with a double list comprehension over ['A','B','C'] and [1,2,3]
cartesian_product = { (x,y) for x in ['A','B','C'] for y in [1,2,3]}

## 12: (Task 12) Sum of numbers in list of list of numbers
LofL = [[.25, .75, .1], [-1, 0], [4, 4, 4, 4]]
# Replace ... with a one-line expression of the form sum([sum(...) ... ]) that
# includes a comprehension and evaluates to the sum of all numbers in all the lists.
LofL_sum = sum({sum(LofL[x]) for x in [1, 2, 0 ]})

## 13: (Task 13) Three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
zero_sum_list = [ (i,j,k) for i in list(S) for j in list(S) for k in list(S) if (i+j+k) == 0 ]

## 14: (Task 14) Nontrivial three-element tuples summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace [ ... ] with a one-line list comprehension in which S appears
exclude_zero_list = [ (i,j,k) for i in list(S) for j in list(S) for k in list(S) if (i+j+k) == 0 ][1:]


## 15: (Task 15) One nontrivial three-element tuple summing to zero
S = {-4, -2, 1, 2, 5, 0}
# Replace ... with a one-line expression that uses a list comprehension in which S appears
first_of_tuples_list = [ (i,j,k) for i in list(S) for j in list(S) for k in list(S) if (i+j+k) == 0 ][0]

## 16: (Task 16) List and set differ
# Assign to example_L a list such that len(example_L) != len(list(set(example_L)))
# For this simply realize that sets enforce unique elements while lists do not.
example_L = [ 1, 2, 2]

## 17: (Task 17) Odd numbers
# Replace {...} with a one-line set comprehension over a range of the 
# form range(n) that emits odd numbers.
odd_num_list_range = {i for i in range(1,100,2)}

## 18: (Task 18) Using range and zip
# In the line below, replace ... with an expression that does not include a comprehension.
# Instead, it should use zip and range.
# Note: zip() does not return a list. It returns an 'iterator of tuples'
L = ['A','B','C','D','E']
range_and_zip = list(zip(range(len(L)),L))

## 19: (Task 19) Using zip to find elementwise sums
A = [10, 25, 40]
B = [1, 15, 20]
# Replace [...] with a one-line comprehension that uses zip together with the variables A and B.
# The comprehension should evaluate to a list whose ith element is the ith element of
# A plus the ith element of B.
list_sum_zip = [sum(i) for i in list(zip(A,B))]

## 20: (Task 20) Extracting the value corresponding to key k from each dictionary in a list
# Replace [...] with a one-line comprehension that uses dlist and k
# and that evaluates to ['Sean','Roger','Pierce']
#
# I misread the next task, thus this and #21 are identical.
dlist = [{'James':'Sean', 'director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce', 'director':'Roger'}]
k = 'James'
value_list = list({ dlist[i].get(k,'NOT PRESENT') for i in range(len(dlist))})

## 21: (Task 21) Extracting the value corresponding to k when it exists
dlist = [{'Bilbo':'Ian','Frodo':'Elijah'},{'Bilbo':'Martin','Thorin':'Richard'}]
k = 'Bilbo'
#Replace [...] with a one-line comprehension 
value_list_modified_1 = list({ dlist[i].get(k,'NOT PRESENT') for i in range(len(dlist))})
k = 'Frodo'
# value_list_modified_2 = [...] # <-- as you do here
value_list_modified_2 = list({ dlist[i].get(k,'NOT PRESENT') for i in range(len(dlist))})

## 22: (Task 22) A dictionary mapping integers to their squares
# Replace {...} with a one-line dictionary comprehension that 
# outputs the squares of the numbers 0 through 99
square_dict = { (i):i*i for i in range(0,100) }

## 23: (Task 23) Making the identity function
D = {'red','white','blue'}
# Replace {...} with a one-line dictionary comprehension.  This seemed like
# it should precede the previous problem.
identity_dict = {(i):i for i in D}

## 24: (Task 24) Mapping integers to their representation over a given base
base = 10
digits = set(range(base))
# Replace { ... } with a one-line dictionary comprehension
# Your comprehension should use the variables 'base' and 'digits' so it will work correctly if these
# are assigned different values (e.g. base = 2 and digits = {0,1})
representation_dict = { (j*base*base+k*base+l):(j,k,l) for j in digits for k in digits for l in digits}

## 25: (Task 25) A dictionary mapping names to salaries
id2salary = {0:1000.0, 1:1200.50, 2:990}
names = ['Larry', 'Curly', 'Moe']
# Replace { ... } with a one-line dictionary comprehension that uses id2salary and names.
listdict2dict = {(names[i]):id2salary.get(i) for i in id2salary.keys()}

## 26: (Task 26) Procedure nextInts
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def nextInts(L): return list(L[i]+1 for i in range(len(L)))


## 27: (Task 27) Procedure cubes
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
def cubes(L): return list(L[i]**3 for i in range(len(L)))


## 28: (Task 28) Procedure dict2list
# Input: a dictionary dct and a list keylist consisting of the keys of dct
# Output: the list L such that L[i] is the value associated in dct with keylist[i]
# Example: dict2list({'a':'A', 'b':'B', 'c':'C'},['b','c','a']) should equal ['B','C','A']
# Complete the procedure definition by replacing [ ... ] with a one-line list comprehension
#
# The challenge on this one was enforcing the order.
#

keylist = ['b','c','a']
dct = {'a':'A', 'b':'B', 'c':'C'}

def dict2list(dct, keylist): return [ dct[keylist[i]] for i in range(len(keylist)) ]
# print(dict2list(dct,keylist))


## 29: (Task 29) Procedure list2dict
# Input: a list L and a list keylist of the same length
# Output: the dictionary that maps keylist[i] to L[i] for i=0,1,...len(L)-1
# Example: list2dict(['A','B','C'],['a','b','c']) should equal {'a':'A', 'b':'B', 'c':'C'}
# Complete the procedure definition by replacing { ... } with a one-line dictionary comprehension
def list2dict(L, keylist): return { (keylist[i]):L[i] for i in range(len(L))}

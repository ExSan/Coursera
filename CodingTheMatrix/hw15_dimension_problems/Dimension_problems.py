# version code dc33ceea27bf+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

from GF2 import one
from independence import rank, is_independent
from mat import Mat
from matutil import listlist2mat, coldict2mat, mat2rowdict, mat2coldict
from solver import solve
from vec import Vec
from The_Basis_problems import *
from vecutil import list2vec
from triangular import triangular_solve
# from foomor import foomorph 


## 1: (Problem 1) Iterative Exchange Lemma
w0 = list2vec([1, 0, 0])
w1 = list2vec([0, 1, 0])
w2 = list2vec([0, 0, 1])

v0 = list2vec([1, 2, 3])
v1 = list2vec([1, 3, 3])
v2 = list2vec([0, 3, 3])

# Fill in exchange_S1 and exchange_S2  IN each, one vector of W is injected and one of V is ejected
# with appropriate lists of 3 vectors

exchange_S0 = [w0, w1, w2]
exchange_S1 = [w0, v1, w2]
exchange_S2 = [v0, v1, w2]
exchange_S3 = [v0, v1, v2]

## 2: (Problem 2) Another Iterative Exchange Lemma
w0 = list2vec([  0, one,   0])
w1 = list2vec([  0,   0, one])
w2 = list2vec([one, one, one])

v0 = list2vec([one,   0, one])
v1 = list2vec([one,   0,   0])
v2 = list2vec([one, one,   0])

exchange_2_S0 = [w0, w1, w2]
exchange_2_S1 = [v0, w1, w2]
exchange_2_S2 = [v0, v1, w2]
exchange_2_S3 = [v0, v1, v2]

# 3: (Problem 3) Morph Lemma Coding
#
# There is a disconnect with this in the inputs are lists but the other routines you'd use
# from last week's homework assume sets.
#

def morph(S, B):
    '''
    Input:
        - S: a list of distinct Vecs
        - B: a list of linearly independent Vecs all in Span S
    Output: a list of pairs of vectors to inject and eject (see problem description)
    Example:
        >>> # This is how our morph works.  Yours may yield different results.
        >>> # Note: Make a copy of S to modify instead of modifying S itself.
        >>> S = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
        >>> B = [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
        >>> morph(S, B)
        [(Vec({0, 1, 2},{0: 1, 1: 1, 2: 0}), Vec({0, 1, 2},{0: 1, 1: 0, 2: 0})), (Vec({0, 1, 2},{0: 0, 1: 1, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 1, 2: 0})), (Vec({0, 1, 2},{0: 1, 1: 0, 2: 1}), Vec({0, 1, 2},{0: 0, 1: 0, 2: 1}))]
        >>> S == [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
        True
        >>> B == [list2vec(v) for v in [[1,1,0],[0,1,1],[1,0,1]]]
        True
        >>> from vec import Vec
        >>> from mat import Mat
        >>> from GF2 import one
        >>> from solver import solve
        >>> M1 = Mat(({0, 1, 2, 3, 4, 5, 6, 7}, {0, 1, 2, 3, 4}), {(1, 2): one, (3, 2): one, (0, 0): 0, (4, 3): one, (7, 1): 0, (3, 0): one, (7, 3): 0, (0, 4): 0, (6, 0): 0, (2, 1): 0, (6, 2): one, (2, 3): 0, (1, 4): 0, (5, 1): 0, (5, 4): one, (4, 2): 0, (1, 0): one, (0, 3): 0, (7, 2): 0, (4, 0): one, (0, 1): 0, (7, 4): 0, (2, 4): 0, (7, 0): 0, (3, 3): one, (5, 2): one, (6, 1): 0, (3, 1): one, (3, 4): one, (4, 4): 0, (1, 1): one, (6, 3): 0, (2, 0): one, (5, 0): 0, (2, 2): 0, (1, 3): 0, (6, 4): one, (5, 3): 0, (4, 1): 0, (0, 2): one})
        >>> B = [Vec({0, 1, 2, 3, 4, 5, 6, 7},{2: one, 4: one})]
        >>> ans = solve(M1,B[0])
        >>> ans==Vec({0, 1, 2, 3, 4},{0: one, 1: one})
        True
        >>> M1 * ans == B[0]
        True
        >>> from GF2 import one
        >>> B = [Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 3: one, 5: one, 19: one, 8: one, 9: one, 10: one, 12: one, 15: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 2: one, 3: one, 4: one, 8: one, 9: one, 10: one, 11: one, 12: one, 13: one, 14: one, 16: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 5: one, 6: one, 7: one, 8: one, 11: one, 13: one, 14: one, 15: one, 16: one, 17: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 2: one, 5: one, 6: one, 7: one, 9: one, 10: one, 11: one, 12: one, 18: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 2: one, 19: one, 4: one, 6: one, 8: one, 9: one, 10: one, 13: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{1: one, 3: one, 4: one, 5: one, 9: one, 10: one, 11: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 1: one, 18: one, 3: one, 4: one, 5: one, 17: one, 7: one, 10: one, 12: one, 13: one})]
        >>> S=[Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 1: one, 2: one, 19: one, 4: one, 5: one, 11: one, 13: one, 14: one, 15: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 2: one, 8: one, 9: one, 10: one, 12: one, 13: one, 15: one, 17: one, 18: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 17: one, 4: one, 6: one, 8: one, 9: one, 10: one, 12: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 17: one, 18: one, 7: one, 9: one, 11: one, 12: one, 13: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 2: one, 3: one, 5: one, 6: one, 7: one, 8: one, 10: one, 11: one, 12: one, 13: one, 17: one, 18: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{19: one, 17: one, 3: one, 4: one, 6: one, 7: one, 8: one, 9: one, 10: one, 13: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 19: one, 2: one, 3: one, 5: one, 6: one, 8: one, 11: one, 13: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 3: one, 4: one, 5: one, 6: one, 17: one, 16: one, 19: one, 15: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 4: one, 5: one, 7: one, 8: one, 11: one, 12: one, 13: one, 16: one, 18: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{1: one, 2: one, 3: one, 4: one, 5: one, 6: one, 7: one, 9: one, 10: one, 12: one, 15: one, 17: one, 19: one})]
        >>> ans2 = morph(S,B)
        >>> ans[1] == (B[1],S[0])
        True
        B[1],S[0]
    '''
    eject_order = []
    Sprime = S.copy()
    Sleft = S.copy() # What's left to eject that we haven't done already?
    for b in B:
      Sprime.append(b) # inject B
      for s in Sleft: # now scan through S and look for something to remove.
         if is_superfluous(Sprime, s):
            eject_order.append((b,s))
            Sleft.remove(s) # remove it from future consideration
            break # next B[i]!
    return eject_order



## 4: (Problem 4) Row and Column Rank Practice
# Please express each solution as a list of Vecs

row_space_1 = [Vec({0, 1, 2}, {0:1 ,1:2, 2:0}), Vec({0, 1, 2}, {0:0, 1:2, 2:1})]
col_space_1 = [Vec({0, 1}, {0:1, 1:0}), Vec({0, 1}, {0:2, 1:2})]

row_space_2 = [Vec({0, 1, 2, 3}, {0:1, 1:4, 2:0, 3:0}), Vec({0, 1, 2, 3}, {0:0, 1:2, 2:2, 3:0}), Vec({0, 1, 2, 3}, {0:0, 1:0, 2:1, 3:1})]
col_space_2 = [Vec({0, 1, 2}, {0:1, 1:0, 2:0}), Vec({0, 1, 2}, {0:4, 1:2, 2:0}), Vec({0, 1, 2}, {0:0, 1:2, 2:1})]

row_space_3 = [Vec({0}, {0:1})] 
col_space_3 = [Vec({0, 1, 2}, {0:1, 1:2, 2:3})]

row_space_4 = [Vec({0, 1}, {0:2, 1:1}), Vec({0, 1}, {0:3, 1:4})]
col_space_4 = [Vec({0, 1, 2}, {0:1, 1:2, 2:3}), Vec({0, 1, 2}, {0:0, 1:1, 2:4})]

## 5: (Problem 5) Subset Basis
def subset_basis(T):
    '''
    Input:
        - T: a set of Vecs
    Output: 
        - set S containing Vecs from T that is a basis for Span T.
    Examples:
        The following tests use the procedure is_independent, provided in module independence
        
        >>> from vec import Vec
        >>> from independence import is_independent
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> sb = subset_basis({a0, a1, a2, a3})
        >>> len(sb)
        3
        >>> all(v in [a0, a1, a2, a3] for v in sb)
        True
        >>> is_independent(sb)
        True

        >>> b0 = Vec({0,1,2,3},{0:2,1:2,3:4})
        >>> b1 = Vec({0,1,2,3},{0:1,1:1})
        >>> b2 = Vec({0,1,2,3},{2:3,3:4})
        >>> b3 = Vec({0,1,2,3},{3:3})
        >>> sb = subset_basis({b0, b1, b2, b3})
        >>> len(sb)
        3
        >>> all(v in [b0, b1, b2, b3] for v in sb)
        True
        >>> is_independent(sb)
        True
        >>> D = {'a','b','c','d'}
        >>> c0, c1, c2, c3, c4 = Vec(D,{'d': one, 'c': one}), Vec(D,{'d': one, 'a': one, 'c': one, 'b': one}), Vec(D,{'a': one}), Vec(D,{}), Vec(D,{'d': one, 'a': one, 'b': one})
        >>> subset_basis({c0,c1,c2,c3,c4}) == {c0,c1,c2,c4}
        True
    '''
    S = set()
    for i in T:
       S.add(i)
       if not(is_independent(S)):
          S.discard(i)
    return S


## 6: (Problem 6) Superset Basis Lemma in Python
def superset_basis(C, T):
    '''
    Input:
        - C: linearly independent set of Vecs
        - T: set of Vecs such that every Vec in S is in Span(T)
    Output:
        Linearly independent set S consisting of all Vecs in C and some in T
        such that the span of S is the span of T (i.e. S is a basis for the span
        of T).
    Example:
        >>> from vec import Vec
        >>> from independence import is_independent
        >>> a0 = Vec({'a','b','c','d'}, {'a':1})
        >>> a1 = Vec({'a','b','c','d'}, {'b':1})
        >>> a2 = Vec({'a','b','c','d'}, {'c':1})
        >>> a3 = Vec({'a','b','c','d'}, {'a':1,'c':3})
        >>> sb = superset_basis({a0, a3}, {a0, a1, a2})
        >>> a0 in sb and a3 in sb
        True
        >>> all(x in [a0,a1,a2,a3] for x in sb)
        True
    '''
    tmp = C.copy()
    for v in T:
        tmp.add(v)
        if is_superfluous(tmp, v):
            tmp.discard(v)
    return tmp



## 7: (Problem 7) My Is Independent Procedure
def my_is_independent(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - boolean: true if the list is linearly independent
    Examples:
        >>> D = {0, 1, 2}
        >>> L = [Vec(D,{0: 1}), Vec(D,{1: 1}), Vec(D,{2: 1}), Vec(D,{0: 1, 1: 1, 2: 1}), Vec(D,{0: 1, 1: 1}), Vec(D,{1: 1, 2: 1})]
        >>> my_is_independent(L)
        False
        >>> my_is_independent(L[:2])
        True
        >>> my_is_independent(L[:3])
        True
        >>> my_is_independent(L[1:4])
        True
        >>> my_is_independent(L[0:4])
        False
        >>> my_is_independent(L[2:])
        False
        >>> my_is_independent(L[2:5])
        False
        >>> L == [Vec(D,{0: 1}), Vec(D,{1: 1}), Vec(D,{2: 1}), Vec(D,{0: 1, 1: 1, 2: 1}), Vec(D,{0: 1, 1: 1}), Vec(D,{1: 1, 2: 1})]
        True
    '''
    return len(L) == rank(L)



## 8: (Problem 8) My Rank
def my_rank(L):
    '''
    Input: 
        - L: a list of Vecs
    Output: 
        - the rank of the list of Vecs
    Example:
        >>> L = [list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]]
        >>> my_rank(L)
        2
        >>> L == [list2vec(v) for v in [[1,2,3],[4,5,6],[1.1,1.1,1.1]]]
        True
        >>> my_rank([list2vec(v) for v in [[1,1,1],[2,2,2],[3,3,3],[4,4,4],[123,432,123]]])
        2
    '''
    return len(subset_basis(L))



## 9: (Problem 9) Direct Sum Unique Representation
def direct_sum_decompose(U_basis, V_basis, w):
    '''
    Input:
        - U_basis: a list of Vecs forming a basis for a vector space U
        - V_basis: a list of Vecs forming a basis for a vector space V
        - w: a Vec in the direct sum of U and V
    Output:
        - a pair (u, v) such that u + v = w, u is in U, v is in V
    Example:
        >>> U_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 1, 2: 0, 3: 0, 4: 6, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 11, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0}), Vec({0, 1, 2, 3, 4, 5},{0: 3, 1: 1.5, 2: 0, 3: 0, 4: 7.5, 5: 0})]
        >>> V_basis = [Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 7, 3: 0, 4: 0, 5: 1}), Vec({0, 1, 2, 3, 4, 5},{0: 0, 1: 0, 2: 15, 3: 0, 4: 0, 5: 2})]
        >>> w = Vec({0, 1, 2, 3, 4, 5},{0: 2, 1: 5, 2: 0, 3: 0, 4: 1, 5: 0})
        >>> (u, v) = direct_sum_decompose(U_basis, V_basis, w)
        >>> (u + v - w).is_almost_zero()
        True
        >>> U_matrix = coldict2mat(U_basis)
        >>> V_matrix = coldict2mat(V_basis)
        >>> (u - U_matrix*solve(U_matrix, u)).is_almost_zero()
        True
        >>> (v - V_matrix*solve(V_matrix, v)).is_almost_zero()
        True
    '''
    W = solve(coldict2mat(U_basis + V_basis), w)
    Wu = Vec(set(range(len(U_basis))), { i : W[i] for i in range(len(U_basis))})
    Wv = Vec(set(range(len(V_basis))), { i : W[i + len(U_basis)] for i in range(len(V_basis))})
    return( coldict2mat(U_basis) * Wu, coldict2mat(V_basis) * Wv)


## 10: (Problem 10) Is Invertible Function
def is_invertible(M):
    '''
    input: A matrix, M
    outpit: A boolean indicating if M is invertible.

    >>> M = Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): 0, (1, 2): 1, (3, 2): 0, (0, 0): 1, (3, 3): 4, (3, 0): 0, (3, 1): 0, (1, 1): 2, (2, 1): 0, (0, 2): 1, (2, 0): 0, (1, 3): 0, (2, 3): 1, (2, 2): 3, (1, 0): 0, (0, 3): 0})
    >>> is_invertible(M)
    True

    >>> M1 = Mat(({0,1,2},{0,1,2}),{(0,0):1,(0,2):2,(1,2):3,(2,2):4})
    >>> is_invertible(M1)
    False
    '''
    Rows=[]
    Cols=[]
    for k,v in mat2rowdict(M).items():
        Rows.append(v)
    for k,v in mat2coldict(M).items():
        Cols.append(v)
    return (rank(Rows) == rank(Cols) and my_is_independent(Rows) and my_is_independent(Cols))


## 11: (Problem 11) Inverse of a Matrix over GF(2)
def find_matrix_inverse(A):
    '''
    Input:
        - A: an invertible Mat over GF(2)
    Output:
        - A Mat that is the inverse of A
    Examples:
        >>> M1 = Mat(({0,1,2}, {0,1,2}), {(0, 1): one, (1, 0): one, (2, 2): one})
        >>> find_matrix_inverse(M1) == Mat(M1.D, {(0, 1): one, (1, 0): one, (2, 2): one})
        True
        >>> M2 = Mat(({0,1,2,3},{0,1,2,3}),{(0,1):one,(1,0):one,(2,2):one})
        >>> find_matrix_inverse(M2) == Mat(M2.D, {(0, 1): one, (1, 0): one, (2, 2): one})
        True
    '''
    return coldict2mat([solve(A, Vec(A.D[0], {i: one})) for i in A.D[0]])


## 12: (Problem 12) Inverse of a Triangular Matrix
def find_triangular_matrix_inverse(A):
    '''
    Supporting GF2 is not required.

    Input: - A: an upper triangular Mat with nonzero diagonal elements
    Output: - Mat that is the inverse of A
    Example:
        >>> A = listlist2mat([[1, .5, .2, 4],[0, 1, .3, .9],[0,0,1,.1],[0,0,0,1]])
        >>> find_triangular_matrix_inverse(A) == Mat(({0, 1, 2, 3}, {0, 1, 2, 3}), {(0, 1): -0.5, (1, 2): -0.3, (3, 2): 0.0, (0, 0): 1.0, (3, 3): 1.0, (3, 0): 0.0, (3, 1): 0.0, (2, 1): 0.0, (0, 2): -0.05000000000000002, (2, 0): 0.0, (1, 3): -0.87, (2, 3): -0.1, (2, 2): 1.0, (1, 0): 0.0, (0, 3): -3.545, (1, 1): 1.0})
        True
    '''
    rowdict = mat2rowdict(A)
    return coldict2mat([triangular_solve([rowvalue for rowvalue in rowdict.values()], [k for k in rowdict.keys()], Vec(A.D[0], {i: 1})) for i in A.D[0]])



# S = [list2vec(v) for v in [[2,4,0],[1,0,3],[0,4,4],[1,1,1]]]
# B = [list2vec(v) for v in [[1,0,0],[0,1,0],[0,0,1]]]
# for (z,w) in morph(S,B):
#    print("injecting ",z)
#    print("ejecting ",w)
#    print()

B = [Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 3: one, 5: one, 19: one, 8: one, 9: one, 10: one, 12: one, 15: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 2: one, 3: one, 4: one, 8: one, 9: one, 10: one, 11: one, 12: one, 13: one, 14: one, 16: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 5: one, 6: one, 7: one, 8: one, 11: one, 13: one, 14: one, 15: one, 16: one, 17: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 2: one, 5: one, 6: one, 7: one, 9: one, 10: one, 11: one, 12: one, 18: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 2: one, 19: one, 4: one, 6: one, 8: one, 9: one, 10: one, 13: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{1: one, 3: one, 4: one, 5: one, 9: one, 10: one, 11: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 1: one, 18: one, 3: one, 4: one, 5: one, 17: one, 7: one, 10: one, 12: one, 13: one})]
S=[Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 1: one, 2: one, 19: one, 4: one, 5: one, 11: one, 13: one, 14: one, 15: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 2: one, 8: one, 9: one, 10: one, 12: one, 13: one, 15: one, 17: one, 18: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 17: one, 4: one, 6: one, 8: one, 9: one, 10: one, 12: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{16: one, 17: one, 18: one, 7: one, 9: one, 11: one, 12: one, 13: one, 14: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 2: one, 3: one, 5: one, 6: one, 7: one, 8: one, 10: one, 11: one, 12: one, 13: one, 17: one, 18: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{19: one, 17: one, 3: one, 4: one, 6: one, 7: one, 8: one, 9: one, 10: one, 13: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 19: one, 2: one, 3: one, 5: one, 6: one, 8: one, 11: one, 13: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 3: one, 4: one, 5: one, 6: one, 17: one, 16: one, 19: one, 15: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{0: one, 1: one, 4: one, 5: one, 7: one, 8: one, 11: one, 12: one, 13: one, 16: one, 18: one, 19: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19},{1: one, 2: one, 3: one, 4: one, 5: one, 6: one, 7: one, 9: one, 10: one, 12: one, 15: one, 17: one, 19: one})]
i = 0
for (z,w) in morph(S,B):
   for k in range(len(S)):
      if S[k] == w:
         print("injectiong ",i,"ejecting ",k)
         break
   i = i + 1

#S = [ Vec({0, 1, 2, 3, 4, 5, 6, 7},{1: one, 2: one, 3: one, 4: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{1: one, 3: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{0: one, 1: one, 3: one, 5: one, 6: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{3: one, 4: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{3: one, 5: one, 6: one}) ]
#B = [ Vec({0, 1, 2, 3, 4, 5, 6, 7},{2: one, 4: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{0: one, 1: one, 2: one, 3: one, 4: one, 5: one, 6: one}), Vec({0, 1, 2, 3, 4, 5, 6, 7},{0: one, 1: one, 2: one, 5: one, 6: one}) ]
#for (z,w) in morph(S,B):
#   print("injecting ",z)
#   print("ejecting ",w)
#   print()

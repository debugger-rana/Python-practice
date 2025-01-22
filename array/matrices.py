# from numpy import *
# m=matrix('1 2 3 ; 4 5 6 ; 7 8 9 ; 10 11 12')
# # print(m , "\n")
# m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9 ; 10 11 12')
# # print(m1,'\n')

# # what if you want to print just the diagonal elements of the matrix
# # print(diagonal(m), '\n')
# # print(diagonal(m1))

# # what if you want to add two matrix
# print(m+m1)
# m3=dot(m,m1)


from numpy import *
m = matrix('1 2 3 ; 4 5 6 ; 7 8 9 ; 10 11 12')
m1 = matrix('1 2 3 ; 4 5 6 ; 7 8 9 ; 10 11 12')

# Multiply matrix m with the transpose of m1
m3 = m * m1.T

print(m3)

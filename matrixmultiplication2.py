import numpy
r1 = [1,2,3]
r2 = [4,5,6]
r3 = [7,8,9]

s1 = [1,2,1]
s2 = [6,2,3]
s3 = [4,2,1]

A = []
B = []
A.append(r1)
A.append(r2)
A.append(r3)

B.append(s1)
B.append(s2)
B.append(s3)

x = numpy.mat(A)
y = numpy.mat(B)
product = x*y
print(product)

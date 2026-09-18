import numpy as np
A = np.array([1,2,3])

#printing the elements in A

for i in A:
     print(i)

#broadcasting in the array

print(A + np.array([2]))

#vector addition through array\

print(A + np.array([2,3,4]))

# applying various functions and operators to an array
print(2 * A)

print(2**A)

print(np.sqrt(A))

print(np.exp(A))

print(np.log(A))

print(np.tanh(A))
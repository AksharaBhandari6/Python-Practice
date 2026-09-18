import numpy as np

#seven methods to do dot product

a = np.array([1,2])
b = np.array([3,4])
#1
dot = 0
for e,f in zip(a,b):
    dot += (e * f)
print(dot)

#2
dot = 0
for i in range(len(a)):
    dot += a[i] * b[i]
print(dot)

#3
print((a*b).sum())

#4
print(a.dot(b))

#5
print(a @ b)

#6
print(np.sum(a*b))

#7
np.dot(a,b)

#to find the magnitude of vector or we may call it the norm of the vector

a_mag = np.sqrt(a@a)
print(a_mag)

b_mag = np.sqrt(b@b)
print(b_mag)

print( np.linalg.norm(a), np.linalg.norm(b))

#to find the value of cosine
cos_val = (a@b) / (a_mag * b_mag)
print(cos_val)

angle = np.arccos(cos_val)
print(angle)#radians
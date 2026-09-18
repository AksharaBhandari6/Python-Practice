import numpy as np
from datetime import datetime
#lists matricies
L1 = [[1,2,3],[4,5,6],[7,8,9]]
L2 = [[1,2,3],[4,5,6],[7,8,9]]
L3 = [[],[],[]]
#array matricies
a = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])

b = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])


t0 = datetime.now()
for r1 in range(len(L1)):
    c2 = 0
    for z in range(3):
        sums = 0
        for c1 in range(len(L1[r1])):
            a = L1[r1][c1] * L2[c1][c2]
            sums += a
        L3[r1].append(sums)
        c2 += 1
    L3.append(L3[r1])
dt1 = datetime.now() - t0


t0 = datetime.now()
c = np.dot(a,b)
dt2 = datetime.now() - t0


print("dt1 / dt2: ", dt1.total_seconds()/dt2.total_seconds())




# total_rep = 0
# while True:
#     total_rep += reps
    
#     for m in (L1): 

#         row = m.index()
        
#         column = 0
#         sum = 0
#         for i in range(len(m)):
            
#             #if row < 2:
#             c = L1[row][i] * L2[row][column]
#             sum += c
#             # else:
#             #     L3[m].append(sum)
#             column += 1
#             reps += 1
#         L3[row].append(sum)
#         # z -= 1
#         if total_rep != 9 :
#            total_rep = 0
#            break
#    # z-'
    
# print(L3)
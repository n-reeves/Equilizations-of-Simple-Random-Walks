import numpy as np
import matplotlib.pyplot as plt
import random

v1 = 1
v2 = -1

vectors_1d = [v1,v2]

v1_2 = np.array([1,0])
v2_2 = np.array([-1,0])
v3_2 = np.array([0,1])
v4_2 = np.array([0,-1])

vectors_2d = [v1_2, v2_2,v3_2,v4_2]

v1_3 = np.array([1,0,0])
v2_3 = np.array([-1,0,0])
v3_3 = np.array([0,1,0])
v4_3 = np.array([0,-1,0])
v5_3 = np.array([0,0,1])
v6_3 = np.array([0,0,-1])

vectors_3d = [v1_3,v2_3,v3_3,v4_3,v5_3,v6_3]

v1_8 = np.array([1,0,0,0,0,0,0,0])
v2_8 = np.array([-1,0,0,0,0,0,0,0])
v3_8 = np.array([0,1,0,0,0,0,0,0])
v4_8 = np.array([0,-1,0,0,0,0,0,0])
v5_8 = np.array([0,0,1,0,0,0,0,0])
v6_8 = np.array([0,0,-1,0,0,0,0,0])
v7_8 = np.array([0,0,0,1,0,0,0,0])
v8_8 = np.array([0,0,0,-1,0,0,0,0])
v9_8 = np.array([0,0,0,0,1,0,0,0])
v10_8 = np.array([0,0,0,0,-1,0,0,0])
v11_8 = np.array([0,0,0,0,0,1,0,0])
v12_8 = np.array([0,0,0,0,0,-1,0,0])
v13_8 = np.array([0,0,0,0,0,0,1,0])
v14_8 = np.array([0,0,0,0,0,0,-1,0])
v15_8 = np.array([0,0,0,0,0,0,0,1])
v16_8 = np.array([0,0,0,0,0,0,0,-1])

vectors_8d = [v1_8,v2_8,v3_8,v4_8,v5_8,v6_8,v7_8,v8_8,v9_8,v10_8,v11_8,v12_8,v13_8,v14_8,v15_8,v16_8]

iter = 1000000
walknum = 1000
equ_1d = 0
equ_2d = 0
equ_3d = 0
equ_8d = 0
x = range(0,iter + 1)
y_1 = [0]
y_2 = [0]
y_3 = [0]
y_8 = [0]
y_1d = []
y_2d = []
y_3d = []
y_8d = []

for i in range(0,walknum):
    for i in range(1,iter+1):
        step_1d = random.choice(vectors_1d)
        step_2d = random.choice(vectors_2d)
        step_3d = random.choice(vectors_3d)
        step_8d = random.choice(vectors_8d)

        pos_1d += step_1d
        pos_2d += step_2d
        pos_3d += step_3d
        pos_8d += step_8d

        if pos_1d == 0:
            equ_1d += 1
        y_1.append(equ_1d)
        if not np.any(pos_2d):
            equ_2d += 1
        y_2.append(equ_2d)
        if not np.any(pos_3d):
            equ_3d += 1
        y_3.append(equ_3d)
        if not np.any(pos_8d):
            equ_8d += 1
        y_8.append(equ_8d)
    y_1d.append(y_1)
    y_2d.append(y_2)
    y_3d.append(y_3)
    y_8d.append(y_8)
    y_1 = [0]
    y_2 = [0]
    y_3 = [0]
    y_8 = [0]
    pos_1d = 0
    pos_2d = np.array([0,0])
    pos_3d = np.array([0,0,0])
    pos_8d = np.array([0,0,0,0,0,0,0,0])
    equ_1d = 0
    equ_2d = 0
    equ_3d = 0
    equ_8d = 0

y_1_cumul = [sum(i) for i in zip(*y_1d)]
y_2_cumul = [sum(i) for i in zip(*y_2d)]
y_3_cumul = [sum(i) for i in zip(*y_3d)]
y_8_cumul = [sum(i) for i in zip(*y_8d)]

y_1_final = [x / walknum for x in y_1_cumul]
y_2_final = [x / walknum for x in y_2_cumul]
y_3_final = [x / walknum for x in y_3_cumul]
y_8_final = [x / walknum for x in y_8_cumul]

plt.figure(figsize = (10,10))
plt.plot(x,y_2_final,label = "2 Dimensions" )
plt.plot(x, y_1_final, label= "1 Dimension")
plt.plot(x,y_3_final, label = "3 Dimensions")
plt.plot(x,y_8_final, label = "8 Dimensions")
plt.legend()
plt.show()

plt.figure(figsize = (10,10))
plt.ylim(0,10)
plt.plot(x,y_2_final,label = "2 Dimensions" )
plt.plot(x, y_1_final, label= "1 Dimension")
plt.plot(x,y_3_final, label = "3 Dimensions")
plt.plot(x,y_8_final, label = "8 Dimensions")
plt.legend()
plt.show()

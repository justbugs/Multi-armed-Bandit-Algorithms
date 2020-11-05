import random
import numpy as np
import math

t_limit = 10
rj = np.zeros((3,t_limit+1))
theta = [0.2,0.4,0.6]

for i in range(t_limit):
    for j in range(3):
        label = random.random()
        if label < theta[j]:
            rj[j][i] = 1
        else:
            rj[j][i] = 0

I = []
count = [0,0,0]
p_theta = [0.0,0.0,0.0]
reward = 0
for t in range(0,2):
    I.append(t+1)
    count[t] += 1
    p_theta[t] = rj[t][t]
    reward += rj[t][t]

c = 1
for t in range(3,t_limit):
    L = []
    for j in range(0,2):    
        a = p_theta[j] + c*math.sqrt(2*math.log(t)/count[j])
        L.append(a)
    label = L.index(max(L))+1
    I.append(label)
    count[label-1]+=1
    p_theta[label-1] = p_theta[label-1] + 1/count[label-1]*(rj[label-1][i] - p_theta[label-1])
    reward += rj[label-1][i]
print(reward)


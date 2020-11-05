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

Beta = [(1.0,1.0),(1.0,1.0),(1.0,1.0)]
#Beta = [(2.0,4.0),(3.0,6.0),(1.0,2.0)]
def sample(j,Beta):
    a,b = Beta[j]
    p_theta = np.random.beta(a,b)
    return p_theta
I = []
reward = 0
for t in range(0,t_limit):
    p_theta = [0.0,0.0,0.0]
    for j in range(0,2):    
        p_theta[j] = sample(j,Beta)
    label = p_theta.index(max(p_theta))+1
    #print(label)
    I.append(label)
    a,b = Beta[label-1]
    Beta[label-1] = (a+rj[label-1][i],b+1-rj[label-1][i])
    print(Beta)
    reward += rj[label-1][i]
print(reward)


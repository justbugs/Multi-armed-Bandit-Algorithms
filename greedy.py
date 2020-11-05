import random
import numpy as np
import math

t_limit = 10000
rj = np.zeros((3,t_limit+1))
theta = [0.4,0.6,0.8]

for i in range(t_limit):
    for j in range(3):
        label = random.random()
        if label < theta[j]:
            rj[j][i] = 1
        else:
            rj[j][i] = 0
#print(rj)


epsilons = [0.1,0.5,0.9]
for epsilon in epsilons:
    greedy_reward = 0
    for i in range(100):
        I = []
        count = [0,0,0]
        p_theta = [0.0,0.0,0.0]
        reward = 0
        for i in range(t_limit):
            label = 0
            if epsilon < random.random():
                label = random.randint(0,2)+1
                #print(label)
                I.append(label)
            else:
                label = p_theta.index(max(p_theta))+1
                I.append(label)
            count[label-1]+=1
            p_theta[label-1] = p_theta[label-1] + 1/count[label-1]*(rj[label-1][i] - p_theta[label-1])
            reward += rj[label-1][i]
        greedy_reward += reward
    greedy_reward = greedy_reward/100
    print("epsilon:",epsilon,"avg_reward",greedy_reward)


c_list = [1,5,10]
for c in c_list:
    UCB_reward = 0
    for i in range(100):
        I = []
        count = [0,0,0]
        p_theta = [0.0,0.0,0.0]
        reward = 0
        for t in range(0,2):
            I.append(t+1)
            count[t] += 1
            p_theta[t] = rj[t][t]
            reward += rj[t][t]
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
        UCB_reward += reward
    UCB_reward = UCB_reward/100  
    print("c:",c,"avg_reward",UCB_reward)


def sample(j,Beta):
    a,b = Beta[j]
    p_theta = np.random.beta(a,b)
    return p_theta

Betas = [[(1.0,1.0),(1.0,1.0),(1.0,1.0)],[(2.0,4.0),(3.0,6.0),(1.0,2.0)]]
for Beta in Betas:
    TS_reward = 0
    for i in range(100):
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
            #print(Beta)
            reward += rj[label-1][i]
        TS_reward += reward
    TS_reward = TS_reward/100  
    print("Bata:",Betas.index(Beta),"avg_reward",TS_reward)    
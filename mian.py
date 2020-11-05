import random
import numpy as np
import math
import matplotlib.pyplot as plt
t_limit = 10000
rj = np.zeros((3,t_limit+1))
theta = [0.4,0.6,0.8]
x = np.linspace(0,t_limit,t_limit)#the abscissa to plot

#independent
for i in range(t_limit):
    for j in range(3):
        label = random.random()
        if label < theta[j]:
            rj[j][i] = 1
        else:
            rj[j][i] = 0

#dependent
for i in range(t_limit):
    label = random.random()
    if label < theta[0]:
        rj[0][i] = 1
        rj[1][i] = 0
        rj[2][i] = 0
    elif label < theta[1]:
        rj[0][i] = 0
        rj[1][i] = 1
        rj[2][i] = 0
    elif label < theta[2]:
        rj[0][i] = 0
        rj[1][i] = 0
        rj[2][i] = 1
    else:
        rj[0][i] = 0
        rj[1][i] = 0
        rj[2][i] = 0
#print(rj)


epsilons = [0.1,0.5,0.9]
for epsilon in epsilons:
    greedy_reward = []
    for j in range(100):
        I = []
        count = [0,0,0]
        p_theta = [0.0,0.0,0.0]
        reward = []
        for i in range(t_limit):
            label = 0
            if epsilon < random.random():
                label = random.randint(0,2)+1
                I.append(label)
            else:
                label = p_theta.index(max(p_theta))+1
                I.append(label)
            count[label-1]+=1
            p_theta[label-1] = p_theta[label-1] + 1/count[label-1]*(rj[label-1][i] - p_theta[label-1])
            reward.append(rj[label-1][i])
        greedy_reward.append(reward)
    #print(len(greedy_reward[1]))
    greedy_avg_reward = []
    for i in range(t_limit):
        value = 0
        for j in range(100):
            value += greedy_reward[j][i]
        greedy_avg_reward.append(value/100)
    #print(len(greedy_avg_reward))
    print("epsilon:",epsilon,"avg_reward",sum(greedy_avg_reward))
    plt.plot(x,greedy_avg_reward)
    plt.show()
    


c_list = [1,5,10]
for c in c_list:
    UCB_reward = []
    for i in range(100):
        I = []
        count = [0,0,0]
        p_theta = [0.0,0.0,0.0]
        reward = []
        for t in range(0,2):
            I.append(t+1)
            count[t] += 1
            p_theta[t] = rj[t][t]
            reward.append(rj[t][t])
        for t in range(2,t_limit):
            L = []
            for j in range(0,2):    
                a = p_theta[j] + c*math.sqrt(2*math.log(t)/count[j])
                L.append(a)
            label = L.index(max(L))+1
            I.append(label)
            count[label-1]+=1
            p_theta[label-1] = p_theta[label-1] + 1/count[label-1]*(rj[label-1][i] - p_theta[label-1])
            reward.append(rj[label-1][i])
        UCB_reward.append(reward)
    #print(len(UCB_reward[1]))
    UCB_avg_reward = []
    for i in range(t_limit):
        value = 0
        for j in range(100):
            value += UCB_reward[j][i]
        UCB_avg_reward.append(value/100)
    #print(len(UCB_avg_reward))
    print("c:",c,"avg_reward",sum(UCB_avg_reward))
    plt.plot(x,UCB_avg_reward)
    plt.show()





def sample(j,Beta):
    a,b = Beta[j]
    p_theta = np.random.beta(a,b)
    return p_theta

Betas = [[(1.0,1.0),(1.0,1.0),(1.0,1.0)],[(2.0,4.0),(3.0,6.0),(1.0,2.0)]]
for Beta in Betas:
    TS_reward = []
    for i in range(100):
        I = []
        reward = []
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
            reward.append(rj[label-1][i])
        TS_reward.append(reward)
    #print(len(TS_reward[1]))
    TS_avg_reward = []
    for i in range(t_limit):
        value = 0
        for j in range(100):
            value += TS_reward[j][i]
        TS_avg_reward.append(value/100)
    #print(len(TS_avg_reward))
    print("Bata:",Betas.index(Beta),"avg_reward",sum(TS_avg_reward))
    plt.plot(x,TS_avg_reward)
    plt.show() 
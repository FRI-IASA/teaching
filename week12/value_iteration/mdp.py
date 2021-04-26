import numpy as np
import random
'''==================================================
Initial set up
=================================================='''

#Hyperparameters
SMALL_ENOUGH = 0.005
GAMMA = 0.9         
NOISE = 0.10  

#Define all states
all_states=[0,1,2,3,4]

#Define rewards for all states
rewards = {}
for i in all_states:
    if i == 4:
        rewards[i] = +10
    else:
        rewards[i] = -1

#Dictionnary of possible actions. We have two "end" states (1,2 and 2,2)
actions = {
    0:['PickB'],
    1:['PlaceBonA','PlaceBonTable'],
    2:['PickB','PickA'],
    3:['PlaceAonB'],
    4:['exit'] 
    }

#Define an initial policy
policy={}
for s in all_states:
    policy[s] = random.choice(actions[s])

#Define initial value function 
V={}
for s in all_states:
    if s in actions.keys():
        V[s] = 0
    #if s ==4:
    #    V[s]=-1
    #if s == (1,2):
    #    V[s]=-1
    #if s == (2,3):
    #    V[s]=1
        
'''==================================================
Value Iteration
=================================================='''

iteration = 0

while True:
    biggest_change = 0
    for s in all_states:            
        if s in policy:
            
            old_v = V[s]
            new_v = 0
            
            for a in actions[s]:
                if a == 'PickB':
                    nxt = 1
                if a == 'PickA':
                    nxt = 3
                if a == 'PlaceBonTable':
                    nxt = 2
                if a == 'PlaceAonB':
                    nxt = 4

                #Choose a new random action to do (transition probability)
                random_1=random.choice([i for i in actions[s]])
                if random_1 == 'PickB':
                    act = 0
                if random_1 == 'PickA':
                    act = 2
                if random_1 == 'PlaceBonTable':
                    act = 1
                if random_1 == 'PlaceAonB':
                    act = 3

                #Calculate the value
                #nxt = tuple(nxt)
                #act = tuple(act)
                v = rewards[s] + (GAMMA * ((1-NOISE)* V[nxt] + (NOISE * V[act]))) 
                if v > new_v: #Is this the best action so far? If so, keep it
                    new_v = v
                    policy[s] = a

       #Save the best of all actions for the state                                
            V[s] = new_v
            biggest_change = max(biggest_change, np.abs(old_v - V[s]))

            
   #See if the loop should stop now         
    if biggest_change < SMALL_ENOUGH:
        break
    iteration += 1

print (policy)
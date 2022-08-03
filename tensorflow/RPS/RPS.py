import random
import numpy as np

def player(prev_play, opponent_history=[]):
    own_his =[]
    guess = 'R'
    opponent_history.append(prev_play)

    # glist = ['R','P','S']
    
    # rcount = opponent_history.count('R')
    # pcount = opponent_history.count('P')
    # scount = opponent_history.count('S')

    # rval = rcount/len(opponent_history)*100
    # pval = pcount/len(opponent_history)*100
    # sval = scount/len(opponent_history)*100

    # if rval > 40 and pval <= 40 and sval <= 10:
    #     guess = random.choices(glist,cum_weights=[20,70,10],k=len(glist))
    #     # guess = 'P'
    # elif pval > 40 and sval <=40 and rval <= 10:
    #     guess = random.choices(glist,cum_weights=[10,20,70],k=len(glist))
    #     # guess = 'S'
    # elif sval > 40 and rval <=40 and pval <= 10:
    #     guess = random.choices(glist,cum_weights=[70,20,0],k=len(glist))
    #     # guess = 'R'
    # else:
    #     guess = random.choice(glist)

    matrx = []

    
    

   



        
    # guess = random.choice(glist)

    # own_his.append(guess)
    # print(own_his)
    print(opponent_history)

    return guess



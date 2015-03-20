# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 14:07:56 2015

@author: dgevans
"""
import matplotlib.pyplot as plt
import numpy as np
import LucasStockey as LS
from calibrations.BGP import M1
from calibrations.CES import M2
import utilities

#initialize mugrid for value function iteration
muvec = np.linspace(-0.7,0.0,200)

M1.transfers = False #Government can't use transfers
PP_seq = LS.Planners_Allocation_Sequential(M1) #solve sequential problem
PP_bel = LS.Planners_Allocation_Bellman(M1,muvec) #solve recursive problem

T = 20
#sHist = utilities.simulate_markov(M1.Pi,0,T)
sHist = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],dtype=int)

#simulate
sim_seq = PP_seq.simulate(1.,0,T,sHist)
sim_bel = PP_bel.simulate(1.,0,T,sHist)

#plot policies
plt.figure(figsize=[14,10])
plt.subplot(3,2,1)
plt.title('Consumption')
plt.plot(sim_seq[0],'-ok')
plt.plot(sim_bel[0],'-xk')
plt.legend(('Sequential','Recursive','Incomplete'),loc='best')
plt.subplot(3,2,2)
plt.title('Labor')
plt.plot(sim_seq[1],'-ok')
plt.plot(sim_bel[1],'-xk')
plt.subplot(3,2,3)
plt.title('Government Debt')
plt.plot(sim_seq[2],'-ok')
plt.plot(sim_bel[2],'-xk')
plt.subplot(3,2,4)
plt.title('Taxes')
plt.plot(sim_seq[3],'-ok')
plt.plot(sim_bel[3],'-xk')
plt.subplot(3,2,5)
plt.title('Government Spending')
plt.plot(M1.G[sHist],'-ok')
plt.plot(M1.G[sHist],'-xk')
plt.plot(M1.G[sHist],'-^k')
plt.subplot(3,2,6)
plt.title('Output')
plt.plot(M1.Theta[sHist]*sim_seq[1],'-ok')
plt.plot(M1.Theta[sHist]*sim_bel[1],'-xk')
plt.savefig('TaxSequence_LS.png')


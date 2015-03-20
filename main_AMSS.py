# -*- coding: utf-8 -*-
"""
Created on Fri Feb 20 14:07:56 2015

@author: dgevans
"""
import matplotlib.pyplot as plt
import numpy as np
import LucasStockey as LS
import AMSS
from calibrations.BGP import M1
from calibrations.CES import M2
from calibrations.BGP import M_example
import utilities

#initialize mugrid for value function iteration
muvec = np.linspace(-0.7,0.01,200)

M1.transfers = True #Government can use transfers
PP_seq = LS.Planners_Allocation_Sequential(M1) #solve sequential problem
PP_bel = LS.Planners_Allocation_Bellman(M1,muvec) #solve recursive problem
PP_im = AMSS.Planners_Allocation_Bellman(M1,muvec)

T = 20
#sHist = utilities.simulate_markov(M1.Pi,0,T)
sHist = np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0],dtype=int)

#simulate
sim_seq = PP_seq.simulate(1.,0,T,sHist)
sim_bel = PP_bel.simulate(1.,0,T,sHist)
sim_im = PP_im.simulate(1.,0,T,sHist)

#plot policies
plt.figure(figsize=[14,10])
plt.subplot(3,2,1)
plt.title('Consumption')
plt.plot(sim_seq[0],'-ok')
plt.plot(sim_bel[0],'-xk')
plt.plot(sim_im[0],'-^k')
plt.legend(('Sequential','Recursive','Incomplete'),loc='best')
plt.subplot(3,2,2)
plt.title('Labor')
plt.plot(sim_seq[1],'-ok')
plt.plot(sim_bel[1],'-xk')
plt.plot(sim_im[1],'-^k')
plt.subplot(3,2,3)
plt.title('Government Debt')
plt.plot(sim_seq[2],'-ok')
plt.plot(sim_bel[2],'-xk')
plt.plot(sim_im[2],'-^k')
plt.subplot(3,2,4)
plt.title('Taxes')
plt.plot(sim_seq[3],'-ok')
plt.plot(sim_bel[3],'-xk')
plt.plot(sim_im[4],'-^k')
plt.subplot(3,2,5)
plt.title('Government Spending')
plt.plot(M1.G[sHist],'-ok')
plt.plot(M1.G[sHist],'-xk')
plt.plot(M1.G[sHist],'-^k')
plt.subplot(3,2,6)
plt.title('Output')
plt.plot(M1.Theta[sHist]*sim_seq[1],'-ok')
plt.plot(M1.Theta[sHist]*sim_bel[1],'-xk')
plt.plot(M1.Theta[sHist]*sim_im[1],'-^k')
plt.savefig('TaxSequence_AMSS.png')

#Now long simulations
T_long = 500
sim_seq_long = PP_seq.simulate(1.,0.,T_long)
sHist_long = sim_seq_long[-2]
sim_im_long = PP_im.simulate(1.,0.,T_long,sHist_long)

plt.figure(figsize=[14,10])
plt.subplot(3,2,1)
plt.title('Consumption')
plt.plot(sim_seq_long[0],'-k')
plt.plot(sim_im_long[0],'-.k')
plt.legend(('Sequential','Incomplete'),loc='best')
plt.subplot(3,2,2)
plt.title('Labor')
plt.plot(sim_seq_long[1],'-k')
plt.plot(sim_im_long[1],'-.k')
plt.subplot(3,2,3)
plt.title('Government Debt')
plt.plot(sim_seq_long[2],'-k')
plt.plot(sim_im_long[2],'-.k')
plt.subplot(3,2,4)
plt.title('Taxes')
plt.plot(sim_seq_long[3],'-k')
plt.plot(sim_im_long[4],'-.k')
plt.subplot(3,2,5)
plt.title('Government Spending')
plt.plot(M1.G[sHist_long],'-k')
plt.plot(M1.G[sHist_long],'-.k')
plt.subplot(3,2,6)
plt.title('Output')
plt.plot(M1.Theta[sHist_long]*sim_seq_long[1],'-k')
plt.plot(M1.Theta[sHist_long]*sim_im_long[1],'-.k')


'''
Time Varying Example
'''

M_example.transfers = True #Government can use transfers
PP_seq_time = LS.Planners_Allocation_Sequential(M_example) #solve sequential problem
PP_im_time = AMSS.Planners_Allocation_Bellman(M_example,muvec)

sHist_h = np.array([0,1,3,4,4,4])
sHist_l = np.array([0,1,2,4,4,4])

sim_seq_h = PP_seq_time.simulate(-0.5,0,6,sHist_h)
sim_im_h = PP_im_time.simulate(-.5,0,6,sHist_h)
sim_seq_l = PP_seq_time.simulate(-.5,0,6,sHist_l)
sim_im_l = PP_im_time.simulate(-.5,0,6,sHist_l)

plt.figure(figsize=[14,10])
plt.subplot(3,2,1)
plt.title('Consumption')
plt.plot(sim_seq_l[0],'-ok')
plt.plot(sim_im_l[0],'-^k')
plt.plot(sim_seq_h[0],'-or')
plt.plot(sim_im_h[0],'-^r')
plt.subplot(3,2,2)
plt.title('Labor')
plt.plot(sim_seq_l[1],'-ok')
plt.plot(sim_im_l[1],'-^k')
plt.plot(sim_seq_h[1],'-or')
plt.plot(sim_im_h[1],'-^r')
plt.subplot(3,2,3)
plt.title('Government Debt')
plt.plot(sim_seq_l[2],'-ok')
plt.plot(sim_im_l[2],'-^k')
plt.plot(sim_seq_h[2],'-or')
plt.plot(sim_im_h[2],'-^r')
plt.subplot(3,2,4)
plt.title('Taxes')
plt.plot(sim_seq_l[3],'-ok')
plt.plot(sim_im_l[4],'-^k')
plt.plot(sim_seq_h[3],'-or')
plt.plot(sim_im_h[4],'-^r')
plt.subplot(3,2,5)
plt.title('Government Spending')
plt.plot(M_example.G[sHist_l],'-ok')
plt.plot(M_example.G[sHist_l],'-^k')
plt.plot(M_example.G[sHist_h],'-or')
plt.plot(M_example.G[sHist_h],'-^r')
plt.subplot(3,2,6)
plt.title('Output')
plt.plot(M_example.Theta[sHist_l]*sim_seq_l[1],'-ok')
plt.plot(M_example.Theta[sHist_l]*sim_im_l[1],'-^k')
plt.plot(M_example.Theta[sHist_h]*sim_seq_h[1],'-or')
plt.plot(M_example.Theta[sHist_h]*sim_im_h[1],'-^r')

# -*- coding: utf-8 -*-

# %% ---------------------------------------------------------------------------

# import rozneho potrebneho...

%load_ext autoreload
%autoreload


import numpy as np

import matplotlib.pyplot as plt

from scipy.integrate import odeint


import sys
sys.path.append('./misc/')


# %% ---------------------------------------------------------------------------

from figFcns_Tex import *

# %% ---------------------------------------------------------------------------











# %% ---------------------------------------------------------------------------
                                                                ### cellB c01 ###
timeVect = np.arange(0,5.1,0.1)

R = 10**6
C = 10**-6
Q_0 = 2*10**-6

riesFcia = Q_0 * np.exp( (-1.0/(R*C)) * timeVect )

# %% -----------------------------------

plt.plot(timeVect, riesFcia) # kreslenie jednoduch. obr.        ### cellE c01 ###

# %% ---------------------------------------------------------------------------

figNameNum = 1
exec(open('misc/figsc_01.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------











# %% ---------------------------------------------------------------------------
                                                                ### cellB c02 ###
def fcn_difRovnica_01(x, t, param):

    R, C = param
    Q = x
    dotQ = (-1.0/(R*C)) * Q

    return dotQ                                                 ### cellE c02 ###

# %% -----------------------------------
                                                                ### cellB c03 ###
def fcn_simSch_01(t_start, t_final, T_s, param):

    R, C = param

    #-----------------------------------------
    t_log = np.arange(sim_t_start, sim_t_final+sim_T_s, sim_T_s).reshape(-1,1)

    #-----------------------------------------
    Q_0 = C * u_0

    #-----------------------------------------
    odeOut = odeint(fcn_difRovnica_01,
                    Q_0,
                    t_log[:,0],
                    args=(param,)
                    )

    return [t_log, odeOut]                                      ### cellE c03 ###

# %% -----------------------------------
                                                                ### cellB c04 ###
# Nastavenia simulacie

sim_t_start = 0
sim_t_final = 5
sim_T_s = 0.05

# ------------

param_C = 10**-6
param_R = 10**6
u_0 = 5

param = [param_R, param_C]                                      ### cellE c04 ###

# %% -----------------------------------
                                                                ### cellB c05 ###
# Simulacia

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param)

sig_napatie = x_log[:,0] * (1/param_C)

plt.plot(t_log, sig_napatie) # kreslenie jednoduch. obr.        ### cellE c05 ###


# %% ---------------------------------------------------------------------------

figNameNum = 2
exec(open('misc/figsc_02.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------














# %% ---------------------------------------------------------------------------

param_C = 10**-6 * 2
param_R = 10**6
u_0 = 5

param = [param_R, param_C]

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param)

sig_napatie_1 = x_log[:,0] * (1/param_C)

# %% ---------------------------------------------------------------------------

param_C = 10**-6 *0.5
param_R = 10**6
u_0 = 5

param = [param_R, param_C]

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param)

sig_napatie_2 = x_log[:,0] * (1/param_C)

# %% ---------------------------------------------------------------------------

param_C = 10**-6
param_R = 10**6 * 0.1
u_0 = 3

param = [param_R, param_C]

t_log, x_log, = fcn_simSch_01(sim_t_start, sim_t_final, sim_T_s, param)

sig_napatie_3 = x_log[:,0] * (1/param_C)

# %% ---------------------------------------------------------------------------

figNameNum = 3
exec(open('misc/figsc_03.py', encoding='utf-8').read())

# %% ---------------------------------------------------------------------------

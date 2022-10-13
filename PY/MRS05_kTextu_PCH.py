# -*- coding: utf-8 -*-

# %% ---------------------------------------------------------------------------

%load_ext autoreload
%autoreload

# %% ---------------------------------------------------------------------------

import numpy as np
from scipy.integrate import odeint

# %% ---------------------------------------------------------------------------

import sys
sys.path.append('./figjobs/')

from figFcns_TeX import *





# %% ---------------------------------------------------------------------------
                                                                ### cellB c01 ###
def fcn_LTIS(x, t, A, b, u):

    dotx = np.matmul(A, x) + np.matmul(b, u)

    return dotx                                                 ### cellE c01 ###








# %% ---------------------------------------------------------------------------
                                                                ### cellB c02 ###
def fcn_simSch(t_start, T_s, finalIndex, sig_u):

    #----------------------------------------------------
    # Alokacia casoveho vektora

    t_log = np.zeros([finalIndex, 1])
    t_log[0,:] = t_start

    #-----------------------------------------
    # Zaciatocne hodnoty signalov

    x_0 = np.zeros(b.shape[0])

    y_0 = np.dot(c.T, x_0.reshape(-1,1))

    #-----------------------------------------
    # Alokacia poli pre zapis signalov (a zapisanie zaciatocnych podmienok)

    x_log = np.zeros([finalIndex, len(x_0)])
    x_log[0,:] = x_0

    y_log = np.zeros([finalIndex, 1])
    y_log[0,:] = y_0

    #-------------

    u_log = np.zeros([finalIndex, 1])
    u_log[0,:] = sig_u[0,:]

    #----------------------------------------------------

    timespan = np.zeros(2)
    for idx in range(1, int(finalIndex)):

        timespan[0] = t_log[idx-1,:]
        timespan[1] = t_log[idx-1,:] + T_s

        t_log[idx,:] = timespan[-1]

        #-----------------------------------------
        # Riadeny system

        odeOut = odeint(fcn_LTIS,
                        x_log[idx-1,:],
                        timespan,
                        args=(A, b, u_log[idx-1,:])
                        )

        x_log[idx,:] = odeOut[-1,:]

        y_log[idx,:] = np.dot(c.T, x_log[idx,:].reshape(-1,1))

        #-----------------------------------------
        # logovanie vstup signalu

        u_log[idx,:] = sig_u[idx,:]

    return [t_log, x_log, y_log, u_log]                         ### cellE c02 ###










# %% ---------------------------------------------------------------------------
                                                                ### cellB c03 ###
sim_t_start = 0
sim_t_final = 10
sim_T_s = 0.001
sim_finalIndex = int(((sim_t_final - sim_t_start)/sim_T_s) + 1) ### cellE c03 ###

# %% ---------------------------------------------------------------------------













# %% ---------------------------------------------------------------------------

#-----------------------------------------                      ### cellB c04 ###
# Jednotkovy skok:

sig_u = np.ones([sim_finalIndex, 1])                            ### cellE c04 ###



# %% ---------------------------------------------------------------------------


#------------------------                                        ### cellB c05 ###
# Parametre systemu

A = np.array([[-1]])
b = np.array([[1]])
c = np.array([[1]])                                             ### cellE c05 ###

#------------------------                                       ### cellB c06 ###
# Simulacia

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u) ### cellE c06 ###



#------------------------
# Obrazok

figName = 'MRS05_PCH_yu'

figNameNum = 1
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------








# %% ---------------------------------------------------------------------------


#------------------------                                        ### cellB c11 ###
# Parametre systemu

A = np.array([[1]])
b = np.array([[1]])
c = np.array([[1]])                                             ### cellE c11 ###

#------------------------
# Simulacia

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)



#------------------------
# Obrazok

figName = 'MRS05_PCH_yu'

figNameNum = 11
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------














# %% ---------------------------------------------------------------------------


#------------------------                                       ### cellB c07 ###
# Parametre systemu

A = np.array([[0]])
b = np.array([[1]])
c = np.array([[1]])                                             ### cellE c07 ###

#------------------------
# Simulacia

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)



#------------------------
# Obrazok

figName = 'MRS05_PCH_yu'

figNameNum = 2
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------

















# %% ------------                                               ### cellB c08 ###
# Aproximacia Dirackovho impulzu:

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s                                         ### cellE c08 ###

# %% ---------------------------------------------------------------------------


#------------------------
# Parametre systemu

A = np.array([[-1]])
b = np.array([[1]])
c = np.array([[1]])

#------------------------
# Simulacia

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)



#------------------------
# Obrazok

figName = 'MRS05_PCH_yu'

figNameNum = 3
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())






# %% ---------------------------------------------------------------------------


#------------------------                                       ### cellB c07 ###
# Parametre systemu

A = np.array([[0]])
b = np.array([[1]])
c = np.array([[1]])                                             ### cellE c07 ###

#------------------------
# Simulacia

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_yu'

figNameNum = 4
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())






# %% ---------------------------------------------------------------------------


#------------------------                                        ### cellB c12 ###
# Parametre systemu

A = np.array([[1]])
b = np.array([[1]])
c = np.array([[1]])                                             ### cellE c12 ###

#------------------------
# Simulacia

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)



#------------------------
# Obrazok

figName = 'MRS05_PCH_yu'

figNameNum = 12
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------
# %% ---------------------------------------------------------------------------
# %% ---------------------------------------------------------------------------
# %% ---------------------------------------------------------------------------
# %% ---------------------------------------------------------------------------






# %% ---------------------------------------------------------------------------





#------------------------                                       ### cellB c31 ###
# Parametre systemu

p_1 = -1
p_2 = -2

A_poly = np.polymul([1, -p_1], [1, -p_2])
B_poly = [0, A_poly[-1]]

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])                      ### cellE c31 ###



print(A_poly)

#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 31
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 311
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())




# %% ---------------------------------------------------------------------------


#------------------------
# Parametre systemu

p_1 = -1
p_2 = -1

A_poly = np.polymul([1, -p_1], [1, -p_2])

B_poly = [0, A_poly[-1]]


print(B_poly)
print(A_poly)

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])


#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 32
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())

#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 321
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------






#------------------------
# Parametre systemu
                                                                ### cellB c33 ###
omega0 = 3
beta = 0.5

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]                                        ### cellE c33 ###

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])



print(B_poly)
print(A_poly)

#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)



#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 33
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 331
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------






# %% ---------------------------------------------------------------------------
# %% ---------------------------------------------------------------------------
# %% ---------------------------------------------------------------------------

def fcn_createAbc2R(A_poly, B_poly):

    A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
    b = np.array([[0], [1]])
    c = np.array([[B_poly[-1]], [B_poly[-2]]])

    return A, b, c

# %% ---------------------------------------------------------------------------



omega0 = 3
sig_u = np.ones([sim_finalIndex, 1])



beta = 0.1

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_0, x_log, y_log_0, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


beta = 0.3

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_1, x_log, y_log_1, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


beta = 0.6

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_2, x_log, y_log_2, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


beta = 1

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_3, x_log, y_log_3, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


#------------------------
# Obrazok

figName = 'MRS05_PCH_len_yx3'

figNameNum = 1
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


# %% ---------------------------------------------------------------------------



omega0 = 3
sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s


beta = 0.1

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_0, x_log, y_log_0, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


beta = 0.3

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_1, x_log, y_log_1, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


beta = 0.6

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_2, x_log, y_log_2, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


beta = 1

A_poly = [1, 2*beta*omega0, omega0**2]
B_poly = [0, A_poly[-1]]
A, b, c = fcn_createAbc2R(A_poly, B_poly)

t_log_3, x_log, y_log_3, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)


#------------------------
# Obrazok

figName = 'MRS05_PCH_len_yx3'

figNameNum = 2
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


# %% ---------------------------------------------------------------------------








# %% ---------------------------------------------------------------------------





#------------------------
# Parametre systemu

p_1 = -1
p_2 = -2

A_poly = np.polymul([1, -p_1], [1, -p_2])
B_poly = [3, A_poly[-1]]

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])


print(np.roots(B_poly))
print(A_poly)



#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 41
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 411
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------





#------------------------
# Parametre systemu

p_1 = -1
p_2 = -2

A_poly = np.polymul([1, -p_1], [1, -p_2])
B_poly = [3, 0]

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])


print(np.roots(B_poly))
print(A_poly)



#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 51
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 511
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())




# %% ---------------------------------------------------------------------------





#------------------------
# Parametre systemu

p_1 = -1
p_2 = 0

A_poly = np.polymul([1, -p_1], [1, -p_2])
B_poly = [0, 1]

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])


print(B_poly)
print(A_poly)



#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 61
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 611
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())







# %% ---------------------------------------------------------------------------





#------------------------
# Parametre systemu

p_1 = 0
p_2 = 0

A_poly = np.polymul([1, -p_1], [1, -p_2])
B_poly = [0, 1]

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])


print(B_poly)
print(A_poly)



#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 71
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 711
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())







# %% ---------------------------------------------------------------------------





#------------------------
# Parametre systemu

p_1 = 0
p_2 = 0

A_poly = np.polymul([1, -p_1], [1, -p_2])
B_poly = [1, 1]

A = np.array([[0, 1], [-A_poly[-1], -A_poly[-2]]])
b = np.array([[0], [1]])
c = np.array([[B_poly[-1]], [B_poly[-2]]])


print(B_poly)
print(A_poly)



#------------------------
# Simulacia

sig_u = np.ones([sim_finalIndex, 1])

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 81
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())


#------------------------
# Simulacia

sig_u = np.zeros([sim_finalIndex, 1])
sig_u[0,:] = 1/sim_T_s

t_log, x_log, y_log, u_log = fcn_simSch(sim_t_start, sim_T_s, sim_finalIndex, sig_u)

#------------------------
# Obrazok

figName = 'MRS05_PCH_len_y'

figNameNum = 811
exec(open('figjobs/' + figName + '.py', encoding='utf-8').read())



# %% ---------------------------------------------------------------------------

# %% ---------------------------------------------------------------------------

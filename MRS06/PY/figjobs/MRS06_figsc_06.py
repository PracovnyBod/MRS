# coding: utf-8




figPlotParam = fcnDefaultFigSize(7.5, 0.14, 0.91, 0.12, 0.45, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1, height_ratios=[70, 30])

#------------------
ax0 = plt.subplot(subPlots[0])


ax0.set_title(u'Výstupná veličina', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'Uhol [°]', y=1, ha='right', rotation='vertical')

ax0.plot(suroveData[:,0], suroveData[:,1],
         '-k', lw=0.8,
         )



#------------------
ax1 = plt.subplot(subPlots[1])


ax1.set_title(u'Vstupná veličina', x=0.01, y=1.02, ha='left')
ax1.set_ylabel(u'$u(t)$ [kg m$^2$ s$^{-2}$]', y=1.2, ha='right', rotation='vertical')

ax1.plot(t_log, u_log,
         '-k', lw=0.8, drawstyle='steps-post',
         )


#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas [s]', x=1.05,  ha='left', va='bottom')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    if ax == ax0:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------










for idx in range(1, u_tabulka.shape[0]):

    ustVstup =  u_tabulka[idx-1][1]
    ustInterval = [u_tabulka[idx-1][0] + (u_tabulka[idx][0]-u_tabulka[idx-1][0])*0.7,
                   u_tabulka[idx][0]
                   ]

    boolMaska = np.logical_and(suroveData[:,0]>ustInterval[0], suroveData[:,0]<=ustInterval[1])

    ustVystCas = suroveData[boolMaska, 0]
    ustVystHodnoty = suroveData[boolMaska, 1]

    ustPriemer = np.mean(ustVystHodnoty)

    # prevodChar[idx-1, 0] = ustVstup
    # prevodChar[idx-1, 1] = ustPriemer


    #------------------------------
    # Kreslenie do obrazka:

    ax0.plot(ustVystCas, ustVystHodnoty,
             '-r', lw=2,
             )

    #------------------------------
    ax0.plot(ustInterval, [ustPriemer, ustPriemer],
             '-b', lw=2,
             )
    #------------------------------
    ax1.plot(ustInterval, [ustVstup, ustVstup],
             '-r', lw=2,
             )














plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

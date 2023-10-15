# -*- coding: utf-8 -*-

figPlotParam = fcnDefaultFigSize(7.0, 0.13, 0.91, 0.09, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1,
                             height_ratios=[60, 40]
                             )

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.plot(t_log, y_log,
         '-', lw=1.0, color='k',
         label='$y(t)$',
         )

#-------
ax0.set_title('Výstupná veličina', x=0.01, y=1.02, ha='left')



#------------------
ax1 = plt.subplot(subPlots[1])

ax1.plot(t_log, u_log,
         '-', lw=1.0, color='k', ds='steps-post',
         label='$u(t)$',
         )

#-------
ax1.set_title('Vstupná veličina', x=0.01, y=1.02, ha='left')



#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0, ax1]:

        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())

        ax.xaxis.set_label_coords(1.01, -0.11)
        ax.yaxis.set_label_coords(-0.02, 1.05)

        ax.set_xlabel(u'čas', ha='left', va='top')

    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0, ax1]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.01, 1.00))

#------------------

plt.savefig('fig/' + figName + '_{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('fig/' + figName + '_{}'.format(figNameNum) +'.pdf')

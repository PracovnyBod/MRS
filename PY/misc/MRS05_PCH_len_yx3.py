# -*- coding: utf-8 -*-

figPlotParam = fcnDefaultFigSize(4.0, 0.13, 0.85, 0.15, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1)

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.plot(t_log_0, y_log_0,
         '-', lw=1.0,
         label='$\\beta = 0.1$',
         )

ax0.plot(t_log_1, y_log_1,
         '-', lw=1.0,
         label='$\\beta = 0.3$',
         )

ax0.plot(t_log_2, y_log_2,
         '-', lw=1.0,
         label='$\\beta = 0.6$',
         )


ax0.plot(t_log_3, y_log_3,
         '-', lw=1.0,
         label='$\\beta = 1.0$',
         )

#-------
ax0.set_title('Výstupná veličina', x=0.01, y=1.02, ha='left')




#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():

    if ax in [ax0]:

        fcnDefaultAxisStyle(ax)

        ax.xaxis.set_minor_locator(AutoMinorLocator())
        ax.yaxis.set_minor_locator(AutoMinorLocator())

        ax.xaxis.set_label_coords(1.05, -0.09)
        ax.yaxis.set_label_coords(-0.02, 1.05)

        ax.set_xlabel(u'čas', ha='left', va='top')

    #-----------------------------

    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax in [ax0]:
        ax.legend(handles_ax, labels_ax, ncol=1, handlelength=1.2, loc=2, bbox_to_anchor=(1.01, 1.00))

#------------------

plt.savefig('fig/' + figName + '_{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('fig/' + figName + '_{}'.format(figNameNum) +'.pdf')

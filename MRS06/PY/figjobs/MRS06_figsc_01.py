# coding: utf-8




figPlotParam = fcnDefaultFigSize(4.5, 0.14, 0.88, 0.15, 0.4, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1, )

#------------------
ax0 = plt.subplot(subPlots[0])

# ax0.set_title(u'Výstup', x=0.01, y=1.02, ha='left')
# ax0.set_ylabel(u'[rad]', y=1.02, ha='right', va='bottom', rotation='vertical', )

ax0.set_title(u'Vstupná veličina', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'$u(t)$ [kg m$^2$ s$^{-2}$]', y=1, ha='right', rotation='vertical')

ax0.plot(t_log, u_log,
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

    if ax == ax0:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------



#------------------

from matplotlib.ticker import AutoMinorLocator
ax0.xaxis.set_minor_locator(AutoMinorLocator())
ax0.yaxis.set_minor_locator(AutoMinorLocator())

#------------------


plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

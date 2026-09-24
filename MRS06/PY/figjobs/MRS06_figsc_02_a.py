# coding: utf-8




figPlotParam = fcnDefaultFigSize(8.4, 0.15, 0.9, 0.12, 0.45, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1, height_ratios=[100, ])

#------------------
ax0 = plt.subplot(subPlots[0])


ax0.set_title(u'Prevodová charakteristika', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'Uhol [°]', y=1, ha='right', va='top', rotation='horizontal')
ax0.set_xlabel(u'Vstup\n$u$ [kg m$^2$ s$^{-2}$]', x=1.05, ha='left', va='bottom')

ax0.plot(prevodChar[:,0], prevodChar[:,1],
         '+r', ms=9, mew=1,
         label=u'Namerané dáta'
         )

ax0.plot(prevodChar[:,0], y_hat,
         '.b', ms=5, mew=1,
         label=u'Model'
         )


#------------------

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())

    if ax == ax0:
        ax.legend(handles_ax, labels_ax, ncol=2, loc=1, bbox_to_anchor=(0.98, 1.1))

#------------------

# plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

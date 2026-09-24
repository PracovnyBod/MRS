# coding: utf-8




# figPlotParam = fcnDefaultFigSize(9, 0.12, 0.93, 0.09, 0.35, 13)
figPlotParam = fcnDefaultFigSize(7, 0.12, 0.91, 0.11, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(2, 1, height_ratios=[65, 35])




#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Výstupná veličina', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'[°]', y=1, ha='right', rotation='vertical')

ax0.plot(posunutaPCH_t, posunutaPCH_y,
         '-k', lw=1.0,
         )


#------------------
ax1 = plt.subplot(subPlots[1])

ax1.set_title(u'Vstupná veličina', x=0.01, y=1.02, ha='left')
ax1.set_ylabel(u'[kg m$^2$ s$^{-2}$]', y=1, ha='right', rotation='vertical')


ax1.plot(posunutaPCH_t, posunutaPCH_u,
         '-k', lw=1.0, drawstyle='steps-post',
         )

from matplotlib.ticker import (MultipleLocator)
ax1.yaxis.set_major_locator(MultipleLocator(0.4))



#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u't [s]', x=1.05, ha='left', va='bottom')


#Doplnujuce info v obr:





ax0.plot([3, posunutaPCH_t[-1]], [Delta_y, Delta_y],
         '-r', lw=1,
         )
ax0.annotate('', xy=(3.5,0), xytext=(3.5,Delta_y),
             arrowprops=dict(arrowstyle='<->',
                             shrinkA=0,
                             shrinkB=0,
                             ec='r',
                             lw=1,
                             ),
            )
ax0.text(3.5, Delta_y*0.5,
         u' $\Delta y$',
         ha='left', va='center', color='red',
        )



ax1.plot([3, posunutaPCH_t[-1]], [0, 0],
         '-r', lw=0,
         )

ax1.annotate('', xy=(3.5,0), xytext=(3.5,u_PB1_okol),
             arrowprops=dict(arrowstyle='<->',
                             shrinkA=0,
                             shrinkB=0,
                             ec='r',
                             lw=1,
                             ),
            )
ax1.text(3.5, u_PB1_okol*0.5,
         u' $\Delta u$',
         ha='left', va='center', color='red',
        )













#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax == ax0:
        ax.legend(handles_ax, labels_ax,
           loc=2, bbox_to_anchor=(0.02, 0.69), ncol=1,
           )

#------------------

# plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

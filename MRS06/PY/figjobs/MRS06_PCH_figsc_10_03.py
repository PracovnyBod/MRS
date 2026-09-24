# coding: utf-8




figPlotParam = fcnDefaultFigSize(8, 0.12, 0.91, 0.1, 0.5, 13)
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
ax0.annotate('', xy=(4.5,0), xytext=(4.5,Delta_y),
             arrowprops=dict(arrowstyle='<->', shrinkA = 0, shrinkB = 0, ec='r', lw=1,),
            )
ax0.text(4.5, Delta_y*0.5,
         u' $\Delta y$',
         ha='left', va='center', color='red',
        )

ax0.annotate('', xy=(3.8,0), xytext=(3.8,Delta_y),
             arrowprops=dict(arrowstyle='<->', shrinkA = 0, shrinkB = 0, ec='r', lw=1,),
            )
ax0.text(3.8, Delta_y*0.5,
         u'\\  100 \%',
         ha='left', va='center', color='red',
        )



ax0.plot([0, 3.5], [Delta_y63, Delta_y63],
         '-g', lw=0.5,
         )

ax0.annotate('', xy=(3.4,0), xytext=(3.4,Delta_y63),
             arrowprops=dict(arrowstyle='<->', shrinkA = 0, shrinkB = 0, ec='g', lw=1,),
            )
ax0.text(3.4, Delta_y63*0.5,
         u'\\  63 \%',
         ha='left', va='center', color='g',
        )



ax0.plot(posunutaPCH_t[temp_Mask], posunutaPCH_y[temp_Mask],
         'og', ms=4, mec='g', mew=1.0, mfc='w',
         )


ax0.plot([T, T], ax0.get_ylim(),
         '-g', lw=1,
         )

ax0.text(T, ax0.get_ylim()[0]-0.1,
         u'$T$',
         ha='center', va='top', color='g',
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

plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

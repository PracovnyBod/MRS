# coding: utf-8




# figPlotParam = fcnDefaultFigSize(8.4, 0.15, 0.9, 0.12, 0.45, 13)
figPlotParam = fcnDefaultFigSize(8.4, 0.15, 0.92, 0.1, 0.45, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1, height_ratios=[100, ])

#------------------
ax0 = plt.subplot(subPlots[0])


ax0.set_title(u'Prevodová charakteristika', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'Uhol [°]', y=1, ha='right', va='bottom', rotation='vertical')
ax0.set_xlabel(u'Vstup\n$u$ [kg m$^2$ s$^{-2}$]', x=1.05, ha='left', va='bottom', rotation='vertical')

ax0.plot(u_ine, y_ine_1,
         '.', color='gray', ms=4, mew=0,
         label=u'Model prevodovej charakteristiky'
         )

ax0.plot(u_PB1, y_PB1,
         '+', ms=10, mew=1.2, mec='r',
         label=u'1.PB'
         )

ax0.plot(u_PB2, y_PB2,
         '+', ms=10, mew=1.2, mec='b',
         label=u'2.PB'
         )

ax0.set_xlim([0, 10])
ax0.set_ylim([0, 90])

#-------------
#Doplnujuce info v obr:

ax0.plot(u_PB1, 0,
         '|', ms=15, mew=1, mec='r',
         )
ax0.text(u_PB1, 3,
         u'$u_{PB1}$',
         ha='center', va='bottom',
        )
ax0.plot(0, y_PB1,
         '_', ms=15, mew=1, mec='r',
         )
ax0.text(0.3, y_PB1,
         u'$y_{PB1}$',
         ha='left', va='center',
        )

ax0.plot(u_PB2, 0,
         '|', ms=15, mew=1, mec='b',
         )
ax0.text(u_PB2, 3,
         u'$u_{PB2}$',
         ha='center', va='bottom',
        )
ax0.plot(0, y_PB2,
         '_', ms=15, mew=1, mec='b',
         )
ax0.text(0.3, y_PB2,
         u'$y_{PB2}$',
         ha='left', va='center',
        )











#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()

    if ax == ax0:
        ax.legend(handles_ax, labels_ax,
            loc=2, bbox_to_anchor=(0.05, 0.60), ncol=1,
            )

#------------------

# plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

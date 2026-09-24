# coding: utf-8




# figPlotParam = fcnDefaultFigSize(9.4, 0.15, 0.88, 0.12, 0.45, 13)
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


ax0.plot([u_PB1-u_PB1_okol, u_PB1-u_PB1_okol, 0], [0, y_PB1_l, y_PB1_l],
         '-', color='r', lw=0.5,
         )
ax0.plot([u_PB1+u_PB1_okol, u_PB1+u_PB1_okol, 0], [0, y_PB1_h, y_PB1_h],
         '-', color='r', lw=0.5,
         )


ax0.plot(u_PB1, y_PB1,
         '+', ms=10, mew=1.2, mec='r',
         label=u'1.PB'
         )

ax0.plot(u_PB2, y_PB2,
         '+', ms=10, mew=1.2, mec='b',
         label=u'2.PB'
         )

ax0.plot([u_PB2-u_PB2_okol, u_PB2-u_PB2_okol, 0], [0, y_PB2_l, y_PB2_l],
         '-', color='b', lw=0.5,
         )
ax0.plot([u_PB2+u_PB2_okol, u_PB2+u_PB2_okol, 0], [0, y_PB2_h, y_PB2_h],
         '-', color='b', lw=0.5,
         )


temp_Mask_PB1 = np.logical_and((u_ine >= u_PB1-u_PB1_okol), (u_ine <= u_PB1+u_PB1_okol))
ax0.plot(u_ine[temp_Mask_PB1], y_ine_1[temp_Mask_PB1],
         '.r', ms=4,
         )

temp_Mask_PB2 = np.logical_and((u_ine >= u_PB2-u_PB2_okol), (u_ine <= u_PB2+u_PB2_okol))
ax0.plot(u_ine[temp_Mask_PB2], y_ine_1[temp_Mask_PB2],
         '.b', ms=4,
         )


ax0.set_xlim([0, 10])
ax0.set_ylim([0, 90])

#-------------
#Doplnujuce info v obr:




#--------
ax0.plot(u_PB1, 0,
         '|', ms=15, mew=2, mec='r',
         )
ax0.text(u_PB1, 3,
         u'$u_{PB1}$',
         ha='center', va='bottom',
        )
ax0.text(u_PB1 - u_PB1_okol, 6,
         u'$u_{PB1_l}$',
         ha='right', va='bottom',
        )
ax0.text(u_PB1 + u_PB1_okol, 6,
         u'$u_{PB1_h}$',
         ha='left', va='bottom',
        )
ax0.annotate('', xy=(u_PB1 - u_PB1_okol,15), xytext=(u_PB1 + u_PB1_okol,15),
             arrowprops=dict(arrowstyle='<->', shrinkA = 0, shrinkB = 0, ec='r', lw=0.5)
            )
ax0.text(u_PB1, 15,
         u'$\Delta u_{PB1}$',
         ha='center', va='bottom',
        )

ax0.plot(0, y_PB1,
         '_', ms=15, mew=2, mec='r',
         )
ax0.text(0.3, y_PB1,
         u'$y_{PB1}$',
         ha='left', va='center',
        )
ax0.text(1, y_PB1_l,
         u'$y_{PB1_l}$',
         ha='left', va='top',
        )
ax0.text(1, y_PB1_h,
         u'$y_{PB1_h}$',
         ha='left', va='bottom',
        )
ax0.annotate('', xy=(2,y_PB1_l), xytext=(2,y_PB1_h),
             arrowprops=dict(arrowstyle='<->', shrinkA = 0, shrinkB = 0, ec='r', lw=0.5)
            )
ax0.text(2, y_PB1,
         u'$\Delta y_{PB1}$',
         ha='left', va='center',
        )

#--------
ax0.plot(u_PB2, 0,
         '|', ms=15, mew=2, mec='b',
         )
ax0.text(u_PB2, 3,
         u'$u_{PB2}$',
         ha='center', va='bottom',
        )
ax0.text(u_PB2 - u_PB2_okol, 6,
         u'$u_{PB2_l}$',
         ha='right', va='bottom',
        )
ax0.text(u_PB2 + u_PB2_okol, 6,
         u'$u_{PB2_h}$',
         ha='left', va='bottom',
        )
ax0.plot(0, y_PB2,
         '_', ms=15, mew=2, mec='b',
         )
ax0.text(0.3, y_PB2,
         u'$y_{PB2}$',
         ha='left', va='center',
        )

ax0.text(1, y_PB2_l,
         u'$y_{PB2_l}$',
         ha='left', va='top',
        )
ax0.text(1, y_PB2_h,
         u'$y_{PB2_h}$',
         ha='left', va='bottom',
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

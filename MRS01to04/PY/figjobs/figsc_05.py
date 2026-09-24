# coding: utf-8


figNamePrefix = 'cv03_fig_'

figPlotParam = fcnDefaultFigSize(5.0, 0.14, 0.88, 0.19, 0.4, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1, )

#------------------
ax0 = plt.subplot(subPlots[0])

ax0.set_title(u'Poloha kyvadla (výchylka)', x=0.01, y=1.02, ha='left')
ax0.set_ylabel(u'[°]', y=1.02, ha='right', va='bottom', rotation='horizontal', )

ax0.plot(timeVect, x[:,0]*180/np.pi,
         '-', lw=0.8, color='k',
         label=u'$\\varphi(t)$ [°]',
         )

# ax0.plot(timeVect, x[:,1],
#          '-', lw=0.8, color='k', dashes=[3,1],
#          label=u'$x_2(t)$ [rad/s]',
#          )

#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas [s]', x=1.05, ha='left', va='center')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant01(fig)

#------------------

tmpfigname = figNamePrefix + '{}'.format(figNameNum)
print(tmpfigname)

# plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('./fig/' + tmpfigname +'.pdf')

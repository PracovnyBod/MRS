# coding: utf-8


figNamePrefix = 'kMRS02_fig_'

figPlotParam = fcnDefaultFigSize(5.0, 0.14, 0.88, 0.19, 0.4, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1, )

#------------------
ax0 = plt.subplot(subPlots[0])

# ax0.set_title(u'Uhlová rýchlosť motora', x=0.01, y=1.02, ha='left')
# ax0.set_ylabel(u'[rad/s]', ha='right', va='bottom', rotation='horizontal', )

ax0.plot(t_log, x_log[:,0],
         '-', lw=0.8, color='k', dashes=[5,2],
         label=u'$i(t)$ [A]',
         )

ax0.plot(t_log, x_log[:,1],
         '-', lw=0.8, color='k',
         label=u'$\\omega(t)$ [rad/s]',
         )










#------------------
for ax in fig.get_axes():
    ax.set_xlabel(u'čas [s]', ha='left', va='top')

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

for ax in fig.get_axes():
    fcnDefaultAxisStyle(ax)
    handles_ax, labels_ax = ax.get_legend_handles_labels()

    ax.xaxis.set_label_coords(1.05, -0.06)
    ax.yaxis.set_label_coords(-0.02, 1.06)


    if ax in [ax0]:
        ax.yaxis.set_major_locator(MultipleLocator(60))
        ax.yaxis.set_minor_locator(MultipleLocator(20))



    if ax in [ax0]:
        ax.legend(handles_ax, labels_ax, loc=1, bbox_to_anchor=(0.98, 1.12))

#------------------

# # plt.savefig('fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
# plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.pdf')

tmpfigname = figNamePrefix + '{}'.format(figNameNum)
print(tmpfigname)

# plt.savefig('./fig/' + figNamePrefix + '{}'.format(figNameNum) +'.png', dpi=200)
plt.savefig('./fig/' + tmpfigname +'.pdf')
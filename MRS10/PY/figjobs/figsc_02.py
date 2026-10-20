# -*- coding: utf-8 -*-

# from figFcns_TeX import *
from figFcns_addhelpers import *






PANELNAME = 'panel_wy'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(9.5, 0.17, 0.9, 0.25, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             # height_ratios=[40, 40, 20],
                             )

#---------------------------------------------
ax0 = plt.subplot(subPlots[0])



ax0.plot(t_log, sig_setpoint,
         '-', lw=0.8, alpha=0.9, color='k', dashes=[5,2],
         label='$w(t)$',
         )

ax0.plot(t_log, y_log,
         '-', lw=0.8, alpha=0.9, color='k',
         label='$y(t)$',
         )

#------------------
ax0.set_title(u'Výstup a vstup URO', x=0.01, y=1.02, ha='left')

#------------------

# Get and store axis limits
x_limits = ax0.get_xlim()
y_limits = ax0.get_ylim()



# annotations

# ------------------------------------------
# time 0 line

belowFigLevel1 = -0.25
belowFigLevel2 = -0.6


ax0.annotate(
    '',
    xy=(0, belowFigLevel1), 
    xycoords='data',
    xytext=(0, belowFigLevel2), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        arrowstyle='-', 
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )



# ------------------------------------------
# y_max

ax0.plot(
    2.725, 1.5072,
    'o', 
    color='k',
    ms=4,
    # mec='k',
    mew=0,
    mfc='k',
)

ax0.annotate(
    '$y_{max}$',
    xy=(2.725, 1.5072), 
    xycoords='data',
    xytext=(5, 3), 
    textcoords='offset points',
    horizontalalignment='left', 
    verticalalignment='bottom'
    )




# ------------------------------------------
# '$\eta_{max}$'

ax0.annotate(
    '',
    xy=(2.725, 1.5072 ), 
    xycoords='data',
    xytext=(2.725, 1.0), 
    textcoords='data',
    ha='center', 
    va='top',
    arrowprops=dict(
        # arrowstyle='<->', 
        arrowstyle='<->,head_width=.1,head_length=0.5',
        # arrowstyle='<->,head_width=.068,head_length=0.5', 
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        # mutation_scale=100,
        # mutation_aspect=1,
        ),
    )


ax0.annotate(
    '$\eta_{max}$',
    xy=(2.725, 1.25 ), 
    xycoords='data',
    xytext=(30, 10), 
    textcoords='offset points',
    ha='left', 
    va='center',
    arrowprops=dict(
        arrowstyle='-', 
        lw=0.4, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    )






# ------------------------------------------
# '$t_{max}$'

ax0.plot([2.725, 2.725], [1, -0.04],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )




ax0.annotate(
    '',
    xy=(2.725, belowFigLevel1), 
    xycoords='data',
    xytext=(2.725, belowFigLevel2+0.05*2), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        arrowstyle='-', 
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )




ax0.annotate(
    '',
    xy=(0, belowFigLevel2+0.05*3), 
    xycoords='data',
    xytext=(2.725, belowFigLevel2+0.05*3), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        # arrowstyle='<->', 
        arrowstyle='<->,head_width=.1,head_length=0.5',
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )

ax0.annotate(
    '$t_{max}$',
    xy=(2.725/2, belowFigLevel2+0.05*3), 
    xycoords='data',
    xytext=(0, 3), 
    textcoords='offset points',
    ha='center', 
    va='bottom',
    annotation_clip=False,
    )







# ------------------------------------------
# '$t_n$'

ax0.plot([-0.37, 0.176], [0.1, 0.1],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )

ax0.plot([0.176, 0.176], [0.1, 0-0.04],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )

ax0.plot([-0.37, 1.226], [0.9, 0.9],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )

ax0.plot([1.226, 1.226], [0.9, 0-0.04],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )



ax0.annotate(
    '',
    xy=(0.176, belowFigLevel1), 
    xycoords='data',
    xytext=(0.176, belowFigLevel2+0.05*5), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        arrowstyle='-', 
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )

ax0.annotate(
    '',
    xy=(1.226, belowFigLevel1), 
    xycoords='data',
    xytext=(1.226, belowFigLevel2+0.05*5), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        arrowstyle='-', 
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )


ax0.annotate(
    '',
    xy=(0.176, belowFigLevel2+0.05*6), 
    xycoords='data',
    xytext=(1.226, belowFigLevel2+0.05*6), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        # arrowstyle='<->', 
        arrowstyle='<->,head_width=.1,head_length=0.5',
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )

# ax0.annotate(
#     '$t_n$',
#     xy=(0.176+((1.226-0.176)/2), belowFigLevel2+0.05*6), 
#     xycoords='data',
#     xytext=(-25, -15), 
#     textcoords='offset points',
#     ha='right', 
#     va='top',
#     annotation_clip=False,
#     arrowprops=dict(
#         arrowstyle='-', 
#         lw=0.5, 
#         color='k',
#         shrinkA=0,
#         shrinkB=0,
#         ),
#     )

ax0.annotate(
    '$t_n$',
    xy=(((1.226-0.176)/2)+0.176, belowFigLevel2+0.05*6), 
    xycoords='data',
    xytext=(0, 3), 
    textcoords='offset points',
    ha='center', 
    va='bottom',
    annotation_clip=False,
    )



# ------------------------------------------
# '$t_{reg}$'

ax0.plot([10.37 -10.37 - 0.37, 20], [0.95, 0.95],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )

ax0.plot([10.37 -10.37 - 0.37, 20], [1.05, 1.05],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )

ax0.plot([10.37, 10.37], [1.05, -0.04],
         '-', lw=0.5, alpha=1.0, color='gray', dashes=[5,2],
         )



ax0.annotate(
    '',
    xy=(10.37, belowFigLevel1), 
    xycoords='data',
    xytext=(10.37, belowFigLevel2), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        arrowstyle='-', 
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )

ax0.annotate(
    '',
    xy=(0, belowFigLevel2+0.05*1), 
    xycoords='data',
    xytext=(10.37, belowFigLevel2+0.05*1), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        # arrowstyle='<->', 
        arrowstyle='<->,head_width=.1,head_length=0.5',
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )

ax0.annotate(
    '$t_{reg}$',
    xy=(10.37/2, belowFigLevel2+0.05*1), 
    xycoords='data',
    xytext=(0, 3), 
    textcoords='offset points',
    ha='center', 
    va='bottom',
    annotation_clip=False,
    )





# ax0.annotate(
#     'pásmo necitlivosti $\pm$ 5 \%',
#     xy=(10.37+1, 1.05 ), 
#     xycoords='data',
#     xytext=(30, 20), 
#     textcoords='offset points',
#     ha='left', 
#     va='bottom',
#     arrowprops=dict(
#         arrowstyle='-', 
#         lw=0.5, 
#         color='k',
#         shrinkA=0,
#         shrinkB=0,
#         ),
#     )



ax0.annotate(
    '2$\delta$',
    xy=(19, 1.05), 
    xycoords='data',
    xytext=(5, 5), 
    textcoords='offset points',
    ha='left', 
    va='bottom',
    # arrowprops=dict(
    #     arrowstyle='-', 
    #     lw=0.5, 
    #     color='k',
    #     shrinkA=0,
    #     shrinkB=0,
    #     ),
    )





ax0.annotate(
    '',
    xy=(19, 1.05), 
    xycoords='data',
    xytext=(0, 15), 
    textcoords='offset points',
    ha='right', 
    va='center',
    arrowprops=dict(
        # arrowstyle='<->', 
        arrowstyle='->,head_width=.1,head_length=0.5',
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )

ax0.annotate(
    '',
    xy=(19, 0.9), 
    xycoords='data',
    xytext=(19, 1.1), 
    textcoords='data',
    ha='right', 
    va='center',
    arrowprops=dict(
        arrowstyle='-',  
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )



ax0.annotate(
    '',
    xy=(19, 0.95), 
    xycoords='data',
    xytext=(0, -15), 
    textcoords='offset points',
    ha='right', 
    va='center',
    arrowprops=dict(
        # arrowstyle='<->', 
        arrowstyle='->,head_width=.1,head_length=0.5',
        lw=0.5, 
        color='k',
        shrinkA=0,
        shrinkB=0,
        ),
    annotation_clip=False,
    )




















# Restore saved axis limits
ax0.set_xlim(x_limits)
ax0.set_ylim(y_limits)


#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant03(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

# plt.close()

#------------------













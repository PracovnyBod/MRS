# -*- coding: utf-8 -*-

from figFcns_TeX import *
from figFcns_addhelpers import *






PANELNAME = 'panel_wy'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(3.5, 0.17, 0.83, 0.17, 0.5, 13)
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

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant03(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

plt.close()

#------------------





















PANELNAME = 'panel_u'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(3.5, 0.17, 0.83, 0.17, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             # height_ratios=[40, 40, 20],
                             )

#---------------------------------------------
ax0 = plt.subplot(subPlots[0])



ax0.plot(t_log, u_log,
         '-', lw=0.8, alpha=0.9, color='k',
         label='$u(t)$',
         )

#------------------
ax0.set_title(u'Akčný zásah', x=0.01, y=1.02, ha='left')

#------------------

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant03(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

plt.close()

#------------------













PANELNAME = 'panel_e_log'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(3.5, 0.17, 0.83, 0.17, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             # height_ratios=[40, 40, 20],
                             )

#---------------------------------------------
ax0 = plt.subplot(subPlots[0])



ax0.plot(t_log, e_log,
         '-', lw=0.8, alpha=0.9, color='k',
         label='$e(t)$',
         )

#------------------
ax0.set_title(u'Regulačná odchýlka', x=0.01, y=1.02, ha='left')

#------------------

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant03(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

plt.close()

#------------------






PANELNAME = 'panel_int_e_log'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(3.5, 0.17, 0.83, 0.17, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             # height_ratios=[40, 40, 20],
                             )

#---------------------------------------------
ax0 = plt.subplot(subPlots[0])



ax0.plot(t_log, int_e_log,
         '-', lw=0.8, alpha=0.9, color='k',
         label='$\\int e(t)$ d$t$',
         )

#------------------
ax0.set_title('Integrál regulačnej odchýlky', x=0.01, y=1.02, ha='left')

#------------------

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant03(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

plt.close()

#------------------




PANELNAME = 'panel_der_e_log'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(3.5, 0.17, 0.83, 0.17, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             # height_ratios=[40, 40, 20],
                             )

#---------------------------------------------
ax0 = plt.subplot(subPlots[0])



ax0.plot(t_log, der_e_log,
         '-', lw=0.8, alpha=0.9, color='k',
        label='d$e(t)/$d$t$',
         )

#------------------
ax0.set_title('Derivácia regulačnej odchýlky', x=0.01, y=1.02, ha='left')

#------------------

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant03(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

plt.close()

#------------------

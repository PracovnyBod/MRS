# -*- coding: utf-8 -*-

exec(open('./figjobs/figFcns_TeX.py', encoding='utf-8').read())
from figFcns_TeX import *

from figFcns_addhelpers import *








PANELNAME = 'p1'

#---------------------------------------------

figPlotParam = fcnDefaultFigSize(3.5, 0.17, 0.83, 0.17, 0.5, 13)
fig = plt.figure(figNameNum, figsize=figPlotParam[0:2])

subPlots = gridspec.GridSpec(1, 1,
                             # height_ratios=[40, 40, 20],
                             )

#---------------------------------------------
ax0 = plt.subplot(subPlots[0])

ax0.plot(plotData_x, plotData_y,
         '-', lw=0.8, alpha=0.9, color='k',
         label='$y(t)$',
         )

#------------------
# ax0.set_title(u'Výstupná veličina', x=0.01, y=1.02, ha='left')

#------------------

#------------------
fcnDefaultLayoutAdj(fig, figPlotParam[2], figPlotParam[3], figPlotParam[4], figPlotParam[5])

fcn_panelformat_variant02(fig)

#------------------
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.png', dpi=240)
plt.savefig(figSaveDir + figName + '_' + PANELNAME +'.pdf')

plt.close()
mpl.rcParams.update(mpl.rcParamsDefault)

#------------------













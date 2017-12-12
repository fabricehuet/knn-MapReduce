from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

from pylab import *

import matplotlib.pyplot as plt
import numpy as np
import csv

#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','blue','green','silver','aqua','magenta','gold','black']
#-----------------------------------------------


rc('font', size=16)
rc('legend', columnspacing=1)
rc('lines', linewidth=3)
rc('lines',markersize=15)

data = np.genfromtxt('../data/params-lsh/lsh-surf-params.csv', delimiter=';',skip_header=2,skip_footer=3,
                     names=['l', 'm', 'w','hdfs','time','accuracy','ratio-recall',
                            'ratiores',	'bucket'])
print data['hdfs'][0:6]

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.07, top = 0.85, right=0.91,wspace=0.3)

taillebar = 0.005;
num = 0;
ax = fig.add_subplot(1,1,1)
a = ax.bar(data['accuracy']-taillebar/2.0,data['ratiores']*100,taillebar,label="percentage",color="skyblue",alpha=0.4)

ax2 = ax.twinx()

#resultsize=42311200
resultsize=1
ax2.plot(data['accuracy'][0:6],data['hdfs'][0:6]/resultsize,'--', c='blue',marker=mark[0],label='set W')
ax2.plot(data['accuracy'][6:12],data['hdfs'][6:12]/resultsize,'--', c='yellowgreen',marker=mark[1],label='set M')
ax2.plot(data['accuracy'][12:18],data['hdfs'][12:18]/resultsize,'--', c='magenta',marker=mark[2],label='set L')

ax2.bar(min(data['accuracy']),min(data['ratiores']),taillebar,label="% knn",color="skyblue",alpha=0.4)


bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
leg = ax2.legend(loc='upper center',bbox_to_anchor=(0.5, 1.2),ncol=4,  fancybox=True, shadow=True)

ax.set_xlabel('Accuracy')
ax2.set_xlabel('Accuracy')
#ax2.set_ylabel('result size ( final = '+str(resultsize)+' byte)')
ax2.set_ylabel('hdfs byte write');
ax.set_ylabel('percentage of knn');

rc('font', size=21)
rc('legend', columnspacing=1)
grid(True)

#-----------------------------------------------

fig.savefig('../../img-perf/perso/lsh/params_surf_acc.pdf',dpi=400)

show()
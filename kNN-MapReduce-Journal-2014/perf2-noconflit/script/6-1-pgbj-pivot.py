#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=18)

path="../data/perso/pgbj/piv.txt"

fig =figure(figsize=(16, 8), dpi=80)
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,4,';')

ax = fig.add_subplot(1,1,1)
taillebar=5
ax.plot(mat[:,0]/1000,mat[:,1]/1000/60,c=colors[0],marker=mark[0],label="25K");
ax.plot(mat[:,0]/1000,mat[:,2]/1000/60,c=colors[1],marker=mark[1],label="50K");
ax.plot(mat[:,0]/1000,mat[:,3]/1000/60,c=colors[2],marker=mark[2],label="100K");

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.13),ncol=3,  fancybox=True, shadow=True)

#ax.xaxis.set_major_formatter(FormatStrFormatter('${%0.0f}^{2}$'))

ax.set_xlabel("Number of pivots ($*10^{3}$)");
ax.set_ylabel("time(min)")

grid(True)
show()
fig.savefig('../../img-perf/perso/pgbj/pivots.pdf',dpi=400)
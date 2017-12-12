#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=26)
rc('legend', fontsize=21)
path="../data/perso/hbknnj/nodes.txt"

indexhbknnj=4;

fig =figure(figsize=(12, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
#fig.subplots_adjust(bottom=0.15, left=0.1, top = 0.85, right=0.9)

label,mat = file2matrix(path,2,';')

ax = fig.add_subplot(1,1,1)
ax.plot(mat[:,0],mat[:,1],'-', c=colors[indexhbknnj],marker=mark[indexhbknnj],label="H-BkNNJ");


leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 0.9),ncol=2,  fancybox=True, shadow=True)

ax.set_xlabel("Number of nodes");
ax.set_ylabel("time(sec)")

ax.grid()
show()
fig.savefig('../../img-perf/perso/hbknnj/nodes.pdf',dpi=400)
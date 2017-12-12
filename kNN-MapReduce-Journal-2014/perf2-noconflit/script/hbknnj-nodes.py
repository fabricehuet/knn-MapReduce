#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *


path="../data/perso/hbknnj/nodes.txt"

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,2,';')

ax = fig.add_subplot(1,1,1)
ax.plot(mat[:,0],mat[:,1],'-', c="b",marker=mark[0],label="hbknnj");


leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=2,  fancybox=True, shadow=True)

ax.set_xlabel("#nodes");
ax.set_ylabel("time(sec)")
	
show()
fig.savefig('../graph/perso/hbknnj/nodes.png',dpi=400)
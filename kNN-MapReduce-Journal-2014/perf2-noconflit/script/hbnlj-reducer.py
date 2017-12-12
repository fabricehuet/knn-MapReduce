#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

path="../data/perso/hbnlj/reducer.txt"

fig =figure(figsize=(16, 8), dpi=80)
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,4,';')

ax = fig.add_subplot(1,1,1)
taillebar=5
ax.plot(mat[:,0],mat[:,1],c=colors[0],marker=mark[0],label="5M");
ax.plot(mat[:,0],mat[:,2],c=colors[1],marker=mark[1],label="50M");
ax.plot(mat[2:5,0],mat[2:5,3],c=colors[2],marker=mark[2],label="100M");

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=3,  fancybox=True, shadow=True)

ax.set_xlabel("#reducer");
ax.set_ylabel("time(sec)")
	
grid(True)
show()
fig.savefig('../graph/perso/hbnlj/reducer.png',dpi=400)
#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *


path="../data/perso/pgbj/sample.txt"

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,3,';')

ax = fig.add_subplot(1,1,1)
taillebar=5
ax.bar(mat[:,0],mat[:,1],taillebar,color="b",label="farthest");
ax.bar(mat[:,0]+taillebar,mat[:,2],taillebar,color="gray",label="kmeans");


leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=2,  fancybox=True, shadow=True)

ax.set_xlabel("#file(M)");
ax.set_ylabel("time(sec)")
	
show()
fig.savefig('../graph/perso/pgbj/sample.png',dpi=400)
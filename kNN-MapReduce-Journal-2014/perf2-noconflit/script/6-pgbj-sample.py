#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=21)

path="../data/perso/pgbj/sample.txt"

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,4,';')

ax = fig.add_subplot(1,1,1)
taillebar=5

ax.plot(mat[:,0]/1000,mat[:,1]/1000/60,color="green",label="kmeans");
ax.plot(mat[:,0]/1000,mat[:,2]/1000/60,color="b",label="farthest");
ax.plot(mat[:,0]/1000,mat[:,3]/1000/60,color="red",label="random");

#ax.set_xticks([5,20,50])

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.13),ncol=3,  fancybox=True, shadow=True)

ax.set_xlabel("Number of records ($*10^3$)");
ax.set_ylabel("Time (min)")

ax.grid()

show()
fig.savefig('../../img-perf/perso/pgbj/sample.pdf',dpi=400)
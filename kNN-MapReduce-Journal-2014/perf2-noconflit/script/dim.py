#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

path="../data/dim/dataset.txt"

fig =figure(figsize=(16, 8), dpi=80)
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,5,';')

ax = fig.add_subplot(1,1,1)
taillebar=5
tablabel = ["hbnlj","pgbj-geo grouping","lsh","hzknnj"]


x = range(size(mat[:,1]))
cpt=1
for tla in tablabel :
	ax.plot(x,mat[:,cpt],c=colors[cpt],marker=mark[cpt]    ,label=tla);
	cpt +=1

tabtick=["2-osm","10-magic","77-twitter","128-sift","281-blog"];
ax.set_xticks(x,tabtick)

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=3,  fancybox=True, shadow=True)

ax.set_xlabel("#reducer");
ax.set_ylabel("time(sec)")
	
grid(True)
show()
fig.savefig('../graph/dim/time.png',dpi=400)
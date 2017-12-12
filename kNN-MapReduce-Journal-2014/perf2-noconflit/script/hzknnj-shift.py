#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

path="../data/perso/hzknnj/shift.txt"

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,3,';')
ax = fig.add_subplot(1,1,1)
ax.bar(mat[:,0],mat[:,1],1,color="b",alpha=0.5,label="shift");
ax2 = ax.twinx();
ax2.plot(mat[:,0],mat[:,2],'--', c="red",marker=mark[0],label="accuracy");
ax.plot(min(mat[:,0]),min(mat[:,1]),'--', c="red",label="accuracy");


ax.set_xlabel("#shift");
ax.set_ylabel("time(sec)",color="blue");
ax2.set_ylabel("accuracy",color="red");

for tl in ax.get_yticklabels():
	    tl.set_color('b')
	
for tl in ax2.get_yticklabels():
	    tl.set_color('r')

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=2,  fancybox=True, shadow=True)
	
show()
fig.savefig('../graph/perso/hzknnj/shift.png',dpi=400)
    
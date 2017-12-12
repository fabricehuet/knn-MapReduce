#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=28)
rc('legend', fontsize=21)
path="../data/perso/hzknnj/shift.txt"

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)

label,mat = file2matrix(path,3,';')
ax = fig.add_subplot(1,1,1)
ax.bar(mat[:,0]-0.5,mat[:,1],1,color="red",alpha=0.5,label="shift");
ax2 = ax.twinx();
ax2.plot(mat[:,0],mat[:,2],'--', c="black",marker=mark[0],label="accuracy");
ax.plot(min(mat[:,0]),min(mat[:,1]),'--', c="black",label="accuracy");

ax.set_xticks([1,4,6,8,10])
ax.set_xlim(right=11.5)

ax.set_xlabel("Number of shifts");
ax.set_ylabel("Time(min)",color="red");
ax2.set_ylabel("Accuracy ",color="black");

for tl in ax.get_yticklabels():
	    tl.set_color('red')

for tl in ax2.get_yticklabels():
	    tl.set_color('black')


mini = min(mat[:,0])
maxi = max(mat[:,0])
inter=1.5;
# msg="$12500$ descriptors"
# t = ax.annotate(msg, xy=(10.5,1), xycoords="data",
#                   va="center", ha="center",
#                   bbox=dict(boxstyle="round", fc="w"))

leg = ax.legend(loc='upper center', fancybox=True, shadow=True)

grid(True)
show()
fig.savefig('../../img-perf/perso/hzknnj/shift.pdf',dpi=400)

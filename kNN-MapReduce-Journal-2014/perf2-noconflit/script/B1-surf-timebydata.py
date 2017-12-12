#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

path     = "../data/surf";
NB=0
TIME=1
rc('font', size=20)

#-------------------------------------------------------------------------------
matrices=[]
tab  = ["lsh","hvdknnj","hbnlj"]
tab2 = ["RankReduce","PGBJ","H-BNLJ"]
for i in tab :
    label,mat = file2matrix(path+"/"+i+"/time.txt",3,';')
    print mat;
    matrices.append(mat)

#----------------------------------------1-------
fig =figure( figsize=(10, 8), dpi=80)

#fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.98, right=0.9)
#fig.subplots_adjust(hspace=0.5)

#fig.suptitle('Impact number data on time and accuracy, hight dimension', fontsize=14, fontweight='bold')
ax = fig.add_subplot(1,1,1)

ax2= ax.twinx()
cpt=0
cptc=1

for mat in matrices :
    if(i=="hbknnj" or i=="hzknnj"):
        continue;
    ax.plot(mat[:,NB]/100,mat[:,TIME]/1000,color=colors[cptc],
            marker=mark[cptc],label=tab2[cpt])
    if(tab[cpt]=="lsh"):
    	ax2.plot(mat[:,NB]/100,mat[:,2],'--',color=colors[cptc],marker=mark[cptc])
    cptc +=1
    cpt += 1
ax.grid()
ax2.grid()
ax.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))
ax2.xaxis.set_major_formatter(FormatStrFormatter('%0.0f'))


#for label in ax.xaxis.get_ticklabels():
#    label.set_rotation(45)
#for label in ax2.xaxis.get_ticklabels():
#    label.set_rotation(45)
#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

ax.set_xlabel('Number of images ($*10^{2}$)') #\n 2000 descriptors/image')
ax2.set_ylabel('Accurancy')
ax.set_ylabel('Time (min)')
box = ax.get_position()

# Put a legend to the right of the current axis
#ax.plot(0,0,'--',color = "black",label="accurancy");

box = ax2.get_position()
ax2.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.2),ncol=5,  fancybox=True, shadow=True)

show()
fig.savefig('../../img-perf/surf/time.pdf')
print("OLD VERSION DO NOT USE")



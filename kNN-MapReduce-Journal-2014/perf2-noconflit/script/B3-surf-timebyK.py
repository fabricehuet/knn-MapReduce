#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

path     = "../data/surf";
NB=0
TIME=1
rc('font', size=20)

#-------------------------------------------------------------------------------
tab  = ["lsh","hvdknnj","hbnlj"]
tab2 = ["RankReduce","PGBJ","H-BNLJ"] 
matrices = []

for i in tab :
    label,mat = file2matrix(path+"/"+i+"/K.txt",3,';')
    matrices.append(mat)
   
#----------------------------------------1-------
fig =figure( figsize=(10, 8), dpi=80)
#fig.subplots_adjust(bottom=0.15, left=0.10, top = 0.95, right=0.90)
#fig.subplots_adjust(hspace=0.5)
#fig.suptitle("Impact K on time and accurancy,hight dimension",fontsize=14,fontweight='bold')

ax = fig.add_subplot(1,1,1)
ax2 = ax.twinx()

cptc=1
cpt=0

for mat in matrices :
	if(tab[cpt]=="lsh"):
		ax2.plot(mat[:,NB],mat[:,2],'--',color="black",marker=mark[cptc],label="RankReduce Accuracy")
	ax.plot(mat[:,NB],mat[:,TIME]/1000,color=colors[cptc],marker=mark[cptc],label=tab2[cpt])
	cpt+=1
	cptc+=1
ax.grid()
#for label in ax.xaxis.get_ticklabels():
#    label.set_rotation(20)
#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

ax.set_xlabel('k')
ax.set_ylabel('Time (min)')
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.2),ncol=5,  fancybox=True, shadow=True)
	
ax2.legend(loc='upper left', fancybox=True, shadow=True)
#-----------------------------------------------

ax2.grid()

#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

#ax2.set_xlabel('#K')
ax2.set_ylabel('Accuracy')
box = ax2.get_position()

  
box = ax2.get_position()
ax2.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

#figtext(.02, .02, "For LSH, to get a good accuracy, it must set the parameters,here W",fontname="Comics")
show()
fig.savefig('../../img-perf/surf/k.pdf',dpi=400)
    

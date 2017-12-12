#!/usr/bin/python
from pylab import *
from readfile import *

path     = "../../datares/surf";
NB=0
TIME=1
#-------------------------------------------------------------------------------
mark =['*','s','d','>','h','v','p','^','+']
colors = ['gold','#00FF00','#FF0066','blue','black','aqua','silver']

#-------------------------------------------------------------------------------
matrices=[]
tab = ["hbnlj","hvdknnj","lsh"] 
tab2 = ["hbnlj","pgbj","rankreduce"] 

for i in tab :
    label,mat = file2matrix(path+"/"+i+"/K.txt",3,';')
    matrices.append(mat)
   
#----------------------------------------1-------
fig =figure( figsize=(10, 8), dpi=80)
fig.subplots_adjust(bottom=0.15, left=0.10, top = 0.95, right=0.90)
fig.subplots_adjust(hspace=0.5)
fig.suptitle("Impact K on time and accurancy,hight dimension",fontsize=14, 
             fontweight='bold')

ax = fig.add_subplot(1,2,1)
title("time")
cpt=0

for mat in matrices :
    ax.plot(mat[:,NB],mat[:,TIME]/1000/60,color="0.4",marker=mark[cpt],
            label=tab[cpt])
    
    cpt += 1
ax.grid()
for label in ax.xaxis.get_ticklabels():
    label.set_rotation(20)
#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

ax.set_xlabel('#K')
ax.set_ylabel('time(min)')
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

ax.legend(loc='upper center', bbox_to_anchor=(1, -0.15),
          fancybox=True, shadow=True, ncol=5)
  


#-----------------------------------------------

ax2 = fig.add_subplot(1,2,2)
title("accuracy")
cpt=0

for mat in matrices :
    ax2.plot(mat[:,NB],mat[:,2],'--',color="0.4",marker=mark[cpt],label=tab[cpt])    
    cpt += 1
ax2.grid()

#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

ax2.set_xlabel('#K')
ax2.set_ylabel('accuracy')
box = ax2.get_position()

  
box = ax2.get_position()
ax2.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

#figtext(.02, .02, "For LSH, to get a good accuracy, it must set the parameters,here W",fontname="Comics")
show()
fig.savefig('../../graph/surf/K.png',dpi=400)
    

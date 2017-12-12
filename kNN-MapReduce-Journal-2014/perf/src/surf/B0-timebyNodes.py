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
#----------------------------------------1-------
fig =figure( figsize=(10, 8), dpi=80)

figtext(0.2, 10, "Impact on number nodes, hight dimension");
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.98, right=0.9)
fig.subplots_adjust(hspace=0.5)
fig.suptitle('Impact on time', fontsize=14, fontweight='bold')


nbFile=[100]
cpo=1
#-------------------------------------------------------------------------------
for nb in nbFile :
    cpt=0
    ax = fig.add_subplot(1,1,1)
   
    matrices=[]
    
    tab = ["hbnlj","hvdknnj","lsh"] 
    tab2 = ["hbnlj","pgbj","rankreduce"] 

    for i in tab :
        label,mat = file2matrix(path+"/"+i+"/nodes.txt",2,';')
        matrices.append(mat)
    
    for mat in matrices :
        ax.plot(mat[:,NB],mat[:,TIME]/1000/60,color="0.4",
                marker=mark[cpt],label=tab2[cpt])
        cpt += 1
        
    ax.grid()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])
    
    ax.set_xlabel('#node')
    ax.set_ylabel('time(min)')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)
    ax.set_title("100x100images")
    
  

# Put a legend below current axis

#-----------------------------------------------


show()
fig.savefig('../../graph/surf/nodes.png',dpi=400)
    



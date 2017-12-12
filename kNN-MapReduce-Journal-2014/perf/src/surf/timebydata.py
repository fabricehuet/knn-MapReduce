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
    label,mat = file2matrix(path+"/"+i+"/time.txt",3,';')
    print mat;
    matrices.append(mat)
   
#----------------------------------------1-------
fig =figure( figsize=(10, 8), dpi=80)

fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.98, right=0.9)
fig.subplots_adjust(hspace=0.5)

fig.suptitle('Impact number data on time and accuracy, hight dimension', fontsize=14, fontweight='bold')
ax = fig.add_subplot(1,2,1)

ax2= fig.add_subplot(1,2,2)
cpt=0

for mat in matrices :
    if(i=="hbknnj" or i=="hzknnj"):
        continue;
    ax.plot(mat[:,NB]/100,mat[:,TIME]/1000/60,color="0.4",
            marker=mark[cpt],label=tab2[cpt])
    ax2.plot(mat[:,NB]/100,mat[:,2],'--',color="0.4",marker=mark[cpt])
    
    cpt += 1
ax.grid()
ax2.grid()
ax.xaxis.set_major_formatter(FormatStrFormatter(' $%0.0f*10^{2}$'))
ax2.xaxis.set_major_formatter(FormatStrFormatter(' $%0.0f*10^{2}$'))


for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(45)
#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

ax.set_xlabel('#images')
ax2.set_xlabel('#images')
ax2.set_ylabel('accurancy')
ax.set_ylabel('time(min)')
box = ax.get_position()

# Put a legend to the right of the current axis
#ax.plot(0,0,'--',color = "black",label="accurancy");
   
box = ax2.get_position()
ax2.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

ax.legend(loc='upper center', bbox_to_anchor=(1, -0.15),
          fancybox=True, shadow=True, ncol=5)

ax.set_title("time")
ax2.set_title("accuracy")

show()
fig.savefig('../../graph/surf/time.png')
    



#!/usr/bin/python
from pylab import *
from readfile import *

name='hzknnj'#'lsh'#'hbnlj'#
path     = "../data/loadbalancing/"+name+".txt" #le nom
indice_color=4 #color a change
CPT=0
CPT_S=1
CPT_R=2
TIME=3
#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','green','blue','silver','aqua','magenta','gold','black']

#-------------------------------------------------------------------------------

label,mat = file2matrix(path,4,';')
   
#-----------------------------------------------
fig =figure()
fig.subplots_adjust(bottom=0.2, left=0.15, top = 0.9, right=0.85)
fig.subplots_adjust(hspace=0.5)

ax = fig.add_subplot(1,1,1)
cpt=0

print mat[:,TIME]
ax.bar(mat[:,CPT],mat[:,CPT_S]*mat[:,CPT_R],
       color=colors[indice_color],alpha=0.7, edgecolor='black',label="#R*#S")
ax.grid()

ax2 = ax.twinx()
ax2.plot(mat[:,CPT],mat[:,TIME]/1000,color='red')
ax2.grid()

ax.set_xlabel('reducers')
ax.set_ylabel('#elements',color="#336699")
for tl in ax.get_yticklabels():
    tl.set_color('#336699')
ax2.set_ylabel('time(s)',color="red")
for tl in ax2.get_yticklabels():
    tl.set_color('r')
    
figtext(.02, .02, "10^5 elements by file\n")

xlabel('reducer')
title(name.upper(),fontweight="bold")
ax.legend(loc='upper right',fancybox=True, shadow=True)
#-----------------------------------------------

fig.savefig('../graph/loadbalancing/'+name+'.png',dpi=200)
    

show()



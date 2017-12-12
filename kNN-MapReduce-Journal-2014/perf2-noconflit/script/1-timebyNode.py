#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

NB=0
TIME=1
#-------------------------------------------------------------------------------
#colors = ['blue','gold','#00FF00','#FF0066','black','aqua','silver']

rc('font', size=14)
rc('legend', columnspacing=1)
tab = ["hzknnj","hlsh","hvknnj","hbnlj","hbknnj"]
# tab2 = ["hzknnj","rankreduce","pgbj","hbnlj","hbknnj"]
tab2 = ["H-zkNNJ","RankReduce","PGBJ","H-BNLJ","H-BkNNJ"]
#mark =['o','d','s','*','v']
#----------------------------------------1-------
fig =figure( figsize=(10, 5.5), dpi=80)

#figtext(0.2, 10, "Impact on number nodes, hight dimension");
fig.subplots_adjust(bottom=0, left=0.07, top = 0.98, right=0.95)
fig.subplots_adjust(hspace=1.5)
#fig.suptitle('Impact on time', fontsize=14, fontweight='bold')


nbFile=[4,200,4000]
#nbFile=[4000]
cpo=1
#ax0=fig.add_subplot(1,3,cpo)
#-------------------------------------------------------------------------------
for nb in nbFile :
    cpt=0
    ax = fig.add_subplot(1,3,cpo)

    cpo+=1
    matrices=[]

    path     = "../data/geo/nodes/"+str(nb);


    for i in tab :
        if(i=="hbknnj" and nb>4):
            continue
        if(i=="hbnlj" and nb>4):
            continue
        if(i=="hvknnj" and nb>200):
            continue
        label,mat = file2matrix(path+"/"+i,2,';')
        matrices.append(mat)

    for mat in matrices :
        print(mat[:,TIME]/1000/60)
        ax.plot(mat[:,NB],mat[:,TIME]/1000/60,linewidth=3,markersize=8,
                marker=mark[cpt],label=tab2[cpt],color=colors[cpt])
        cpt += 1

    ax.grid()
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.75])

    ax.set_xlabel('Number of nodes')
    if(cpo==2):
        ax.set_ylabel('Time (min)')

    if(cpo==2):
       #ax.legend(loc='upper center', bbox_to_anchor=(1.7, -0.09),
        #  fancybox=True, shadow=True, ncol=5)
        ax.legend(loc='upper center', bbox_to_anchor=(1.7, 1.22),
             fancybox=True, shadow=True, ncol=5)

    ax.set_title("$"+str(nb)+ "$"+"$*10^{3}$ records")



# Put a legend below current axis

#-----------------------------------------------


show()
fig.savefig('../../img-perf/geo/data/nodes.pdf',dpi=400)




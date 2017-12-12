#!/usr/bin/python
from pylab import *
from readfile import *

path     = "../data/strategy-voronoi";
NB=0
TIME=1
#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['#00FF00','#FF0066','#66CCFF','aqua','gold','black','red','magenta']

hatches = ['-', '+', 'O','x', '*', 'o', 'O', '//']
#-------------------------------------------------------------------------------
matrices=[]
tab = ["hvdknnj-greedy-conf50R.txt","hvdknnj-greedy-conf20R.txt","hvdknnj-geo-conf20R.txt"] 
labelg = ["greedy 50 reducers","greedy 20 reducers","geo 20 reducers"] 

for i in tab :
    label,mat = file2matrix(path+"/"+i,6,';')
    matrices.append(mat)
   
#----------------------------------------1-------
fig =figure()
fig.subplots_adjust(bottom=0.2, left=0.08, top = 0.9, right=0.85)
fig.subplots_adjust(hspace=0.5)

ax = fig.add_subplot(1,1,1)
cpt=0
ax2 = ax
width=1
rect=[]
res=[]
for i in range(2,6) : 
    rect.append(i)
for mat in matrices :
    temp= ax.plot(mat[:,NB]/10,mat[:,TIME]/1000/60,color=colors[cpt],marker=mark[cpt],label=labelg[cpt])
    res.append(temp)
    tps=0
    for i in range(2,6) : 
        tps += mat[:,7-i]/1000/60
    for i in range(2,6) : 
        rect[i-2] = ax2.bar(mat[:,NB]/10+(width+0.1)*cpt,tps,width,color=colors[cpt], edgecolor='black',hatch=hatches[i])
        tps -= mat[:,7-i]/1000/60
    
    print mat[:,1];
    cpt += 1
ax.grid()
ax.xaxis.set_major_formatter(FormatStrFormatter(' $%0.0f*10^{6}$'))

for label in ax.xaxis.get_ticklabels():
    label.set_rotation(20)
    
# Add invisible data to add another legend

#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

xlabel('#data by file')
ylabel('time(min)')
title("TIME FOR DIFFERENTS CONFIGURATIONS OF VORONOI",fontweight="bold")
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

# Put a legend to the right of the current axis
n=[]        
for i in range(2,6):
    n.append(ax.bar(0,0,color = "gray", hatch=hatches[i]))

l1 = plt.legend(n, ('phase2','grouping','phase1','pivots'),
                 fancybox=True, shadow=True,loc=[1.01,0.4])  

plt.gca().add_artist(l1)
print ax.legend
ax.legend(loc='upper left', fancybox=True, shadow=True,bbox_to_anchor=(1, 1))

#-----------------------------------------------

show()
fig.savefig('../graph/voronoi-timeStrategy2.png',dpi=200)
    



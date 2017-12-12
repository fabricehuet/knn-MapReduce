#!/usr/bin/python
from pylab import *
from readfile import *

path     = "../../datares/";
NB=0
TIME=2
#-------------------------------------------------------------------------------
rc('font', size=16)
rc('legend', columnspacing=1)
rc('lines', linewidth=3)
rc('lines',markersize=8)
#tab = ["hzknnj","lsh","hvdknnj","hbnlj","hbknnj"] 
tab = ["hzknnj","lsh", "hvdknnj", "hbnlj","hbknnj"]
tab2 = ["H-zkNNJ","RankReduce","PGBJ","H-BNLJ","H-BkNNJ"] 
mark =['o','d','s','*','v']
#-------------------------------------------------------------------------------
matrices=[]
# tab = ["hbknnj","hbnlj","hvdknnj","hzknnj","lsh"] 
# tab2 = ["hbknnj","hbnlj","pgbj","hzknnj","rankreduce"] 
for i in tab :
    label,mat = file2matrix(path+"/all-2/"+i+".txt",3,';')
    print mat;
    matrices.append(mat)
   
#----------------------------------------1-------
fig =figure( figsize=(10, 8), dpi=80)

#fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.98, right=0.9)
#fig.subplots_adjust(hspace=0.5)

#fig.suptitle('Impact number data on time and accuracy,low dimension', fontsize=14, fontweight='bold')
ax = fig.add_subplot(1,1,1)
cpt=0
ax.set_xscale('log')

plt.ylim(0, 150.0)

for mat in matrices :
    print("xxx " + tab2[cpt])
    print(mat[:,NB])
    print(mat[:,TIME]/1000/60)
    ax.plot(mat[:,NB],mat[:,TIME]/1000/60,
            marker=mark[cpt],label=tab2[cpt])
 #   ax2.plot(mat[:,NB]/100,mat[:,2],'--',color="0.4",marker=mark[cpt])
    
    cpt += 1
ax.grid()
#ax2.grid()
ax.xaxis.set_major_formatter(FormatStrFormatter(' $%0.0f*10^{5}$'))
#ax2.xaxis.set_major_formatter(FormatStrFormatter(' $%0.0f*10^{5}$'))


for label in ax.xaxis.get_ticklabels():
    label.set_rotation(45)
#for label in ax2.xaxis.get_ticklabels():
 #   label.set_rotation(45)
#figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")

ax.set_xlabel('#data by file')
#ax2.set_xlabel('#data by file')
#ax2.set_ylabel('accurancy')
ax.set_ylabel('time(min)')
box = ax.get_position()

# Put a legend to the right of the current axis
#ax.plot(0,0,'--',color = "black",label="accurancy");
   
#box = ax2.get_position()
#ax2.set_position([box.x0, box.y0 + box.height * 0.1,
#                 box.width, box.height * 0.8])
box = ax.get_position()
ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.8])

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15),
          fancybox=True, shadow=True, ncol=5)

#ax.set_title("time")
#ax2.set_title("accuracy")

#show()
fig.savefig('../../../img-perf/geo/data/time.png')
    



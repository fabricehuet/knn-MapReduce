#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *


CPT=0
CPT_S=1
CPT_R=2
TIME=3
rc('font', size=26)
rc('legend', fontsize=21)
#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','green','blue','silver','aqua','magenta','gold','black']

#-------------------------------------------------------------------------------

tab     = ["geo_20r_400","greedy_20r_400","greedy_50r_400"];
nametab = ["geo 20 reducers","greedy 20 reducers","greedy 50 reducers"];

width =1


def func(path,colorfond='aqua', colorfond2='blue',cptindtab = 0) :
	label,mat = file2matrix(path,4,';')

	#-----------------------------------------------
	fig =figure(figsize=(10, 8), dpi=80)
	#fig.subplots_adjust(bottom=0.2, left=0.15, top = 0.9, right=0.85)
	#fig.subplots_adjust(hspace=0.5)

	ax = fig.add_subplot(1,1,1)
	cpt=0

	print mat[:,TIME]
	ax.bar(mat[:,CPT]-width/2.0,mat[:,CPT_S]/1000,width,color=colorfond,alpha=0.7, edgecolor='black',label="#S")
	ax.bar(mat[:,CPT]-width/2.0,mat[:,CPT_R]/1000,width,color=colorfond2, edgecolor='black',label="#R")
	ax.grid()

	#ax2 = ax.twinx()
	#ax2.plot(mat[:,CPT],mat[:,TIME]/1000,color='red')
	#ax2.grid()

	ax.set_xlabel('Reducer number')
        ax.set_ylabel('Number of Elements ($*10^{3}$)')
        #for tl in ax.get_yticklabels():
        #tl.set_color(colorfond2)
	#ax2.set_ylabel('time(s)',color="red")
	#for tl in ax2.get_yticklabels():
	#    tl.set_color('r')

	#figtext(.02, .02, "An example of bad balancing for 4x10^5 elements by file\n")

	xlabel('Reducer number')
	#title(nametab[cptindtab].upper(),fontweight="bold"),
	cptindtab+=1

        leg = ax.legend(loc='upper left',  fancybox=True, shadow=True)
        show();
        fig.savefig('../../img-perf/perso/pgbj/'+name+'.pdf',dpi=200)


	#-----------------------------------------------

for name in tab :
	path= "../data/loadbalancing/voronoi/"+name+".txt"
	func(path,'#85c895','green')
#func( "../data/loadbalancing/dim/386-rand.txt",'#85c895','green')
#func( "../data/loadbalancing/dim/386-realtxt",'#85c895','green')



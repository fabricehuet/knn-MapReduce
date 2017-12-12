#!/usr/bin/python
from pylab import *
from readfile import *


CPT=0
CPT_S=1
CPT_R=2
TIME=3
#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','green','blue','silver','aqua','magenta','gold','black']

#-------------------------------------------------------------------------------

tab     = ["geo_20r_400","greedy_20r_400","greedy_50r_400"];
nametab = ["geo 20 reducers","greedy 20 reducers","greedy 50 reducers"];
cptindtab = 0;

for name in tab :
	path= "../data/loadbalancing/voronoi/"+name+".txt"
	
	label,mat = file2matrix(path,4,';')
	   
	#-----------------------------------------------
	fig =figure()
	fig.subplots_adjust(bottom=0.2, left=0.15, top = 0.9, right=0.85)
	fig.subplots_adjust(hspace=0.5)
	
	ax = fig.add_subplot(1,1,1)
	cpt=0
	
	print mat[:,TIME]
	ax.bar(mat[:,CPT],mat[:,CPT_S],color='aqua',alpha=0.7, edgecolor='black',label="#S")
	ax.bar(mat[:,CPT],mat[:,CPT_R],color='blue', edgecolor='black',label="#R")
	ax.grid()
	
	ax2 = ax.twinx()
	ax2.plot(mat[:,CPT],mat[:,TIME]/1000,color='red')
	ax2.grid()
	
	ax.set_xlabel('reducers')
	ax.set_ylabel('#elements',color="blue")
	for tl in ax.get_yticklabels():
	    tl.set_color('b')
	ax2.set_ylabel('time(s)',color="red")
	for tl in ax2.get_yticklabels():
	    tl.set_color('r')
	    
	figtext(.02, .02, "An example of bad balancing for 4x10^5 elements by file\n")
	
	xlabel('reducer')
	title(nametab[cptindtab].upper(),fontweight="bold"),
	cptindtab+=1

	ax.legend(loc='upper right',fancybox=True, shadow=True)
	#-----------------------------------------------
	
	fig.savefig('../graph/loadbalancing/voronoi/'+name+'_loadbalancing.png',dpi=200)
	    
	
	show();
	

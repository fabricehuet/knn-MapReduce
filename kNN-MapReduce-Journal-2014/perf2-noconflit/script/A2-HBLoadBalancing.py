#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

name='hbnlj'#'lsh'#'hbnlj'#

tab  = ["hzknnj","lsh","hvdknnj","hbnlj","hbknnj"]
tab2 = ["H-zkNNJ","RankReduce","PGBJ","H-BNLJ","H-BkNNJ"]
colors = ['red','blue','grey','green','magenta','aqua','gold','black']


rc('font', size=30)
rc('legend', fontsize=25)
rc('legend', columnspacing=1)
rc('lines', linewidth=5)
rc('lines',markersize=20)
indice_color=4 #color a change
CPT=0
CPT_S=1
CPT_R=2
TIME=3
cptc=0
width=0.8
cpt=0
for name in tab :
	if(name=="hvdknnj" or name=="hbknnj"):
		continue
	path     = "../data/loadbalancing/"+name+".txt" #le nom
	label,mat = file2matrix(path,4,';')

	#-----------------------------------------------
	fig =figure(figsize=(14, 8), dpi=80)

	fig.subplots_adjust(bottom=0.15, left=0.1, right=0.85)
	#fig.subplots_adjust(hspace=0.5)

	ax = fig.add_subplot(1,1,1)


	#print mat[:,TIME]
	divider =1
	legend = "$*10^{"
	if name=="hbnlj" :
		divider = pow(10,9)
		legend = legend+"9}$"
	if name=="lsh"	:
		divider = pow(10,7)
		legend = legend+"7}$"
	if name=="hzknnj"	:
		divider = pow(10,10)
		legend = legend+"10}$"
	print(mat[:,CPT_S]*mat[:,CPT_R])
	ax.bar(mat[:,CPT]-width/2.0,mat[:,CPT_S]*mat[:,CPT_R]/divider,width,
	       color=colors[cptc],alpha=0.5, edgecolor='black',label="#R*#S")
	ax.grid()
	ax.set_yticks(np.arange(0,1.8,0.4))

	ax2 = ax.twinx()
	ax2.plot(mat[:,CPT],mat[:,TIME]/1000/60,color='black')
	ax2.grid()

	ax.set_xlabel('Reducer Number')
        ax.set_ylabel('Number of Elements (' + legend + ")" )
        #color=colors[cptc])
#	for tl in ax.get_yticklabels():
#tl.set_color(colors[cptc])
	ax2.set_ylabel('Time(min)',color="black")
	ax2.set_yticks(np.arange(0,46,10))
	ax2.set_ylim(0.1,46)
	ax.set_ylim(0.01,1.8)
	for tl in ax2.get_yticklabels():
	    tl.set_color('black')

	#figtext(.02, .02, "10^5 elements by file\n")

	#xlabel('reducer')
	#title(name.upper(),fontweight="bold")
	if cpt == 2 :
		leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 0.95),ncol=5,  fancybox=True, shadow=True)
	else :
		leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.15),ncol=5,  fancybox=True, shadow=True)

	cpt+=1


	#-----------------------------------------------
	cptc+=1
	fig.savefig('../../img-perf/perso/loadbalancing/'+name+'.pdf')
	show()



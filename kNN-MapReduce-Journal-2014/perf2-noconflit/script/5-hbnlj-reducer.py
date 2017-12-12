#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=20)

path="../data/perso/hbnlj/reducer.txt"
path2="../data/perso/hbnlj/reducer-memory.txt"


label,mat = file2matrix(path,4,';')

label2,mat2 = file2matrix(path2,4,';')#stoage


def partie_function(num,A,B,l,col,A2,B2,un=False,dernier=False):
	ax = fig.add_subplot(1,3,num)
	taillebar=5
	#ax.plot(mat[:,0],mat[:,1]/1000/60,c=colors[0],marker=mark[0],label="125K");
	#ax.plot(mat[1:4,0],mat[1:4,2]/60,c=colors[1],marker=mark[1],label="250K");

	ax2 = ax.twinx()
	ax2.set_ylim(0,5)
	taillebar=0.3
	a = ax2.bar(A2-taillebar/2,B2+1,0.3,label="storage",color="green",alpha=taillebar)
	if dernier :
		ax2.set_ylabel('Space requirement',color="green")

	ax.plot(A,B,c=col,marker=mark[2],label=l);
	print l
	print B2
	print ">>"
	leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.2),ncol=1,  fancybox=True, shadow=True)
        #for tl in ax2.get_yticklabels():
#tl.set_color('green')

	#ax.xaxis.set_major_formatter(FormatStrFormatter('${%0.f}^{2}$'))
	ax.axes.get_xaxis().set_ticks(A)

	ax.set_xlabel("Number of partition");
	if un :
		ax.set_ylabel("time(min)")
	grid(True)

fig =figure(figsize=(16, 6), dpi=80)
fig.subplots_adjust(bottom=0.15, left=0.05, top = 0.85, right=0.95,wspace=0.4)

partie_function(1,mat[:4,0],mat[:4,1]/1000/60,"12.5K","r",mat2[:4,0],mat2[:4,1],True)
partie_function(2,mat[1:4,0],mat[1:4,2]/1000/60,"25K","g",mat2[1:4,0],mat2[1:4,2])
partie_function(3,mat[1:,0],mat[1:,3]/1000/60,"50K","b",mat2[1:,0],mat2[1:,3],False,True)


fig.savefig('../../img-perf/perso/hbnlj/reducer.pdf',dpi=400)

show()
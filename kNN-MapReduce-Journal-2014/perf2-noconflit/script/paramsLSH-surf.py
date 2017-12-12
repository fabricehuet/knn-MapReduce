#!/usr/bin/python
from pylab import *
from readfile import *

path     = "../data/params-lsh/surf/";


def partie_function(num,name,mat,taillebar,msg,ok=True):
	
	ax = fig.add_subplot(1,3,num)
	b = ax.plot(min(mat[:,0]),min(mat[:,1]),'--',color=colors[0],label="accuracy")#pour la legende c'est vide sinon
	a = ax.bar(mat[:,0],mat[:,1],taillebar,label="time")
	
	ax2 = ax.twinx()
	ax2.plot(mat[:,0],mat[:,3],'--', c=colors[0],marker=mark[0])
	
	ax.set_ylim([0,200])
	ax2.set_ylim([0,1])
	ax.set_xlabel(name)
		
	ax.set_ylabel('time(min)')
	ax2.set_ylabel('accuracy')
		
	if(ok):
		#ax.legend(loc='upper left',fancybox=True, shadow=True)
		#ax2.legend(loc='upper right',fancybox=True, shadow=True)
		
		bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
		leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.1),ncol=2,  fancybox=True, shadow=True)
#[a, b], ['time','accuracy'],
	
	
	mini = min(mat[:,0])
	maxi = max(mat[:,0])
	inter=(maxi+mini)/4
	t = ax.annotate(msg, xy=(mini+inter,180), xycoords="data",
                  va="center", ha="center",
                  bbox=dict(boxstyle="round", fc="w"))
	grid(True)
	return;	            



#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','blue','green','silver','aqua','magenta','gold','black']
#-----------------------------------------------


rc('font', size=14)
rc('legend', columnspacing=1)

fig =figure(figsize=(16, 8), dpi=80)
#title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)


label,matW = file2matrix(path+"W.txt",4,';')
label,matM = file2matrix(path+"M.txt",4,';')
label,matL = file2matrix(path+"L.txt",4,';')

partie_function(1,"W (*10^5)",matW,5,"M=7, W=5x10^6",False);
partie_function(2,"M",matM,2,"L=1, W=5x10^5",True);
partie_function(3,"L",matL,1,"L=1, M=6",False);


plt.tight_layout(pad=3.0, w_pad=2.5, h_pad=1.0)

#-----------------------------------------------

show()
fig.savefig('../graph/params-lsh/params-lsh-surf.png',dpi=400)
    
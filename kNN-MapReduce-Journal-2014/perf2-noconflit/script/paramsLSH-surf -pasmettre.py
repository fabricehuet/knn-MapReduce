#!/usr/bin/python
from pylab import *
from readfile import *

path     = "../data/params-lsh/surf/";




def partie_function(num,name,mat,taillebar,ok=True):
	
	ax = fig.add_subplot(1,3,num)
	ax.bar(mat[:,0],mat[:,1],taillebar,label="time")
	
	ax2 = ax.twinx()
	ax2.plot(mat[:,0],mat[:,3],'--', c=colors[0],marker=mark[0],label="accuracy")
	
	ax.set_ylim([0,200])
	ax2.set_ylim([0,1])
	ax.set_xlabel(name)
		
	ax.set_ylabel('time(min)')
	ax2.set_ylabel('accuracy')
		
	if(ok):
		ax.legend(loc='upper left',fancybox=True, shadow=True)
		ax2.legend(loc='upper right',fancybox=True, shadow=True)
		#ax.set_title("M")
		
	bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)

	t = ax2.text(0, -5, "Accuracy optimal", ha="center", va="center", rotation=60,
            size=15,
            bbox=bbox_props)
	grid(True)
	return;	            



#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','blue','green','silver','aqua','magenta','gold','black']
#-----------------------------------------------
fig =figure(figsize=(16, 8), dpi=80)
title("LSH : impact of differents parameters\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)


label,matW = file2matrix(path+"W.txt",4,';')
label,matM = file2matrix(path+"M.txt",4,';')
label,matL = file2matrix(path+"L.txt",4,';')

partie_function(1,"W (*10^5)",matW,5,False);
partie_function(2,"M",matM,2);
partie_function(3,"L",matL,1,False);

#-----------------------------------------------

show()
fig.savefig('../graph/params-lsh/params-lsh-surf',dpi=400)
    
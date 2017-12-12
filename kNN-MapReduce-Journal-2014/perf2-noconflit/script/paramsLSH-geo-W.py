#!/usr/bin/python
from pylab import *
from readfile import *

path     = "../data/params-lsh/params-lsh--geo-W.txt"

label,mat = file2matrix(path,6,';')

#-------------------------------------------------------------------------------
mark =['d','v','o','^','>','h','s','p','*','+']
colors = ['red','blue','green','silver','aqua','magenta','gold','black']
#-----------------------------------------------
fig =figure()

title("LSH : impact W on accuracy\n")
fig.subplots_adjust(bottom=0.1, left=0.1, top = 0.9, right=0.9)
fig.subplots_adjust(hspace=0.5)

ax = fig.add_subplot(1,1,1)
ax.plot(mat[:,0],mat[:,3]/1000/60, c=colors[1],marker=mark[1],label="time")
ax2 = ax.twinx()
ax2.plot(mat[:,0],mat[:,1],'--', c=colors[0],marker=mark[0],label="accuracy")
ax.plot(0,0,'--', c=colors[0],marker=mark[0],label="accuracy")

ax.legend(loc='upper left',fancybox=True, shadow=True)
ax.set_xlabel('W')
ax.set_ylabel('time(min)')
ax2.set_ylabel('accuracy')
ax.set_title("Time vs Accuracy")

bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
t = ax2.text(275000, 0.91, "Accuracy optimal", ha="center", va="center", rotation=60,
            size=15,
            bbox=bbox_props)
grid(True)
show()


fig2 =figure()
ax3 = fig2.add_subplot(1,1,1)
ax3.bar(mat[:,0],mat[:,5], 5000,label="#bucket")
ax4 = ax3.twinx()
ax4.plot(mat[:,0],mat[:,1],'--', c=colors[0],marker=mark[0],label="accuracy")

ax3.plot(0,0,'--', c=colors[0],marker=mark[0],label="accuracy")

ax3.set_title("#Bucket vs Accuracy")

ax3.legend(loc='upper left',fancybox=True, shadow=True)

ax3.set_xlabel('W')
ax3.set_ylabel('#bucket')
ax4.set_ylabel('accuracy')
grid(True)
#-----------------------------------------------

show()
fig.savefig('../graph/params-lsh/params-lsh--geo-W-time.png',dpi=200)
fig2.savefig('../graph/params-lsh/params-lsh--geo-W-buck.png',dpi=200)
    



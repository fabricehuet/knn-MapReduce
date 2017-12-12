#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=40)
rc('legend', fontsize=30)
rc('legend', columnspacing=1)
rc('lines', linewidth=5)
rc('lines',markersize=20)

path     = "../data/params-lsh/params-lsh--geo-W.txt"

label,mat = file2matrix(path,6,';')
rc('font', size=28)
rc('legend', fontsize=21)
#-------------------------------------------------------------------------------
rc('lines',markersize=15)

fig =figure(figsize=(16, 8), dpi=80)

#title("LSH : impact W on accuracy\n")
fig.subplots_adjust(bottom=0.15, left=0.09, top = 0.9, right=0.91,wspace=0.55,hspace=0.5)

taillebar=1.5
ax = fig.add_subplot(1,2,1)
print mat[:,2]
#ax.plot(mat[:,0]/10000,mat[:,3]/1000/60, c=colors[1],marker=mark[1],label="time")
tmp = mark[0]
mark[0] = mark[1]
mark[1] = tmp


#a = ax.bar(mat[:,0]/10000-taillebar/2.0,mat[:,3]/1000/60,taillebar,label="time",color=colors[],alpha=0.4)

a = ax.plot(mat[:,0]/10000,mat[:,3]/1000/60,label="time",color="blue",alpha=0.8,marker=mark[1])

ax.axes.get_xaxis().set_ticks(mat[:,0]/10000)
ax.set_ylim(3.6,4.35)

#grid(True)
ax2 = ax.twinx()
ax2.plot(mat[:,0]/10000,mat[:,1],'--', c=colors[0],marker=mark[0],label="recall")
ax2.plot(mat[:,0]/10000,mat[:,1]*(1/mat[:,4]),'-', c="purple",marker=mark[2],label="precision")

ax.plot(0,0,'--', c=colors[0],marker=mark[0],label="recall")
ax.plot(0,0,'-', c="purple",marker=mark[2],label="precision")

#ax.legend(loc='center right',fancybox=True, shadow=True)
bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.15),ncol=3,  fancybox=True, shadow=True)

ax.set_xlabel('W ($*10^{4}$)')
ax.set_ylabel('Time (min)')
#, color=colors[1])
#for tl in ax.get_yticklabels():
#	    tl.set_color(colors[1])
grid(True)
ax2.set_ylabel('Recall & Precision')
#ax.set_title("Time vs Accuracy")



bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
#leg = ax.legend(loc='upper center',bbox_to_anchor=(0.5, 1.2),ncol=1,  fancybox=True, shadow=True)

# t = ax2.text(275000, 0.91, "Optimal Accuracy", ha="center", va="center", rotation=60,
#             size=15,
#             bbox=bbox_props)

#-------------------------------------------------------------------------------
#fig2 =figure(figsize=(16, 8), dpi=80)
ax3 = fig.add_subplot(1,2,2)
ax3.bar(mat[:,0]/10000-1.5,mat[:,5]/1000, 3,label="buckets",alpha=0.4)
#for tl in ax3.get_yticklabels():
#	    tl.set_color(colors[1])
ax3.axes.get_xaxis().set_ticks(mat[:,0]/10000)
ax3.set_ylim(0,12.5)
#grid(True)
ax4 = ax3.twinx()
ax4.plot(mat[:,0]/10000,mat[:,1],'--', c=colors[0],marker=mark[0],label="recall")

ax3.plot(0,0,'--', c=colors[0],marker=mark[0],label="recall")

#ax3.set_title("#Bucket vs Accuracy")

#ax3.legend(loc='center top',fancybox=True, shadow=True)

bbox_props = dict(boxstyle="rarrow,pad=0.2", fc="pink", ec="k", lw=2)
leg = ax3.legend(loc='upper center',bbox_to_anchor=(0.5, 1.15),ncol=3,  fancybox=True, shadow=True)

ax3.set_xlabel('W ($*10^{4}$)')
ax3.set_ylabel('Number of buckets ($*10^{3}$)')
#, color=colors[1])
ax4.set_ylabel('Recall')

#for tl in ax2.get_yticklabels():
#    tl.set_visible(False)
#for tl in ax3.get_yticklabels():
#    tl.set_visible(False)
grid(True)
#-----------------------------------------------

show()
fig.savefig('../../img-perf/perso/lsh/params_geo_time.pdf',dpi=400)
#fig2.savefig('../../img-perf/perso/lsh/params_geo_acc.pdf',dpi=400)




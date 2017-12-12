#!/usr/bin/python
from pylab import *
from readfile import *
from mycolor import *

rc('font', size=21)
rc('legend', fontsize=20)


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
labelg = ["Greedy 50 reducers","Greedy 20 reducers","Geo 20 reducers"]

for i in tab :
    label,mat = file2matrix(path+"/"+i,6,';')
    matrices.append(mat)

#----------------------------------------1-------
def details() :
    fig =figure(figsize=(16, 8), dpi=80)
    #fig.subplots_adjust(bottom=0.2, left=0.08, top = 0.9, right=0.85)
    #fig.subplots_adjust(hspace=0.5)

    ax = fig.add_subplot(1,1,1)
    cpt=0
    ax2 = ax
    width=0.2
    rect=[]
    res=[]
    for i in range(2,6) :
        rect.append(i)
    for mat in matrices :
        temp= ax.plot(log2(mat[:,NB]/100),mat[:,TIME]/1000/60,color=colors[cpt],marker=mark[cpt],label=labelg[cpt])
        res.append(temp)
        tps=0
        for i in range(2,6) :
            tps += mat[:,7-i]/1000/60
        for i in range(2,6) :
            print(mat[:,NB])
            rect[i-2] = ax2.bar(log2(mat[:,NB]/100)+ width*(cpt-1.5),tps,width,color=colors[cpt], edgecolor='black',alpha=0.7,hatch=hatches[i])
            tps -= mat[:,7-i]/1000/60

        print mat[:,1];
        cpt += 1
    ax.grid()
    #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.f}$'))
    # for label in ax.xaxis.get_ticklabels():
    #     label.set_rotation(20)

    # Add invisible data to add another legend

    #figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")


    ax.set_xticks(arange(-3,10,1))
    #ax.set_xticks([12.5,25,50,100,200,400])

    ax.set_xticklabels([0.125,0.25,0.5,1,2,4])
    xlabel('Number of records ($*10^{5}$)')
    ylabel('Time (minutes)')
    #title("TIME FOR DIFFERENTS CONFIGURATIONS OF VORONOI",fontweight="bold")
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])

    # Put a legend to the right of the current axis
    n=[]
    label2=('phase2','grouping','phase1','pivots')
    for i in range(2,6):
        n.append(ax.bar(0,0,color = "white", hatch=hatches[i]))


    l1=plt.legend(n,label2,fancybox=True, bbox_to_anchor=(0.27, 1),ncol=1)
    plt.gca().add_artist(l1)
    print ax.legend
    ax.legend(loc='upper center', fancybox=True, shadow=True,bbox_to_anchor=(0.5, 1.14),ncol=5)

    show()
    fig.savefig('../../img-perf/perso/pgbj/strategy.pdf',dpi=400)


def simple() :
    fig =figure(figsize=(12, 8), dpi=80)
    #fig.subplots_adjust(bottom=0.2, left=0.08, top = 0.9, right=0.85)
    #fig.subplots_adjust(hspace=0.5)

    ax = fig.add_subplot(1,1,1)
    cpt=0
    ax.set_xticks(log2([0.5,1,2,4]))
    ax.set_xticklabels([0.5,1,2,4])
    ax.set_xlabel('Number of records ($*10^{5}$)')
    ax.set_ylabel('Time (minutes)')
    ax.grid()
    ax2=ax.twinx()
    ax2.set_ylabel("Grouping Time (seconds)")
    width=0.2
    for mat in matrices :
        ax.plot(log2(mat[:,NB]/100),mat[:,TIME]/1000/60,color=colors[cpt],marker=mark[cpt],label=labelg[cpt])
        print(log2(mat[:,NB]/100))
        #res.append(temp)
        #tps=0
        # for i in range(2,6) :
        #     tps += mat[:,7-i]/1000/60
        # for i in range(2,6) :
        #     print(mat[:,NB])
        ax2.bar(log2(mat[:,NB]/100)+ width*(cpt-1.5),mat[:,4]/1000,width,color=colors[cpt], edgecolor='black',alpha=0.7)
        print(log2(mat[:,NB]/100))
            # tps -= mat[:,7-i]/1000/60

        # print mat[:,1];
        cpt += 1

    #ax.xaxis.set_major_formatter(FormatStrFormatter('$2^{%1.f}$'))
    # for label in ax.xaxis.get_ticklabels():
    #     label.set_rotation(20)

    # Add invisible data to add another legend

    #figtext(.02, .02, "An example of bad balancing for 32x10^5 elements by file\n")



    #title("TIME FOR DIFFERENTS CONFIGURATIONS OF VORONOI",fontweight="bold")
    box = ax.get_position()
    #ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
    ax.legend(loc='upper center', fancybox=True, shadow=True,bbox_to_anchor=(0.4, 0.95),ncol=2)

    show()
    fig.savefig('../../img-perf/perso/pgbj/strategy.pdf',dpi=400)

#-----------------------------------------------

#details()
simple()

